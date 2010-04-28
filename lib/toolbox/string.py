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
Some string functions for ToolBox package.
"""

import os.path
import gettext
import locale
import sys
import re
import codecs

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


# ###################################
# String funcions for toolbox package
# ###################################

def escape(string):
    """
    Escape the given string so that it can be included in double-quoted strings.

    Examples:
    >>> escape('Say:
    ...   "hello, world!"
    ... ')
    '"Say:\\n  \\"hello, world!\\"\\n"'

    :Parameters:
        -`string`: the string to escape
        -`return`: the escaped string
    """
    return string.replace('\\', '\\\\') \
                 .replace('\t', '\\t') \
                 .replace('\r', '\\r') \
                 .replace('\n', '\\n') \
                 .replace('\"', '\\"')


def unescape(string):
    """
    Reverse `escape` the given string.

    Examples:
    >>> print unescape('"Say:\\n  \\"hello, world!\\"\\n"')
    Say:
      "hello, world!"
    <BLANKLINE>

    :Parameters:
        -`string`: the string to unescape
        -`return`: the unescaped string
    """
    return string.replace('\\\\', '\\') \
                 .replace('\\t', '\t') \
                 .replace('\\r', '\r') \
                 .replace('\\n', '\n') \
                 .replace('\\"', '\"')

# EOF
