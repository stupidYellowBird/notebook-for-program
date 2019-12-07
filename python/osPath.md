
# os.path

```python
 os.path.abspath("d:\\new\\test.txt")  #返回绝对路径
 os.path.basename("d:\\new\\test.txt") #返回文件名
 os.path.dirname("d:\\new\\test.txt") #返回文件夹路径
 os.path.exists("d:\\new")  #
 os.path.lexists("d:\\new")
 os.path.expanduser("d:\\new\\text.txt")
 os.path.getatime("d:\\new")  #最后文件的访问时间
 os.path.getmtime("d:\\new") #最后修改路径时间
 os.path.getctime("d:\\new")  #创建时间
 os.path.getsize("d:\\new\\")  #或许路径的大小 字节为单位
 os.path.isabs("d:\\")  #是否是绝对路径
 os.path.isfile("d:\\new\\hello.txt")   #判断是否是文件
 os.path.isdir("d:\\new")   #判断是否是目录
 os.path.islink("d:\\new\\hello.txt") #判断是否是链接
 os.path.join("d:\\new","hello.txt")    #合并文件路径
 os.path.normcase("d:\\new\\hello.txt")
 os.path.relpath("d:\\new\\hello.txt")  #相对路径
 os.path.split("d:\\new\\hello.txt")  #分离文件名，返回一个
 os.path.splitdrive("d:\\new\\hello.txt")  #分离磁盘驱动器
 os.path.splitext("d:\\new\\hello.txt")  #分离文件名和扩展名
```

## pathlib 面向对象的path

```python
# from pathlib import *
path()

```
