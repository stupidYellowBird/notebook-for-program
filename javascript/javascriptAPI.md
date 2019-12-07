array.join(separator)//方法用于把数组中的所有元素转换一个字符串,用separator分隔//
string.anchor(name)//该方法返回加了 <a> 标签的字符串, <a name="name">string</a>//
string.big()//该方法返回加了 <big> 标签的字符串,<big>string</big>//
string.blink()//该方法返回加了 <blink> 标签的字符串,<blink>string</blink>//
string.bold()//该方法返回加了 <b> 标签的字符串,<b>string</b>//
string.fixed()//该方法返回加了 <tt> 标签的字符串, <tt>string</tt>//
string.fontcolor(color)//使用指定的颜色来显示字符串。<font color="colorvalue">string</font>,为字符串规定 font-color。该值必须是颜色名(red)、RGB 值(rgb(255,0,0))或者十六进制数(#FF0000)。//
string.fontsize(size)//使用指定的尺寸来显示字符串。 size 参数必须是从 1 至 7 的数字。<font size="size">string</font>//
string.italics()//使用斜体显示字符串。
string.link(url)//该方法返回加了 <a> 标签的字符串,<a href="url">string</a>
string.small()//该方法返回加了 <small> 标签的字符串,<small>string</small>//
string.strike()//该方法返回加了 <strike> 标签的字符串, <strike>string</strike>
string.sub()//该方法返回加入 <sub> 标签的字符串，<sub>string</sub>//
string.sup()//该方法返回加入 the <sup> 标签的字符串, <sup>string</sup>//

array1.concat(array2,array3,...,arrayX)//该方法用于连接两个或多个数组,该方法不会改变现有的数组，而仅仅会返回被连接数组的一个副本。//
array.indexOf(item,start)//返回某个指定的字符串值item在字符串中首次出现的位置,start为起始搜索位置//
array.lastIndexOf(item,start)//反向搜索,返回一个指定的字符串值最后出现的位置，在一个字符串中的指定位置从后向前搜索//
array.pop()//删除数组的最后一个元素并返回删除的元素//
array.push(item1, item2, ..., itemX)//向数组的末尾添加一个或多个元素，并返回新的长度。注意： 新元素将添加在数组的末尾。注意： 此方法改变数组的长度。//
array.reverse()//用于颠倒数组中元素的顺序。//
array.shift()//把数组的第一个元素从其中删除，并返回第一个元素的值。//
array.slice(start, end)//切片//
array.sort(sortfunction)//对数组的元素进行原址排序。排序顺序可以是字母或数字，并按升序或降序。默认排序顺序为按字母升序。//
array.splice(index,howmany,item1,.....,itemX)//插入、删除或替换数组的元素。Index位置,howmany删除多少个元素,items添加的元素//
array.toString()//把数组转换为字符串，并返回结果。注意： 数组中的元素之间用逗号分隔。(和join的区别???)//
array.unshift(item1,item2, ..., itemX)//向数组的开头添加一个或更多元素，并返回新的长度。//
array.valueOf()//返回 Array 对象的原始值//
////
element.getAttributeNode(attributename)//从当前元素中通过名称获取属性节点//
文档是一个文档。////
所有的HTML元素都是元素节点。////
所有 HTML 属性都是属性节点。////
文本插入到 HTML 元素是文本节点。are text nodes。////
注释是注释节点。////

