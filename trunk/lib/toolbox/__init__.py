#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# __init__.py:  defines this directory as the 'toolbox' package.
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
Miscellaneous utility functions ...

Some of this functions are from "Dive Into Python", a free Python book for
experienced programmers, other from Internet ...
Thanks to:
    http://diveintopython.org/  Mark Pilgrim <f8dy@diveintopython.org>
"""
__author__ = "Jose Riguera Lopez <jriguera@gmail.com>"
__version__ = "0.3.0"
__date__ = "April 2010"
__license__ = "GPL (v3 or later)"
__copyright__ ="(c) Jose Riguera"


__package_name__ = "toolbox"
__package_revision__ = '0'
__package_version__ = '0.3.0'
__package_released__ = "October 2008"
__package_author__ = "Jose Riguera Lopez <jriguera@gmail.com>"
__package_license__ = "GPL (v2 or later)"
__package_copyright__ ="(c) Jose Riguera, October 2008"


__all__ = ["iosys", "exceptions", "string", "i18n"]
from iosys import *
from exceptions import *
from string import *
from i18n import *


# EOF
