

## 关于PIL库的一些概念
pil能处理的图片类型：pil可以处理光栅图片(像素数据组成的的块)。
通道：一个图片可以包含一到多个数据通道，如果这些通道具有相同的维数和深度，Pil允许将这些通道进行叠加

**模式：**

- 1	1位像素，黑和白，存成8位的像素
- L	8位像素，黑白
- P	8位像素，使用调色板映射到任何其他模式
- RGB	3×8位像素，真彩
- RGBA	4×8位像素，真彩+透明通道
- CMYK	4×8位像素，颜色隔离
- YCbCr	3×8位像素，彩色视频格式
- I	32位整型像素
- F	32位浮点型像素


**尺寸：** 通过图片对象的size属性可以得到图片的尺寸，结果这是一个二元组，包含水平和垂直方向上的像素数。
**坐标：** Pil采取左上角为(0,0)的坐标系统
**调色板：**mode("P")为每个像素定义具体的颜色值
**图片信息：**可以通过info属性读取一张图片的附加信息，这个与图片的格式有关。
滤镜:在对图片的几何操作中可能会将多个输入像素映射到单个的输出像素，pil提供4种不同的采样滤镜(在目前的版本中，后续的版本可能支持更多)

- NEAREST	最近
- BILINEAR	双线型
- BICUBIC	双三次插值
- ANTIALIAS	平滑


　　在RGB模式下，每个图片由三个通道叠加而成，每个模式下为一个灰度图，当有一个调色板来调色的时候，这三张灰度图的叠加即可合成3*8位(每个像素)的一个真彩图片。pil库中，图片之间的模式(mode)可以转化。下面给出一些简单的例子，例子中的所有图片均来自于国家地理的官网，为了使得文档比较短小，每个图片均使用Pil缩放成1/2大小，如有侵权嫌疑，请尽快联系，我会删除这些图片。

　　所有的图片操作必须有一个操作对象，Pil提供open(filename)进行这个过程

### 打开图片

　　1.导入pil的Image模块

　　2.使用open(filename)打开文件，返回一个image对象
```
im = Image.open('filename')

```
此后，一切关于图片的操作均基于这个对象。
　　打开后，我们可以查看一些图片信息，如im.format, im.size, im.mode等。调用im.show()会在图片查看工具中显示当前操作的image对象，这个跟个人的系统有关系，我系统中默认是用Windows Picture and Fax Viewer打开的。这个方法用来查看临时的图片效果。

### 读写图片

　　pil中转换图片格式非常简单(转换图片模式是另一个概念，不要混淆)，只需要调用img.save(filename)即可比如有一个bmp(位图)图片，使用img = Image.open('file.bmp')打开后，只需要img.save('file.jpg')即可转换。不过一般情况下，save(filename)是不用做这个用途的，通常，save用以保存一个临时的image对象到硬盘。而转换工作由一个功能更为强大的convert()方法来完成。

### 拷贝，粘贴，合并
```
box = (100,100,500,500)#设置要拷贝的区域

```
将im表示的图片对象拷贝到region中，大小为(400*400)像素。这个region可以用来后续的操作(region其实就是一个Image对象)，box变量是一个四元组(左，上，右，下)。
```
region = im.crop(box)
region = region.transpose(Image.ROTATE_180)#从字面上就可
```
以看出，先把region中的Image反转180度，然后再放回到region中。
```
im.paste(region, box)#粘贴box大小的region到原先的图片对象中。

```
　　前面说过，每一个RGB都是由三个通道的灰度图叠加的，所以pil提供了将这三个通道分离的方法


```python
r,g,b = im.split()#分割成三个通道
r.show() #红色通道的灰度图
g.show()  #绿色通道的灰度图
b.show() #蓝色通道的灰度图
im = Image.merge("RGB", (b, g, r))#将b,r两个通道进行翻转,生成互换红蓝通道后的合成图
```
### 几何转变

　　几何转变提供resize,rotate等方法，用以重定义图片大小，对图片进行旋转等操作，在实际应用中比较广泛。
```python
　 out = img.resize((128, 128))#resize成128*128像素大小。
　 out = img.rotate(45)#逆时针旋转45度
```

### 逆时针45度
　　镜面效果，左右翻转
　　transpose()方法预定义了一些旋转方式，如
　　左右反转，上下翻转，逆时针旋转(90,180,270)度等，非常方便，rotate()和transpose()方法在表现上没有任何不同。

### 图片加强

