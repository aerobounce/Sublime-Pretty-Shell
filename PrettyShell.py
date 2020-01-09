#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# PrettyShell.py
#
# AGPLv3 License
# Created by github.com/aerobounce on 2019/11/18.
# Copyright © 2019 aerobounce. All rights reserved.
#

from subprocess import Popen, PIPE
import tempfile

import sublime
import sublime_plugin


class PrettyShellCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Load settings
        settings = sublime.load_settings("Pretty Shell.sublime-settings")

        # Read current file
        selection = sublime.Region(0, self.view.size())
        target_text = self.view.substr(selection)

        # Make temp file
        tmp_file = tempfile.NamedTemporaryFile()
        tmp_file_path = tmp_file.name

        # Write texts
        with open(tmp_file_path, mode="w", encoding="utf-8") as tmp:
            tmp.write(target_text)

        # Compose shfmt command
        simplify = "-s " if settings.get("simplify", True) else ""
        language = "-ln \"{0}\" ".format(settings.get("language", "bash"))
        indent = "-i {0} ".format(settings.get("indent", "0"))
        binop = "-bn " if settings.get("binop", True) else ""
        switchcase = "-ci " if settings.get("switchcase", True) else ""
        rediop = "-sr " if settings.get("rediop", True) else ""
        align = "-kp " if settings.get("align", True) else ""
        minify = "-mn " if settings.get("minify", True) else ""

        command = "shfmt "
        command += "{0}".format(simplify)
        command += "{0}".format(language)
        command += "{0}".format(indent)
        command += "{0}".format(binop)
        command += "{0}".format(switchcase)
        command += "{0}".format(rediop)
        command += "{0}".format(align)
        command += "{0}".format(minify)
        command += "-w \"{0}\"".format(tmp_file_path)

        # Format
        # print(command)
        Popen(command, shell=True, stdout=PIPE).stdout.read()
        # print(Popen(command, shell=True, stderr=PIPE).stderr.read())

        # Read result
        with open(tmp_file_path, encoding="utf-8") as tmp:
            output = tmp.read()

        # Replace with result
        self.view.replace(edit, selection, output)


class AutoFormatter(sublime_plugin.ViewEventListener):
    def on_pre_save(self):
        settings = sublime.load_settings("Pretty Shell.sublime-settings")
        if settings.get("pretty_on_save", False):
            if "Bash" in self.view.settings().get("syntax"):
                self.view.run_command("pretty_shell")
