# python 的字典
# 键key是不可变对象，字符串、数值、元组，
# 访问字典元素，d[key]
# 删除字典元素 del d[key]

d = {'a':2,'b':3,}
# 以列表的形式，返回key的集合
d.keys()
# 以列表的形式，返回value集合
d.values()
# 随机弹出一个键值对
d.popitem() -> tuple(key,value)
# 弹出指定键key
d.pop(key,default)
# 以列表的形式，返回键值对(key,value)元组集合
d.items()
# 用序列sequence初始化一个字典，初始值为value
d.fromkeys(seq,value)
# 清除字典元素
d.clear() -> None
# shallow copy浅复制
d.copy()
# 如果d[key]不存在，则设置d[key]=default
d.setdefault(key,default=None)
# 如果key不存在，返回default
d.get(key,default)
# python3.x不包含has_key()函数，用__contain__
# python2 用has_key()
d.__contains__(key)
# 添加dict2的键值对
d.update(dict2)