　　**滤镜: **ImageFilter模块提供了很多预定义的图片加强滤镜。比如一个常用的滤镜,细节(detail滤镜)
```pthon
import ImageFilter
out = im.filter(ImageFilter.DETAIL)

```

　　直接操作像素点

　　不但可以对每个像素点进行操作，而且，每一个通道都可以独立的进行操作。比如，将每个像素点的亮度(不知道有没有更专业的词)增大20%
```python
out = img.point(lambda i : i * 1.2)#注意这里用到一个匿名函数(那个可以把i的1.2倍返回的函数),对每个点都做20%的增强

```

　　如上边的那个例子，我们可以将一个RGB模式的图分离成三个通道的层

```
r,g,b = img.split()#神奇而又强大的python语法

```
然后对一个通道进行加强或减弱操作，完成后我们又可以使用Merge将通道合并，从而改变图片的色调(冷暖色调的互换)等。

　　更高级的图片加强，可以使用ImageEnhance模块，其中包含了大量的预定义的图片加强方式。
```
import ImageEnhance
enh = ImageEnhance.Contrast(im)
enh.ehhance(1.5).show("50% more contrast")

```
　　读写图片的更多方式

　　通常，我们使用open方法进行图片的打开操作。但是这不是唯一的方式。完全可以跟python的IO整合起来。如
```

fp = open("file.jpg", "rb")
im = Image.open(fp)

```
　　甚至，你可以从一个字符串中读出图片数据来(python真是神奇啊)。
```

import StringIO
img = Image.open(StringIO.StringIO(buffer))

```
=============================
>Abstract:This context introduces some methods used to fullfill simply image processing task in python programming language.Although the best image processing toolkit is the Image Processing Toolbox of MATLAB,python is superior to this toolkit when your staff is somewhat “simple” or simple but boring and exhausting image processing commitment. 

Keywords:Image Processing Image Enhancement Python

1.引言:

提到图像处理，人们通常想到的工具是MATLAB。诚然，MATLAB提供了一个强大的图像处理工具箱。但是，对于简单的图像处理任务而言，采用一 种高级的语言将起到事半功倍的效果。Python无疑就是实现这一功能的理想选择。Python的面向对象、弱数据类型等等特性都使得用它来进行简单的图 像处理的时候非常的简洁方便。

2.简介：

PythonWare公司提供了免费的图像处理工具包PIL(Python Image Library),该软件包提供了基本的图像处理功能，如：改变图像大小，旋转图像，图像格式转换，色场空间转换，图像增强，直方图处理，插值和滤波等 等。虽然在这个软件包上要实现类似MATLAB中的复杂的图像处理算法并不太适合，但是Python的快速开发能力以及面向对象等等诸多特点使得它非常适 合用来进行原型开发。

在PIL中，任何一副图像都是用一个Image对象表示，而这个类由和它同名的模块导出，因此，要加载一副图像，最简单的形式是这样的：

```
import Image

img = Image.open(“dip.jpg”)
```

注意：第一行的Image是模块名；第二行的img是一个Image对象； Image类是在Image模块中定义的。关于Image模块和Image类，切记不要混淆了。现在，我们就可以对img进行各种操作了，所有对img的 操作最终都会反映到到dip.img图像上。

PIL提供了丰富的功能模块：Image,ImageDraw,ImageEnhance,ImageFile等等。最常用到的模块是Image, ImageDraw,ImageEnhance这三个模块。下面我对此分别做一介绍。关于其它模块的使用请参见说明文档.有关PIL软件包和相关的说明文 档可在PythonWare的站点www.pythonware.com上获得。

3．Image模块：

Image模块是PIL最基本的模块，其中导出了Image类，一个Image类实例对象就对应了一副图像。同时，Image模块还提供了很多有用的函数。

（1）打开一副图像文件：
```

import Image

img = Image.open(“dip.jpg”)
```

这将返回一个Image类实例对象，后面的所有的操作都是在img上完成的。在这里，我们读入的图像是：



（2）调整图像大小:

```
import Image

img = Image.open("img.jpg")

new_img = img.resize((128,128),Image.BILINEAR)

new_img.save("new_img.jpg")
```

原来的图像大小是256x256,现在，保存的new_img.jpg的大小是128x128:



就是这么简单，需要说明的是Image.BILINEAR指定采用双线性法对像素点插值。

（3）旋转图像：

现在我们把刚才调整过大小的图像旋转45度：

```
import Image

img = Image.open("img.jpg")

new_img = img.resize((128,128),Image.BILINEAR)

rot_img = new_img.rotate(45)

rot_img.save("rot_img.jpg")
```

