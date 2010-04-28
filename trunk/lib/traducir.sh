#!/bin/sh

xgettext --default-domain=sxmltemplate --output=locale/sxmltemplate.pot sxmltemplate.py exceptions.py
mkdir -p locale/es/LC_MESSAGES
mkdir -p locale/en/LC_MESSAGES
cp locale/sxmltemplate.pot locale/es/sxmltemplate.po
nano locale/es/sxmltemplate.po
msgfmt --output-file=locale/es/LC_MESSAGES/sxmltemplate.mo locale/es/sxmltemplate.po
cp locale/es/sxmltemplate.po locale/en/sxmltemplate.po
nano locale/en/sxmltemplate.po
msgfmt --output-file=locale/en/LC_MESSAGES/sxmltemplate.mo locale/en/sxmltemplate.po


xgettext --default-domain=toolbox --output=locale/toolbox.pot iosys.py exceptions.py string.py
mkdir -p locale/es/LC_MESSAGES
mkdir -p locale/en/LC_MESSAGES
cp locale/toolbox.pot locale/es/toolbox.po
nano locale/es/toolbox.po
msgfmt --output-file=locale/es/LC_MESSAGES/toolbox.mo locale/es/toolbox.po
cp locale/es/toolbox.po locale/en/toolbox.po
nano locale/en/toolbox.po
msgfmt --output-file=locale/en/LC_MESSAGES/toolbox.mo locale/en/toolbox.po

