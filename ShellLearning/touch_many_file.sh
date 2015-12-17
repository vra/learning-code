#!/bin/sh

for name in {1..100}.txt
do 
	touch $name
done

#touch -a 只改变文件访问时间
#touch -m 只更改文件内容修改时间
