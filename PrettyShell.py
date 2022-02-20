#!/usr/bin/env python
# coding: utf-8
#
# PrettyShell.py
#
# AGPLv3 License
# Created by github.com/aerobounce on 2019/11/18.
# Copyright © 2019-2022, aerobounce. All rights reserved.
#

from html import escape
from re import compile
from subprocess import PIPE
from subprocess import Popen
from subprocess import CalledProcessError, SubprocessError


from sublime import LAYOUT_BELOW
from sublime import Edit, Phantom, PhantomSet, Region, View
from sublime import error_message as alert, load_settings, packages_path
from sublime_plugin import TextCommand, ViewEventListener

SETTINGS_FILENAME = "Pretty Shell.sublime-settings"
ON_CHANGE_TAG = "reload_settings"
UTF_8 = "utf-8"
PHANTOM_STYLE = """
<style>
    div.error-arrow {
        border-top: 0.4rem solid transparent;
        border-left: 0.5rem solid color(var(--redish) blend(var(--background) 30%));
        width: 0;
        height: 0;
    }
    div.error {
        padding: 0.4rem 0 0.4rem 0.7rem;
        margin: 0 0 0.2rem;
        border-radius: 0 0.2rem 0.2rem 0.2rem;
    }
    div.error span.message {
        padding-right: 0.7rem;
    }
    div.error a {
        text-decoration: inherit;
        padding: 0.35rem 0.7rem 0.45rem 0.8rem;
        position: relative;
        bottom: 0.05rem;
        border-radius: 0 0.2rem 0.2rem 0;
        font-weight: bold;
    }
    html.dark div.error a {
        background-color: #00000018;
    }
    html.light div.error a {
        background-color: #ffffff18;
    }
</style>
"""


def plugin_loaded():
    PrettyShell.settings = load_settings(SETTINGS_FILENAME)
    PrettyShell.reload_settings()
    PrettyShell.settings.add_on_change(ON_CHANGE_TAG, PrettyShell.reload_settings)


def plugin_unloaded():
    PrettyShell.settings.clear_on_change(ON_CHANGE_TAG)


