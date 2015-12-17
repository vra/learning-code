#!/bin/sh

if [ $# -eq 0 ]
then 
	echo "$0: you must give one integers"
	exit 1
fi

if test $1 -gt 0
	then
		echo "$1 is greater than zero"
	else
		echo "$1 is litter than zero"
fi
