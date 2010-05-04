��          �      ,      �  e  �  �  �  	   �  (   �  I   �  J        X  *   w     �  J   �  /     #   8     \  !   v     �     �  P  �  e    *  ~  	   �$  (   �$  I   �$  J   &%     q%  *   �%     �%  J   �%  /   !&  #   Q&     u&  !   �&     �&     �&                             
                             	                    
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
  
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
         ; lineterminator = 


    # Other values
    [template]
         author = Noe
         date = December 2008

Example of input template file:

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

CSV input data file for the above XML template:

    NUMBER, CONTENIDO0, CONTENIDO2
    0, prueba0, TEST 0
    1, data1, TEST 1
    2, data 2, TEST 2

The output file is left as an exercise for the reader ... 
 - ERROR:  Cannot find the configuration file '%s'. Cannot open '%(input)s' for reading: I/O error (%(errno)s): %(strerror)s. Cannot open '%(output)s' for writing: I/O error (%(errno)s): %(strerror)s. Cannot parse XML template: %s. Cannot understand config file format '%s'. Processing CSV data: '%s'. Processing input file '%(input)s' with XML template '%(xmltemplate)s' ...  Reading CSV file, line %(line)s: %(exception)s. Reading configuration file '%s' ... Searching config file ... Using default compiled values ... XML file '%s' generated. ~ %s processed lines. Project-Id-Version: 0.3.0
Report-Msgid-Bugs-To: Jose Riguera <jriguera@gmail.com>
POT-Creation-Date: 2010-05-04 21:37+0200
PO-Revision-Date: 2010-05-04 22:30+0200
Last-Translator: Jose Riguera Lopez <jriguera@gmail.com>
Language-Team: English <>
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
 
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.
  
[python] %(program)s [-c <file>] [-i <file>] [-n 'root.node ...'] [-o <file>] [-t <file>]

Options:

        -c, --config <file>                Configuration file.
        -h, --help                         Show this help and exits.
        -i, --input <file>                 Input data in CSV format.
        -n, --templatenodes "root.node"    Template node(s) (in XML Template).
        -o, --output <file>                XML output file.
        -t, --template <file>              XML input Template.

The XML resulting file is generated from the structure of the XML Template file by repeating those nodes indicated by "templatenodes" (see configuration file) for each line of data in the CSV input file. To do this, the program replaces the headers listed in XML Template with data from each line of the CSV file, generating the same number of nodes that lines in CSV file. The nodes are indicated with the complete 'path' from the root node of the XML document to the node to be "repeated", each element is separated by '.' , for example: "XMLRootElement.element.node". The root node is not a valid template node, for obvious reasons. 

The CSV input file and/or XML output file can be stdin and stdout (respectively) by simply stating '-' instead of the file name. 

The program looks for the default configuration file "csv2xmlgen.cfg", but it is not necessary if all the arguments of the program are supplied, the rest of arguments take the default value. These entries are permitted and established by default in the configuration file:

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
    ; lineterminator = 


    # Other values
    [template]
    author = Noe
    date = December 2008

Example of input template file:

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

CSV input data file for the above XML template:

    NUMBER, CONTENIDO0, CONTENIDO2
    0, prueba0, TEST 0
    1, data1, TEST 1
    2, data 2, TEST 2

The output file is an exercise for the reader ... 
 - ERROR:  Cannot find the configuration file '%s'. Cannot open '%(input)s' for reading: I/O error (%(errno)s): %(strerror)s. Cannot open '%(output)s' for writing: I/O error (%(errno)s): %(strerror)s. Cannot parse XML template: %s. Cannot understand config file format '%s'. Processing CSV data: '%s'. Processing input file '%(input)s' with XML template '%(xmltemplate)s' ...  Reading CSV file, line %(line)s: %(exception)s. Reading configuration file '%s' ... Searching config file ... Using default compiled values ... XML file '%s' generated. ~ %s processed lines. 