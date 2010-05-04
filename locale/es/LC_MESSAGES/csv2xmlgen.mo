��          �      ,      �  e  �  �  �  	   �  (   �  I   �  J        X  *   w     �  J   �  /     #   8     \  !   v     �     �  P  �  �    7  �  	   &  6   "&  Q   Y&  T   �&      '  4   '     Q'  J   m'  4   �'  *   �'  &   (  +   ?(     k(     �(                             
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
PO-Revision-Date: 2010-05-04 22:24+0200
Last-Translator: Jose Riguera Lopez <jriguera@gmail.com>
Language-Team: Spanish <>
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
 
Este programa es software libre: usted puede redistribuirlo y/o modificarlo bajo los términos de la Licencia Pública General GNU publicada por la Fundación para el Software Libre, ya sea la versión 3 de la Licencia, o (a su elección) cualquier versión posterior.

Este programa se distribuye con la esperanza de que sea útil, pero SIN GARANTÍA ALGUNA; ni siquiera la garantía implícita MERCANTIL o de APTITUD PARA UN PROPÓSITO DETERMINADO. Consulte los detalles de la Licencia Pública General GNU para obtener una información más detallada. 

Debería haber recibido una copia de la Licencia Pública General GNU junto a este programa. En caso contrario, consulte <http://www.gnu.org/licenses/>.
  
[python] %(program)s [-c <file>] [-i <file>] [-n 'root.node ...'] [-o <file>] [-t <file>]

Opciones:

        -c, --config <file>                Fichero de configuración.
        -h, --help                         Muestra esta ayuda y sale.
        -i, --input <file>                 Datos de entrada en formato CSV.
        -n, --templatenodes "root.node"    Nodos de la plantilla XML.
        -o, --output <file>                Fichero XML de salida.
        -t, --template <file>              Plantilla XML de entrada.

El fichero XML resultante se genera a partir de la plantilla de entrada, repitiendo aquellos nodos indicados por "templatenodes" (ver fichero de configuración) ante cada nueva línea de datos del fichero de entrada CSV. Para ello, se sustituyen las cabeceras indicadas en la plantilla XML, con  los datos de cada línea CSV, generando el mismo número de nodos que líneas del fichero CSV. Los nodos se indican con el 'camino' completo desde el nodo raíz del documento XML hasta el nodo que debe repetirse, separando cada elemento por '.', por ejemplo: "XMLRootElement.element.node". El nodo raíz no es un elemento plantilla válido, por motivos obvios.

El fichero de entrada CSV y/o el fichero XML de salida pueden ser la entrada y salida estándar (respectivamente) simplemente indicando '-' en lugar del fichero.

Por defecto se busca el fichero de configuración "csv2xmlgen.cfg", pero no es necesario tener el fichero si establecen todos los argumentos del programa, para el resto de argumentos se toman los valores por defecto. Las entradas permitidas y establecidas por defecto son las siguientes:

    # Fichero de configuración del programa csv2xmlgen. 
    # Todas las secciones son obligatorias, aunque no tengan contenido. 
    # Esto es un comentario, no se procesa, y ...
    ; este es otro comentario que tampoco se tiene en cuenta.
    # Aquí se muestran los parámetros por defecto.

    # Opciones principales
    [main]
    CsvInputFile = entrada.csv
    XmlOutputFile = salida.xml
    XmlTemplate = plantilla.xml
    TemplateNodes = XMLRootElement.element0.node1 XMLRootElement.element2.node0
    # Separador para indicar valores por defecto en la plantilla.
    SeparatorKey = |
    # Valor por defecto, para datos sin valor por defecto.
    DefaultValue = 

    # Datos de entrada CSV (Comma Separated Values)
    [csv]
    # Si el CSV, no tiene cabeceras, se deben indicar aquí.
    ; Headers = Header1 Header2 Header3 Header4
    # Separador de los datos de entrada.
    delimiter = ,
    # Carácter de escape.
    ;quotechar = "
    # Codificación de los datos. Intenta determinar la mejor codificación
    # a partir de la lista indicada.
    encoding = utf-8 windows-1252 iso-8859-1 iso-8859-2 us-ascii

    # Datos de salida XML
    [xml]
    # Carácter fin de línea.
    ; lineterminator = \\r\\n

    # Valores para indicar plantilla por defecto.
    [template]
    autor = Noe
    fecha = Octubre 2008

Ejemplo de plantilla XML de entrada:

    <XMLRootElement author="%%(autor)s" date="%%(fecha|ano da pera)s">
        <element0 id="%%(NUMBER|0)s">
            <node1>
                El contenido 0 es %%(CONTENIDO0|sin contenido)s
            </node1>
        </element0>
        <element2>
            <node0>
                El contenido 2 es %%(CONTENIDO2|sin contenido)s
            </node0>
        </element2>
    </XMLRootElement>

Datos CSV de entrada para la plantilla XML anterior:

    NUMBER,CONTENIDO0,CONTENIDO2
    0,prueba0,prueba2
    1,datos csv,datos csv
    2, entrada,contenido

El fichero de salida se deja como ejercicio al avispado lector ...
 - ERROR:  Imposible encontrar el fichero de configuración '%s'. Imposible abrir '%(input)s' para lectura: Error de E/S (%(errno)s): %(strerror)s. Imposible abrir '%(output)s' para escritura: Error de E/S (%(errno)s): %(strerror)s. Imposible analizar XML: %s. Formato del fichero configuración desconocido '%s'. Procesando datos CSV: '%s'. Procesando fichero '%(input)s' con la plantilla XML '%(xmltemplate)s' ...  Leyendo fichero CSV, línea %(line)s: %(exception)s. Leyendo fichero de configuración '%s' ... Buscando fichero de configuración ... Usando valores establecidos por defecto ... Fichero XML '%s' generado. ~ %s líneas procesadas. 