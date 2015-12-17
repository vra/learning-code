#!/bin/sh

#test whether a file is executable

if test -x $1
then
	echo "$1 is executable "
else 
	echo "$1 is not executable"
fi

