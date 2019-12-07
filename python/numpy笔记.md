## numpy 学习笔记
### 基本属性
ndadrry.ndim
ndarry.shape #返回数组的长宽高，即每一个维度的len
ndarry.size     #返回数组的元素个数
ndarry.dtype   #dtype可以是 complex，int16，float64，float16
ndarry.itemsize
ndarry.data

### 创造array
np.array([2,3,4])  #trans a list to a array
np.arry(2,3,4) ~~ #Error!~~
np.array( [ [1,2], [3,4] ], dtype=complex )
np.zeros((3,4)) #返回全0数组
np.ones((3,4)) #返回全1数组
np.empty((3,4)) #返回一个空数组，每个元素是随机的
np.random.random((3,4))
np.arrange(start,end,step)
np.linespace(star,end,the number of the elements)

### 调整大小
np.reshape(2,3,4)

### arrary 操作
a-b
a+b
a**2 #每个数的平方
np.sine(a) #作为参数
a < 35 #判断每个元素是否大于35，返回一个bool数组
a.sum #对所有元素求和
a.max #求最大值
a.min #最小值

### 通用函数
输入一个数组，返回一个数组
sin ,cos, exp,all, any, apply_along_axis, argmax, argmin, argsort, average, bincount, ceil, clip, conj, corrcoef, cov, cross, cumprod, cumsum, diff, dot, floor, inner, inv, lexsort, max, maximum, mean, median, min, minimum, nonzero, outer, prod, re, round, sort, std, sum, trace, transpose, var, vdot, vectorize, where

### 索引、切片、迭代
a[:6:2] = -1000    # equivalent to a[0:6:2] = -1000; from start to position 6, exclusive, set every 2nd element to -1000
a[ : :-1]  # reversed a
b[0:5, 1]   # each row in the second column of b
b[1:3, : ]  # 返回第2到第4行
x[1,2,...] is equivalent to x[1,2,:,:,:]

use the flat attribute which is an iterator over all the elements of the array
```
for element in b.flat:
    print(element)
```
### shape 操作（Manipulation）
```
a.ravel()  # returns the array, flattened，返回一个被压平的一维数组
```
```
a.reshape(6,2)  # returns the array with a modified shape
```
```
a.T  # 转置
```
```
a.resize((2,6)) #this method modifies the array itself
```
If a dimension is given as -1 in a reshaping operation, the other dimensions are automatically calculated
### shadow copy 和 deep copy
b = a            # no new object is created
b is a           # a and b are two names for the same ndarray object
c = a.view()  #The view method creates a new array object that looks at the same data.
c.base is a    # c is a view of the data owned by a
True
d = a.copy()  #deep copy
d.base is a   # d doesn't share anything with a
False
### 叠加数组
np.vstack((a,b)) #纵向叠加
np.hstack((a,b))  #横向叠加
```
a = np.array([4.,2.])
>>> b = np.array([3.,8.])
>>> np.column_stack((a,b))     # returns a 2D array
array([[ 4., 3.],
       [ 2., 8.]])
>>> np.hstack((a,b))           # the result is different
array([ 4., 2., 3., 8.])
>>> a[:,newaxis]               # this allows to have a 2D columns vector
array([[ 4.],
       [ 2.]])
>>> np.column_stack((a[:,newaxis],b[:,newaxis]))
array([[ 4.,  3.],
       [ 2.,  8.]])
>>> np.hstack((a[:,newaxis],b[:,newaxis]))   # the result is the same
array([[ 4.,  3.],
       [ 2.,  8.]])
```
### bool
b = a > 4  # b is a boolean with a's shape
a[b]       # 1d array with the selected elements
a[b] = 0   # All elements of 'a' higher than 4 become 0
