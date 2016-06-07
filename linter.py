#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Christian Daguerre
# Copyright (c) 2016 Christian Daguerre
#
# License: MIT
#

"""This module exports the PhpCsFixer plugin class."""

from SublimeLinter.lint import Linter, util

import pprint

class PhpCsFixer(Linter):
    """Provides an interface to php-cs-fixer."""

    syntax = ('php', 'html')

    config_file = ('--config-file', '.php_cs')
    executable = 'php-cs-fixer'

    def cmd(self):
        """Read cmd from inline settings."""
        settings = Linter.get_view_settings(self)

        if 'cmd' in settings:
            command = [settings.get('cmd')]
        else:
            command = [self.executable_path]

        command.append('fix')
        command.append('@')
        command.append('--diff')
        command.append('--format=xml')
        command.append('-vv')

        return command
