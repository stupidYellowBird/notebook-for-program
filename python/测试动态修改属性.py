# 动态修改类和对象
class Person():
    # __slots__限制实例能动态添加的属性
    # 更快的属性访问速度
    # 更小的内存消耗,当需要大量创建实例时，每个实例都有个__dict__字典来存储实例变量，浪费内存
    
    # 实例的dict只保持实例的变量，对于类的属性是不保存的，类的属性包括变量和函数。
    # 由于每次实例化一个类都要分配一个新的dict，因此存在空间的浪费，因此有了__slots__。
    # __slots__是一个元组，包括了当前能访问到的属性。
    # 当定义了slots后，slots中定义的变量变成了类的描述符，相当于java，c++中的成员变量声明，
    # 类的实例只能拥有slots中定义的变量，不能再增加新的变量。注意：定义了slots后，就不再有dict。
   
    # 一般，任何类的实例包含一个字典__dict__,
    # Python通过这个字典可以将任意属性绑定到实例上。

    __slots__=('age','name','say')
    pass
# 添加类变量
Person.name = 'tom'
tom =Person()
print(tom.name)
# 添加实例变量
tom.age=18
print(tom.name)

def say(self,sth):
    print('my name is {0.name}，{1}'.format(self,sth))

# 给类添加方法
Person.say=say
tom.say('nice to meet you')
# __slots__允许类动态添加新的属性
Person.tel='1111'
print(tom.tel)
# __slots__ 不允许实例动态添加属性
# tom.address='new york'
# print(tom.address)

# __slots__的继承问题
# 1.子类中没有 __slots__，而父类中有，父类的__slots__对当前类不起作用
class student(Person):
    pass

student.address='new  york'
tom =student()
print(tom.address)

# 2.子类中有__slots__，而父类中有，只要子类__slots__生效

# 为了能使用动态属性,在__slots__中添加__dict__
__slots__=('__dict__',)