# 内置函数
1. abs()　　获取绝对值
    >>> a = -10
    >>> a.__abs__()
    10
2. all()　　接受一个迭代器，如果迭代器的所有元素都为真，那么返回True，否则返回False
3. any()　　接受一个迭代器，如果迭代器里有一个元素为真，那么返回True,否则返回False
4. ascii()　　调用对象的__repr__()方法，获得该方法的返回值.
5. bin(),　6. oct(),  7. hex()  　　三个函数功能为：将十进制数分别转换为2/8/16进制。
8. bool()　　测试一个对象是True还是False.
9. bytes()　　将一个字符串转换成字节类型
    >>> s = 'python'
    >>> x = bytes(s, encoding='utf-8')
    b'python'
    >>> a = '王'
    >>> s = bytes(a, encoding='utf-8')
    b'\xe7\x8e\x8b'
10. str()　　将字符类型/数值类型等转换为字符串类型
    >>> str(b'\xe7\x8e\x8b', encoding='utf-8')  # 字节转换为字符串
    '王'
    >>> str(1)   # 整数转换为字符串
    '1'
11. callable()　　判断对象是否可以被调用，能被调用的对象就是一个callables对象，比如函数和带有__call__()的实例。
    >>> callable(max)
    True
    >>> callable([1, 2, 3])
    False
    >>> callable(None)
    False
    >>> callable('str')
    False
12. char()，13. ord()　　查看十进制数对应的ASCII字符/查看某个ASCII对应的十进制数。
    >>> chr(-1)
    Traceback (most recent call last):
    File "<pyshell#26>", line 1, in <module>
        chr(-1)
    ValueError: chr() arg not in range(0x110000)
    >>> chr(0)
    '\x00'
    >>> ord('\x00')
    0
    >>> ord('7')
    55
14. classmethod()　　
15. complie()　　将字符串编译成python能识别或可以执行的代码，也可以将文字读成字符串再编译。
    compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
    将source编译为代码或者AST对象。代码对象能过通过exec语句来执行或者eval()进行求值。
    参数source：字符串或者AST（abstract syntax trees）对象。
    参数filename：代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。
    参数model：指定编译代码的种类。可以指定'exec', 'eval', 'single'。
    参数flag和dont_inherit：这两个参数为可选参数。

    >>> s  = "print('helloworld')"
    >>> r = compile(s, "<string>", "exec")
    >>> r
    <code object <module> at 0x000001C648038390, file "<string>", line 1>
16. complex()
    创建一个值为real + imag * j的复数或者转化一个字符串或数为复数。如果第一个参数是字符串，则不需要指定第二个参数。
    参数real：int，long，float或字符串。
    参数imag：int，long，float。
17. delattr()　　删除对象的属性
18. dict()　　创建数据字典
    >>> a = dict()  空字典
    {}
    >>> b = dict(one = 1, two =2)
    {'one': 1, 'two': 2}
    >>> c = dict({'one':1 ,'two':2})
    {'one': 1, 'two': 2}
19. dir()　　
    不带参数时返回当前范围内的变量，方法和定义的类型列表，
    带参数时返回参数的属性，方法列表。
20. divmod()　　分别取商和余数
    >>> divmod(20,6)
    (3, 2)
21. enumerate()　　返回一个可以枚举的对象，该对象的next()方法将返回一个元组。
    >>> test = ['a', 'b', 'c']
    >>> for k,v in enumerate(test):
        print(k,v)
    
    # 输出结果：
    0 a
    1 b
    2 c
22. eval()　　将字符串str当成有效的表达式来求值并返回计算结果
    >>> s = "1+2*3"
    >>> eval(s)
    7
23. exec()　　执行字符串或complie方法编译过的字符串，没有返回值
24. filter()　　过滤器，构造一个序列，等价于[ item for item in iterables if function(item)]，在函数中设定过滤条件，逐一循环迭代器中的元素，将返回值为True时的元素留下，形成一个filter类型数据。
    filter(function, iterable)
    参数function：返回值为True或False的函数，可以为None。
    参数iterable：序列或可迭代对象。
  
25. float()　　讲一个字符串或整数转换为浮点数。
  
26. format()　　格式化输出字符串，format(value, format_spec)实质上是调用了value的__format__(format_spec)方法。
  
27. frozenset()　　创建一个不可修改的集合。
    frozenset([iterable])
    set和frozenset最本质的区别是前者是可变的，后者是不可变的。当集合对象会被改变时（例如删除，添加元素），只能使用set，
    一般来说使用fronzet的地方都可以使用set。
    参数iterable：可迭代对象。
    　
28. getattr()　　获取对象的属性
    getattr(object, name [, defalut])
    获取对象object名为name的特性，如果object不包含名为name的特性，将会抛出AttributeError异常；如果不包含名为name的特性
    且提供default参数，将返回default。
 
29. globals()　　返回一个描述当前全局变量的字典
30. hasattr(object，name)
    判断对象object是否包含名为name的特性（hasattr是通过调用getattr(object，name)）是否抛出异常来实现的。
    参数object：对象
    参数name：特性名称
    >>> hasattr(list, 'append')
    True
    >>> hasattr(list, 'add')
    False
