#!/bin/bash

#-e: 对引号里面的内容使用转义字符
#注意：执行的时候要用 bash + 文件名来执行
echo -e "\e[1;30m Black text \e[0m"
echo -e "\e[1;31m Red text \e[0m"
echo -e "\e[1;32m Green text \e[0m"
echo -e "\e[1;33m Yellow text \e[0m"
echo -e "\e[1;34m Blue text \e[0m"
echo -e "\e[1;35m 洋红 text \e[0m"
echo -e "\e[1;36m 青色 text \e[0m"
echo -e "\e[1;37m White text \e[0m"


echo -e "\e[1;40m Black background \e[0m"
echo -e "\e[1;41m Red background \e[0m"
echo -e "\e[1;42m Green background \e[0m"
echo -e "\e[1;43m Yellow background \e[0m"
echo -e "\e[1;44m Blue background \e[0m"
echo -e "\e[1;45m 洋红 background \e[0m"
echo -e "\e[1;46m 青色 background \e[0m"
echo -e "\e[1;47m White background \e[0m"
