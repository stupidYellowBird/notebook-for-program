# 魔法函数

# 类的构造与删除
__new__     #
__init__    #实例化后，python自动调用init初始化实例
__del__     #析构函数，使用del删除对象时，调用这个方法
# 在 Python 中，当我们创建一个类的实例时，类会先调用 __new__(cls[, ...]) 
# 来创建实例，然后 __init__ 方法再对该实例（self）进行参数初始化。
# 关于 __new__ 和 __init__ 有几点需要注意：
    # __new__ 是在 __init__ 之前被调用的；
    # __new__ 是类方法，__init__ 是实例方法；
    # 重载 __new__ 方法，需要返回类的实例；
# 一般情况下，我们不需要重载 __new__ 方法。但在某些情况下，
# 我们想控制实例的创建过程，这时可以通过重载 __new_ 方法来实现，比如单例模式。

__base__  #对象基类
__bases__
__name__  #对象名
__class__ #对象类
__mro__   #methd reseach orderd
__doc__   #对象文档


# 二元操作 重载二元运算
+	                object.__add__(self, other)
-	                object.__sub__(self, other)
*	                object.__mul__(self, other)
//	                object.__floordiv__(self, other)
/	                object.__div__(self, other)
%	                object.__mod__(self, other)
**	                object.__pow__(self, other[, modulo])
<<	                object.__lshift__(self, other)
>>	                object.__rshift__(self, other)
&	                object.__and__(self, other)
^	                object.__xor__(self, other)
|	                object.__or__(self, other)

# 扩展二元操作
+=	                object.__iadd__(self, other)
-=	                object.__isub__(self, other)
*=	                object.__imul__(self, other)
/=	                object._                _idiv__(self, other)
//=	                object.__ifloordiv__(self, other)
%=	                object.__imod__(self, other)
**=	                object.__ipow__(self, other[, modulo])
<<=	                object.__ilshift__(self, other)
>>=	                object.__irshift__(self, other)
&=	                object.__iand__(self, other)
^=	                object.__ixor__(self, other)
|=	                object.__ior__(self, other)

# 一元操作符
-	                object.__neg__(self)
+	                object.__pos__(self)
abs()	            object.__abs__(self)
~	                object.__invert__(self)
complex()	        object.__complex__(self)
int()	            object.__int__(self)
long()	            object.__long__(self)
float()	            object.__float__(self)
oct()	            object.__oct__(self)
hex()	            object.__hex__(self)
round()	            object.__round__(self, n)
floor()	            object__floor__(self)  #向下取整
ceil()	            object.__ceil__(self)   #向上取整
trunc()	            object.__trunc__(self)


# 比较函数：          
<	                object.__lt__(self, other)  #less than
<=	                object.__le__(self, other)  #less and equil
==	                object.__eq__(self, other)  #equil
!=	                object.__ne__(self, other)  #not equil
>=	                object.__ge__(self, other)  #great and equil
>	                object.__gt__(self, other)  #great than

# 类的表示、输出：
str()	            object.__str__(self) 
repr()	            object.__repr__(self)
len()	            object.__len__(self)
hash()	            object.__hash__(self) 
bool()	            object.__nonzero__(self) 
dir()	            object.__dir__(self)
sys.getsizeof()	    object.__sizeof__(self)
unicode()           object.__unicode__(self)


# 类容器：
len()	            object.__len__(self)
self[key]	        object.__getitem__(self, key)
self[key] = value	object.__setitem__(self, key, value)
del[key]            object.__delitem__(self, key)
iter()	            object.__iter__(self)
reversed()	        object.__reversed__(self)
in操作	            object.__contains__(self, item)
字典key不存在时	     object.__missing__(self, key)


# 迭代器协议
# 可迭代对象必须实现__iter__方法,__iter__方法返回一个迭代器对象
# 迭代器对象必须实现__next__方法，__next__方法返回一个值
__iter__    #返回一个迭代器对象
__next__    #__next__方法要在完值后抛出StopIteration
# 对象可以同时实现以上两种方法，__iter__返回self


# 上下文管理协议context manager
__enter__(self)     #进入with语句
__exit__(self,exc_type,_exc_val,exc_tb)     #退出with语句
# exc_type 异常类
# exc_val 异常内容
# exc_tb 异常位置
 
__reduce__
__reduce_ex__
__setattr__
__getattr__         #当对象属性不存在时调用这个方法
__delattr__
__getattribute__    #查找对象属性时，无论有没有都会调用这个方法，__getattribute__比__getattr__优先级高

                    #在__getattribute__方法中不要使用self.__dict__，同样会被__getattribute__方法
                    # 拦截，从而造成死循环.另外不要使用.点操作符，也会造成死循环，调用父类的__getattribute__

__getitem__  #当使用for in语句时，如果对象没有实现迭代器协议，即__iter__ __next__方法会查找__getitem__方法，如果没有会报错对象“对象不是迭代器”
__setitem__
__delitem__

__call__   如果是函数或者在类中定义 __call__ 方法，就可以对实例进行调用callable()

    class Point(object):
        def __init__(self, x, y):
            self.x, self.y = x, y
        def __call__(self, z):
            return self.x + self.y + z
    使用如下：

    >>> p = Point(3, 4)
    >>> callable(p)     # 使用 callable 判断对象是否能被调用
    True
    >>> p(6)            # 传入参数，对实例进行调用，对应 p.__call__(6)
    13                  # 3+4+6

# 模块的内置变量
__doc__             文件注释
__file__            
__import__
__name__            标识模块的名字的一个系统变量。假如当前模块是主模块（也就是调用其他模块的模块），
                    那么此模块名字就是”main“，通过if判断这样就可以执行“main”后面的主函数内容；假如此模块是被import的，则此
                    模块名字为文件名字（不加后面的.py），通过if判断这样就会跳过“main”后面的内容；
                    if __name__='main':
__package__


# 代码对象的常用属性




class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __getattr__(self, attr):
        if attr == 'z':
            return 0
        raise AttributeError("Point object has no attribute %s" % attr)

    def __setattr__(self, *args, **kwargs):  
        print 'call func set attr (%s, %s)' % (args, kwargs)
        return object.__setattr__(self, *args, **kwargs)

    def __delattr__(self, *args, **kwargs):  
        print 'call func del attr (%s, %s)' % (args, kwargs)
        return object.__delattr__(self, *args, **kwargs)

>>> p = Point(3, 4)
call func set attr (('x', 3), {})
call func set attr (('y', 4), {})
>>> p.z
0
>>> p.z = 7
call func set attr (('z', 7), {})
>>> p.z
7
>>> p.w
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 8, in __getattr__
AttributeError: Point object has no attribute w
>>> p.w = 8
call func set attr (('w', 8), {})
>>> p.w
8
>>> del p.w
call func del attr (('w',), {})
>>> p.__dict__
{'y': 4, 'x': 3, 'z': 7}
call