31. hash(object)　哈希值
    如果对象object为哈希表类型，返回对象object的哈希值。哈希值为整数，在字典查找中，哈希值用于快递比价字典的键。
    两个数值如果相等，则哈希值也相等。

32. help()　　返回对象的帮助文档
    调用内建的帮助系统，如果不包含参数，交互式帮助系统将在控制台启动。
    如果参数为字串，则可以是模块，类，方法等名称，并且帮助页面将会在控制台打印。
    参数也可以为任意对象
33. id()　　返回对象的内存地址
34. input()　　获取用户输入内容

35. int()　　将一个字符串或数值转换为一个普通整数
    int([x[,radix]])
    如果参数是字符串，那么它可能包含符号和小数点。参数radix表示转换的基数（默认是10进制）。
    它可以是[2,36]范围内的值，或者0。如果是0，系统将根据字符串内容来解析。
    如果提供了参数radix，但参数x并不是一个字符串，将抛出TypeError异常；
    否则，参数x必须是数值（普通整数，长整数，浮点数）。通过舍去小数点来转换浮点数。
    如果超出了普通整数的表示范围，一个长整数被返回。
    如果没有提供参数，函数返回0。

36. isinstance()　　检查对象是否是类的对象，返回True或False
    isinstance(obj, cls)

37. issubclass()　　检查一个类是否是另一个类的子类。返回 True 或 False
    issubclass(sub, super)

38. iter()　
    iter(o[, sentinel])
    返回一个iterator对象。该函数对于第一个参数的解析依赖于第二个参数。
    如果没有提供第二个参数，参数o必须是一个集合对象，支持遍历功能（__iter__()方法）或支持序列功能（__getitem__()方法），
    参数为整数，从零开始。如果不支持这两种功能，将处罚TypeError异常。
    如果提供了第二个参数，参数o必须是一个可调用对象。在这种情况下创建一个iterator对象，每次调用iterator的next()方法来无
    参数的调用o，如果返回值等于参数sentinel，触发StopIteration异常，否则将返回该值。
39. len()　　返回对象长度，参数可以是序列类型（字符串，元组或列表）或映射类型（如字典）
40. list()　　列表构造函数。
    list([iterable])
    list的构造函数。参数iterable是可选的，它可以是序列，支持编译的容器对象，或iterator对象。
    该函数创建一个元素值，顺序与参数iterable一致的列表。如果参数iterable是一个列表，将创建
    列表的一个拷贝并返回，就像语句iterables[:]。　
41. locals()　　打印当前可用的局部变量的字典
    不要修改locals()返回的字典中的内容；改变可能不会影响解析器对局部变量的使用。
    在函数体内调用locals()，返回的是自由变量。修改自由变量不会影响解析器对变量的使用。
    不能在类区域内返回自由变量。
42. map()
    map(function, iterable,...)
    对于参数iterable中的每个元素都应用fuction函数，并将结果作为列表返回。
    如果有多个iterable参数，那么fuction函数必须接收多个参数，这些iterable中相同索引处的元素将并行的作为function函数的参数。
    如果一个iterable中元素的个数比其他少，那么将用None来扩展改iterable使元素个数一致。
    如果有多个iterable且function为None，map()将返回由元组组成的列表，每个元组包含所有iterable中对应索引处值。
    参数iterable必须是一个序列或任何可遍历对象，函数返回的往往是一个列表(list)。
    
    li = [1,2,3]
    data = map(lambda x :x*100,li)
    print(type(data))
    data = list(data)
    print(data)
    运行结果：
    <class 'map'>
    [100, 200, 300]

43.max(iterable [,args...][, key])　　返回给定元素里最大值
    如果只提供iterable参数，函数返回可遍历对象（如：字符串，元组或列表）中最大的非空元素。
    如果提供多个参数，那么返回值最大的那个参数。
    可选参数key是单参数的排序函数。
    如果提供key参数，必须是以命名的形式，如：max(a, b, c, key = fun)
44. memoryview()
45. min(iterable [,args...][, key])　　返回给定元素里最小值    
    如果只提供iterable参数，函数返回可遍历对象（如：字符串，元组或列表）中最小的非空元素。
    如果提供多个参数，那么返回值最小的那个参数。
    可选参数key是单参数的排序函数。
    如果提供key参数，必须是以命名的形式，如：max(a, b, c, key = fun)
46. next()　　返回一个可迭代数据结构（如列表）中的下一项
47. object()
    获取一个新的，无特性(geatureless)对象。Object是所有类的基类。它提供的方法将在所有的类型实例中共享。
    该函数时2.2.版本新增，2.3版本之后，该函数不接受任何参数。
