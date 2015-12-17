#!/bin/bash
#file name : interactive.sh

read -p "Enter number:" no;
read -p "Enter name:" name
echo You have entered $no,$name;

#自动向命令发送输出
#echo -e "1\n\hello\n" |./interactive.sh 
#output: You have entered 1,hello

#也可以从文件导入交互式输入数据
#./interactive.sh < input.data
