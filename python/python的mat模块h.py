# 数学模块math
import math as m
# 三角函数
m.acos    #反余弦   
m.asin  #反正弦
m.atan    # 反正切
m.atan2(y,x)  #返回atan(y/x)
m.cos 
m.sin
m.tan
m.degrees #角度转弧度
m.hypot(x,y)    #返回sqrt(x**2+y**2),hypotenuse(直角斜边)
m.radians     #角度转弧度

# 双曲函数
m.acosh      
m.asinh
m.tanh
m.sinh
m.cosh
m.atanh

# 常量
m.e
m.pi
m.tau     #6.28 即2pi
m.inf   # math.inf ==cmath.inf      --> True
m.nan   # c.nan==m.nan    --> False
        # c.nan ==c.nan   --> False
        # m.nan==m.nan    --> False
        # type(c.inf)   <class 'float'>
        # type(c.nan)   <class 'float'>

m.ceil    #向上取整
m.floor   #向下取整
m.trunc     # 返回整数部分
m.copysign(x,y)     #返回一个数大小(magnitude)等于x，符号等于y，即x复制y的符号


m.erf
m.erfc
m.exp(x)     #返回e的x次幂
m.ldexp(x,i)   #返回x*(2**i)
m.expm1   #返回exp(x) -1的精确值，避免精确的损失
m.fabs    #浮点数f的绝对值
m.factorial   #阶乘

m.fmod
divmod(x,y)     #带余除法
m.modf      #返回一个元组（整数部分，小数部分）
m.frexp(x)   #返回一个元组(mantissa,exponent),当x=0，返回(0,0),其他情况下0.5<=abs(m)<1
# 浮点数的一般表示方法 在数学中，表示一个浮点数需要三要素：
# 尾数（mantissa） 、指数（exponent，又称阶码）和基数（base）， 
# 都用其第一个字母来表示的话， 那么任意一个浮点数n可以表示成下
# 列形式：n=m× be,例如 
# 2.134e-20

m.fsum(iterable)  #对序列求和
m.gamma()   #gama函数
m.lgamma
m.gcd (x,y)    #最小公倍数great common divisor

# 判断函数
m.isclose(a,b,rel_tol=1e-9,abs_tol=0.0) #判断x和y是否足够近，relative tolerant相对公差，absolute tolerant 绝对公差
m.isfinite #判断x是否为无穷或者NaN
m.isinf   #判断x是否为无穷值
m.isnan   #判断是否为NaN(not a number)

m.log(x,base=e)
m.log10
m.log1p     #log(1+x) 当x接近0时的计算方法 log(x)=log(1+x)
m.log2
m.pow
m.sqrt

