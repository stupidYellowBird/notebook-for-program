# re - 正则表达式操作源代码： Lib / re.py

要搜索的模式和字符串都可以是Unicode字符串以及8位字符串。不能将Unicode字符串与字节模式匹配，反之亦然; 类似地，当要求替换时，替换字符串必须与模式和搜索字符串具有相同的类型。

使用Python的原始字符串表示法来表示正则表达式模式; 在前缀的字符串文字中，不以任何特殊方式处理反斜杠'r'。所以r"\n"是一个包含'\'和的双字符字符串'n'，"\n"而是包含换行符的单字符字符串。

1.正则表达式语法

正则表达式可以连接起来形成新的正则表达式; 如果A和B都是正则表达式，那么AB也是正则表达式。

重复限定符（*，+，?，{m,n}，等等）不能直接嵌套。这避免了非贪婪修饰符后缀的模糊性?，以及其他实现中的其他修饰符。为了对内部重复应用第二次重复，可以使用括号。例如，表达式(?:a{6})*匹配六个'a'字符的任意倍数。

特殊字符是：
'.'
（点。）在默认模式下，它匹配**除换行之外**的任何字符。如果DOTALL已指定标志，则匹配包括换行符在内的任何字符。

'^'
（Caret。）匹配字符串的**开头**，并且在MULTILINE模式下也会在每个换行符后立即匹配。

'$'
匹配字符串的结尾或在字符串**末尾的换行符之前**，并且在MULTILINE模式中也匹配换行符之前。foo匹配'foo'和'foobar'，而正则表达式foo$只匹配'foo'。更有趣的是，通常foo.$在'foo1\nfoo2\n'匹配'foo2'中搜索，但在MULTILINE模式中搜索'foo1' ; 搜索单个$in 'foo\n'将找到两个（空）匹配：一个在换行符之前，一个在字符串末尾。

'*'
使得到的RE匹配前面RE的**0或更多次**重复，尽可能多的重复。ab*将匹配'a'，'ab'或'a'，后跟任意数量的'b'。

'+'
使得到的RE匹配前一个RE的**1次或更多次**重复。ab+将匹配'a'后跟任何非零数字'b'; 它不会只匹配'a'。

'?'
使得到的RE匹配前面RE的**0或1次**重​​复。ab?将匹配'a'或'ab'。

*?, +?, ??
的'*'，'+'和'?'默认都是贪婪的 ; 它们匹配尽可能多的文本。有时这种行为是不可取的; 如果RE <.*>匹配<a> b <c>，它将匹配整个字符串，而不仅仅是<a>。?在限定符之后添加使得它以非贪婪或最小的方式执行匹配; 尽可能少的字符将匹配。使用RE <.*?>仅匹配<a>。

{m}
指定应匹配前一个RE的**m个副本**; 较少的匹配导致整个RE不匹配。例如，a{6}将匹配正好六个'a'字符，但不匹配五个字符。

{m,n}
使得到的RE匹配前一个RE的**m到n次重复**，尝试匹配**尽可能多的重复**。例如，a{3,5}将匹配3到5个'a'字符。省略m指定零的下限，省略n指定无限上限。例如，a{4,}b将匹配aaaab或一千个'a'字符后跟一个b，但不是aaab。可以不省略逗号，或者将修饰符与先前描述的形式混淆。

{m,n}?
使得到的RE匹配前一个RE的**m到n次重复**，尝试匹配**尽可能少的重复**。这是前一个限定符的非贪婪版本。例如，在6个字符的字符串上'aaaaaa'，a{3,5}将匹配5个'a'字符，而a{3,5}?只匹配3个字符。

'\'
要么**转义特殊字符**（允许你匹配像'*'，'?'等等那样的字符），要么发出特殊序列的信号; 下面讨论特殊序列。

如果你没有使用原始字符串来表达模式，请记住Python也使用反斜杠作为字符串文字中的转义序列; 如果Python的解析器无法识别转义序列，则反斜杠和后续字符将包含在结果字符串中。但是，如果Python识别结果序列，则反斜杠应重复两次。这很复杂且难以理解，因此强烈建议您使用原始字符串，除了最简单的表达式。

[]
用于表示**一组**字符。
[amk]将匹配'a'，'m'或'k'。

字符的范围可以通过给两个字符，并通过把它们分开来表示'-'，
例如[a-z]将匹配任何小写ASCII字母，
[0-5][0-9]将所有的后两位数字从匹配00到59，
[0-9A-Fa-f]会匹配任何十六进制数字。
如果-被转义（例如[a\-z]）或者如果它被放置为第一个或最后一个字符（例如[a-]），它将匹配文字'-'。

特殊字符在内部失去特殊意义。
例如，[(+*)]将匹配任何文字字符的'('，'+'，'*'，或')'。

虽然它们匹配的字符取决于是否或模式有效，但在集合中也接受诸如\w或\S（在下面定义）之类的字符类。ASCIILOCALE
可以通过补充该组来匹配不在范围内的字符。如果该组的第一个字符是'^'，则将匹配该组中不存在的所有字符。例如，[^5]将匹配除了之外的任何字符'5'，并且[^^]将匹配除了之外的任何字符'^'。^如果它不是集合中的第一个字符，则没有特殊含义。
要匹配']'集合中的文字，请在其前面加上反斜杠，或将其放在集合的开头。例如，无论是[()[\]{}]和[]()[{}]都将匹配一个括号。

'|'
A|B，其中A和B可以是任意RE，创建一个与**A或B**匹配的正则表达式。任意数量的RE都可以通过'|'这种方式分开。这也可以在组内使用（见下文）。扫描目标字符串时，'|'从**左到右**尝试分隔的RE 。当一个模式完全匹配时，接受该分支。这意味着一旦A匹配，B将不会进一步测试，即使它会产生更长的整体匹配。换句话说，'|'操作符从不贪心。要匹配文字'|'，请使用\|或将其括在字符类中，如[|]。