document.activeElement//返回当前获取焦点元素,该属性是只读的。为元素设置焦点，可以使用element.focus() 方法。可以使用document.hasFocus() 方法来查看当前元素是否获取焦点。//
document.addEventListener(event, func,useCapture)//向文档添加句柄//
document.adoptNode(node)//从另外一个文档返回 adapded 节点到当前文档。//
document.anchors//返回对文档中所有 Anchor 对象的引用。//
document.applets//返回对文档中所有 Applet 对象的引用。//
document.baseURI//返回文档的绝对基础 URI//
document.body//返回文档的body元素//
document.close()//关闭用 document.open() 方法打开的输出流，并显示选定的数据。//
document.cookie//设置/返回当前文档所有 键/值 对的所有 cookies//
document.createAttribute(attr)//创建一个属性节点,用setAttributeNode(att)给制定节点添加属性节点//
document.createComment("My personal comments")//创建注释节点。<!--My personal comments-->//
document.createDocumentFragment()//创建空的 DocumentFragment 对象，并返回此对象。//
document.createElement("BUTTON")//创建元素节点。<button></button>//
document.createTextNode(text)//创建文本节点。用appendchild()添加到指定节点//
document.doctype//返回与文档相关的文档类型声明 (DTD)。<!DOCTYPE html>//
document.documentElement//返回文档的根节点//
document.documentMode//返回用于通过浏览器渲染文档的模式//
document.documentURI//设置或返回文档的位置//
document.domain//返回当前文档的域名。//
document.domConfig//返回normalizeDocument()被调用时所使用的配置//
document.embeds//返回文档中所有嵌入的内容（embed）集合//
document.forms//返回对文档中所有 Form 对象引用。//
document.getElementsByClassName()//返回文档中所有指定类名的元素集合，作为 NodeList 对象。//
document.getElementById()//返回对拥有指定 id 的第一个对象的引用。//
document.getElementsByName()//返回带有指定名称的对象集合。//
document.getElementsByTagName()//返回带有指定标签名的对象集合。//
document.images//返回对文档中所有 Image 对象引用。//
document.implementation//返回处理该文档的 DOMImplementation 对象。//
document.importNode()//把一个节点从另一个文档复制到该文档以便应用。//
document.inputEncoding//返回用于文档的编码方式（在解析时）。//
document.lastModified//返回文档被最后修改的日期和时间。//
document.links//返回对文档中所有 Area 和 Link 对象引用。//
document.normalize()//删除空文本节点，并连接相邻节点//
document.normalizeDocument()//删除空文本节点，并连接相邻节点的//
document.open()//打开一个流，以收集来自任何 document.write() 或 document.writeln() 方法的输出。//
document.querySelector(CSSselectors)//返回文档中匹配指定的CSS选择器的第一元素//
document.querySelectorAll(CSSselectors)//document.querySelectorAll() 是 HTML5中引入的新方法，返回文档中匹配的CSS选择器的所有元素节点列表//
document.readyState//返回文档状态 (载入中……)//
document.referrer//返回载入当前文档的文档的 URL。//
document.removeEventListener()//移除文档中的事件句柄(由 addEventListener() 方法添加)//
document.renameNode()//重命名元素或者属性节点。//
document.scripts//返回页面中所有脚本的集合。//
document.strictErrorChecking//设置或返回是否强制进行错误检查。//
document.title//返回当前文档的标题。//
document.URL//返回文档完整的URL//
document.write()//向文档写 HTML 表达式 或 JavaScript 代码。//
document.writeln()//等同于 write() 方法，不同的是在每个表达式之后写一个换行符。//
documentObject.xmlVersion//设置或返回文档的 XML 版本。//
document.documentElement//documentElement 属性以一个元素对象返回一个文档的文档元素。HTML 文档返回对象为HTML元素。注意： 如果 HTML 元素缺失，返回值为 null。//

string.charAt(index)//返回指定位置的字符。//
string.charCodeAt(index)//返回指定位置的字符的 Unicode 编码。//
String.fromCharCode(n1, n2, ..., nX)//接受一个指定的 Unicode 值，然后返回一个字符串。该方法是 String 的静态方法，字符串中的每个字符都由单独的 Unicode 数字编码指定。//
string.match(regexp)//在字符串内检索指定的值，或找到一个或多个正则表达式的匹配。//
string.replace(searchvalue,newvalue)//在字符串中用一些字符替换另一些字符，或替换一个与正则表达式匹配的子串。//
string.search(searchvalue)//检索字符串中指定的子字符串，或检索与正则表达式相匹配的子字符串。如果没有找到任何匹配的子串，则返回 -1,返回子字符串起始位置//
string.split(separator,limit)//把一个字符串分割成字符串数组。提示： 如果把空字符串 ("") 用作 separator，那么 stringObject 中的每个字符之间都会被分割。注意： split() 方法不改变原始字符串。separator字符串或正则表达式,limit限制返回字符数组的长度.//
string.substr(start,length)//在字符串中抽取从start 下标开始 的指定数目lentgh的字符//
string.substring(from, to)//截取字符串//
string.toLowerCase()//用于把字符串转换为小写//
string.toUpperCase()//把字符串转换为大写。//

