#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
            output = popen.stdout.read().decode("utf-8")

            # Replace result if only exit code is 0
            if popen.wait() == 0:
                # Replace with result
                self.view.replace(edit, selection, output)

            # Print error message
            else:
                print("Pretty Shell error:", popen.stderr.read().decode("utf-8"))


class AutoFormatter(sublime_plugin.ViewEventListener):
    def on_pre_save(self):
        if "Bash" in self.view.settings().get("syntax"):
            if sublime.load_settings(SETTINGS_FILENAME).get("pretty_on_save"):
                self.view.run_command("pretty_shell")
