# 面向对象


# 私有变量
# 属性名称前加两个下划线__name,变成私有变量
# 解释器把双下划线的私有变量转换为  _classname__name，任然可以访问私有变量
# 单下划线开头的变量也是私有变量，约定熟成
# 获取变量可以定义函数get_name,设置函数定义set_name,用来对参数进行检查
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')
    
    def set_score(self, score):
        self.__score = score

# property装饰器
# 定义只读属性，就只定义getter方法，不定义setter方法
class Student(object):
    
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

# 
# 
# 
# 多继承之mixin（混入）模式
# 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。
# 但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为Mixin。


# 枚举类
from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# 这样我们就获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员：
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
# value属性则是自动赋给成员的int常量，默认从1开始计数。
# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
from enum import Enum, unique
@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
# @unique装饰器可以帮助我们检查保证没有重复值。

#  getattr 和 getattribute
# 当调用某个不存在的属性是，Python 会调用 getattr 函数。
# 当调用任何一个属性时，Python 都会调用 getattribute 函数。通常不建议重写该方法，
# 该方法把持了所有调用属性的入口，如果重写的不好，可能会弄巧成拙。


# 元类编程

# 使用type()动态创建类,三个参数
# 1. class的名称name；
# 2. 继承的基类集合，注意Python支持多重继承，如果只有一个基类，别忘了tuple的单元素写法；
# 3. class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上，即__dict__属性。

type(name:str,bases:tuple,dict:Dict) 

# 使用metaclass控制类的行为
# 先metaclass，再class，后实例
# 类是对象，叫类对象。类对象的类叫元类。
# type --> class(对象) -->instance
# python2.x 使用__metaclass__
# python3.x

class b(object，metaclass=Metaclass):
    pass
# 定义metaclass,必须继承至type
class Metaclass(type):
    def __new__(cls,*arg,**kw):
        return super.__new__(cls,*arg,**kw)

# 当既有基类又有 metaclass 时，会首先找 metaclass，现在当前的类中找 metaclass，如果找不带，就在
#  BaseClass 中找 metaclass，如果还找不到，就在模块中找 metaclass。如果都找不到就调用 type 创建。






