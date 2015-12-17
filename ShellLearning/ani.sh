#!/bin/bash
#
#Usage: ani -n -a -s -w -d 
#
#
#help_ani(): To print help
#
help_ani()
{
	echo "Usage: $0 -n -a -s -w -d"
	echo "Options: These are optional arguments"
	echo "-n name of animal"
	echo "-a age of animal"
	echo "-s sex of animal"
	echo "-w weight of animal"
	echo "-d demo values (if any fo the above options are used"
	echo "their values are not taken)"

	exit 1
}


#begin main procedure

#if no arguments given
if [ $# -lt 1 ]; then
	help_ani
fi

isdef=0

while getopts n:a:s:w:d opt
do
	case "$opt" in
	n) na="$OPTARG";;
	a) age="$OPTARG";;
	s) sex="$OPTARG";;
	w) weight="$OPTARG";;
	d) isdef=1;;
	\?) help_ani;;
	esac
done

if [ $isdef -eq 1 ]
then
	echo "Animal name:$na, Age:$age, Sex:$sex, Weight:$weight(user define mode)"
else 
	#set default value
	isdef=0
	na=HelloKitty
	age="3 Month"
	sex=Female
	weight=5kg

	echo "Animal name:$na, Age:$age, Sex:$sex, Weight:$weight(demo  mode)"
fi

