
---





---


# Introduccion #

**csv2xmlgen** is a python program to generate XML files based on a input
template. It has been developed for generating KML files (Google Earth
layers) from CSV data, but it can be used to process any kind of XML
defined with the suitable template.

## Details ##

The XML resulting file is generated from the structure of the XML Template
file by repeating those nodes indicated by "_templatenodes_" (see configuration
file) for each line of data in the CSV input file. To do this, the program
replaces the headers listed in XML Template with data from each line of the
CSV file, generating the same number of nodes that lines in CSV file. The
nodes are indicated with the complete 'path' from the root node of the XML
document to the node to be "repeated", each element is separated by **.** (dot),
for example: "_XMLRootElement.element.node_". The root node is not a valid
template node, for obvious reasons.

## Options ##

The program looks for the default configuration file "_csv2xmlgen.cfg_", but it
is not necessary if all the arguments of the program are supplied, the rest
of arguments take the default value.

### Command line arguments ###

```
[python] csv2xmlgen.py [-c <file>] [-i <file>] [-n 'root.node ...'] [-o <file>] [-t <file>]
```

Command line options:
```
        -c, --config <file>                Configuration file.
        -h, --help                         Show this help and exits.
        -i, --input <file>                 Input data in CSV format.
        -n, --templatenodes "root.node"    Template node(s) (in XML Template).
        -o, --output <file>                XML output file.
        -t, --template <file>              XML input Template.
```

The CSV input file and/or XML output file can be _stdin_ and _stdout_
(respectively) by simply stating **-** instead of the file name.

### Configuration file ###

These entries are permitted and established by default in the
configuration file:

```
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
# Delete entrys (and children) with this tag if key is not found.
DeleteTag = -

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

# EOF
```

### XML Template file ###

Contents of example input template file _plantilla.xml_:

```
<XMLRootElement Author="%(author)s" date="%(date|ano da pera)s">
       <element0 id="%(NUMBER|0)s">
          <node1 id="%(NUMBER|0)s">
             The content is %(CONTENIDO0|no content)s .
          </node1>
       </element0>
       <element2>
          <node0 id="%(NUMBER|-)s">
              The content is %(CONTENIDO2|-)s .
          </node0>
       </element2>
</XMLRootElement>
```

### CSV input data ###

CSV input data file for the above XML template, _entrada.csv_:

```
NUMBER,CONTENIDO0,CONTENIDO2
0,prueba0,TEST 0
1,,
2,data 2,TEST 2
```

### XML Output file ###

```
<?xml version="1.0" encoding="utf-8"?>
<XMLRootElement Author="Jose" date="December 2008">
   <element0 id="0">
      <node1 id="0">
             The content is  prueba0 .
      </node1>
      <node1 id="1">
             The content is no content .
      </node1>
      <node1 id="2">
             The content is  data 2 .
      </node1>
   </element0>
   <element2>
      <node0 id="0">
              The content is  TEST 0 .
      </node0>
      <node0 id="2">
              The content is  TEST 2 .
      </node0>
   </element2>
</XMLRootElement>
<!--XML generated with csv2xmlgen version 0.4.0 at Sun Jan  9 21:44:39 2011.-->
<!--csv2xmlgen (c) Jose Riguera, October 2008, a GPL (v3 or later) program created by Jose Riguera Lopez <jriguera@gmail.com>.-->

```