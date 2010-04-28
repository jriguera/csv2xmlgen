#! /usr/bin/env python
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
I/O Operations for ToolBox package.
"""

import os.path
import gettext
import locale
import sys
import ConfigParser
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


# ##################################
# I/O operations for toolbox package
# ##################################

def die (msg, begin='  ', program=os.path.basename(sys.argv[0])):
    """
    Prints an error and exit(1).

    :Parameters:
        -`msg`: error message.
        -`begin`: prefix for error message.
        -`program`: program name.
    """
    d = {'begin': begin, 'program': program, 'msg': msg }
    message = _("%(begin)s[%(program)s] Fatal error!: %(msg)s\n") % d
    sys.stderr.write(message)
    sys.exit(1)


def openReadAnything(source):
    """
    It opens an URI, filename, or string for reading.

    This function lets you define parsers that take any input source
    (URL, pathname to local or network file, or actual data as a string)
    and deal with it in a uniform manner.  Returned object is guaranteed
    to have all the basic stdio read methods (read, readline, readlines).
    Just .close() the object when you're done with it.
    
    Examples:
    >>> from xml.dom import minidom
    >>> sock = openAnything("http://localhost/kant.xml")
    >>> doc = minidom.parse(sock)
    >>> sock.close()
    >>> sock = openAnything("c:\\inetpub\\wwwroot\\kant.xml")
    >>> doc = minidom.parse(sock)
    >>> sock.close()

    :Parameters:
        -`source`: any input source.
        -`return`: file descriptor.
    """
    if hasattr(source, "read"):
        return source
    if source == "-":
        import sys
        return sys.stdin
    # try to open with urllib (if source is http, ftp, or file URL)
    import urllib
    try:
        return urllib.urlopen(source)
    except (IOError, OSError):
        pass
    # try to open with native open function (if source is pathname)
    try:
        #return open(source)
        return codecs.open(source, "r", encoding="utf-8")
    except (IOError, OSError):
        pass
    # treat source as string
    import StringIO
    return StringIO.StringIO(str(source))


def openWriteAnything(source):
    """
    It opens stdout, filename, or string for writting.

    This function lets you define funcions that take any output source
    (pathname to local or network file, or actual data as a string)
    and deal with it in a uniform manner. Returned object is guaranteed
    to have all the basic stdio write methods.
    Just .close() the object when you're done with it.

    :Parameters:
        -`source`: any output (stdout, filename, or string)
        -`return`: file descriptor.
    """
    if hasattr(source, "write"):
        return source
    if source == "-":
        import sys
        return sys.stdout
    # try to open with native open function (if source is pathname)
    try:
        #return open(source, 'wb')
        return codecs.open(source, "wb", encoding="utf-8")
    except (IOError, OSError):
        pass
    # treat source as string
    import StringIO
    return StringIO.StringIO(str(source))


def configRead(configuration, defaults={}, sectionerror=False):
    """
    It reads the configuration from an initialized ConfigParser object `configuration`
    and return a dictionary with sections as keys and for each key, other dictionary 
    with keys from that section. Also, ends up setting default values from `defaults`
    (usually from argv) whose structure is the same as described above.

    Examples:
    >>> import ConfigParser
    >>> configuration = ConfigParser.ConfigParser()
    >>> configuration.read('file.cfg')
    >>> defaultconfig = {}
    >>> defaultconfig['main'] = {}
    >>> defaultconfig['main']['csvinputfile'] = input
    >>> defaultconfig['xml'] = {}
    >>> options = configRead(configuration, defaultconfig)

    :Parameters:
        -`configuration`: ConfigParser object.
        -`defaults`: dict with default values.
        -`sectionerror`: True for raise exceptions.
        -`return`: dictionary.
    """
    config = {}
    for section in defaults.keys():
        dictionary = {}
        if not configuration.has_section(section):
            if sectionerror:
                raise NoSectionError(section)
        else:
            options = configuration.options(section)
            for option in options:
                try:
                    dictionary[option] = configuration.get(section, option)
                except:
                    dictionary[option] = None
        for key, value in defaults[section].items():
            if value:
                dictionary[key] = value
            else:
                value = dictionary.get(key, None)
                dictionary[key] = value
        config[section] = dictionary
    return config


# EOF
