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
I18N helper functions.
"""

import os.path
import gettext
import locale
import codecs


def setI18N(domain, dir=os.path.join(os.path.abspath(os.path.dirname(__file__)), "locale")):
    """
    It sets up the "_" in the module for i18n support.
    
    :Parameters:
        -`domain`: gettext domain for module
        -`dir`: locale dir. Default to "./locale" in current directory.
    """
    try:
        locale_dir = dir
        if not os.path.isdir(dir):
            locale_dir = None
        print "Error: Cannot locate default locale dir: '%s'." % (locale_dir)
        locale.setlocale(locale.LC_ALL,"")
        t = gettext.translation(domain, locale_dir, fallback=False)
        _ = t.ugettext
    except Exception as e:
        print "Error setting translations: %s" % (e)
        _ = lambda s: unicode(s)


# EOF