decodeURI(uri)//对 encodeURI() 函数编码过的 URI 进行解码。对以下在 URI 中具有特殊含义的 ASCII 标点符号，encodeURI() 函数是不会进行转义的： , / ? : @ & = + $ # (可以使用 encodeURIComponent() 方法分别对特殊含义的 ASCII 标点符号进行编码。).//
encodeURI(uri)//把字符串作为 URI 进行编码//
encodeURIComponent(uri)//encodeURIComponent() 函数可把字符串作为 URI 组件进行编码。该方法不会对 ASCII 字母和数字进行编码，也不会对这些 ASCII 标点符号进行编码： - _ . ! ~ * ' ( ) 。其他字符（比如 ：;/?:@&=+$,# 这些用于分隔 URI 组件的标点符号），都是由一个或多个十六进制的转义序列替换的。//
decodeURIComponent(uri)//对 encodeURIComponent() 函数编码的 URI 进行解码。//
escape(string)//对字符串进行编码，这样就可以在所有的计算机上读取该字符串。该方法不会对 ASCII 字母和数字进行编码，也不会对下面这些 ASCII 标点符号进行编码： * @ - _ + . / 。其他所有的字符都会被转义序列替换。提示： 使用 unescape() 方法对字符串进行解码。//
unescape(string)//对通过 escape() 编码的字符串进行解码。//
String(object)//把对象的值转换为字符串。//
isFinite(value)//isFinite() 函数用于检查其参数是否是无穷大。如果 number 是 NaN（非数字），或者是正、负无穷大的数，则返回 false。//
isNaN(value)//isNaN() 函数用于检查其参数是否是非数字值。如果参数值为 NaN 或字符串、对象、undefined等非数字值则返回 true, 否则返回 false。//
Number(object)//Number() 函数把对象的值转换为数字。如果对象的值无法转换为数字，那么 Number() 函数返回 NaN。//
eval(string)//eval() 函数计算 JavaScript 字符串，并把它作为脚本代码来执行。如果参数是一个表达式，eval() 函数将执行表达式。如果参数是Javascript语句，eval()将执行 Javascript 语句。//
parseFloat(string)//parseFloat() 函数可解析一个字符串，并返回一个浮点数。该函数指定字符串中的首个字符是否是数字。如果是，则对字符串进行解析，直到到达数字的末端为止，然后以数字返回该数字，而不是作为字符串。注意： 字符串中只返回第一个数字。注意： 开头和结尾的空格是允许的。注意： 果字符串的第一个字符不能被转换为数字，那么 parseFloat() 会返回 NaN。//
parseInt(string, radix基数)//当参数 radix 的值为 0，或没有设置该参数时，会根据 string 来判断数字的基数。以 "0x" 开头 会解析为十六进制的整数。以 0 开头，ECMAScript 3 解析为八进制或十六进制的数字。以 1 ~ 9 的数字开头，将解析为十进制的整数。注意： 只有字符串中的第一个数字会被返回。注意： 开头和结尾的空格是允许的。注意：如果字符串的第一个字符不能被转换为数字，那么 parseFloat() 会返回 NaN。注意：在字符串以"0"为开始时旧的浏览器默认使用八进制基数。ECMAScript 5，默认的是十进制的基数。//

