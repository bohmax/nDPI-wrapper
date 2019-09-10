#!/bin/bash
NDPIDEST=../src/lib
READERDEST=../example

#file to copy to ndpi library
cp ndpi_wrap.c $NDPIDEST
if [ $? -ne 0 ]
then
    exit 1
fi
#assume the other one we will correct if the first ne have success
cp ndpi_example.py $NDPIDEST
cp ndpi_typestruct.py $NDPIDEST

#file to copy in the Reader
cp Reader_wrap.c $READERDEST
if [ $? -ne 0 ]
then
    exit 1
fi
#assume the other one we will correct if the first ne have success
cp Reader_struct.py $READERDEST
cp Reader_example.py $READERDEST
cp Reader_wrap.py $READERDEST
cp Makefile.wrap $READERDEST

cd $READERDEST

#gcc -c -I../include ndpi_wrap.c
make -f Makefile.wrap