import numpy as np 

# // numpy 的主要 对象是 同质的 多维数组 ndarray 别名array
# numpy的array和 array.array不一样，array.array只是一维

ndarray.ndim  # 数组的维度
ndarray.shape #
ndarray.size  #数组的总数量
ndarray.dtype #numpy.int32, numpy.int16, and numpy.float64 
ndarray.itemsize   #等价于ndarray.dtype.itemsize.
ndarray.data

# 创建数组
a = np.array([2,3,4])
b = np.array([(1.5,2,3), (4,5,6)])
c = np.array( [ [1,2], [3,4] ], dtype=complex )
d = np.zeros( (3,4) )
d = np.zeros_like(d)  #返回一个同样shape的zero数组
e = np.ones( (2,3,4), dtype=np.int16 )
e = np.ones_like(e) 
f = np.empty( (2,3) ) 
f = np.empty_like( (f) 
g = np.arange( 10, 30, 5 )   
h = np.linspace( 0, 2, 9 )
i =  np.fromfile(file)
j = np.fromfunction(func)
k = np.random.rand(3,2)  # 随机数


# %%
import pandas_reader



#基本操作
c = a-b 
b**2  #每个元素平方
10*np.sin(a) #数乘
a<35    # 布尔
A.dot(B)    #矩阵相乘
A @ B   #矩阵相乘
a *= 3 # inplace
b += a  # inplace
a.max()
a.min()
b.sum(axis=0) #对列求和
b.min(axis=1)   #对行求最小值
b.cumsum(axis=1) #对行累加
# 通用函数
# all, any, apply_along_axis, argmax, argmin, argsort, 
# average, bincount, ceil, clip, conj, corrcoef, cov, cross,
# cumprod, cumsum, diff, dot, floor, inner, inv, lexsort,
# max, maximum, mean, median, min, minimum, nonzero, 
# outer, prod, re, round, sort, std, sum, trace, 
# transpose, var, vdot, vectorize, where


# 索引、切片、迭代
b[2,3,5]  #第三行第四列第五排
b[ : ,1]  # 每个axis都有一个切片
c[1,...]  # 等价于c[1,:,:]  省略符

for element in b.flat # 对每个元素迭代
for row in b:  #对行迭代
for index, x in np.ndenumerate(a): 
#np.ndenumerate(a)为多维数组的迭代器 返回索引（元组）和值

# 变形操作 reshape
a.ravel()  # 拍平数组
a.reshape(6,2)
a.T
a.resize((2,6)) #参数为元组
a.reshape(3,-1)  #某个参数为-1，则自动计算其实际值


# 分块
np.hsplit(a,3)
np.vsplit(x, 2)
# view 浅复制
c = a.view()

# 深复制 

d = a.copy()  

# %%
