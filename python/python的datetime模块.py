import datetime 
import time
# import date

import calendar

# 一、time模块
time.asctime(t:tuple) -> str #将一个时间元组转换成ascii字符串
time.time()     #返回当前系统时间时间戳，至纪元（epoch 1970，1，1）以来的秒数
time.sleep(secs:float) ->None #延迟执行，secs为subseconds
time.strptime(string,format) -> time.struct_time #解析时间字符串，返回struct_time
time.strftime(format,t:timetuple/struct_time)->str #时间转换为字符串
time.ctime(secs)    #将一个时间元组转换成字符串
time.gmtime(secs)   #格林尼治时间戳 greenwich mean time/universal time 世界时
time.localtime(secs)    #返回本地时间stuct_time 时间元组
time.mktime(t:tupletime/struct_time)    #返回时间戳
time.process_time()
time.clock()    #在window中第一次调用返回进程运行时间，第二次调用返回上一次调用的时间
time.clock_getres
time.clock_gettime
time.monotonic
time.perf_counter
time.tzset()    #改变时区
time.daylight
time.get_clock_info

# rcf 3339  
# iso 8601 时间格式




# 时间元组
# tm_year(年)                  2018
# tm_mon(月)                   1 到 12
# tm_mday(日)                  1 到 31
# tm_hour(时)                  0 到 23
# tm_min(分)                   0 到 59
# tm_sec(秒)                   0 到 61 (60或61 是闰秒)
# tm_wday(weekday)             0到6 (0是周一)
# tm_yday(一年的第几天)          1 到 366
# tm_isdst(是否是夏令时)         -1, 0, 1, -1是决定是否为夏令时的标志


# 时间格式化
# %a    本地星期名称的简写（如星期四为Thu）
# %A    本地星期名称的全称（如星期四为Thursday）
# %b    本地月份名称的简写（如八月份为agu）
# %B    本地月份名称的全称（如八月份为august）
# %c    本地相应的日期表示和时间表示
# %d    一个月中的第几天（01 - 31）
# %f    微秒（范围0.999999）
# %H    一天中的第几个小时（24小时制，00 - 23）
# %I    第几个小时（12小时制，0 - 11）
# %j    一年中的第几天（001 - 366）
# %m    月份（01 - 12）
# %M    分钟数（00 - 59）
# %p    本地am或者pm的标识符
# %S    秒数（00 - 59）
# %U    一年中的星期数。（00 - 53星期天是一个星期的开始。）第一个星期天之 前的所有天数都放在第0周。
# %w    一个星期中的第几天（0 - 6，0是星期天）
# %W    和%U基本相同，不同的是%W以星期一为一个星期的开始。
# %x    本地相应的日期表示
# %X    本地相应的时间表示
# %y    两位数的年份表示（00-99）
# %Y    四位数的年份表示（000-9999）
# %z    与UTC时间的间隔（如果是本地时间，返回空字符串）
# %Z    时区的名字（如果是本地时间，返回空字符串）



