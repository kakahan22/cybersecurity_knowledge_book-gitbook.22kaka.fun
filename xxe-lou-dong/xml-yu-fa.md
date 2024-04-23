---
description: xml语法是xxe漏洞的基础。
---

# 📒 XML语法

## ①xml的定义：

xml是可扩展标记语言，他是为了传输数据而不是显示数据。他他不像html一样，他是没有预定义的标签。





***



## ②xml的基本格式与基本语法

### Ⅰ基本格式框架：

直接借鉴大牛的总结

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?><!--xml文件的声明-->
<bookstore>                                                 <!--根元素-->
<book category="COOKING">        <!--bookstore的子元素，category为属性-->
<title>Everyday Italian</title>           <!--book的子元素，lang为属性-->
<author>Giada De Laurentiis</author>                  <!--book的子元素-->
<year>2005</year>                                     <!--book的子元素-->
<price>30.00</price>                                  <!--book的子元素-->
</book>                                                 <!--book的结束-->
</bookstore>                                       <!--bookstore的结束-->
```

上面的standalon的值是yes的时候表示DTD仅用于验证文档结构，从而外部实体将被禁用，但他的默认值是no。



### Ⅱ.基本语法

其实感觉大部分语法和html差不多，就是一定要有根元素。

如果多个字符需要转义，则可以将这些内容存放到CDATA里面，比如

```xml
<![CDATA[ 内容 ]]>
```







***

## ③DTD

xml文档有自己的一个格式规范，这个格式规范是由一个叫做DTD的东西控制的。

### Ⅰ实体引用

XML元素以形如\<tag>foo\</tag>的标签开始和结束，如果内部出现<等特殊字符就会解析失败，为了避免，XML用实体引用替换特殊字符。XML预定的五个实体引用，即`&lt , &gt ,&amp, &apos,` \&quot分别替换`< , >,  &, ' , "`



### ⅡDTD的引入方式

可以在文档内部声明也可以外部引用。

**1.内部引用**

比如我们内部声明：放在xml文档中，就是一般的html的文件开头

```xml
<!DOCTYPE 根元素名称 [元素声明]>
```

比如

```xml
<?xml version="1.0"?>
<!DOCTYPE note [<!--定义此文档是 note 类型的文档-->
<!ELEMENT note (to,from,heading,body)><!--定义note元素有四个元素-->
<!ELEMENT to (#PCDATA)><!--定义to元素为”#PCDATA”类型-->
<!ELEMENT from (#PCDATA)><!--定义from元素为”#PCDATA”类型-->
<!ELEMENT head (#PCDATA)><!--定义head元素为”#PCDATA”类型-->
<!ELEMENT body (#PCDATA)><!--定义body元素为”#PCDATA”类型-->
]>
<note>
<to>Y0u</to>
<from>@re</from>
<head>v3ry</head>
<body>g00d!</body>
</note>
```

**2.外部引用**

（1）引入外部dtd文件

```xml
<!DOCTYPE 根元素名称 SYSTEM "dtd路径">
```

（2）使用外部的dtd文件（网络上的dtd文件）

```xml
<!DOCTYPE 根元素 PUBLIC "DTD名称" "DTD文档的URL">
```

当使用外部DTD时，通过如下语法引入：

```xml
<!DOCTYPE root-element SYSTEM "filename">
```

示例：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE root-element SYSTEM "test.dtd">
<note>
<to>Y0u</to>
<from>@re</from>
<head>v3ry</head>
<body>g00d!</body>
</note>
```

上面的引用的test.dtd的内容是

```xml
<!ELEMENT to (#PCDATA)><!--定义to元素为”#PCDATA”类型-->
<!ELEMENT from (#PCDATA)><!--定义from元素为”#PCDATA”类型-->
<!ELEMENT head (#PCDATA)><!--定义head元素为”#PCDATA”类型-->
<!ELEMENT body (#PCDATA)><!--定义body元素为”#PCDATA”类型-->
```







***

## ④PCDATA

意思就是被解析的字符数据。PCDATA是会被解析器解析的文本。被解析的文本中不应该包含`&, < ,>` 字符，要用`&amp, &lt,&gt`来替换







***

## ⑤CDATA

是字符数据的意思，CDATA是不会被解析器解析的文本，在这些文本中的标签不会被当做标记来对待，其中的实体也不会被展开。







***

## ⑥DTD元素

上面我们其实提到过，就是定义的时候，但是他具体的代表用图来显示















































































## 参考门：

{% embed url="https://xz.aliyun.com/t/6887?time__1311=n4%2BxnD0DRDyB5AKDsYohrDuD0OuQDgmOD7qhD&alichlgref=https%3A%2F%2Fxz.aliyun.com%2Ft%2F6887#toc-0" %}







