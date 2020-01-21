#!/usr/bin/env python
# coding: utf-8
#
# PrettyShell.py
#
# AGPLv3 License
# Created by github.com/aerobounce on 2019/11/18.
# Copyright © 2019 aerobounce. All rights reserved.
#

from subprocess import PIPE, Popen

import sublime
import sublime_plugin

SETTINGS_FILENAME = "Pretty Shell.sublime-settings"
OUTPUT_PANEL_NAME = "pretty_shell_error"


class PrettyShellCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Read current file
        selection = sublime.Region(0, self.view.size())
        target_text = self.view.substr(selection)

        # Retrieve settings
        settings = sublime.load_settings(SETTINGS_FILENAME)

        shfmt_bin_path = "{0} ".format(settings.get("shfmt_bin_path"))
        simplify = "-s " if settings.get("simplify") else ""
        language = '-ln "{0}" '.format(settings.get("language"))
        indent = "-i {0} ".format(settings.get("indent"))
        binop = "-bn " if settings.get("binop") else ""
        switchcase = "-ci " if settings.get("switchcase") else ""
        rediop = "-sr " if settings.get("rediop") else ""
        align = "-kp " if settings.get("align") else ""
        minify = "-mn" if settings.get("minify") else ""

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

        # Format and Read result
        with Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE) as popen:
            popen.stdin.write(target_text.encode("utf-8"))
            popen.stdin.close()
            stdout = popen.stdout.read().decode("utf-8")
            stderr = popen.stderr.read().decode("utf-8")

            # Replace result if only stderr is empty
            if stderr == "":
                self.view.replace(edit, selection, stdout)

            # Update output panel state
            self.manage_output_panel(edit, stderr)

    def manage_output_panel(self, edit, stderr):
        # Remove output panel
        if stderr == "":
            self.view.window().destroy_output_panel(OUTPUT_PANEL_NAME)
            return

        # Otherwise update output panel
        panel = self.view.window().find_output_panel(OUTPUT_PANEL_NAME)

        # Initialize output panel
        if not panel:
            panel = self.view.window().create_output_panel(OUTPUT_PANEL_NAME)
            panel.settings().set("draw_centered", True)
            panel.settings().set("syntax", "Packages/ShellScript/Bash.sublime-syntax")

        # Update output panel
        stderr = "Pretty Shell error:\n" + stderr
        panel.set_read_only(False)
        # Replace with strings
        panel.replace(edit, sublime.Region(0, panel.size()), stderr)
        panel.set_viewport_position((0, 0), False)
        # Set no selections
        panel.sel().clear()
        # Show panel
        panel.show(panel.size() - 1)
        panel.set_read_only(True)

        # Show output panel
        self.view.window().run_command(
            "show_panel", {"panel": "output.{0}".format(OUTPUT_PANEL_NAME)}
        )


class AutoFormatter(sublime_plugin.ViewEventListener):
    def on_pre_save(self):
        if "Bash" in self.view.settings().get("syntax"):
            if sublime.load_settings(SETTINGS_FILENAME).get("pretty_on_save"):
                self.view.run_command("pretty_shell")
