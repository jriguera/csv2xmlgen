#!/usr/bin/env bash
#
# A script to generate a kmz layer with photos using csv2xmlgen
# Author: Jose Riguera Lopez <jriguera@gmail.com> January 2009
# License: GNU General Public License v3 or later
#

# Default values
CSV2XMLGEN=./csv2xmlgen.py
ZIPPROGRAM=zip
ZIPOPTIONS="-1 -m"


# Program

help() {
    cat <<HELP 
Usage:
    $(basename $0) csv2xmlgen.cfg /photo/source/dir output.kmz 
   
    This script generates a KMZ file (Google Earth Layer) with the output file of csv2xmlgen.
    It gets all pictures from "/photo/source/dir" and compress then with zip program in order to
    create a kmz file.
    It is necessary to create a XML template and a configuration file according to data in CSV
    file in order to generate the desired kmz file.
    
HELP
}

EXPECTED_ARGS=3
CSV2XMLGENCFG=$1
PHOTODIR=$2
OUTKMZ=$3

if [ $# -lt $EXPECTED_ARGS ]; then
    help
    exit 1
fi
if [ ! -d "$PHOTODIR" ]; then
    echo "ERROR: Cannot access to $PHOTODIR ."
    help
    exit 1
fi
if [ ! -f "$CSV2XMLGENCFG" ]; then
    echo "ERROR: Cannot find $CSV2XMLGENCFG ."
    help
    exit 1
fi

rvalue=0
output=$(grep -i XmlOutputFile "$CSV2XMLGENCFG" | cut -d'=' -f 2)
$CSV2XMLGEN -c "$CSV2XMLGENCFG"
if [ $rvalue != 0 ]; then 
    echo "ERROR: generating $output ."
    exit $rvalue
fi
if ! echo "$OUTKMZ" | grep -qe "^/"; then
    programdir=$(cd $(dirname "$0"); pwd)
    OUTKMZ="$programdir/$OUTKMZ"
fi

echo "Generating $OUTKMZ ..."
tempdir=$(mktemp -d)
cp $PHOTODIR/*.* "$tempdir"
cp $output "$tempdir"
(
    cd $tempdir
    $ZIPPROGRAM $ZIPOPTIONS $OUTKMZ *.*
    rvalue=$?
)
rm -rf "$tempdir"

if [ $rvalue = 0 ]; then 
    echo "$OUTKMZ generated."
fi
exit $rvalue

