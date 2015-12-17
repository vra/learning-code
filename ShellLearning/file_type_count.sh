#!/bin/bash

# this script print types and numbers of each type of file in target directory 

if [ $# -ne 1 ];
then
	echo $0 basepath;
	echo
fi

path=$1

#declare variable ,-A indicate the variable is a array 
declare -A statarray

#done < filename: read line from filename
while read line;
do
	ftype=`file -b $line | cut -d, -f1`
	let statarray["$ftype"]++
done< <(find $path -type f -print)


echo ==============File types and counts============

#$array[@]:return each element of array
for ftype in "${!statarray[@]}";
do	
	echo $ftype : ${statarray["$ftype"]}
done