于是我们保存到rot_img.jpg的图像看起来像下面这样：



（4）格式转换：

假设我们要把上面生成的rot_img.jpg转换成bmp图像，要做到这一点这太简单了：只需要在上面的代码后面添加下面这样一行即可：

```
rot_img.save("con_img.bmp")
```

如果不指定保存格式，PIL将自动根据文件名后缀完成格式之间的转换，是不是很简单呢？

（5）直方图统计：

Image类实例的histogram()方法能够对直方图数据进行统计，并将结果做为一个列表(list)返回。比如，我们对上面的旋转后生成的图像进行直方图统计：

```
import Image

img = Image.open("img.jpg")

new_img = img.resize((128,128),Image.BILINEAR)

rot_img = new_img.rotate(45)

print rot_img.histogram()
```

运行之后将打印出所有256个灰度级像素点个数的统计值：

[2819, 22, 82, 119, 186, 204, 212, 218, 223, 200, 151, 103, 129, 74, 80, 83, 110, 70, 59, 64, 59, 58, 35, 45, 42, 38, 32, 39, 33, 19, 24, 26, 32, 17, 33, 24, 34, 19, 18, 15, 11, 23, 16, 15, 21, 13, 20, 22, 27, 10, 29, 26, 18, 16, 28, 18, 26, 37, 36, 25, 28, 36, 28, 31, 22, 20, 15, 13, 15, 18, 12, 15, 21, 21, 12, 18, 17, 12, 11, 18, 16, 14, 21, 20, 18, 19, 15, 20, 22, 16, 22, 15, 23, 26, 16, 8, 13, 19, 30, 16, 15, 11, 22, 12, 14, 8, 10, 14, 13, 8, 12, 22, 11, 13, 18, 16, 21, 21, 14, 14, 11, 14, 15, 9, 23, 19, 15, 17, 9, 10, 11, 12, 14, 16, 9, 17, 15, 20, 14, 18, 18, 32, 34, 55, 54, 51, 72, 78, 83, 99, 118, 171, 138, 177, 191, 158, 159, 123, 106, 136, 121, 121, 148, 137, 118, 145, 150, 150, 133, 98, 111, 118, 111, 104, 129, 124, 104, 144, 126, 118, 133, 124, 108, 87, 87, 83, 85, 75, 76, 75, 62, 84, 46, 61, 54, 54, 63, 45, 54, 66, 46, 52, 51, 49, 51, 52, 62, 50, 67, 72, 53, 53, 83, 54, 39, 57, 31, 53, 31, 38, 38, 42, 31, 29, 38, 39, 39, 26, 43, 36, 45, 68, 57, 60, 42, 39, 41, 38, 46, 44, 40, 47, 57, 45, 59, 53, 59, 81, 78, 75, 95, 46, 62, 1, 0, 0]

小结：以上介绍了Image模块最基本的功能，作为对PIL库初步的认识已经足够了，值得说明的是，这里提到只是Image一部分功能而已，要对整个Image模块的功能有一个全面的了解和掌握，请参见PIL-handbook.pdf。

4.ImageDraw模块：

ImageDraw模块提供了基本的图形能力，这里的图形能力指的主要是图形的绘制能力。PIL库提供了比较丰富的图形绘制函数，可以绘制直线、弧 线、矩形、多边形、椭圆、扇形等等。ImageDraw实现了一个Draw类，所有的图形绘制功能都是在Draw类实例的方法中实现的。实例化一个 Draw类实例很简单：

```
import Image,ImageDraw

img = Image.open("img.jpg")

draw = ImageDraw.Draw(img)
```

首先要导入ImageDraw模块。然后，因为绘图操作是在图像上进行的，因此实例化Draw类的时候要把Image对象img通过参数传递给Draw类的构造函数。现在，你就可以调用draw的各种方法在img上绘制图形了。

(1)绘制直线：

```
import Image,ImageDraw

img = Image.open("img.jpg")

draw = ImageDraw.Draw(img)

width,height = img.size

draw.line(((0,0),(width-1,height-1)),fill=255)

draw.line(((0,height-1),(width-1,0)),fill=255)

img.save("cross_line.jpg")
```

解释一下上面这段代码：

前面三行这里就不解释了。width,height = img.size是得到img的大小，得到这两个属性的主要目的是要在下面的两行代码中使用：
```

draw.line(((0,0),(width-1,height-1)),fill=255)

draw.line(((0,height-1),(width-1,0)),fill=255)
```

