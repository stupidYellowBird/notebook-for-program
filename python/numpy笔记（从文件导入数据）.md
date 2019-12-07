### delimiter argument分隔符
Once the file is defined and open for reading, genfromtxt splits each non-empty line into a sequence of strings. Empty or commented lines are just skipped. The delimiter keyword is used to define how the splitting should take place.

```
data = "1, 2, 3\n4, 5, 6"
>>> np.genfromtxt(BytesIO(data), delimiter=",")
array([[ 1.,  2.,  3.],
       [ 4.,  5.,  6.]])
```
By default, genfromtxt assumes delimiter=None, meaning that the line is split along white spaces (including tabs) and that consecutive white spaces（连续空白符） are considered as a single white space.


Alternatively, we may be dealing with a fixed-width file（固定宽度文件）, where columns are defined as a given number of characters. In that case, we need to set delimiter to a single integer (if all the columns have the same size) or to a sequence of integers (if columns can have different sizes):
```
>>> data = "  1  2  3\n  4  5 67\n890123  4"
>>> np.genfromtxt(BytesIO(data), delimiter=3)
array([[   1.,    2.,    3.],
       [   4.,    5.,   67.],
       [ 890.,  123.,    4.]])
>>> data = "123456789\n   4  7 9\n   4567 9"
>>> np.genfromtxt(BytesIO(data), delimiter=(4, 3, 2))
array([[ 1234.,   567.,    89.],
       [    4.,     7.,     9.],
       [    4.,   567.,     9.]])
```

### The autostrip argument去除前后空格
By default, when a line is decomposed into a series of strings, the individual entries are not stripped of leading nor trailing white spaces（头部和尾部空格）. This behavior can be overwritten by setting the optional argument autostrip to a value of True:

```
>>> data = "1, abc , 2\n 3, xxx, 4"
>>> # Without autostrip
>>> np.genfromtxt(BytesIO(data), delimiter=",", dtype="|U5")
array([['1', ' abc ', ' 2'],
       ['3', ' xxx', ' 4']],
      dtype='|U5')
>>> # With autostrip
>>> np.genfromtxt(BytesIO(data), delimiter=",", dtype="|U5", autostrip=True)
array([['1', 'abc', '2'],
       ['3', 'xxx', '4']],
      dtype='|U5')
```
### The comments argument
注释符是可选参数，默认为"#",在注释符后面的文字会被忽略掉
 ```
np.genfromtxt(BytesIO(data), comments="#", delimiter=",")
```
notable exception 如果可选参数names=True, the first commented line will be examined for names.

### skip lines and choose columns
 np.genfromtxt(BytesIO(data),skip_header=3, skip_footer=5)
 np.genfromtxt(BytesIO(data), usecols=(0, -1))  #第一列和最后一列，切片语法
 np.genfromtxt(BytesIO(data),names="a, b, c", usecols=("a", "c")) #给每一列赋名

 ### choose data type
-dtype=float
-dtype=(int, float, float)
-dtype="i4,f8,|U3"
-a dictionary with two keys 'names' and 'formats'.
-dtype=[('A', int), ('B', float)] # a sequence of tuples (name, type),
 dtype=[('a', '<i8'), ('b', '<i8'), ('c', '<i8')])
- an existing numpy.dtype object.
- the special value None. In that case, the type of the columns will be determined from the data itself (see below).

 When dtype=None, the type of each column is determined iteratively from its data. We start by checking whether a string can be converted to a boolean (that is, if the string matches true or false in lower cases); then whether it can be converted to an integer, then to a float, then to a complex and eventually to a string. This behavior may be changed by modifying the default mapper of the StringConverter class

We may sometimes need to define the column names from the data itself. In that case, we must use the names keyword with a value of True. The names will then be read from the first line (after the skip_header ones), even if the line is commented out:

```
>>> data = BytesIO("So it goes\n#a b c\n1 2 3\n 4 5 6")
>>> np.genfromtxt(data, skip_header=1, names=True)
array([(1.0, 2.0, 3.0), (4.0, 5.0, 6.0)],
      dtype=[('a', '<f8'), ('b', '<f8'), ('c', '<f8')])

```
The default value of names is None. If we give any other value to the keyword, the new names will overwrite the field names we may have defined with the dtype:

```
>>> data = BytesIO("1 2 3\n 4 5 6")
>>> ndtype=[('a',int), ('b', float), ('c', int)]
>>> names = ["A", "B", "C"]
>>> np.genfromtxt(data, names=names, dtype=ndtype)
array([(1, 2.0, 3), (4, 5.0, 6)],
      dtype=[('A', '<i8'), ('B', '<f8'), ('C', '<i8')])

```
