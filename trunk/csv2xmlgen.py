#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 
# csv2xmlgen.py
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
A program to generate XML files based on a input template. It has been 
developed for generating KML files (Google Earth layers) from CSV data, 
but it can be used to process any kind of XML defined with the template. 
"""
__program__ = "csv2xmlgen"
__author__ = "Jose Riguera Lopez <jriguera@gmail.com>"
__version__ = "0.3.0"
__date__ = "October 2008"
__license__ = "GPL (v3 or later)"
__copyright__ ="(c) Jose Riguera, October 2008"

import os
import sys
import getopt
import time
import re
import csv
import codecs
import gettext
import locale

import ConfigParser
import xml.dom.minidom

# Modules directory
sys.path.append("lib")
try:
    import sxmltemplate
except ImportError:
    print "Sorry, you don't have the SXMLTemplate package installed, and this"
    print "script relies on it. Please copy SXMLTemplate package into lib and try again."
    sys.exit(1)

try:
    import toolbox
except ImportError:
    print "Sorry, you don't have the ToolBox package installed, and this"
    print "script relies on it. Please copy ToolBox.package into lib and try again."
    sys.exit(1)

# I18N gettext support
__GETTEXT_DOMAIN__ = "csv2xmlgen"
__PACKAGE_DIR__ = os.path.abspath(os.path.dirname(__file__))
__LOCALE_DIR__ = os.path.join(__PACKAGE_DIR__, "locale")

try:
    if not os.path.isdir(__LOCALE_DIR__):
        print "Error: Cannot locate default locale dir: '%s'." % (__LOCALE_DIR__)
        __LOCALE_DIR__ = None
    locale.setlocale(locale.LC_ALL,"")
    gettext.install(__GETTEXT_DOMAIN__, __LOCALE_DIR__)
except Exception as e:

    _ = lambda s: unicode(s)
    print "Error setting up the translations: %s" % (e)


# Default Values
CSVdelimiter = ','
CSVquotechar = '"'
CSVencoding = "utf-8 windows-1252 iso-8859-1 iso-8859-2 us-ascii"
XMLseparatorKey = "|"
XMLdefaultValue = " "
XMLlineterminator = "\\n"


def main(options):
    # main program
    
    input = options['main']['csvinputfile']
    try:
        fd = toolbox.openReadAnything(input)
    except IOError as (errno, strerror):
        d = {'input': input, 'errno': errno, 'strerror': strerror }
        toolbox.die(_("Cannot open '%(input)s' for reading: I/O error (%(errno)s): %(strerror)s.") % d)
    
    output = options['main']['xmloutputfile']
    try:
        fdout = toolbox.openWriteAnything(output)
    except IOError as (errno, strerror):
        d = {'output': output, 'errno': errno, 'strerror': strerror }    
        toolbox.die(_("Cannot open '%(output)s' for writing: I/O error (%(errno)s): %(strerror)s.") % d)
    
    # Set up the XML Template
    template = options['main']['xmltemplate']
    try:
        xmltemplate = sxmltemplate.SXMLTemplate(template)
        xmltemplate.separatorKey = options['main']['separatorkey']
        xmltemplate.defaultValue = options['main']['defaultvalue']
        xmltemplate.setTemplates(options['main']['templatenodes'])
    except sxmltemplate.SXMLTemplateError as e:
        toolbox.die(_("Cannot parse XML template: %s.") % e)
    xmltemplate.setRootInfo(options['template'])
    
    d = { 'input': input, 'xmltemplate': template }
    msg(_("Processing input file '%(input)s' with XML template '%(xmltemplate)s' ... ") % d)
    
    # Process CSV data
    lines = 0
    try:
        lines = processCsv(fd, xmltemplate, options['csv'])
    except Exception as e:
        msg(_("Processing CSV data: '%s'.") % e, _("- ERROR: "))
    msg(_("~ %s processed lines.") % lines)
    
    # Close things and do signature
    fd.close()
    dom = xmltemplate.getDom()
    sign = "XML generated with " + __program__ + " version " + __version__ + " at " + time.asctime() + "."
    comment = dom.createComment(sign)
    dom.appendChild(comment)
    sign = __program__ + " " + __copyright__ + ", a " + __license__ + " program created by " + __author__ + "."
    comment = dom.createComment(sign)
    dom.appendChild(comment)
    dom.writexml(fdout, "", "   ", toolbox.unescape(options['xml']['lineterminator']), "utf-8")
    fdout.close()
    msg(_("XML file '%s' generated.") % output)


def processCsv(fd, xmltemplate, options):
    lines = 0
    header = options['headers']
    delimiter = options['delimiter']
    quotechar = options['quotechar']
    encodings = options['encoding']
    if header:
        reader = csv.DictReader(fd, fieldnames=header, delimiter=delimiter, quotechar=quotechar)
    else:
        reader = csv.DictReader(fd, delimiter=delimiter, quotechar=quotechar)
    try:
        for row in reader:
            #print row
            # utf-8 -> unicode because CSV works in utf-8!!
            data = {}
            for k,v in row.iteritems():
                # try to determine the best csv encoding
                key = k.strip()
                for enc in encodings:
                    try:
                        data[key] = unicode(v, enc, "strict")
                        #data[k.strip()] = v.decode(enc)
                        break
                    except:
                        pass
                else:
                    data[key] = v
            xmltemplate.setData(data)
            lines = lines + 1
    except csv.Error as e:
        d = {'line': lines, 'exception': e }
        msg(_("Reading CSV file, line %(line)s: %(exception)s.") % d, _("- ERROR: "))
        return lines
    return lines


def msg(m, begin="* ", end='\n'):
    sys.stderr.write("%s%s%s" % (begin, m, end))


def usage():
    d = {}
    d['program'] = __program__
    use = _(""" 
