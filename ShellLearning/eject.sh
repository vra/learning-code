#!/bin/sh

#eject: 弹出光驱托盘
eject

#eject -t 合上光驱托盘,注意有些硬件不支持这个命令
eject -t

# -T 如果是合上的,则打开,如果是打开的,则合上.有些硬件也不支持这个命令
eject -T


