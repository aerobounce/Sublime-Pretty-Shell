#!/usr/bin/env python
# coding: utf-8
#
# PrettyShell.py
#
# AGPLv3 License
# Created by github.com/aerobounce on 2019/11/18.
# Copyright © 2019 to Present, aerobounce. All rights reserved.
#

import html
import re
from subprocess import PIPE, Popen

import sublime
import sublime_plugin

SETTINGS_FILENAME = "Pretty Shell.sublime-settings"
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
PHANTOM_SETS = {}


def update_phantoms(view, stderr, region):
    view_id = view.id()

    view.erase_phantoms(str(view_id))
    if view_id in PHANTOM_SETS:
        PHANTOM_SETS.pop(view_id)

    if not stderr:
        return

    if not view_id in PHANTOM_SETS:
        PHANTOM_SETS[view_id] = sublime.PhantomSet(view, str(view_id))

    # Extract line and column
    digits = re.compile(r"\d+|$").findall(stderr)
    line = int(digits[0]) - 1
    column = int(digits[1]) - 1

    if region:
        line += view.rowcol(region.begin())[0]

    # Format error message
    pattern = "<standard input>:[0-9]{1,}:[0-9]{1,}:."
    stderr = re.compile(pattern).sub("", stderr)

    def erase_phantom(self):
        view.erase_phantoms(str(view_id))

    phantoms = []
    point = view.text_point(line, column)
    phantoms.append(
        sublime.Phantom(
            sublime.Region(point, view.line(point).b),
            (
                "<body id=inline-error>"
                + PHANTOM_STYLE
                + '<div class="error-arrow"></div><div class="error">'
                + '<span class="message">'
                + html.escape(stderr, quote=False)
                + "</span>"
                + "<a href=hide>"
                + chr(0x00D7)
                + "</a></div>"
                + "</body>"
            ),
            sublime.LAYOUT_BELOW,
            on_navigate=erase_phantom,
        )
    )
    PHANTOM_SETS[view_id].update(phantoms)


def shfmt(view, edit, use_selection, minify):
    # Load settings file
    settings = sublime.load_settings(SETTINGS_FILENAME)

    # Retrieve settings (No need for nil fallback here)
    shfmt_bin_path = "{} ".format(settings.get("shfmt_bin_path"))
    simplify = "-s " if settings.get("simplify") else ""
    language = '-ln "{}" '.format(settings.get("language"))
    indent = "-i {} ".format(settings.get("indent"))
    binop = "-bn " if settings.get("binop") else ""
    switchcase = "-ci " if settings.get("switchcase") else ""
    rediop = "-sr " if settings.get("rediop") else ""
    align = "-kp " if settings.get("align") else ""
    minify = "-mn" if (settings.get("minify") or minify) else ""

    # Compose shfmt command
    command = (
        shfmt_bin_path
        + simplify
        + language
        + indent
        + binop
        + switchcase
        + rediop
        + align
        + minify
    )

    # Format

    def format_text(target_text, selection, region):
        # Open subprocess with the command
        with Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE) as popen:
            # Write selection into stdin, then ensure the descriptor is closed
            popen.stdin.write(target_text.encode("utf-8"))
            popen.stdin.close()
            # Read stdout and stderr
            stdout = popen.stdout.read().decode("utf-8")
            stderr = popen.stderr.read().decode("utf-8")

            # Replace with result if only stderr is empty
            if not stderr:
                view.replace(edit, selection, stdout)

            # Present alert if 'shfmt' not found
            if "command not found" in stderr:
                sublime.error_message(
                    "Pretty Shell - Error:\n"
                    + stderr
                    + "Specify absolute path to 'shfmt' in settings"
                )
                return stderr

            # Update Phantoms
            update_phantoms(view, stderr, region)

            return stderr

    # Prevent needles iteration AMAP
    has_selection = any([not r.empty() for r in view.sel()])
    if (settings.get("format_selection_only") or use_selection) and has_selection:
        for region in view.sel():
            if region.empty():
                continue

            # Break at the first error
            if format_text(view.substr(region), region, region):
                break

    else:
        # Don't format entire file when use_selection is true
        if use_selection:
            return

        # Use entire region/string of view
        selection = sublime.Region(0, view.size())
        target_text = view.substr(selection)
        format_text(target_text, selection, None)


class PrettyShellCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        shfmt(self.view, edit, False, False)


class PrettyShellSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        shfmt(self.view, edit, True, False)


class PrettyShellMinifyCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        shfmt(self.view, edit, False, True)


class PrettyShellMinifySelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        shfmt(self.view, edit, True, True)


class PrettyShellListener(sublime_plugin.ViewEventListener):
    def on_pre_save(self):
        if "Bash" in self.view.settings().get("syntax"):
            if sublime.load_settings(SETTINGS_FILENAME).get("format_on_save"):
                self.view.run_command("pretty_shell")

    def on_close(self):
        view_id = self.view.id()
        if view_id in PHANTOM_SETS:
            PHANTOM_SETS.pop(view_id)
