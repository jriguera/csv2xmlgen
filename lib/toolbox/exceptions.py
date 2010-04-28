#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright © 2008 Jose Riguera Lopez <jriguera@gmail.com>
#
"""
Exceptions for ToolBox package.
"""

import os.path
import gettext
import locale

__GETTEXT_DOMAIN__ = "toolbox"
__PACKAGE_DIR__ = os.path.abspath(os.path.dirname(__file__))
__LOCALE_DIR__ = os.path.join(__PACKAGE_DIR__, "locale")

try:
    if not os.path.isdir(__LOCALE_DIR__):
        print "Error: Cannot locate default locale dir: '%s'." % (__LOCALE_DIR__)
        __LOCALE_DIR__ = None
    locale.setlocale(locale.LC_ALL,"")
    t = gettext.translation(__GETTEXT_DOMAIN__, __LOCALE_DIR__, fallback=False)
    _ = t.ugettext
except Exception as e:
    print "Error setting up the translations: %s" % (e)
    _ = lambda s: unicode(s)


# ##############################
# Exceptions for toolbox package
# ##############################

class Error(Exception):
    """
    Exception raised for errors in this module.

    :Parameters:
        - `message`: the string that represents an explanation of the error.
    """
    def __init__(self, message='ToolBoxError!'):
        self.value = message
    def __str__(self):
        return repr(self.value)

# EOF
