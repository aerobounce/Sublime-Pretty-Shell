#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# PrettyShell.py
#
# AGPLv3 License
# Created by github.com/aerobounce on 2019/11/18.
# Copyright © 2019 aerobounce. All rights reserved.
#

import sublime
import sublime_plugin
from uuid import uuid4
from subprocess import Popen, PIPE
from os import remove

class PrettyShellCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        settings=sublime.load_settings("Pretty Shell.sublime-settings")

        # Store cursor region
        # original_regions = self.view.sel()

        # Prepare formatted result
        # If has no selection, entire regions will be used
        # for region in self.view.sel():
        #     if region.empty():
        selection = sublime.Region(0, self.view.size())
            # else:
            #     selection = region
        target_text = self.view.substr(selection)

        # Make temp file
        tmp_file_path = "/tmp/" + str(uuid4())

        # Write texts
        with open(tmp_file_path, mode='w', encoding='utf-8') as tmp:
            tmp.write(target_text)

        # Format temp file with shfmt
        indent = str(settings.get("indent"))
        language = str(settings.get("language"))
        simplify = "-s" if settings.get("simplify", True) else ""
        binop = "-bn" if settings.get("binop", True) else ""
        switchcase = "-ci" if settings.get("switchcase", True) else ""
        rediop = "-sr" if settings.get("rediop", True) else ""
        align = "-kp" if settings.get("align", True) else ""
        minify = "-mn" if settings.get("minify", True) else ""

        command = "shfmt -w -i {1} -ln \"{2}\" {3} {4} {5} {6} {7} {8} \"{0}\"".format(tmp_file_path,
                                                                                       indent,
                                                                                       language,
                                                                                       simplify,
                                                                                       binop,
                                                                                       switchcase,
                                                                                       rediop,
                                                                                       align,
                                                                                       minify)
        # print(command)
        Popen(command, shell=True, stdout=PIPE).stdout.read()

        # Read result
        with open(tmp_file_path, encoding='utf-8') as temp:
            output = temp.read()

        # Remove temp file
        remove(tmp_file_path)

        # Replace with result
        self.view.replace(edit, selection, output)

        # Restore cursor region
        # try:
        #     selection = original_regions[0]
        #     self.view.sel().clear()
        #     self.view.sel().add(selection)
        # except IndexError:
        #     return


class AutoFormatter(sublime_plugin.ViewEventListener):
    def on_pre_save(self):
        settings=sublime.load_settings("Pretty Shell.sublime-settings")
        if settings.get("pretty_on_save") == True:
            if "Bash" in self.view.settings().get("syntax"):
                self.view.run_command("pretty_shell")