这两行代码在img图像的两个对角线方向绘制了两条直线。最后，我们把绘制了两条对角线的图像保存为cross_line.jpg,最后得到的效果如下面所示：



(2)绘制圆：
```

import Image,ImageDraw

img = Image.open("img.jpg")

width,height = img.size

draw = ImageDraw.Draw(img)

draw.arc((0,0,width-1,height-1),0,360,fill=255)

img.save("circle.jpg")
```

这几行代码和上面绘制对角线的代码相比，只更改了一行，即：
```

draw.arc((0,0,width-1,height-1),0,360,fill=255)
```

说明：

(0,0,width-1,height-1)指定了所画弧线的界限；

0,360是所画弧线的起始角度和终止角度；

fill=255指定了所画线的颜色，注意：PIL的文档上说这里应该用outline=255,但是我发现实际只能用fill=255来指定弧线的颜色。

绘制圆后的图像：



小结：有关图形绘制的操作都是类似的，因此这里只给出一个简略的介绍。详细规范请参见PIL-handbook.pdf。

5．ImageEnhance模块：

这个模块提供了一个常用的图像增强工具箱。可以用来进行色彩增强、亮度增强、对比度增强、图像尖锐化等等增强操作。所有操作都有相同形式的接口—— 通过相应类的enhance方法实现：色彩增强通过Color类的enhance方法实现；亮度增强通过Brightness类的enhance方法实 现；对比度增强通过Contrast类的enhance方法实现；尖锐化通过Sharpness类的enhance方法实现。所有的操作都需要向类的构造 函数传递一个Image对象作为参数，这个参数定义了增强作用的对象。同时所有的操作都返回一个新的Image对象。如果传给enhance方法的参数是 1.0，则不对原图像做任何改变，直接返回原图像的一个拷贝。下面我们通过几个简单的例子进行说明：

（1）亮度增强：

```
import Image,ImageEnhance

img = Image.open("img.jpg")

brightness = ImageEnhance.Brightness(img)

bright_img = brightness.enhance(2.0)

bright_img.save("bright.jpg")
```

说明：
```

brightness = ImageEnhance.Brightness(img)
```

这一行把img传给Brightness类，得到一个Brightness类实例；

```
bright_img = brightness.enhance(2.0)
```

这一行调用brightness实例的enhance方法，传入的参数指定将亮度增强2倍；

我们最后得到bright.jpg图像看起来像这样：



右边的的图像是增强之前的图像(原图像)，注意两者的亮度差比是很大的。

（2）图像尖锐化：
```

import Image,ImageEnhance

img = Image.open("img.jpg")

sharpness = ImageEnhance.Sharpness(img)

sharp_img = sharpness.enhance(7.0)

sharp_img.save("bright.jpg")
```

这段代码和上面的完全类似，因此这里不做过多的说明。我们来看一下增强前后的效果对比：



右边的的图像是增强之前的原图像，注意两者的尖锐化程度是很不一样的。

（3）对比度增强：

```
import Image,ImageEnhance

img = Image.open("img.jpg")

contrast = ImageEnhance.Contrast(img)

contrast_img = contrast.enhance(2.0)

contrast_img.save("contrast.jpg")
```

同上，我们只看增强前后的效果对比：



很明显，增强之后的图像（左边）比原来的图像（右边）对比度提高了。

小结：用ImageEnhance来进行常用的图像增强是有效的，并且很简单。当然，对于精细复杂的图像增强操作而言这里提供的功能不够强大，但是在进行简单的图像增强操作的时候，一种简单易行的解决方案无疑是很吸引人的。

6.总结：

在批处理或者简单的图像处理任务中，采用python和PIL（Python Image Library）的组合来完成图像处理任务是一个很不错的选择。设想有一个需要对某个文件夹下的所有图像将对比度提高2倍的任务。用python来做将是 十分简单的。当然，我也不得不承认python在图像处理方面的功能还比较弱，显然还不适合用来进行滤波、特征提取等等一些更为复杂的应用。我个人的观点 是，当你要实现这些“高级”的算法的时候，好吧，把它交给MATLAB去完成。但是，如果你面对的只是一个通常的不要求很复杂算法的图像处理任务，那么， python应该才是你的最佳搭档。

参考文献：

1．《数字图像处理》（第二版）；冈萨雷斯；电子工业出版社；2003；

2．《Python Image Library Handbook》；Fredrik Lundh,Matthew Ellis；PythonWare.Inc；2002；

3．《Python Documentation》(Release 2.3.3)；Guido van Rossum；2003；

4．www.python.org

5．www.pythonware.org
