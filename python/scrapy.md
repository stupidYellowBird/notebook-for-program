# scrapy

## 创建一个新的Scrapy项目

`scrapy startproject tutorial`
生成的工程目录结构如下：

```python
    tutorial
    │  items.py
    │  pipelines.py
    │  settings.py
    │  __init__.py
    │
    └─spiders
         __init__.py

```

这些文件主要是：

- scrapy.cfg: 项目配置文件
- tutorial/: 项目python模块, 呆会代码将从这里导入
- tutorial/items.py: 项目items文件
- tutorial/pipelines.py: 项目管道文件
- tutorial/settings.py: 项目配置文件
- tutorial/spiders: 放置spider的目录

### 定义提取的Item

它通过创建一个`scrapy.item.Item`类来声明，定义它的属性为`scrpy.item.Field`对象，就像是一个对象关系映射(ORM).
我们通过将需要的item模型化，来控制从dmoz.org获得的站点数据，比如我们要获得站点的名字，url和网站描述，我们定义这三种属性的域。要做到这点，我们编辑在tutorial目录下的items.py文件，我们的Item类将会是这样

```python
from scrapy.item import Item, Field
class DmozItem(Item):
    title = Field()
    link = Field()
    desc = Field()
```

### 写一个Spider用来爬取网站，并提取Items

Spider是用户编写的爬虫类，放置在spiders目录下。
要建立一个Spider，继承自基类`scrapy.spider.BaseSpider`，并确定三个主要的、强制的属性：

1. `name`：爬虫的识别名，它必须是唯一的，在不同的爬虫中你必须定义不同的名字.
2. `start_urls`：爬虫开始爬的一个URL列表。爬虫从这里开始抓取数据，所以，第一次下载的数据将会从这些URLS开始。其他子URL将会从这些起始URL中继承性生成。
3. `parse()`：爬虫的方法，调用时候传入从每一个URL传回的Response对象作为参数，response将会是parse方法的唯一的一个参数,这个方法负责解析返回的数据、匹配抓取的数据(解析为item)并跟踪更多的URL。

```python
from scrapy.spider import BaseSpider

class DmozSpider(BaseSpider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)
```

启动爬虫`scrapy crawl dmoz`

### 提取Items

```html
Scrapy 使用一种叫做 XPath selectors的机制，xpath的使用如下：
/head/title: 选择HTML文档<head>元素下面的<title> 标签。
/head/title/text(): 选择前面提到的<title> 元素下面的文本内容
//td: 选择所有 <td> 元素
//div[@class="mine"]: 选择所有包含 class="mine" 属性的div 标签元素
```

保存数据`scrapy crawl dmoz -o items.json -t json`

### 写一个Item Pipeline用来存储提取出的Items
