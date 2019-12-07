import random

random.randint(a:int,b:int)    #返回一个[a,b]区间的int，包括两端点
random.randrange(start:int,stop:int or None,step:int)  -> int
random.Random(x:any)    # 随机数生成器，x为空，生成一个0到1之间的随机数，0<=n<1
random.choice(sequence) #在序列中选择一个随机数
random.choices(population:Sequence,weights,cum_weights,k:int) 
# population 集群，weights 相对权重，cum_weights累加权重，k选取次数
# 从集群中选取k次，每次选一个element组成一个新列表，python3.6新增
# 参数weights设置相对权重，它的值是一个列表，表示每一个成员被抽取到的概率。
# 比如weights=[1,2,3,4,5],那么第一个成员的概率就是P=1/(1+2+3+4+5)=1/15。
# cum_weights设置累加权重，Python会自动把相对权重转换为累加权重，即如果你直接给出累加权重，那么就不需要
# 给出相对权重。比如weights=[1,2,3,4],那么cum_weights=[1,3,6,10]

random.seed(a,version=2)  #参数a省略，意味着取系统时间
random.sample(population,k:int) ->list  #从集群中选出有限个元素组成新的序列，k为新序列的长度
random.shuffle(x:list[any],random)  #从新打乱序列的顺序，从新洗牌
random.uniform(a:float,b:float) -> float #返回一个在区间[a,b)的数字，精度取决于round
random.getrandbits(k)  #返回一个数n，n < 2^k

#随机分布
random.betavariate(alpha,beta)   #beta分布
random.gammavariate(alpha,beta) #gamma分布
random.gauss(mu,sigma) #高斯分布
random.lognormvariate(mu,sigma) #对数正太分布
random.paretovariate(alpha) #帕累托分布
random.triangular(low,high,mode) #三角分布
random.vonmisesvariate(mu,kappa)    #冯米塞尔分布，圆上的正态分布
random.weibullvariate(alpha,beta) #韦伯分布
random.expovariate(lambd)  #指数函数，lambd不能为0，为正数，返回0到正无穷，为负数返回负无穷到0
random.normalvariate(mu,sigma)  #正态分布

random.getstate() #获得当前状态，用于恢复时使用
random.setstate(state) #用getstate()得到的状态来恢复当前状态