grep match_pattern filename

grep word filename --color=auto

grep -E "[a-z]+": -E:表示使用拓展的grep，即egrep，支持正则表达式

grep -o:只输出匹配部分
grep -v:反转，只输出不匹配部分

grep -c "text" filename:统计匹配部分出现的行数

grep -n:打印出匹配字符串所在行数

grep -b -o 打印出匹配字符串在该行的字符偏移数,从0开始计数
grep -l PATTERN filename1 filename2 filename3:输出包含匹配内容的文件名
grep -L PATTERN filename1 filename2 filename3:输出不包含匹配内容的文件名

grep PATTERN path -R -n :在path及其子目录中递归搜索匹配点，并输出匹配行数

grep -i 忽略大小写

grep -e PATTERN1 -e PATTERN2 :多样式匹配
grep -f pattern_file source_file:从pattern_file 中的匹配方式来匹配

--include *{.cpp,.c,.sh,.h}:只匹配某些内容
--exclude *** 	不匹配这些内容

--exclude-dir:排除某些目录

grep -Z:匹配以0值字符结束的内容
grep -q:静默输出，只输出是否存在

grep -B number :打印匹配行之前的number行
grep -A number :打印匹配行之后的number行
grep -C number :打印匹配行之前和之后的number行


