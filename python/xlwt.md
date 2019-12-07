```
import os,xlwt,datetime
### 新建一个Workbook
data =xlwt.Workbook()
### 新建一个sheet，名称为'sheet'
sheet = data.add_sheet(u"sheet")
### 创建格式style1
style1 = xlwt.XFStyle()
```

### 设置字体格式
```
font1 = xlwt.Font()
font1.name = 'Times New Roman'
font1.colour_index = 2  #字体颜色为红色
0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan
# 下划线类型
font1.underline = xlwt.Font.UNDERLINE_DOUBLE
- UNDERLINE_DOUBLE 代表双下划线，
- UNDERLINE_NONE,
- UNDERLINE_SINGLE,
- UNDERLINE_SINGLE_ACC,
- UNDERLINE_DOUBLE,
- UNDERLINE_DOUBLE_ACC
# 设置上标
font1.escapement = xlwt.Font.ESCAPEMENT_SUPERSCRIPT
font1.family = xlwt.Font.FAMILY_ROMAN
font1.height = 0x190
# 0x190是16进制，换成10进制为400，然后除以20，就得到字体的大小为20
style1.font = font1
#将创建的font1字体格式应用到style1上
font1.italic = True  #斜体
font1.struck_out = True   #删除线
font1.height = 0x258   #字体大小为30
```
### 设置列宽
```python
sheet.col(0).width = 6000
sheet.set_col_default_width(2)
```
### 设置单元格对齐方式
```python
alignment = xlwt.Alignment()    #创建alignment
alignment.horz = xlwt.Alignment.HORZ_CENTER   #设置水平对齐为居中，
#May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER,
 HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
alignment.vert = xlwt.Alignment.VERT_CENTER   #设置垂直对齐为居中，
#May be: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
style3.alignment = alignment   #应用alignment到style3上
```
### 插入时间
```python
style3.num_format_str = 'YYYY-MM-DD HH:MM:SS'   #设置时间格式
sheet.write(1,1,datetime.datetime.now(),style3)   #在第2行第2列插入当前时间，格式为style3
```
### 设置单元格背景颜色

```python
pattern_yellow = xlwt.Pattern()  #创建pattern_yellow
pattern_yellow.pattern = xlwt.Pattern.SOLID_PATTERN  #设置填充模式为全部填充
pattern_yellow.pattern_fore_colour = 5    #设置填充颜色为yellow黄色
style1.pattern = pattern_yellow  #把设置的pattern应用到style3上
```

### 设置单元格边框

```python
borders = xlwt.Borders()   #创建borders
borders.left = xlwt.Borders.DASHED #设置左边框的类型为虚线
#May be: NO_LINE, THIN, MEDIUM, DASHED, DOTTED, THICK, DOUBLE, HAIR, MEDIUM_DASHED,
THIN_DASH_DOTTED, MEDIUM_DASH_DOTTED, THIN_DASH_DOT_DOTTED, MEDIUM_DASH_DOT_DOTTED, SLANTED_MEDIUM_DASH_DOTTED, or 0x00 through 0x0D.
borders.right = xlwt.Borders.THIN  #设置右边框的类型为细线
borders.top = xlwt.Borders.DOTTED   #设置上边框的类型为打点的
borders.bottom = xlwt.Borders.THICK  #设置底部边框类型为粗线
borders.left_colour = 0x10  #设置左边框线条颜色
style1.borders = borders    #将borders应用到style1上
```
### 写入单元格
```
sheet.write(3, 0, 'HuZhangdong', style1)
```
### 保存
```
data.save(u'e:\\3.xls')

```
函数xlwt.Workbook()只能新建一个excel文档，不能打开一个已经存在的文档，下一章会讲解如何通过xlutils修改一个已经存在的excel文档。