48. open()　　打开文件
    open(filename [, mode [, bufsize]])
    打开一个文件，返回一个file对象。 如果文件无法打开，将处罚IOError异常。
    应该使用open()来代替直接使用file类型的构造函数打开文件。
    参数filename表示将要被打开的文件的路径字符串；
    参数mode表示打开的模式，最常用的模式有：'r'表示读文本，'w'表示写文本文件，'a'表示在文件中追加。
    Mode的默认值是'r'。
    当操作的是二进制文件时，只要在模式值上添加'b'。这样提高了程序的可移植性。
    可选参数bufsize定义了文件缓冲区的大小。0表示不缓冲；1表示行缓冲；任何其他正数表示使用该大小的缓冲区；
    负数表示使用系统默认缓冲区大小，对于tty设备它往往是行缓冲，而对于其他文件往往完全缓冲。如果参数值被省却。
    使用系统默认值。
49. pow()　　幂函数
50. print(value, ...,sep='',end='\n',file=sys.stdout,flush=False)　　输出函数
    python2中的print语句被python3中的print()函数取代。
    如何限制print的默认换行：将end设为空即可。
51. property()
52. range(start, stop[, step])　根据需要生成一个指定范围的数字，可以提供你需要的控制来迭代指定的次数
    参数说明：
    start: 计数从start开始，默认是0，range(10) 等价于range(0,10)
    stop: 计数到stop结束，并不包括stop，range(3) 会产生0,1,2 没有3
    step: 步长，默认为1，步长可以为负数但是不能为0，range(0,3) 等价于range(0,3,1)
    注意事项：
    用于创建包含连续算术值的列表(list)。常用于for循环。参数必须是普通整数。
    >>> range(0,10,2)  # 第一个参数是起始数，第二个是终止数(不包含这个)，第三个数步数
    range(0, 10, 2)    # 返回结果并不是一个列表，而是一个生成器
    print(list(range(3,0,-1)))  # 表示从3到0（不包含stop），步长为-1即每次自减1
    [3,2,1]
53. repr(object)　　将任意值转换为字符串，供计时器读取的形式
    返回一个对象的字符串表示。有时可以使用这个函数来访问操作。
    对于许多类型来说，repr()尝试返回一个字符串，eval()方法可以使用该字符串产生对象；
    否则用尖括号括起来的，包含类名称和其他二外信息的字符串被返回。
54. reversed(seq)　　　反转，逆序对象  
    返回一个逆序的iterator对象。参数seq必须是一个包含__reversed__()方法的对象或支持序列操作(__len__()和__getitem__())
55. round()　　四舍五入
    round(x [, n])
    对参数x的第n+1位小数进行四舍五入，返回一个小数位数为n的浮点数。
    参数n的默认值是0。结果是一个浮点数。如round(0.5)结果为1.0
56. set()    class set([iterable])  返回一个新的set对象，可以选择从iterable取得的元素，set是一个内置的类。
57. setattr()　　与getattr()相对应，setattr(object,name,value) 参数是一个对象，一个字符串和一个任意值。字符串可以命名现有属性或新属性。如果对象允许，该函数将赋值给该属性。
    setattr(x, 'foobar', 123) 相当于x.foobar = 123
58. slice()　　切片功能,  slice(start, stop[, step])
59. sorted()　　排序
    >>> sorted([36,6,-12,9,-22])  列表排序
    [-22, -12, 6, 9, 36]
    >>> sorted([36,6,-12,9,-22],key=abs) 高阶函数，以绝对值大小排序
    [6, 9, -12, -22, 36]
    >>> sorted(['bob', 'about', 'Zoo', 'Credit'])  字符串排序，按照ASCII的大小排序
    ['Credit', 'Zoo', 'about', 'bob']
    如果需要排序的是一个元组，则需要使用参数key，也就是关键字。
    >>> a = [('b',2), ('a',1), ('c',0)]
    >>> list(sorted(a,key=lambda x:x[1]))   按照元组第二个元素排序
    [('c', 0), ('a', 1), ('b', 2)]
    >>> list(sorted(a,key=lambda x:x[0]))   按照元组第一个元素排序
    [('a', 1), ('b', 2), ('c', 0)]
    >>> sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower) 忽略大小写排序
    ['about', 'bob', 'Credit', 'Zoo'] 
    >>> sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower,reverse=True) 反向排序
    ['Zoo', 'Credit', 'bob', 'about']
60. staticmethod()  在类中定义一个静态方法的函数，通常@staticmethod 下面接一个函数，如此使用
61. str()　　字符串构造函数
62. sum()　　求和
63. super()　　调用父类的方法
64. tuple()　　元组构造函数
65. type()　　显示对象所属的类型
66. vars()　vars([object])  使用__dict__属性返回模块，类，实例或任何其他对象的__dict__属性。
67. zip()　　将对象逐一配对，相当于制作一个迭代器，用于聚合每个迭代的元素。zip(*iterables)
    list_1 = [1,2,3]
    list_2 = ['a','b','c']
    s = zip(list_1,list_2)
    print(list(s))
    
    运行结果：
    [(1, 'a'), (2, 'b'), (3, 'c')]
68. __import__()
    该函数由import 语句调用，它可以被替换（导入builtins模块和分配给builtins.__import__）来改变import语句的语义，但是并不建议如此使用。
