# cmath 模块
import cmath as c 

定义无穷
a=float('inf')
# 定义复数 注意不要有乘号*
z=1+0j
z=1+1j
z=1+1J

z.conjugate()  #共轭
z.real
z.imag

z.

# 此模块中的函数接受整数、浮点数或复数作为参数。
# 他们还接受具有 __complex__() 或__float__() 方法：
# 这些方法分别用于将对象转换为复数或浮点数，然后将函数应用于转换结果。

# 常量
c.tau # 2pi
c.e  
c.pi
c.inf
c.infj #实部为0，虚部为无穷
c.nan

c.sqrt
c.exp
c.log(x,base=e)
c.log10(x)

c.isclose(a,b,rel_tol=1e-9,abs_tol=0) #判断a和b是否足够近，rel_tol为相对公差， abs_tol绝对公差
c.isfinite(z) #real 和image都为有限
c.isinf  #real 和image有一个为无穷
c.isnan

c.phase(z:complex)->float #返回辐角 phase 相位角
c.polar(z:complex) ->tuple[float,float] #直角坐标转换为极坐标
c.rect(r:float,phi:float)->complex  #极坐标转换直角坐标

# 三角函数
c.acos
c.asin
c.atan
c.cos
c.sin
c.tan

# 双曲函数
c.acosh
c.asinh
c.atanh
c.cosh
c.tanh
c.sinh