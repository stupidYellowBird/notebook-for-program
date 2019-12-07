// 删除属性
delete book.author
delete book["title"]
// 只会删除自有属性，要想删除继承属性，必须从原型对象上去删除他
// 属性不存在，也不会报错，返回true，如果delete后面不是属性访问表达式
// 也会返回true


// 检测属性
var o={"x":1}
"x" in o 
"toString" in o 
o.hasOwnPreoperty("x")
o.hasOwnPreoperty("toString") //false toString是继承属性，非自有属性
o.propertyIsEnumerable("x")  //判断属性是否为可枚举属性
o.y !==undefined //false 属性不存在

// 原型
var p = {x:1}
var o = Object.create(p)
p.isPrototypeOf(o) //true p是o的原型
Object.prototype.isPrototypeOf(p) //true object.prototype是p的原型
//类属性
//可扩展性


// 序列化对象
// 函数、正则表达式、error对象和undefined值不能序列化和还原
// 只能序列化对象的可枚举对象
// 日期序列化为ISO字符串，参照Date.toJSON()函数，JSON.parse()依然保留字符串形式
// NaN Infinity -Infinity序列化为null
//  JSON.parse() JSON.stringify 都可接受第二个可选参数，自定义序列化和反序列化操作
o = {x:1,y:[false,null,undefined]}
s = JSON.stringify(o)
p = JSON.parse(s) 

// 对象方法
toString()
toLocaleString() //返回本地化字符串
toJSON() //定义对象序列化行为
valueOf() //返回对象的原始值

// 数组
a = Array(10)
a =[1,2,3,4,5,6,7,8,9,0]
a = Object.keys(o) //对象属性组成的数组
a = Object.values() //对象值数组
a.push('zero')
a.push(...ittems)
a.pop()
s.shift()
a.unshift(...ittems)


a.join(separator) //连接数组
a.reverse()
a.sort(compare_function) //不带参数时，默认为字母顺序，undefined放在末尾
//比较函数，接受两个参数，返回一个数字
a.concat(any) 
a.flat()
a.slicce(start,stop)
s.splice()

a.forEach()
a.map(func)
a.flatMap()
a.filter()
a.every()   //类似于数学上的for all
a.some()  //类似于数学上的存在
a.reduce(function (item,index) {  
},)
a.reduceRight()
a.indexof()
a.lastIndexOf() //反向收索


// 正则表达式
//定义，类似perl语法,两个斜杠包围
var pattern = /s$/  //以s符号结尾
var pattern =RegExp("s$") 
// 特殊字符 \ ? |
// \o \t \n \v \f \r \xnn \uxxxx \cX
// [abc]  [^abc]  . \w \W \s \S \d \D \b
// {m,n} {n,} {n} ? + * 重复
// 非贪婪匹配 ?? +? *? {1,5}?
// | 或者 ()分组 (?: ) \n
// ^开头 $结尾 \b匹配单词边界 \B匹配非单词边界 (?=p) (?!p)
// i 不区分大小写 g 全局匹配 m多行匹配模式

// 正则方法
s = "sjdakfakfka"
s.search(pattern)
s.replace(pattern,newstring) //替换操作
s.match(pattern) //如果正则表达式包含g修饰符，返回一个数组，包含所有的匹配结果，
// 如果没有g修饰符，也返回一个数组，包含子表达式
s.split(pattern) //正则表达式当作分割符