(...)
匹配括号内的正则表达式，并指示组的开始和结束; 可以在执行匹配后检索组的内容，并且可以在字符串中稍后与\number特殊序列匹配，如下所述。要匹配的文字'('或')'使用\(或\)，或将它们括字符类中：[(] [)]。

(?...)
这是一种扩展符号（'?'以下a '('除此之外没有意义）。'?'确定构造的含义和进一步语法之后的第一个字符。扩展通常不会创建新组; (?P<name>...)是这个规则的唯一例外。以下是当前支持的扩展。

(?aiLmsux)
（从所述一组一个或多个字母'a'，'i'，'L'，'m'，'s'，'u'，'x'。）该组匹配空字符串; 这些字母为整个正则表达式设置了相应的标志:( re.AASCII-only matching），re.I（ignore case），re.L（locale dependent），re.M（multi-line），re.S（dot match all）和re.X（verbose）。（标志在模块内容中描述。）如果您希望将标志包含在正则表达式的一部分中，而不是将标志参数传递给re.compile()函数，这将非常有用。应首先在表达式字符串中使用标志。

(?:...)
常规括号的非捕获版本。匹配括号内的正则表达式，但在执行匹配或稍后在模式中引用后，无法检索组匹配的子字符串。

(?imsx-imsx:...)
（零或从所述一组多个字母'i'，'m'，'s'，'x'，任选接着进行'-'随后的一个或多个字母，从同一组。）中的字母设置或取消相应的标志：re.I（忽略大小写）， re.M（多线）， re.S（点匹配所有）和re.X（详细），表达的一部分。（这些标志中描述模块内容。）

(?P<name>...)
与常规括号类似，但组匹配的子字符串可通过符号组名称名称访问。组名必须是有效的Python标识符，并且每个组名只能在正则表达式中定义一次。符号组也是编号组，就像组未命名一样。

可以在三种上下文中引用命名组。如果模式是(?P<quote>['"]).*?(?P=quote)（即匹配引用单引号或双引号的字符串）：

引用组“引用”的上下文	方法参考它
在相同的模式本身	
(?P=quote) （如图所示）
\1
处理匹配对象时 m	
m.group('quote')
m.end('quote') （等等。）
在传递给repl参数的字符串中re.sub()	
\g<quote>
\g<1>
\1

(?P=name)
对命名组的反向引用; 它匹配前面名为name的组匹配的任何文本。

(?#...)
一条评论; 简单地忽略括号的内容。

(?=...)
匹配如果...匹配下一个，但不消耗任何字符串。这称为先行断言。例如，只有在其后跟时才Isaac (?=Asimov)匹配。'Isaac ''Asimov'

(?!...)
匹配如果...下次不匹配。这是一个负面的先行断言。例如，只有在没有后跟的情况下Isaac (?!Asimov)才会匹配。'Isaac ''Asimov'

(?<=...)
如果字符串中的当前位置前面有匹配，则匹配，...该匹配结束于当前位置。这被称为积极的外观断言。(?<=abc)def将找到一个匹配abcdef，因为lookbehind将备份3个字符并检查包含的模式是否匹配。所包含的模式必须只匹配一些固定长度的串，这意味着abc或者a|b是允许的，但a*并a{3,4}不是。请注意，以正向后向断言开头的模式在搜索字符串的开头不匹配; 你很可能想要使用search()函数而不是match()函数：

>>> import re
>>> m = re.search（'（？<= abc）def'，'abcdef'）
>>> m.group（0）
“高清”
此示例查找连字符后面的单词：

>>> m = re.search（'（？<=  - ）\ w +'，'spam-egg'）
>>> m.group（0）
'蛋'
版本3.5中已更改：添加了对固定长度的组引用的支持。

(?<!...)
如果字符串中的当前位置前面没有匹配，则匹配...。这被称为负面的后观断言。与正向lookbehind断言类似，包含的模式必须仅匹配某些固定长度的字符串。以负反向断言开始的模式可以在被搜索的字符串的开头匹配。
(?(id/name)yes-pattern|no-pattern)
yes-pattern如果具有给定id或名称的组存在，则尝试匹配，如果no-pattern不存在则尝试匹配。no-pattern是可选的，可以省略。例如，(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)是一个贫穷的电子邮件匹配模式，这将匹配'<user@host.com>'以及'user@host.com'，但不与'<user@host.com'也'user@host.com>'。
特殊序列由'\'下面列表中的一个字符组成。如果普通字符不是ASCII数字或ASCII字母，则生成的RE将匹配第二个字符。例如，\$匹配角色'$'。

\number
匹配相同编号的组的内容。组从1开始编号。例如，(.+) \1匹配'the the'或'55 55'，但不是'thethe'（注意组后面的空格）。此特殊序列只能用于匹配前99个组中的一个。如果第一个数字数是0，或数为3个八进制数字长，也不会被解释为一组匹配，但与八进制值的字符数。里面'['和']'一个字符类，所有的数字逃逸被视为字符。
\A
仅匹配字符串的开头。
\b
匹配空字符串，但仅匹配单词的开头或结尾。单词被定义为Unicode字母数字或下划线字符的序列，因此单词的结尾由空格或非字母数字的非下划线Unicode字符表示。注意，正式地，\b定义为a \w和\W字符之间的边界（反之亦然），或者在\w字符串的开头/结尾之间。这意味着，r'\bfoo\b'比赛'foo'，'foo.'，'(foo)'，'bar foo baz'但不'foobar'还是'foo3'。

默认使用Unicode字母数字，但可以使用ASCII标志更改。在字符范围内，\b表示退格符，以便与Python的字符串文字兼容。

\B
匹配空字符串，但仅当它不在单词的开头或结尾时。这意味着，r'py\B'比赛'python'，'py3'，'py2'，而不是'py'，'py.'或'py!'。\B正好相反\b，所以单词字符是Unicode字母数字或下划线，虽然这可以通过使用ASCII标志来改变。
\d
对于Unicode（str）模式：
匹配任何Unicode十进制数字（即Unicode字符类别[Nd]中的任何字符）。这包括[0-9]，还有许多其他数字字符。如果ASCII仅使用该标志[0-9]匹配（但该标志影响整个正则表达式，因此在这种情况下使用显式[0-9]可能是更好的选择）。
对于8位（字节）模式：
匹配任何十进制数字; 这相当于[0-9]。
\D
匹配任何不是Unicode十进制数字的字符。这与之相反\d。如果ASCII使用该标志，则该变为等效[^0-9]（但该标志影响整个正则表达式，因此在这种情况下使用显式[^0-9]可能是更好的选择）。
\s
对于Unicode（str）模式：
匹配Unicode空白字符（其中包括[ \t\n\r\f\v]许多其他字符，例如许多语言中排版规则强制要求的非破坏空格）。如果使用该ASCII标志，则仅[ \t\n\r\f\v]匹配（但该标志影响整个正则表达式，因此在这种情况下使用显式[ \t\n\r\f\v]可能是更好的选择）。
对于8位（字节）模式：
匹配ASCII字符集中考虑空格的字符; 这相当于[ \t\n\r\f\v]。
\S
匹配任何不是Unicode空白字符的字符。这与之相反\s。如果ASCII使用该标志，则该变为等效[^ \t\n\r\f\v]（但该标志影响整个正则表达式，因此在这种情况下使用显式[^ \t\n\r\f\v]可能是更好的选择）。
\w
对于Unicode（str）模式：
匹配Unicode字符; 这包括大多数可以成为任何语言单词的一部分的字符，以及数字和下划线。如果使用该ASCII标志，则仅[a-zA-Z0-9_]匹配（但该标志影响整个正则表达式，因此在这种情况下使用显式[a-zA-Z0-9_]可能是更好的选择）。
对于8位（字节）模式：
匹配ASCII字符集中被认为是字母数字的字符; 这相当于[a-zA-Z0-9_]。
\W
匹配任何非Unicode字符的字符。这与之相反\w。如果ASCII使用该标志，则该变为等效[^a-zA-Z0-9_]（但该标志影响整个正则表达式，因此在这种情况下使用显式[^a-zA-Z0-9_]可能是更好的选择）。
\Z
仅匹配字符串末尾的匹配项。
正则表达式解析器也接受Python字符串文字支持的大多数标准转义：

\ a \ b \ f \ n
\ r \ t \ u \ u
\ v \ x \\
（注意，\b它用于表示单词边界，并且仅在字符类中表示“退格”。）

'\u'和'\U'转义序列仅在Unicode模式中识别。在字节模式中，它们不受特殊处理。

八度逃逸包含在有限的形式中。如果第一个数字是0，或者如果有三个八进制数字，则认为它是八进制数。否则，它是一个组引用。至于字符串文字，八进制转义的长度最多为三位数。

改变在3.3版本：在'\u'和'\U'转义序列已被添加。
在版本3.6中更改：'\'现在包含和ASCII字母的未知转义是错误。

2.模块内容

在版本3.6中更改：标志常量现在是实例RegexFlag，它是的子类enum.IntFlag。

re.compile(pattern, flags=0)
将正则表达式模式编译为正则表达式对象，可以使用它match()和search()方法进行匹配。

可以通过指定标志值来修改表达式的行为。值可以是以下任何变量，使用OR（|运算符）组合。

prog = re.compile（pattern）
result = prog.match（string）

result = re.match（pattern，string）
但是re.compile()，当在单个程序中多次使用表达式时，使用和保存生成的正则表达式对象以便重用会更有效。

注意，传递给最新模式的编译版本re.compile()和模块级匹配函数被缓存，因此一次只使用几个正则表达式的程序不必担心编译正则表达式。

re.A
re.ASCII
让\w，\W，\b，\B，\d，\D，\s和\S执行ASCII-只匹配完整的Unicode匹配代替。这仅对Unicode模式有意义，并且对于字节模式将被忽略。

请注意，为了向后兼容，该re.U标志仍然存在（以及它的同义词re.UNICODE及其嵌入式副本(?u)），但这些在Python 3中是多余的，因为默认情况下匹配对于字符串是Unicode（并且字节不允许Unicode匹配）。

re.DEBUG
显示有关已编译表达式的调试信

re.I
re.IGNORECASE
执行不区分大小写的匹配; 表达式[A-Z]也会匹配小写字母。这不受当前语言环境的影响，并且可以按预期用于Unicode字符。

re.L
re.LOCALE
让\w，\W，\b，\B，\s以及\S依赖于当前的语言环境。不鼓励使用此标志，因为语言环境机制非常不可靠，并且它一次只能处理一个“文化”; 你应该使用Unicode匹配，这是Python 3中针对Unicode（str）模式的默认设置。该标志只能用于字节模式。

版本3.6中更改：re.LOCALE仅可用于字节模式且与之不兼容re.ASCII。

re.M
re.MULTILINE
指定时，模式字符'^'匹配字符串的开头和每行的开头（紧跟在每个换行符之后）; 并且模式字符'$'在字符串的末尾和每行的末尾（紧接在每个换行符之前）匹配。默认情况下，'^'仅匹配字符串的开头，并且'$'仅匹配字符串的结尾，紧接在字符串末尾的换行符（如果有）之前。

re.S
re.DOTALL
使'.'特殊字符与任何字符匹配，包括换行符; 没有此标志，'.'将匹配除换行符之外的任何内容。

re.X
re.VERBOSE
此标志允许您编写看起来更好且更易读的正则表达式，允许您在视觉上分离模式的逻辑部分并添加注释。模式中的空格被忽略，除非在字符类中或前面有未转义的反斜杠。当一行包含一个#不在字符类中并且前面没有非转义反斜杠#的行时，将忽略从最左边到行尾的所有字符。

re.match(pattern, string, flags=0)
如果字符串开头的零个或多个字符与正则表达式模式匹配，则返回相应的匹配对象。None如果字符串与模式不匹配则返回; 请注意，这与零长度匹配不同。

请注意，即使在MULTILINE模式下，re.match()也只会匹配字符串的开头而不是每行的开头。

如果要在字符串中的任何位置找到匹配项，search()请改为使用（另请参阅search（）与match（））。

re.fullmatch(pattern, string, flags=0)
如果整个字符串与正则表达式模式匹配，则返回相应的匹配对象。None如果字符串与模式不匹配则返回; 请注意，这与零长度匹配不同。

版本3.4中的新功能。

re.split(pattern, string, maxsplit=0, flags=0)
按模式的出现拆分字符串。如果在模式中使用捕获括号，则模式中所有组的文本也将作为结果列表的一部分返回。如果maxsplit非零，则最多发生maxsplit拆分，并且字符串的其余部分将作为列表的最后一个元素返回。

>>> re.split（'\ W +'，'Words，words，words。'）
['单词'，'单词'，'单词'，'']

>>> re.split（'（\ W +）'，'单词，单词，单词。'）
['Words'，'，'，'words'，'，'，'words'，'。'，'']

>>> re.split（'\ W +'，'Words，words，words。'，1）
['单词'，'单词，单词。']

>>> re.split（'[af] +'，'0a3B9'，flags = re.IGNORECASE）
['0'，'3'，'9']
如果分隔符中有捕获组并且它在字符串的开头匹配，则结果将以空字符串开头。对于字符串的结尾也是如此：

>>> re.split（'（\ W +）'，'... words，words ...'）
[''，'...'，'words'，'，'，'words'，'...'，'']
这样，始终在结果列表中的相同相对索引处找到分隔符组件。

注意

split()当前没有在空模式匹配上拆分字符串。例如：

>>> re.split（'x *'，'axbc'）
['a'，'bc']
即使'x*'在'a'之前，'b'和'c'之间以及'c'之后也匹配0'x'，当前这些匹配将被忽略。['', 'a', 'b', 'c', '']在未来的Python版本中将实现正确的行为（即在空匹配上拆分并返回），但由于这是一个向后不兼容的更改，因此FutureWarning将同时引发。

目前只能匹配空字符串的模式永远不会拆分字符串。由于这与预期的行为不匹配，ValueError因此将从Python 3.5开始引发：

>>> re.split（“^ $”，“foo \ n \ nbar \ n”，flags = re.M）
Traceback（最近一次调用最后一次）：
  在<module>中的文件“<stdin>”，第1行
  ...
ValueError：split（）需要非空模式匹配。
在3.1版中更改：添加了可选的flags参数。


re.findall(pattern, string, flags=0)
返回的所有非重叠的匹配的字符串。该字符串进行扫描左到右，并以发现的顺序返回。如果模式中存在一个或多个组，则返回组列表; 如果模式有多个组，这将是一个元组列表。

re.finditer(pattern, string, flags=0)
返回一个迭代器，该字符串进行扫描左到右，并匹配以发现的顺序返回。

re.sub(pattern, repl, string, count=0, flags=0)
返回通过替换repl替换字符串中最左边的非重叠模式而获得的字符串。如果未找到模式，则返回字符串不变。repl可以是字符串或函数; 如果它是一个字符串，则处理其中的任何反斜杠转义。也就是说，转换为单个换行符，转换为回车符，依此类推。未知的逃脱，如独自留下。反向引用（例如）将替换为模式中第6组匹配的子字符串。例如：\n\r\&\6

>>> re.sub（r'def \ s +（[a-zA-Z _] [a-zA-Z_0-9] *）\ s * \（\ s * \）：'，
... r'static PyObject * \ npy_ \ 1（void）\ n {'，
...'def myfunc（）：'）
'static PyObject * \ npy_myfunc（void）\ n {'
如果repl是一个函数，则会为每个非重叠的模式调用调用它。该函数接受单个匹配对象参数，并返回替换字符串。例如：

>>> def dashrepl（matchobj）：
...如果matchobj.group（0）==' - '：return''
......别的：返回' - '
>>> re.sub（' -  {1,2}'，dashrepl，'pro ---- gram-files'）
'程序文件'
>>> re.sub（r'\ sAND \'s'，'＆'，'Baked Beans and Spam'，flags = re.IGNORECASE）
'焗豆和垃圾邮件'
模式可以是字符串或RE对象。

可选参数count是要替换的模式最大出现次数; count必须是非负整数。如果省略或为零，则将替换所有出现的事件。仅当与前一个匹配不相邻时，才会替换模式的空匹配，因此sub('x*', '-', 'abc')返回'-a-b-c-'。

在字符串型repl参数中，除了上面描述的字符转义和反向引用之外，\g<name>还将使用name由(?P<name>...)语法定义的命名组匹配的子字符串。\g<number>使用相应的组号; \g<2>因此，等同于\2，但在替代品中并不含糊\g<2>0。\20将被解释为对组20的引用，而不是对组2的引用，后跟文字字符'0'。反向引用\g<0>替代了RE匹配的整个子字符串。

在3.1版中更改：添加了可选的flags参数。

版本3.5中已更改：不匹配的组将替换为空字符串。

在版本3.6中更改：包含和ASCII字母的模式中的未知转义'\'现在是错误。

从版本3.5开始不推荐使用，将在版本3.7中删除：由repl组成的未知转义'\'和ASCII字母现在引发弃用警告，并且在Python 3.7中将被禁止。

re.subn(pattern, repl, string, count=0, flags=0)
执行相同的操作sub()，但返回元组(new_string, number_of_subs_made)。

在3.1版中更改：添加了可选的flags参数。

版本3.5中已更改：不匹配的组将替换为空字符串。

re.escape(string)
除了ASCII字母，数字和以外，转义模式中的所有字符'_'。如果要匹配可能包含正则表达式元字符的任意文字字符串，这将非常有用。

在3.3版本中更改：该'_'字符不再逃跑。

re.purge()
清除正则表达式缓存。

exception re.error(msg, pattern=None, pos=None)
传递给此处其中一个函数的字符串不是有效的正则表达式（例如，它可能包含不匹配的括号）或在编译或匹配期间发生其他错误时引发的异常。如果字符串不包含模式匹配，则永远不会出错。错误实例具有以下附加属性：

msg
未格式化的错误消息。

pattern
正则表达式模式。

pos
编译失败的模式索引。

lineno
该行对应于pos。

colno
对应于pos的列。

版本3.5中已更改：添加了其他属性。

3.正则表达式对象
经过编译的正则表达式对象支持以下方法和属性：

regex.search(string[, pos[, endpos]])
扫描字符串，查找此正则表达式生成匹配项的第一个位置，并返回相应的匹配对象。None如果字符串中没有位置与模式匹配则返回; 请注意，这与在字符串中的某个点找到零长度匹配不同。

可选参数pos给出了搜索开始的字符串中的索引; 它默认为0。这并不完全等同于切割字符串; 该'^'模式字符在字符串的真正开始，并在仅仅一个换行符后的位置相匹配，但不一定，其中搜索是启动索引。

可选参数endpos限制字符串的搜索范围; 它就好像字符串是endpos字符长，所以只搜索pos中的字符才能endpos - 1匹配。如果endpos小于pos，则不会找到匹配项; 否则，如果rx是一个已编译的正则表达式对象，rx.search(string, 0, 50)则相当于rx.search(string[:50], 0)。

>>> pattern = re.compile（“d”）
>>> pattern.search（“dog”）＃在索引0处匹配
<_sre.SRE_Match对象; span =（0,1），match ='d'>
>>> pattern.search（“dog”，1）#No match; 搜索不包括“d”

regex.match(string[, pos[, endpos]])
如果字符串开头的零个或多个字符与此正则表达式匹配，则返回相应的匹配对象。如果字符串与模式不匹配则返回; 请注意，这与零长度匹配不同。None

可选的pos和endpos参数具有与该search()方法相同的含义。

>>> pattern = re.compile（“o”）
>>> pattern.match（“dog”）＃不匹配“o”不在“dog”的开头。
>>> pattern.match（“dog”，1）＃匹配为“o”是“dog”的第2个字符。
<_sre.SRE_Match对象; span =（1,2），match ='o'>
如果要在字符串中的任何位置找到匹配项，search()请改为使用（另请参阅search（）与match（））。

regex.fullmatch(string[, pos[, endpos]])
如果整个字符串与此正则表达式匹配，则返回相应的匹配对象。None如果字符串与模式不匹配则返回; 请注意，这与零长度匹配不同。

可选的pos和endpos参数具有与该search()方法相同的含义。

>>> pattern = re.compile（“o [gh]”）
>>> pattern.fullmatch（“dog”）＃不匹配“o”不在“dog”的开头。
>>> pattern.fullmatch（“ogre”）＃不匹配，因为不是完整的字符串匹配。
>>> pattern.fullmatch（“doggie”，1,3）＃匹配给定范围内。
<_sre.SRE_Match对象; span =（1,3），match ='og'>
版本3.4中的新功能。

regex.split(string, maxsplit=0)
与split()函数相同，使用编译的模式。

regex.findall(string[, pos[, endpos]])
与findall()函数类似，使用已编译的模式，但也接受可选的pos和endpos参数，这些参数限制了搜索区域match()。

regex.finditer(string[, pos[, endpos]])
与finditer()函数类似，使用已编译的模式，但也接受可选的pos和endpos参数，这些参数限制了搜索区域match()。

regex.sub(repl, string, count=0)
与sub()函数相同，使用编译的模式。

regex.subn(repl, string, count=0)
与subn()函数相同，使用编译的模式。

regex.flags
正则表达式匹配标志。这是给出的标志，模式中的compile()任何(?...)内联标志和隐式标志的组合，例如UNICODE模式是否为Unicode字符串。

regex.groups
模式中捕获组的数量。

regex.groupindex
一个字典，用于映射由(?P<id>)组编号定义的任何符号组名称。如果模式中没有使用符号组，则字典为空。

regex.pattern
从中编译RE对象的模式字符串。

4.匹配对象
匹配对象的布尔值始终为True，在没有匹配到时match()和search()返回None
match = re.search(pattern, string)
if match:
    process(match)

匹配对象支持以下方法和属性：

match.expand(template)
返回通过在模板字符串模板上执行反斜杠替换获得的字符串，如sub()方法所做。诸如转义为转义为\n适当字符的转义，数字反向引用（\1，\2）和命名反向引用（\g<1>，\g<name>）将被相应组的内容替换。

版本3.5中已更改：不匹配的组将替换为空字符串。

match.group([group1, ...])
返回匹配的一个或多个子组。如果只有一个参数，则结果为单个字符串; 如果有多个参数，则结果是一个元组，每个参数有一个项目。如果没有参数，group1默认为零（返回整个匹配）。如果groupN参数为零，则相应的返回值是整个匹配的字符串; 如果它在包含范围[1..99]中，则它是与相应的带括号的组匹配的字符串。如果组编号为负数或大于模式中定义的组数，IndexError则会引发异常。如果一个组包含在不匹配的模式的一部分中，则相应的结果为None。如果一个组包含在多次匹配的模式的一部分中，则返回最后一个匹配。

>>> m = re.match（r“（\ w +）（\ w +）”，“Isaac Newton，物理学家”）
>>> m.group（0）＃整场比赛
'艾萨克·牛顿'
>>> m.group（1）＃第一个带括号的子组。
“艾萨克”
>>> m.group（2）＃第二个带括号的子组。
“牛顿”
>>> m.group（1,2）＃多个参数给我们一个元组。
（'艾萨克·牛顿'）
如果正则表达式使用(?P<name>...)语法，则groupN参数也可以是按组名称标识组的字符串。如果字符串参数未在模式中用作组名，IndexError则会引发异常。

一个中等复杂的例子：

>>> m = re.match（r“（？P <first_name> \ w +）（？P <last_name> \ w +）”，“Malcolm Reynolds”）
>>> m.group（'first_name'）
“马尔科姆”
>>> m.group（'last_name'）
“雷诺”
命名组也可以通过其索引引用：

>>> m.group（1）
“马尔科姆”
>>> m.group（2）
“雷诺”
如果一个组匹配多次，则只能访问最后一个匹配：

>>> m = re.match（r“（..）+”，“a1b2c3”）＃匹配3次。
>>> m.group（1）＃仅返回最后一场比赛。
'C3'
match.__getitem__(g)
这与之相同m.group(g)。这样可以更轻松地从匹配中访问单个组：

>>> m = re.match（r“（\ w +）（\ w +）”，“Isaac Newton，物理学家”）
>>> m [0]＃整场比赛
'艾萨克·牛顿'
>>> m [1]＃第一个带括号的子组。
“艾萨克”
>>> m [2]＃第二个带括号的子组。
“牛顿”
版本3.6中的新功能。

match.groups(default=None)
返回包含匹配的所有子组的元组，从1到多个组都在模式中。该默认参数用于那些没有参加比赛组; 它默认为None。

例如：

>>> m = re.match（r“（\ d +）\。（\ d +）”，“24.1632”）
>>> m.groups（）
（'24'，'1632'）
如果我们将小数位和其后的所有内容都设为可选，则并非所有组都可以参与匹配。None除非给出默认参数，否则这些组将默认为：

>>> m = re.match（r“（\ d +）\。？（\ d +）？”，“24”）
>>> m.groups（）＃第二组默认为None。
（'24'，无）
>>> m.groups（'0'）＃现在，第二组默认为'0'。
（'24'，'0'）
match.groupdict(default=None)
返回包含匹配的所有已命名子组的字典，由子组名称键入。该默认参数用于那些没有参加比赛组; 它默认为None。例如：

>>> m = re.match（r“（？P <first_name> \ w +）（？P <last_name> \ w +）”，“Malcolm Reynolds”）
>>> m.groupdict（）
{'first_name'：'Malcolm'，'last_name'：'Reynolds'}
match.start([group])
match.end([group])
返回由group匹配的子字符串的开始和结束的索引; group默认为零（表示整个匹配的子字符串）。返回-1如果组存在，但无助于比赛。对于匹配对象米，和一组克这并有助于匹配，则子组由匹配克（相当于m.group(g)）是

m.string [m.start（克）：m.end（克）]
请注意，如果组匹配空字符串，m.start(group)则相等。例如，之后，是1，是2，并且都是2，并引发异常。m.end(group)m = re.search('b(c?)', 'cba')m.start(0)m.end(0)m.start(1)m.end(1)m.start(2)IndexError

一个将从电子邮件地址中删除remove_this的示例：

>>> email =“tony@tiremove_thisger.net”
>>> m = re.search（“remove_this”，电子邮件）
>>>电子邮件[：m.start（）] +电子邮件[m.end（）：]
'tony@tiger.net'
match.span([group])
对于匹配m，返回2元组(m.start(group), m.end(group))。请注意，如果组没有为匹配做出贡献，那么就是这样(-1, -1)。组默认为零，整个匹配。

match.pos
传递给正则表达式对象或方法的pos的值。这是RE引擎开始寻找匹配项的字符串索引。search()match()

match.endpos
的值endpos被传递到search()或match()一个的方法regex对象。这是RE引擎不会超出的字符串索引。

match.lastindex
最后匹配的捕获组的整数索引，或者None根本没有匹配的组。例如，表述(a)b，((a)(b))以及((ab))将具有lastindex == 1如果施加到串'ab'，而表达(a)(b)将有lastindex == 2，如果施加到相同的字符串。

match.lastgroup
最后匹配的捕获组None的名称，或者该组没有名称，或者根本没有匹配的组。

match.re
正则表达式对象，其match()或者search()方法生成此匹配实例。

match.string
传递给match()或的字符串search()。

5.正则表达式示例
5.1。检查一对
在这个例子中，我们将使用以下辅助函数来更优雅地显示匹配对象：

def displaymatch（匹配）：
    如果匹配为无：
        返回无
    return'<匹配：％r，groups =％r>'％（match.group（），match.groups（））
假设您正在编写一个扑克程序，其中玩家的手被表示为5个字符的字符串，每个字符代表一张牌，“a”代表王牌，“k”代表国王，“q”代表女王，“j”代表杰克， “t”代表10，“2”代表“9”代表具有该值的卡片。

要查看给定字符串是否是有效的手，可以执行以下操作：

>>> valid = re.compile（r“^ [a2-9tjqk] {5} $”）
>>> displaymatch（valid.match（“akt5q”））＃有效。
“<匹配：'akt5q'，群组=（）>”
>>> displaymatch（valid.match（“akt5e”））＃无效。
>>> displaymatch（valid.match（“akt”））＃无效。
>>> displaymatch（valid.match（“727ak”））＃有效。
“<匹配：'727ak'，群组=（）>”
最后一手牌，"727ak"包含一对或两张相同价值的牌。要将其与正则表达式匹配，可以使用反向引用：

>>> pair = re.compile（r“。*（。）。* \ 1”）
>>> displaymatch（pair.match（“717ak”））#7对。
“<匹配：'717'，groups =（'7'，）>”
>>> displaymatch（pair.match（“718ak”））＃没有对。
>>> displaymatch（pair.match（“354aa”））#Ale对。
“<匹配：'354aa'，groups =（'a'，）>”
要找出该对包含的卡，可以group()按以下方式使用匹配对象的方法：

>>> pair.match（“717ak”）。组（1）
'7'

#Error，因为re.match（）返回None，它没有group（）方法：
>>> pair.match（“718ak”）。组（1）
Traceback（最近一次调用最后一次）：
  在<module>中的文件“<pyshell＃23>”，第1行
    re.match（r“。*（。）。* \ 1”，“718ak”）。组（1）
AttributeError：'NoneType'对象没有属性'group'

>>> pair.match（“354aa”）。组（1）
'一个'

5.2。模拟scanf（）
Python目前没有等效的scanf()。正则表达式通常比scanf()格式字符串更强大，但也更冗长。下表提供了scanf()格式标记和正则表达式之间的一些或多或少的等效映射。

scanf() 代币	正则表达式
%c   .
%5c  .{5}
%d   [-+]?\d+
%e， %E，%f，%g [-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?
%i   [-+]?(0[xX][\dA-Fa-f]+|0[0-7]*|\d+)
%o  [-+]?[0-7]+
%s  \S+
%u  \d+
%x， %X [-+]?(0[xX])?[\dA-Fa-f]+

5.3 search（）vs. match（）
Python提供了两种基于正则表达式的基本操作：re.match()仅在字符串的开头re.search()检查匹配，同时检查字符串中任何位置的匹配（这是Perl默认执行的操作）。

例如：

>>> re.match（“c”，“abcdef”）＃不匹配
>>> re.search（“c”，“abcdef”）#Match
<_sre.SRE_Match对象; span =（2,3），match ='c'>
以逗号开头的正则表达式'^'可用于search()限制字符串开头的匹配：

>>> re.match（“c”，“abcdef”）＃不匹配
>>> re.search（“^ c”，“abcdef”）#No match
>>> re.search（“^ a”，“abcdef”）#Match
<_sre.SRE_Match对象; span =（0,1），match ='a'>
但请注意，在MULTILINE模式中match()仅匹配字符串的开头，而使用search()带有开头的正则表达式'^'将匹配每行的开头。

>>> re.match（'X'，'A \ nB \ nX'，re.MULTILINE）#No match
>>> re.search（'^ X'，'A \ nB \ nX'，re.MULTILINE）#Match
<_sre.SRE_Match对象; span =（4,5），match ='X'>
5.4。制作电话簿
split()将字符串拆分为由传递的模式分隔的列表。该方法对于将文本数据转换为可由Python轻松读取和修改的数据结构非常有用，如以下创建电话簿的示例所示。

首先，这是输入。通常它可能来自一个文件，这里我们使用三引号字符串语法：

>>> text =“”“Ross McFluff：834.345.1254 155 Elm Street
...
...罗纳德希思莫尔：892.345.3428 436芬利大道
... Frank Burger：925.541.7625 662 South Dogwood Way
...
...
... Heather Albrecht：548.326.4584 919 Park Place“”“
条目由一个或多个换行符分隔。现在我们将字符串转换为一个列表，每个非空行都有自己的条目：

>>> entries = re.split（“\ n +”，text）
>>>条目
['Ross McFluff：834.345.1254 155 Elm Street'，
'Ronald Heathmore：892.345.3428 436 Finley Avenue'，
'Frank Burger：925.541.7625 662 South Dogwood Way'，
'Heather Albrecht：548.326.4584 919 Park Place']
最后，将每个条目拆分为包含名字，姓氏，电话号码和地址的列表。我们使用maxsplit参数，split()因为地址有空格，我们的分裂模式，在其中：

>>> [re.split（“：？”，条目，3）在条目中输入]
[['Ross'，'McFluff'，'834.345.1254'，'155 Elm Street']，
['Ronald'，'Heathmore'，'892.345.3428'，'436 Finley Avenue'，
['Frank'，'Burger'，'925.541.7625'，'662 South Dogwood Way']，
['Heather'，'Albrecht'，'548.326.4584'，'919 Park Place']]
该:?模式匹配姓氏后的冒号，因此它不会出现在结果列表中。随着maxsplit中4，我们可以分开的，街道名称门牌号码：

>>> [re.split（“：？”，条目，4）在条目中输入]
[['Ross'，'McFluff'，'834.345.1254'，'155'，'Elm Street']，
['Ronald'，'Heathmore'，'892.345.3428'，'436'，'Finley Avenue']，
['Frank'，'Burger'，'925.541.7625'，'662'，'South Dogwood Way']，
['希瑟'，'阿尔布雷希特'，'548.326.4584'，'919'，'公园广场']]
5.5。文字蒙古
sub()用字符串或函数的结果替换模式的每次出现。此示例演示如何使用sub()函数“munge”文本，或者随机化句子中每个单词中除第一个和最后一个字符之外的所有字符的顺序：

>>> def repl（m）：
... inner_word = list（m.group（2））
... random.shuffle（inner_word）
... return m.group（1）+“”。join（inner_word）+ m.group（3）
>>> text =“Abdolmalek教授，请及时报告你的缺席情况。”
>>> re.sub（r“（\ w）（\ w +）（\ w）”，repl，text）
'Poefsrosr Aealmlobdk，pslaee重新定义了你的abmsetoces plmrptoy。
>>> re.sub（r“（\ w）（\ w +）（\ w）”，repl，text）
'Pofsroser Aodlambelk，plasee reoprt yuor asnebces potlmrpy。
5.6。找到所有副词
findall()匹配所有出现的模式，而不仅仅是第一个模式search()。例如，如果一个人是作家并且想要在某些文本中找到所有副词，他或她可能会findall()以下列方式使用：

>>> text =“他被小心翼翼地伪装，但被警方迅速抓获。”
>>> re.findall（r“\ w + ly”，text）
['小心'，'快'']
5.7。查找所有副词及其位置
如果想要获得关于模式的所有匹配的更多信息而不是匹配的文本，finditer()那么它是有用的，因为它提供匹配对象而不是字符串。继续前面的例子，如果一个是想要在某些文本中找到所有副词及其位置的作家，他或她将以finditer()下列方式使用：

>>> text =“他被小心翼翼地伪装，但被警方迅速抓获。”
>>> for re in finditer（r“\ w + ly”，text）：
... print（'％02d-％02d：％s'％（m.start（），m.end（），m.group（0）））
07-16：小心
40-47：很快
5.8。原始字符串表示法
原始字符串表示法（r"text"）保持正则表达式理智。没有它，'\'正则表达式中的每个反斜杠（）都必须以另一个为前缀来转义它。例如，以下两行代码在功能上是相同的：

>>> re.match（r“\ W（。）\ 1 \ W”，“ff”）
<_sre.SRE_Match对象; span =（0,4），match ='ff'>
>>> re.match（“\\ W（。）\\ 1 \\ W”，“ff”）
<_sre.SRE_Match对象; span =（0,4），match ='ff'>
当想要匹配文字反斜杠时，必须在正则表达式中对其进行转义。使用原始字符串表示法，这意味着r"\\"。如果没有原始字符串表示法，必须使用"\\\\"，使以下代码行功能相同：

>>> re.match（r“\\”，r“\\”）
<_sre.SRE_Match对象; span =（0,1），match ='\\'>
>>> re.match（“\\\\”，r“\\”）
<_sre.SRE_Match对象; span =（0,1），match ='\\'>
5.9。编写Tokenizer
甲标记生成器或扫描仪分析的字符串进行分类字符组。这是编写编译器或解释器的有用的第一步。

文本类别使用正则表达式指定。该技术是将它们组合成单个主正则表达式并循环连续匹配：

导入集合
进口重新

Token = collections.namedtuple（'Token'，['typ'，'value'，'line'，'column']）

def tokenize（代码）：
    keywords = {'IF'，'THEN'，'ENDIF'，'FOR'，'NEXT'，'GOSUB'，'RETURN'}
    token_specification = [
        （'NUMBER'，r'\ d +（\。\ d *）？'），＃整数或十进制数
        （'ASSIGN'，r'：='），＃赋值运算符
        （'END'，r';'），＃Statement终止符
        （'ID'，r'[A-Za-z] +'），＃标识符
        （'OP'，r'[+ \  -  * /]'），＃算术运算符
        （'NEWLINE'，r'\ n'），＃Line endings
        （'跳过'，r'[\ t] +'），＃跳过空格和标签
        （'MISMATCH'，r'。'），＃任何其他角色
    ]
    tok_regex ='|'。join（'（？P <％s>％s）'对应于token_specification中的％对）
    line_num = 1
    line_start = 0
    for in re.finditer（tok_regex，code）：
        kind = mo.lastgroup
        value = mo.group（kind）
        如果善意=='NEWLINE'：
            line_start = mo.end（）
            line_num + = 1
        elif kind =='SKIP'：
            通过
        elif kind =='MISMATCH'：
            引发RuntimeError（f {{value！r}意外在线{line_num}'）
        其他：
            if kind =='ID'和关键字中的值：
                kind = value
            column = mo.start（） -  line_start
            yield Token（种类，值，line_num，列）

statements ='''
    如果数量那么
        总计：=总计+价格*数量;
        税：=价格* 0.05;
    万一;
“””

对于tokenize（语句）中的标记：
    打印（标记）
标记生成器生成以下输出：

令牌（typ ='IF'，值='IF'，行= 2，列= 4）
令牌（typ ='ID'，值='数量'，行= 2，列= 7）
令牌（typ ='THEN'，值='THEN'，行= 2，列= 16）
令牌（typ ='ID'，值='总'，行= 3，列= 8）
令牌（typ ='ASSIGN'，值='：='，行= 3，列= 14）
令牌（typ ='ID'，值='总'，行= 3，列= 17）
令牌（typ ='OP'，值='+'，行= 3，列= 23）
令牌（typ ='ID'，值='价格'，行= 3，列= 25）
令牌（typ ='OP'，值='*'，行= 3，列= 31）
令牌（typ ='ID'，值='数量'，行= 3，列= 33）
令牌（typ ='END'，value =';'，line = 3，column = 41）
令牌（typ ='ID'，值='税'，行= 4，列= 8）
令牌（typ ='ASSIGN'，值='：='，行= 4，列= 12）
令牌（typ ='ID'，值='价格'，行= 4，列= 15）
令牌（typ ='OP'，value ='*'，line = 4，column = 21）
令牌（typ ='NUMBER'，值='0.05'，行= 4，列= 23）
令牌（typ ='END'，value =';'，line = 4，column = 27）
令牌（typ ='ENDIF'，值='ENDIF'，行= 5，列= 4）
令牌（typ ='END'，值=';'，行= 5，列= 9）