[python] %(program)s [-c <file>] [-i <file>] [-n 'root.node ...'] [-o <file>] [-t <file>]

Options:

        -c, --config <file>                Configuration file.
        -h, --help                         Show this help and exits.
        -i, --input <file>                 Input data in CSV format.
        -n, --templatenodes "root.node"    Template node(s) (in XML Template).
        -o, --output <file>                XML output file.
        -t, --template <file>              XML input Template.

The XML resulting file is generated from the structure of the XML Template 
file by repeating those nodes indicated by "templatenodes" (see configuration
file) for each line of data in the CSV input file. To do this, the program 
replaces the headers listed in XML Template with data from each line of the 
CSV file, generating the same number of nodes that lines in CSV file. The 
nodes are indicated with the complete 'path' from the root node of the XML 
document to the node to be "repeated", each element is separated by '.' , 
for example: "XMLRootElement.element.node". The root node is not a valid 
template node, for obvious reasons. 

The CSV input file and/or XML output file can be stdin and stdout 
(respectively) by simply stating '-' instead of the file name. 

The program looks for the default configuration file "csv2xmlgen.cfg", but it
is not necessary if all the arguments of the program are supplied, the rest 
of arguments take the default value. These entries are permitted and 
established by default in the configuration file:

    # csv2xmlgen configuration file. 
    # All sections are mandatory, even without content. 
    # This is a comment, not processed, and ...
    ; this is another comment that was not taken into account.
    # Here are the default value of program parameters.
    
    # Main options
    [main]
         CsvInputFile = entrada.csv
         XmlOutputFile = salida.xml
         XmlTemplate = plantilla.xml
         TemplateNodes = XMLRootElement.element0.node1 XMLRootElement.element2.node0
         # Separator to indicate default values in the XML Template.
         SeparatorKey = |
         # Default value for data without default value in the XML template file
         DefaultValue = 

    # CSV input file (Comma Separated Values)
    [csv]
         # If the CSV has no header, must be given here
         ; Headers = Header1 header2 Header3 Header4
         # CSV separator data character
         delimiter =,
         # Escape character
         ; quotechar = `"`
         # Data encoding. Try to determine the best encoding from de list below
         encoding = utf-8 windows-1252 iso-8859-1 iso-8859-2 us-ascii

    # XML output data
    [xml]
         # End of line character
         ; lineterminator = \n

    # Other values
    [template]
         author = Noe
         date = December 2008

