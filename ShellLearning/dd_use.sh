#dd命令用法总结
#用法:从if复制内容到of
#
#
dd if=/dev/zero of=junk.data bs=1M count=1

if:表示输入文件的位置,默认是标准输入,所以不指定if的话,会从stdin读取内容
of:表示输出文件的位置,默认是标准输出,所以不指定of的话,会从stdout输出内容


bs: block size,指定块的大小
count:指定复制多少块

此外,dd命令还可以测量内存操作的速度(命令执行输出的最后一行即速度)