element.tagName//返回元素的标签名。HTML 返回 tagName 属性的值是大写的。//
element.getAttributeNode(attributename)//从当前元素中通过名称获取属性节点。如果你仅想返回属性值请使用 getAttribute 方法。//
element.getAttribute(attributename)//通过名称获取属性的值。//
elementNode.getAttributeNodeNS(ns,name)//通过命名空间 URI(namespace) 和名称取得属性节点//
elementNode.getAttributeNS(ns,name)//通过命名空间 URI 和名称取得属性值。//
element.hasAttribute(attributename)//检查元素是否有 attributename属性//
element.hasAttributeNS(ns,name) //在当前元素节点拥有匹配指定命名空间和名称的属性时返回 TRUE，否则返回 FALSE。//
element.removeAttribute(attributename)//删除指定的属性//
element.removeAttributeNode(attributenode)//从元素中删除指定的属性节点。该方法从当前元素的属性集合中删除（并返回）一个 Attr 节点。如果 DTD 给删除的属性设置了默认值，那么该方法将添加一个新的 Attr 节点，表示这个默认值。用 removeAttribute() 方法代替该方法往往会更简单。//
elementNode.removeAttributeNS(ns,name)//删除通过命名空间和名称指定的属性。//
element.setAttribute(attributename,attributevalue)//创建或改变某个新属性。//
element.setAttributeNode(attributenode)//用于添加新的属性节点。如果元素中已经存在指定名称的属性，那么该属性将被新属性替代。如果新属性替代了已有的属性，则返回被替代的属性，否则返回 NULL。//

