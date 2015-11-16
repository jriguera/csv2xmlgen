
---





---


# Introduction #

The program **csv2xmlgen** is a XML generator based on the template system developed
in the **sxmltemplate.py** module/package. This package can be considered the core
of the program.

## Details ##

The module contains a class which generates XML documents based on a template
source (file, string, ...) setting the part of XML template which will be cloned
and repeated on each input data.
Clue: http://blog.ianbicking.org/templating-via-dict-wrappers.html

### Implementation ###

Here you are the code. The class **`TemplateDict`** inherits from python class
**`dict`** (python dictionary) and redefines **`__getitem__`** method which is
used by the string operator **`%`** (python string template operator). The rest
of code works with XML documents using the API of **minidom** and **csv** modules.

You can see the full source code in _Source_ section.

```
# ###################################
# SXMLTemplate implementation package
# ###################################

class SXMLTemplate:
    """
    Base class for Simple XML Templates

    It generates a XML DOM document that is based on a xml template source (file, string ...) 
    that will be filled with external data by appending the selected new xml elements with  
    data. Into XML input template, it changes all keys with the format $(key|defautlvalue)s 
    into the data of "key" from the param dictionary, or "defaultvalue" if key is not found 
    in dictionary.
    
    Public Attibutes:

        :param sizeLimit: = 1024 -> (bytes) max size of template source.
        :param separatorKey: = "|" -> separator for default key values.
        :param separatorXml: = "." -> separator to indicates repeateable elements.
        :param defaultValue: = "NULL" -> default value for keys without default values.
        :param deletetag: = "" -> with this value, a key will be deleted if not exists.
    """
    sizeLimit = 1048576 
    separatorKey = "|"
    separatorXml = "."
    defaultValue = " "
    deletetag = "-"
    magic = "-#_---__-"


    class TemplateDict(dict):
        """
        Class for string templates with dictionaries objects and operator %

        This class inherits all attributes, methods, ... from dict and redefines "__getitem__"
        in order to return a default value when an element is not found. The format 
        "key<separator>defaultvalue" indicates that if "key" is not found, then "defaultvalue" 
        will be returned. It is like an OR: returns value or "defaultvalue". 
        It is possible to define a global default value for all keys.
        """
        def __getitem__(self, key):
            try:
                k, default = key.split(SXMLTemplate.separatorKey, 1)
            except ValueError:
                k = key.split(SXMLTemplate.separatorKey, 1)[0]
                default = SXMLTemplate.defaultValue
            random = SXMLTemplate.magic
            value = self.get(k, default + random)
            if value == SXMLTemplate.deletetag + random:
                raise UserWarning
            return self.get(k, default)
# [...]
```