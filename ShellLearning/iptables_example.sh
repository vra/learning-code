#!/bin/bash

#flush the selected chain. if none is given, equal to delete all rules one by one
iptables -F
iptables -X

#delete rules in nat talbe
iptables -t nat -F
iptables -t nat -X

#INPUT表示对网关的访问,这里表示不允许任何人访问网关
iptables -P INPUT DROP

#OUTPUT 表示网关对外部网络的访问,允许访问任何地址
iptables -P OUTPUT ACCEPT

#FORWARD 表示转发端口.默认将所有转发的数据都丢弃
iptables -P FORWARD DROP

iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT 
iptables -A FORWARD -m state --state ESTABLISHED RELATED -j ACCEPT 
