#
#This file contains some quite useful alias in command line
#

0.如果用一个alias代替的系统原来的命令,通过\command可以执行原命令

1. alias ls= "ls --color=auto"#彩色输出ls结果
2. alias ll="ls --color -al"
3. alias grep="grep --color=auto"
4. mcd(){ mkdir -p "$1"; cd "$1";}
5. cls(){ cd "$1"; ls; }
6. backup(){ cp "$1"{,.bak};}
7. md5check(){ md5sum "$1" | grep "$2";}

#用上一个运行的命令创建一个脚本
8. alias makescript="fc -rnl | head -1 >"

#搜索历史命令:histg [关键字]
9. alias histg="history | grep "

10. alias ..="cd .."
11. alias ...="cd ../.."

#解压任何类型的文档 extract [压缩文件名]
12. extract()
{
	if [ -f $1 ]; then
	case $1 in
	*.tar.bz2) 	tar xjf 	$1 	;;
	*.tar.gz) 	tar xzf 	$1 	;;	
	*.bz2)		bunzip2 	$1	;;	
	*.rar) 		unrar e 	$1 	;;	
	*.gz)		gunzip 		$1	;;
	*.tar)		tar xf 		$1 	;;
	*.tbz2)		tar xjf 	$1	;;
	*tgz)		tar xzf		$1	;;
	*.zip)		unzip		$1	;;
	*.Z)		uncompress	$1	;;
	*.7z)		7z x		$1	;;
	*)			echo "'$1' cannot be extracted via extract()" ;;
	esac

	else
		echo "$1 is not a valid file"
	fi
}

13. alias cmount="mount | column -t"
14. alias meminfo="free -m -l -t"

#找到某个进程的PID: ps? [进程名]
15. alias ps? = "ps aux | grep "

#下载整个网站: websiteget http://www.baidu.com
16. alias websiteget = "wget --random-wait -r -p -e robots=off -U Chromium"

#显示哪些应用程序连接到网络
17. alias listen = "lsof -P -i -n"

#显示活动的端口
18. alias port = "netstat -tulanp"

#有趣的命令
19. alias busy = "cat /dev/uradom | hexdump -C | grep 'ca fe'"
