# 1.字母处理
#首字母大写
str.capitalize()
# 首字母全部小写
str.casefold()
#交换大小写
str.swapcase()
#首字母大写
str.title() 
#全部大写 
str.upper()
#全部小写   
str.lower()

# 2.对齐
# 左对齐
str.ljust(width,[fillchar])
# 右对齐
str.rjust(width,[fillchar])
# 居中对齐
str.center(width,[fillchar])
# 右对齐数字字符串，以0填充
str.zfill(width)
# 字符串断句,将字符串中的换行符转换成空格
str.expandtabs(tabsize:int)


# 3.字符串搜索
# 查找是否有子字符串,返回第一次出现的索引，如未找到，返回-1
str.find(sub,start,end)
# 从右往左查找
str.rfind(sub,start,end)
# 统计子字符出现次数
str.count(sub,start,end)
# 检测是否包含子字符串
str.index(sub,start,end)

# 4.通用方法
# 长度
len(str)
# 索引下标切片遍历

# 5.替换
str.replace(old,new,count)
# 返回一个翻译表，用于    str.translate()
str.maketrans()
# 根据table翻译
str.translate(table)

# 6.去除字符串
# 如果chars为空，去除头尾的空格，如果不为空去除指定的字符
str.strip([chars])
str.lstrip([chars])
str.rstrip([chars])

# 7.字符串分割
#将字符串分割成列表,sep分割符，maxsplit最大分割数量
str.split(sep:optionl,maxsplit)
str.rsplit()
# 行分割（\r, \n ,\r\n),keepends为真，则保留换行符
str.splitlines(keepends:bool)
# 分割成三元组(header,sep,tail)
str.partition(sep)

# 8.字符串判断
# 开头
str.startswith(prefix,start=0,end=len(str))
# 结尾
str.endswith(suffix,start,end)
# 是否包含字母和数字
str.isalnum()
# 是否只有数字
str.isdigit()
# 是否只有数字
str.isnumeric()
# 如果全是大写
str.isupper()
# 如果全是小写
str.islower()
# 是否是字母表字母
str.isalpha()
# 是否合法变量名
str.isidentifier()
# 是否全为空格
str.isspace()
# 是否为可打印字符
str.isprintable()
# 是否首字母大写
str.istitle()

# 9.连接
str.join(iterable)
'\n'.join('a','b','c')

# 10.格式化
str.format()


# List列表
# 添加
list.append(object)
# 清除列表
list.clear()
# 浅复制
list.copy()
# 计数
list.count(object)
# 扩展
list.extend(iterable)
# 返回索引
list.index(object,start=0,stop=end)
# 插入
list.insert(index,object)
# 移除并返回
list.pop(index)
# 移除
list.remove(object)
# 反转
list.reverse()
# 排序
list.sort(reverse=False)
# 列表推导式  
# 字典

# 浅复制
dict.copy()
用序列初始化一个字典，默认值都是value
dict.fromkeys(sequence，value=None)
# 如果值不存在，返回None,也可以指定返回的值M
dict.get(key,M)
# 将字典转换为多维数组
dict.items()
# 获取所有的key值
dict.keys()
# 获取所有的值
dict.values()


# 删除元素
dict.pop(key)
del dict['key']
# 随机弹出并返回某个项
dict.popitem()
#清除字典
dict.clear()

# 设置值，如果key存在则返回get(key)
dict.setdefault(key,value)
# 将指定字典的值更新到另一字典中
dict.update()


