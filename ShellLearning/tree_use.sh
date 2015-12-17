tree path -P PATTERN:打印path下面的符合PATTERN的文件
例子:tree / -P "*.txt"

tree path -I PATTERN: 忽略path 目录下符合PATTERN的文件

tree -h:同时打印出文件和目录的大小

tree path -H http://localhost -o output.html:在当前目录下生成HTML格式的树形文件