Example input template file:

    <XMLRootElement Author="%%(author)s" date='%%(date|ano da pera)s'>
       <element0 id='%%(NUMBER|0)s'>
          <node1>
             The content is %%(CONTENIDO0|no content)s .
          </node1>
       </element0>
       <element2>
          <node0>
              The content is %%(CONTENIDO2|no content)s .
          </node0>
       </element2>
    </XMLRootElement>

CSV input data file

    NUMBER, CONTENIDO0, CONTENIDO2
    0, prueba0, TEST 0
    1, data1, TEST 1
    2, data 2, TEST 2

The output file is left as an exercise for the reader ... 
""")
    print use % d
    print "\n" + __program__ + " version " + __version__ + ", " + __copyright__
    print "Created by " + __author__ 
    license = _("""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
""")
    print license


if __name__ == "__main__":
    # Args
    try:
        longopts = ["config=", "input=","output=","template=", "templatenodes", "help"]
        opts, args = getopt.getopt(sys.argv[1:], "c:i:o:t:n:h", longopts)
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    output = None
    input = None
    template = None
    # Set up default config file name
    config = os.path.splitext(sys.argv[0])[0] + '.cfg'
    templatenodes = None
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        if o in ("-c", "--config"):
            config = a
        if o in ("-i", "--input"):
            input = a
        if o in ("-o", "--output"):
            output = a
        if o in ("-t", "--template"):
            template = a
        if o in ("-n", "--templatenodes"):
            templatenodes = a
    # Check if it is necessary a config file ...
    if output and input and template and templatenodes:
        needconfigfile = False
    else:
        msg(_("Searching config file ..."))
        needconfigfile = True
    # Read the config file ...
    hasconfigfile = True
    configuration = ConfigParser.ConfigParser()
    if not os.path.isfile(config):
        hasconfigfile = False
        if needconfigfile:
            toolbox.die(_("Cannot find the configuration file '%s'.") % os.path.basename(config))
    if hasconfigfile:
        try:
            msg(_("Reading configuration file '%s' ...") % os.path.basename(config))
            configuration.read(config)
        except:
            toolbox.die(_("Cannot understand config file format '%s'.") % os.path.basename(config))
    # Override the configuration values of the file if they are in the 
    # line parameters of the program.
    defaultconfig = {}
    defaultconfig['main'] = {}
    defaultconfig['main']['csvinputfile'] = input
    defaultconfig['main']['xmloutputfile'] = output
    defaultconfig['main']['xmltemplate'] = template
    defaultconfig['main']['templatenodes'] = templatenodes 
    defaultconfig['csv'] = {}
    defaultconfig['xml'] = {}
    defaultconfig['template'] = {}
    if hasconfigfile:
        options = toolbox.configRead(configuration, defaultconfig)
    else:
        msg(_("Using default compiled values ..."))
        options = defaultconfig
    if options['main'].has_key('templatenodes'):
        options['main']['templatenodes'] = options['main']['templatenodes'].split()
    else: 
        options['main']['templatenodes'] = []
    if options['csv'].has_key('headers'):
        options['csv']['headers'] = options['csv']['headers'].split()
    else: 
        options['csv']['headers'] = []
    # Default values if they were not set up
    options['csv'].setdefault('delimiter', CSVdelimiter)
    options['csv'].setdefault('quotechar', CSVquotechar)
    options['csv'].setdefault('encoding', CSVencoding)
    options['csv']['encoding'] = options['csv']['encoding'].split()
    options['main'].setdefault('separatorkey', XMLseparatorKey)
    options['main'].setdefault('defaultvalue', XMLdefaultValue)
    options['xml'].setdefault('lineterminator', XMLlineterminator)
    # Main program
    main(options)
    sys.exit()


#EOF

