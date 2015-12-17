#!/usr/bin/expect

#spawn:指定需要自动化哪一个命令
#注意:需要让interactive.sh 获得执行权限
spawn ./interactive.sh

#expect 提供需要指定的消息
expect "Enter number:"

#send :要发送的消息
send "1\n"

expect "Enter name:"
send "hello\n"

expect eof

