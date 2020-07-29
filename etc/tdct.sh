#!/bin/sh

if [ -f ./Makefile ]
then
   TOP=`grep -m 1 "TOP=" ./Makefile | cut -d= -f2`
else 
   echo "No makefile from which the get TOP!"
   exit 1;
fi

if [ -z "$TOP" ]; then
   echo "TOP not defined!"
   exit 1
fi

echo "TOP: $TOP"
echo

dbPaths=`convertGemRelease.pl -T$TOP dbPaths | tr " " ":" | sed 's/^://'`
if [ ! -z "$dbPaths" ]; then
   export SYS_TDCT_PATHS=$dbPaths:$SYS_TDCT_PATHS
fi
echo "SYS_TDCT_PATHS: $SYS_TDCT_PATHS"

schPaths=`convertGemRelease.pl -T$TOP schPaths | tr " " ":" | sed 's/^://'`
export TDCT_SCH_PATHS=$schPaths
echo "TDCT_SCH_PATHS: $TDCT_SCH_PATHS"
echo "EPICS_EXTENSIONS: $EPICS_EXTENSIONS"
echo

export TDCT_BROWSER=/usr/bin/firefox
java -jar $TDCT/tdct.jar -ignoreversion -cfg ./tdct.cfg $@