nodelist.length//返回节点集合的数目。//
nodelist.item(index)//返回一个节点列表中指定索引的节点。//
node.attributes//返回值： NamedNodeMap 对象, 表示属性的集合。//
node.lastChild//返回文档的最后一个子节点//
node.namespaceURI//namespaceURI 属性为被选节点返回命名空间的 URI。注意：元素节点继承父节点的命名空间，因此，XHTML文档中的所有元素命名空间URI为 "http://www.w3.org/1999/xhtml"。//
node.nextSibling//返回某个元素之后紧跟的元素（处于同一树层级中）。返回节点以节点对象返回。注意： 如果元素紧跟后面没有元素则返回 null.//
node.nodeName//可依据节点的类型返回其名称。如果节点是一个元素节点 , nodeName 属性将返回标签名。如果节点是一个属性节点， nodeName 属性将返回属性名。其他节点类型, nodeName 属性将返根据不同的节点类型返回不同的节点名称。//
////
////
////
////
////
////
////
////
////
////
////
////
////
window.closed//返回一个布尔值，表明窗口是否已经关闭。//
window.defaultStatus//设置或返回窗口状态栏中的默认文本。该属性可读可写。该文本会在页面加载时被显示。//
window.frames//返回窗口中所有命名的框架。使用 frames.length 来获取框架的数量。//
window.history //历史对象//
window.innerWidth/window.innerHeight//返回/设置窗口的文档显示区的高度,返回设置窗口的文档显示区的宽度。//
window.Location//Location 对象//
window.name//设置或返回存放窗口的名称的一个字符串。//
window.navigator //Navigator对象//
window.opener//当使用window.open()打开一个窗口，您可以使用此属性返回来自目标窗口源（父）窗口的详细信息。代码提示： window.opener.close()将关闭源（父）窗口。//
window.outerWidth/window.outerHeight//设置或返回一个窗口的外部高度，包括所有界面元素（如工具栏/滚动条）。outerWidth属性设置或返回窗口的外部宽度，包括所有的界面元素（如工具栏/滚动）。注意： 使用 innerWidth 和 innerHeight 属性获取去除工具条与滚动条的窗口高度与宽度。//
"window.pageXOffset
"//设置或返回当前页面相对于窗口显示区左上角的 X 位置,//
window.pageYOffset//设置或返回当前页面相对于窗口显示区左上角的 Y 位置。//
window.parent//返回当前窗口的父窗口。//
window.screen//window.screen对象在编写时可以不使用 window 这个前缀。screen.availWidth - 可用的屏幕宽度screen.availHeight - 可用的屏幕高度//
window.screenLeft / window.screenTop//screenLeft和screenTop属性返回窗口相对于屏幕的X和Y坐标。//
window.screenX / window.screenY//screenX和screenY属性返回窗口相对于屏幕的X和Y坐标。//
window.self//返回对窗口自身的只读引用。//
window.status//设置或返回窗口状态栏中的文本。//
window.top//Top属性返回当前窗口的最顶层浏览器窗口//
window.alert(message)//显示带有一条指定消息和一个 确认 按钮的警告框。//
window.blur()//把键盘焦点从顶层窗口移开。//
window.clearInterval(id_of_setinterval)//取消由 setInterval() 设置的 timeout。参数必须是由 setInterval() 返回的 ID 值。//
window.clearTimeout(id_of_settimeout)//取消由 setTimeout() 方法设置的 timeout。参数必须是由setTimeout()返回的ID值。//
window.close()//关闭浏览器窗口。//
window.confirm(message)//显示一个带有指定消息和确认及取消按钮的对话框。点击"确定"返回true，否则返回false。//
HTMLElementObject.focus()//focus() 方法用于为元素设置焦点（如果可以设置）。提示：使用 blur() 方法来移除元素焦点。//
window.moveBy(x,y)//相对窗口的当前坐标把它移动指定的像素。//
window.moveTo(x,y)//把窗口的左上角移动到一个指定的坐标。//
window.open(URL,name,specs,replace)//打开一个新的浏览器窗口或查找一个已命名的窗口。//
window.print()//打印当前窗口的内容。//
prompt(msg,defaultText)//显示可提示用户进行输入的对话框,返回用户输入的字符串。//
window.resizeBy(width,height)//根据指定的像素来调整窗口的大小。此方法定义指定窗口的右下角角落移动的像素，左上角将不会被移动(它停留在其原来的坐标).//
window.resizeTo(width,height)//把窗口大小调整为指定的宽度和高度。//
window.scrollBy(xnum,ynum)//把内容滚动指定的像素数,要使此方法工作 window 滚动条的可见属性必须设置为true！//
window.scrollTo(xpos,ypos)//把内容滚动到指定的坐标。//
window.setInterval(code,millisec,lang)//code 必需,要调用的函数或要执行的代码串。millisec 必须,周期性执行或调用 code 之间的时间间隔，以毫秒计。lang 可选, JScript | VBScript | JavaScript.返回的 ID 值可用作 clearInterval() 方法的参数//
window.setTimeout(code,millisec,lang)//用于在指定的毫秒数后调用函数或计算表达式。//
////
navigator.appCodeName//所有的浏览器返回 "Mozilla"作为该属性的值//
navigator.appName//所有的浏览器返回 "Netscape"作为该属性的值//
navigator.appVersion//Returns either "4.0" or a string representing version information about the browser.//
navigator.cookieEnabled //cookie是否可用,只读属性.//
navigator.platform//"MacIntel", "Win32", "FreeBSD i386", "WebTV OS"//
navigator.userAgent//"userAgent = appCodeName/appVersion number (Platform; Security; OS-or-CPU; Localization; rv: revision-version-number) product/productSub 
Application-Name Application-Name-version"//
////
////
////
////
screen.availHeight//availHeight 属性声明了显示浏览器的屏幕的可用高度，以像素计。在 Windows 这样的操作系统中，这个可用高度不包括分配给半永久特性（如屏幕底部的任务栏）的垂直空间。//
screen.availWidth//availWidth 属性声明了显示浏览器的屏幕的可用宽度，以像素计。在 Windows 这样的操作系统中，这个可用高度不包括分配给半永久特性（如屏幕底部的任务栏）的垂直空间。//
screen.colorDepth//返回目标设备或缓冲器上的调色板的比特深度。//
screen.height//浏览器的屏幕的高度//
screen.pixelDepth//屏幕的颜色分辨率（比特每像素）//
screen.width//浏览器的屏幕的宽度，以像素计//
history.back()//加载历史列表中的前一个 URL（如果存在),等价于点击后退按钮或调用 history.go(-1)。//
history.forward()//加载历史列表中的下一个 URL,等价于点击前进按钮或调用 history.go(1)。//
history.go(number|URL)//加载历史列表中的某个具体的页面。参数是数字，要访问的 URL 在 History 的 URL 列表中的相对位置。（-1上一个页面，1前进一个页面)。或一个url字符串，字符串必须是局部或完整的URL，该函数会去匹配字符串的第一个URL。//
location.hash//可读可写，该字符串是 URL 的锚部分（从 # 号开始的部分）,假设当前的URL是//www.w3cschool.cn/test.htm＃PART2  输出#part2//
location.host//可读可写，可设置或返回当前 URL 的主机名称和端口号。//
location.hostname//可读可写，可设置或返回当前 URL 的主机名。//
location.href//可读可写，可设置或返回当前显示的文档的完整 URL//
location.pathname//可读可写，可设置或返回当前 URL 的路径部分//
location.port//可读可写，可设置或返回当前 URL 的端口部分//
location.protocol//可读可写，可设置或返回当前 URL 的协议//
location.search//可读可写，可设置或返回当前 URL 的查询部分（问号 ? 之后的部分）//
location.assign(URL)//加载一个新的文档(与打开新页面有什么区别???)//
location.reload(forceGet)//重新载入当前文档,类似于点击刷新页面按钮,参数设置为 true，那么无论文档的最后修改日期是什么，它都会绕过缓存，从服务器上重新下载该文档。这与用户在单击浏览器的刷新按钮时按住 Shift 健的效果是完全一样。//
////
Date.getDate()//返回月份的某一天//
Date.getDay()//返回一周（0~6）的某一天,周日0//
Date.getFullYear()//返回年份的 4 位数字//
Date.getHours()//返回时间的小时字段//
Date.getMilliseconds()//返回值是 0 ~ 999 之间的一个整数，该数字代表毫秒数。var d = new Date("July 21, 1983 01:15:00:526");var n = d.getMilliseconds();n 输出结果:526//
Date.getMinutes()//回时间的分钟字段//
Date.getMonth()//返回表示月份的数字, 一月为 0, 二月为 1, 以此类推。//
Date.getSeconds()//返回时间的秒。返回值是 0 ~ 59 之间的一个整数//
Date.getTime()//指定的日期和时间距 1970 年 1 月 1 日午夜（GMT 时间）之间的毫秒数//
Date.getTimezoneOffset()//"返回格林威治时间和本地时间之间的时差，以分钟为单位。

