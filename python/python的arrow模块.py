# 面向对象的时间模块arrow
import arrow

# 创建arrow对象
arrow.utcnow()  #<Arrow [2013-05-07T04:20:39.369271+00:00]>
arrow.now()     #<Arrow [2013-05-06T21:20:40.841085-07:00]>
arrow.now('US/Pacific')     #<Arrow [2013-05-06T21:20:44.761511-07:00]>

# Create timestamps (int or float):
arrow.get(1367900664)   #<Arrow [2013-05-07T04:24:24+00:00]>
arrow.get(1367900664.152325)    #<Arrow [2013-05-07T04:24:24.152325+00:00]>

# Use a naive or timezone-aware datetime, or flexibly specify a timezone:
arrow.get(datetime.utcnow())    # <Arrow [2013-05-07T04:24:24.152325+00:00]>
arrow.get(datetime(2013, 5, 5), 'US/Pacific')   # <Arrow [2013-05-05T00:00:00-07:00]>

from dateutil import tz
arrow.get(datetime(2013, 5, 5), tz.gettz('US/Pacific'))     # <Arrow [2013-05-05T00:00:00-07:00]>
arrow.get(datetime.now(tz.gettz('US/Pacific')))             #<Arrow [2013-05-06T21:24:49.552236-07:00]>

# 从字符串中解析
arrow.get('2013-05-05 12:30:45', 'YYYY-MM-DD HH:mm:ss')
<Arrow [2013-05-05T12:30:45+00:00]>

# 在字符串中查找时间
arrow.get('June was born in May 1980', 'MMMM YYYY')         # <Arrow [1980-05-01T00:00:00+00:00]>

# Some ISO-8601 compliant strings are recognized and parsed without a format string:
arrow.get('2013-09-30T15:34:00.000-07:00')                  # <Arrow [2013-09-30T15:34:00-07:00]>

# Arrow objects can be instantiated directly too, with the same arguments as a datetime:
arrow.get(2013, 5, 5)       # <Arrow [2013-05-05T00:00:00+00:00]>
arrow.Arrow(2013, 5, 5)     # <Arrow [2013-05-05T00:00:00+00:00]>

# 属性Properties
# Get a datetime or timestamp representation:
a = arrow.utcnow()
a.datetime  #datetime.datetime(2013, 5, 7, 4, 38, 15, 447644, tzinfo=tzutc())
a.timestamp     #1367901495

# Get a naive datetime, and tzinfo:
a.naive     #datetime.datetime(2013, 5, 7, 4, 38, 15, 447644)
a.tzinfo    #tzutc()

# Get any datetime value:
a.year      #2013
# Call datetime functions that return properties:
a.date()    #datetime.date(2013, 5, 7)
a.time()    #datetime.time(4, 38, 15, 447644)


# Replace & Shift
arw = arrow.utcnow()      #<Arrow [2013-05-12T03:29:35.334214+00:00]>
arw.replace(hour=4, minute=40)      #更改时间
arw.shift(weeks=+3)         #<Arrow [2013-06-02T03:29:35.334214+00:00]>
arw.replace(tzinfo='US/Pacific')    #更改时区

# 格式化Format
arrow.utcnow().format('YYYY-MM-DD HH:mm:ss ZZ')         #'2013-05-07 05:23:16 -00:00'

# 转换Convert
# Convert to timezones by name or tzinfo:
utc = arrow.utcnow()        #<Arrow [2013-05-07T05:24:11.823627+00:00]>
utc.to('US/Pacific')        #<Arrow [2013-05-06T22:24:11.823627-07:00]>
utc.to(tz.gettz('US/Pacific'))      #<Arrow [2013-05-06T22:24:11.823627-07:00]>
# Or using shorthand:
utc.to('local')     #<Arrow [2013-05-06T22:24:11.823627-07:00]>
utc.to('local').to('utc')   #<Arrow [2013-05-07T05:24:11.823627+00:00]>

# Humanize
past = arrow.utcnow().shift(hours=-1)
past.humanize()         #'an hour ago'
# Or another Arrow, or datetime:
present = arrow.utcnow()
future = present.shift(hours=2)
future.humanize(present)    # 'in 2 hours'

# Support for a growing number of locales (see locales.py for supported languages):
future = arrow.utcnow().shift(hours=1)
future.humanize(a, locale='ru')  #'через 2 час(а,ов)'

# Ranges & Spans
# Get the time span of any unit:
arrow.utcnow().span('hour') # (<Arrow [2013-05-07T05:00:00+00:00]>, <Arrow [2013-05-07T05:59:59.999999+00:00]>)
# Or just get the floor and ceiling:
arrow.utcnow().floor('hour')    #<Arrow [2013-05-07T05:00:00+00:00]>
arrow.utcnow().ceil('hour')     #<Arrow [2013-05-07T05:59:59.999999+00:00]>
# You can also get a range of time spans:
start = datetime(2013, 5, 5, 12, 30)
end = datetime(2013, 5, 5, 17, 15)
for r in arrow.Arrow.span_range('hour', start, end):
    print rep(i)
