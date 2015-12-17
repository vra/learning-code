#!/bin/sh
#this program is used to calculate the area of a triangle

#-n option make sure not begin a new line
echo -n "input h:"
read h

echo -n "input b:"
read b

#scale=2表示保留2位小数
area=$(echo "scale=2;(1/2) * $b * $h" | bc)
echo "area of this triangle is $area"

