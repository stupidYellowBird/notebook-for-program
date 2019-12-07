# python编码问题

1. 字符串通过编码转换为字节码，字节码通过解码转换为字符串
str--->(encode)--->bytes，bytes--->(decode)--->str

2. 输出系统编码
import sys
print('目前系统的编码为：',sys.getdefaultencoding())

decode()括号中为什么写utf-8，而不写gbk，可以这样理解，因为要解码，你总得告诉它我是什么编码的吧，比如我原先是utf-8格式的编码，现在要解码，但是如果冒充utf-8，说自己是gbk，那就会出现乱码

utf-8和gbk之间都是通过unicode来做一个中间转换的操作