例如，如果时区为 GMT+2, 将返回-120 。注意： 由于使用夏令时的惯例，该方法的返回值不是一个常量。提示： 协调世界时，又称世界统一时间，世界标准时间，国际协调时间，简称UTC（Universal Coordinated Time）。注意： UTC 时间即是 GMT（格林尼治） 时间。"//
Date.getUTCDate()()//getUTCDate() 方法可根据世界时返回一个月 (UTC) 中的某一天。//
Date.getUTCFullYear()//根据世界时从 Date 对象返回四位数的年份。//
Date.getUTCHours()//根据世界时返回 Date 对象的小时 (0 ~ 23)。//
Date.getUTCMilliseconds()//根据世界时返回 Date 对象的毫秒(0 ~ 999)。//
Date.getUTCMinutes()//根据世界时返回 Date 对象的分钟 (0 ~ 59)。//
Date.getUTCMonth()//根据世界时从 Date 对象返回月份 (0 ~ 11)。//
Date.getUTCSeconds()//根据世界时返回 Date 对象的秒钟 (0 ~ 59)。//
Date.getYear()//已废弃。 请使用 getFullYear() 方法代替。//
Date.parse(datestring)//返回1970年1月1日午夜到指定日期（字符串）的毫秒数。//
Date.setDate(day)//设置 Date 对象中月的某一天 (1 ~ 31)。0 为上一个月的最后一天,-1 为上一个月最后一天之前的一天.如果当月有 31 天:32 为下个月的第一天.如果当月有 30 天:32 为下一个月的第二天.返回1970年1月1日午夜至调整过日期的毫秒数。在 ECMAScript 标准化之前，该方法什么都不返回。//
Date.setFullYear(year,month,day)//"设置 Date 对象中的年份（四位数字）。year 必需。表示年份的四位整数。用本地时间表示。
month 可选,介于 0 ~ 11 之间：-1 为去年的最后一个月,12 为明年的第一个月,13 为明年的第二个月"//
Date.setHours(hour,min,sec,millisec)//设置 Date 对象中的小时 (0 ~ 23)。Hour -1 为昨天的最后一小时,24 为明天的第一小时y. min -1 为上一小时的最后一分钟,60 为下一小时的第一分钟//
Date.setMilliseconds(millisecond)//设置 Date 对象中的毫秒 (0 ~ 999)。-1 为上一秒钟的最后一毫秒,1000 为下一秒钟的第一毫秒,1001 为下一秒钟的第二毫秒,返回1970年1月1日午夜至调整过的日期的毫秒表示。//
Date.setMinutes(min,sec,millisec)//设置 Date 对象中的分钟 (0 ~ 59)。//
Date.setMonth(month,day)//设置 Date 对象中月份 (0 ~ 11)。返回1970年一月一日午夜至调整过的日期的毫秒表示。在 ECMAScript 标准化之前，该方法什么都不返回//
Date.setSeconds(sec,millisec)//设置 Date 对象中的秒钟 (0 ~ 59)。1970年1月1日至调整过的日期的毫秒表示。在 ECMAScript 标准化之前，该方法什么都不返回。//
Date.setTime()//setTime() 方法以毫秒设置 Date 对象。//
Date.setUTCDate()//根据世界时设置 Date 对象中月份的一天 (1 ~ 31)。//
Date.setUTCFullYear()//根据世界时设置 Date 对象中的年份（四位数字）。//
Date.setUTCHours()//根据世界时设置 Date 对象中的小时 (0 ~ 23)。//
Date.setUTCMilliseconds()//根据世界时设置 Date 对象中的毫秒 (0 ~ 999)。//
Date.setUTCMinutes()//根据世界时设置 Date 对象中的分钟 (0 ~ 59)。//
Date.setUTCMonth()//根据世界时设置 Date 对象中的月份 (0 ~ 11)。//
Date.setUTCSeconds()//setUTCSeconds() 方法用于根据世界时 (UTC) 设置指定时间的秒字段。//
Date.setYear()//已废弃。请使用 setFullYear() 方法代替。//
Date.toDateString()//把 Date 对象的日期部分转换为字符串。//
Date.toGMTString()//已废弃。请使用 toUTCString() 方法代替。//
Date.toISOString()//使用 ISO 标准返回字符串的日期格式。//
Date.toJSON()//以 JSON 数据格式返回日期字符串。//
Date.toLocaleDateString()//根据本地时间格式，把 Date 对象的日期部分转换为字符串。//
Date.toLocaleTimeString()//根据本地时间格式，把 Date 对象的时间部分转换为字符串。//
Date.toLocaleString()//据本地时间格式，把 Date 对象转换为字符串。//
Date.toString()//把 Date 对象转换为字符串。//
Date.toTimeString()//把 Date 对象的时间部分转换为字符串。//
Date.toUTCString()//根据世界时，把 Date 对象转换为字符串。//
Date.UTC()//根据世界时返回 1970 年 1 月 1 日 到指定日期的毫秒数。//
Date.valueOf()//返回 Date 对象的原始值。原始值为1970年1月1日午夜以来的毫秒数！//
////
Anchor 对象属性////
charset//设置或返回被链接资源的字符集。//
href//设置或返回被链接资源的 URL。//
hreflang//设置或返回被链接资源的语言代码。//
name//设置或返回一个链接的名称。//
rel//设置或返回当前文档与目标 URL 之间的关系。//
rev//设置或返回目标 URL 与之间当前文档的关系。//
target//设置或返回在何处打开链接。//
type//设置或返回被链接资源的 MIME 类型。//