# Or just iterate over a range of time:
for r in arrow.Arrow.range('hour', start, end):
    print repr(r)
# <Arrow [2013-05-05T12:30:00+00:00]>
# <Arrow [2013-05-05T13:30:00+00:00]>
# <Arrow [2013-05-05T14:30:00+00:00]>
# <Arrow [2013-05-05T15:30:00+00:00]>

# Factories
# Use factories to harness Arrow’s module API for a custom Arrow-derived type. First, derive your type:
class CustomArrow(arrow.Arrow):
    def days_till_xmas(self):
        xmas = arrow.Arrow(self.year, 12, 25)
             if self > xmas:
                xmas = xmas.shift(years=1)
                return (xmas - self).days
# Then get and use a factory for it:

factory = arrow.ArrowFactory(CustomArrow)
custom = factory.utcnow()   # <CustomArrow [2013-05-27T23:35:35.533160+00:00]>
custom.days_till_xmas()     #211

# Supported Tokens
# Use the following tokens in parsing and formatting. Note that they’re not the same as the tokens for strptime(3):

# Token

Output

Year    YYYY    2000, 2001, 2002 … 2012, 2013
        YY      00, 01, 02 … 12, 13
Month   MMMM    January, February, March … 1
        MMM     Jan, Feb, Mar … 1
        MM      01, 02, 03 … 11, 12
        M       1, 2, 3 … 11, 12

Day of Year     
        DDDD    001, 002, 003 … 364, 365
        DDD     1, 2, 3 … 364, 365

Day of Month
        DD      01, 02, 03 … 30, 31
        D       1, 2, 3 … 30, 31
        Do      1st, 2nd, 3rd … 30th, 31st

Day of Week 
        dddd    Monday, Tuesday, Wednesday … 2
        ddd     Mon, Tue, Wed … 2
        d       1, 2, 3 … 6, 7

Hour    HH      00, 01, 02 … 23, 24
        H       0, 1, 2… 23, 24
        hh      01, 02, 03 … 11, 12
        h       1, 2, 3 … 11, 12

AM / PM
        A       AM, PM, am, pm 1
        a       am, pm 1

Minute  mm      00, 01, 02 … 58, 59
        m       0, 1, 2 … 58, 59

Second  ss      00, 01, 02 … 58, 59
        s       0, 1, 2 … 58, 59

Sub-second
        S…      0, 02, 003, 000006, 123123123123… 3

Timezone
        ZZZ     Asia/Baku, Europe/Warsaw, GMT … 4
        ZZ      -07:00, -06:00 … +06:00, +07:00, +08, Z
        Z       -0700, -0600 … +0600, +0700, +08, Z

Timestamp
        X       1381685817, 1381685817.915482 … 5
# 注意：
        1(1,2,3,4)  localization support for parsing and formatting
        2(1,2)  localization support only for formatting
        3       the result is truncated to microseconds, with half-to-even rounding.
        4       timezone names from tz database provided via dateutil package
        5       this token cannot be used for parsing timestamps out of natural # language strings due to compatibility reasons

# Escaping Formats
# Tokens, phrases, and regular expressions in a format string can be escaped 
# when parsing by enclosing them within square brackets.

# 标记和短语Tokens & Phrases
# Any token or phrase can be escaped as follows:
fmt = "YYYY-MM-DD h [h] m"
arrow.get("2018-03-09 8 h 40", fmt)         # <Arrow [2018-03-09T08:40:00+00:00]>

fmt = "YYYY-MM-DD h [hello] m"
arrow.get("2018-03-09 8 hello 40", fmt)     # <Arrow [2018-03-09T08:40:00+00:00]>

fmt = "YYYY-MM-DD h [hello world] m"
arrow.get("2018-03-09 8 hello world 40", fmt)   #<Arrow [2018-03-09T08:40:00+00:00]>

# 正则表达式Regular Expressions，使用方括号包含正则表达式.
fmt = r"ddd[\s+]MMM[\s+]DD[\s+]HH:mm:ss[\s+]YYYY"       # \s+ 匹配任意多空格、换行
arrow.get("Mon Sep 08 16:41:45 2014", fmt)              #<Arrow [2014-09-08T16:41:45+00:00]>
arrow.get("Mon \tSep 08   16:41:45     2014", fmt)      # <Arrow [2014-09-08T16:41:45+00:00]>
arrow.get("Mon Sep 08   16:41:45   2014", fmt)          #<Arrow [2014-09-08T16:41:45+00:00]>