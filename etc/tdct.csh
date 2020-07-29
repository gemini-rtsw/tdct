#!/bin/csh

if ( -f ./Makefile ) then
   set TOP=`grep -m 1 "TOP=" ./Makefile | cut -d= -f2`
else 
   echo "No makefile from which the get TOP!"
   exit 1;
endif

if ( -z "$TOP" ) then
   echo "TOP not defined!"
   exit 1
endif

echo "TOP: $TOP"
echo

set dbPaths=`convertGemRelease.pl -T${TOP} dbPaths | tr " " ":" | sed 's/^://'`
if ( ! -z "${dbPaths}" ) then
   setenv SYS_TDCT_PATHS ${dbPaths}:${SYS_TDCT_PATHS}
endif
echo "SYS_TDCT_PATHS: ${SYS_TDCT_PATHS}"
echo

set schPaths=`convertGemRelease.pl -T${TOP} schPaths | tr " " ":" | sed 's/^://'`
setenv TDCT_SCH_PATHS ${schPaths}
echo "TDCT_SCH_PATHS: ${TDCT_SCH_PATHS}"
echo
setenv TDCT_BROWSER /usr/bin/firefox

java -jar ${TDCT}/tdct.jar -cfg ./tdct.cfg $*
