#!/bin/sh

#
#打印当前目录下的符号链接
#

#符号链接文件的权限标记部分都是以l开头的
#第8部分为文件名
ls -l | grep "^l" | awk '{ print $8 }'

#第二种方法
find . -type l -print

#打印出符号链接的指向目标
ls -l symbolink | awk '{ print $10 }'

#第二种方法
readlink symbolink

