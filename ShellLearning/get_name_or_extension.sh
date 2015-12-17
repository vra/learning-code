#!/bin/bash

#file name :get_name_or_extension.sh
#do what: practise using of %,%%,#,##

file_jpg="sample.jpg"
name=${file_jpg%.*}
extension=${file_jpg#*.}

echo all File name is: $file_jpg,
echo name:$name,
echo extension: $extension

var=hack.fun.book.txt

echo ${var%%.*} #result is hack
echo ${var%.*} #result is hack.fun.book

echo ${var#*.} #result is fun.book.txt
echo ${var##*.} #result is txt