class PrettyShell:
    settings = load_settings(SETTINGS_FILENAME)
    phantom_sets = {}
    shell_command = ""
    shell_cwd = ""
    format_on_save = True
    show_error_inline = True
    scroll_to_error_point = True

    @classmethod
    def reload_settings(cls):
        cls.format_on_save = cls.settings.get("format_on_save")
        cls.show_error_inline = cls.settings.get("show_error_inline")
        cls.scroll_to_error_point = cls.settings.get("scroll_to_error_point")

        simplify = cls.settings.get("simplify")
        minify = cls.settings.get("minify")
        language = cls.settings.get("language")
        indent = cls.settings.get("indent")
        binop = cls.settings.get("binop")
        switchcase = cls.settings.get("switchcase")
        rediop = cls.settings.get("rediop")
        align = cls.settings.get("align")
        fnbrace = cls.settings.get("fnbrace")

        cls.shell_command = cls.settings.get("shfmt_bin_path")
        if simplify:
            cls.shell_command += " -s"
        if minify:
            cls.shell_command += " -mn"
        if language:
            cls.shell_command += ' -ln "{}"'.format(language)
        if indent:
            cls.shell_command += " -i {}".format(indent)
        if binop:
            cls.shell_command += " -bn"
        if switchcase:
            cls.shell_command += " -ci"
        if rediop:
            cls.shell_command += " -sr"
        if align:
            cls.shell_command += " -kp"
        if fnbrace:
            cls.shell_command += " -fn"

        # Note: For Windows only, UNC path error workaround.
        # ("CMD does not support UNC paths as current directories.")
        # This may not be needed in Sublime Text 4.
        #
        # Popen needs non UNC `cwd` to be specified.
        # It seems `cwd` can be any path as long as it's a non UNC path
        cls.shell_cwd = packages_path()

    @classmethod
    def update_phantoms(cls, view: View, stderr: str, error_point: int):
        view_id = view.id()

        if not view_id in cls.phantom_sets:
            cls.phantom_sets[view_id] = PhantomSet(view, str(view_id))

        # Create Phantom
        def phantom_content():
            # Remove unneeded text from stderr
            error_message = compile(r"[0-9]{1,}:[0-9]{1,}:.").sub("", stderr)
            return (
                "<body id=inline-error>"
                + PHANTOM_STYLE
                + '<div class="error-arrow"></div><div class="error">'
                + '<span class="message">'
                + escape(error_message, quote=False)
                + "</span>"
                + "<a href=hide>"
                + chr(0x00D7)
                + "</a></div>"
                + "</body>"
            )

        new_phantom = Phantom(
            Region(error_point, view.line(error_point).b),
            phantom_content(),
            LAYOUT_BELOW,
            lambda _: view.erase_phantoms(str(view_id)),
        )
        # Store Phantom
        cls.phantom_sets[view_id].update([new_phantom])

    @staticmethod
    def parse_error_point(view: View, stderr: str):
        digits = compile(r"\d+|$").findall(stderr)
        if not stderr or not digits[0]:
            return
        line = int(digits[0]) - 1
        column = int(digits[1]) - 1
        return view.text_point(line, column)

    @classmethod
    def execute_format(cls, view: View, edit: Edit):
        # Get entire string
        entire_region = Region(0, view.size())
        entire_text = view.substr(entire_region)

        # Early return
        if not entire_text:
            return

        # Execute shell and get output
        try:
            with Popen(cls.shell_command, cwd=cls.shell_cwd, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE) as popen:
                # Nil check to suppress linter
                if not popen.stdin or not popen.stdout or not popen.stderr:
                    return
                # Write target_text into stdin and ensure the descriptor is closed
                popen.stdin.write(entire_text.encode(UTF_8))
                popen.stdin.close()
                # Read stdout and stderr
                stdout = popen.stdout.read().decode(UTF_8)
                stderr = popen.stderr.read().decode(UTF_8)
                stderr = stderr.replace("<standard input>:", "")
                stderr = stderr.replace("\n", "")

        except CalledProcessError as e:
            stdout = ""
            stderr = "{0} {1}".format(e, e.output)
            print("[Pretty Shell] CalledProcessError:")
            print(e.output)

        except SubprocessError as e:
            stdout = ""
            stderr = "{0} {1}".format(e)
            print("[Pretty Shell] SubprocessError:")
            print(e)

        # Print command executed to the console
        print("[Pretty Shell] Popen:", cls.shell_command)

        # Present alert for 'command not found'
        if "command not found" in stderr:
            alert("Pretty Shell\n" + stderr)
            return

        # Parse possible error point
        error_point = cls.parse_error_point(view, stderr)

        # Present alert for other errors
        if stderr and not error_point:
            alert("Pretty Shell\n" + stderr)
            return

        # Print parsing error
        if error_point:
            print("[Pretty Shell]", stderr)

        # Store original viewport position
        original_viewport_position = view.viewport_position()

        # Replace with stdout only if stderr is empty
        if stdout and not stderr:
            view.replace(edit, entire_region, stdout)

        # Update Phantoms
        view.erase_phantoms(str(view.id()))
        if cls.show_error_inline and error_point:
            cls.update_phantoms(view, stderr, error_point)

        # Scroll to the syntax error point
        if cls.scroll_to_error_point and error_point:
            view.sel().clear()
            view.sel().add(Region(error_point))
            view.show_at_center(error_point)
        else:
            # Restore viewport position
            view.set_viewport_position((0, 0), False)
            view.set_viewport_position(original_viewport_position, False)


class PrettyShellCommand(TextCommand):
    def run(self, edit):
        PrettyShell.execute_format(self.view, edit)


class PrettyShellListener(ViewEventListener):
    def on_pre_save(self):
        if PrettyShell.format_on_save:
            if "Bash" in self.view.settings().get("syntax"):
                self.view.run_command("pretty_shell")

    def on_close(self):
        view_id = self.view.id()

        if view_id in PrettyShell.phantom_sets:
            PrettyShell.phantom_sets.pop(view_id)
