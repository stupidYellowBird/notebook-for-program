## Emmet 语法

后代     >      ul.li*5
上级     ^
兄弟     +      div+p+a
分组     ()     div>(header>ul>li*2>a)+footer>p
自增     $      ul>li.item$*5  ul>li.item$$$*5
                ul>li.item$@-*5倒序
                ul>li.item$@3*5 从某个数开始
class类 .       ul>li.title  p.class1.class2.class3
id类    #
混合            form#search.wide
自定义属性      p[title=”Hello world”] td[rowspan=2 colspan=3 title]
文本：{}        a{Click me}  p>{Click }+a{here}+{ to continue}
隐式标签        ul>.class       table>.row>.col


### 表单
form
form:get
form:post
input：text input
input:image, input:i
input:button, input:b
input:reset
input:hidden, input:h
input:search
input:email
input:url
input:password, input:p
input:datetime
input:date
input:datetime-local
input:month
input:week
input:time
input:tel
input:number
input:color
input:checkbox, input:c
input:radio, input:r
input:range
input:file, input:f
input:submit, input:s
input:image, input:i
input:button, input:b
select
select:disabled, select:d
option, opt
textarea

### 按钮
button:submit, button:s, btn:s
button:reset, button:r, btn:r
button:disabled, button:d, btn:d

### CSS
#### 背景
bg      background:#000;
bg+     background:#fff url() 0 0 no-repeat;
bg:n    background:none;
bgc     background-color:#fff;
bgc:t   background-color:transparent;
bgi     background-image:url();
bgi:n   background-image:none;
bgr     background-repeat:;
bgr:n   background-repeat:no-repeat;
bgr:x   background-repeat:repeat-x;
bgr:y   background-repeat:repeat-y;
bgr:sp  background-repeat:space;
bgr:rd  background-repeat:round;
bga     background-attachment:;
bga:f   background-attachment:fixed;
bga:s   background-attachment:scroll;
bgp     background-position:0 0;
bgpx    background-position-x:;
bgpy    background-position-y:;
bgbk    background-break:;
bgbk:bb background-break:bounding-box;
bgbk:eb background-break:each-box;
bgbk:c  background-break:continuous;
bgcp    background-clip:padding-box;
bgcp:bb background-clip:border-box;
bgcp:pb background-clip:padding-box;
bgcp:cb background-clip:content-box;
bgcp:nc background-clip:no-clip;
bgo     background-origin:;
bgo:pb  background-origin:padding-box;
bgo:bb  background-origin:border-box;
bgo:cb  background-origin:content-box;
bgsz    background-size:;
bgsz:a  background-size:auto;
bgsz:ct background-size:contain;
bgsz:cv background-size:cover;

#### 边距
m       margin:;
m:a     margin:auto;
mt      margin-top:;
mt:a    margin-top:auto;
mr      margin-right:;
mr:a    margin-right:auto;
mb      margin-bottom:;
mb:a    margin-bottom:auto;
ml      margin-left:;
ml:a    margin-left:auto;
p       padding:;
pt      padding-top:;
pr      padding-right:;
pb      padding-bottom:;
pl      padding-left:;
