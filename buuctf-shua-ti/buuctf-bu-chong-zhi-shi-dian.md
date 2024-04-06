# 💘 BUUCTF补充知识点

## 1.php网站备份

网站备份有两部分，一部分是数据库内容，另一部分是网站的源码。

常用的备份文件的后缀有



| 常见备份文件后缀                                                                      |
| ----------------------------------------------------------------------------- |
| .git                                                                          |
| .svn                                                                          |
| .swp                                                                          |
| .bak                                                                          |
| .bash\_history                                 .\~                       .bkf |

***

## 2.传参不允许含有字母

当传入的参数不允许含有字母，但是我们执行命令，查找命令这种的都需要传入字母的，这个时候的处理方法就是往变量面前加一个空格。比如$\_GET\['name']，我们在url输入的是?  name=。在？后面有一个空格。这个常用来绕过一个waf。

它的原理是

> 现在的变量叫（空格）name，不是name，但是php解析器在处理的时候会把空格去掉，这样就能够成功了，并且还上传的字母。

***

## 3.联合注入可以自己创建结果

联合注入有个小技巧，就是当联合查询不存在的数据的时候，他会自动创建这个不存在的数据，会创建一个虚拟数据让你找到。所以如果我们有时候不知道一个密码的时候可以自动创建一个密码或者用户名之类的去绕过

<figure><img src="../.gitbook/assets/image (169).png" alt=""><figcaption></figcaption></figure>





***



## <mark style="color:red;">※4.preg\_replace与RCE</mark>

这个是做题说的preg\_replace与RCE漏洞的问题。

我们是按照先知社区的来学习，因为这个完全没有遇到过，第一次看到别人这么说。

### ①案例引入

这例子他也是用的我碰到题目的例子。真是让人sad。但是他说案例简单，我哭死。

<figure><img src="../.gitbook/assets/image (10) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

这里解释一下这个/e模式究竟是什么吧。也解释一下这个函数（有点坚持不下去了）

> preg\_replace()执行正则表达式的搜索和替换。在subject中搜索pattern模式的匹配项，并且替换为replacement，如果指定了limi个匹配，则仅替换limit个匹配。
>
> ```php
>  preg_replace ( mixed $pattern , mixed $replacement , mixed $subject [, int $limit ] )
> ```

{% hint style="info" %}
/e 修正符使 preg\_replace() 将 replacement 参数当作 PHP 代码（在适当的逆向引用替换完之后）。提示：要确保 replacement 构成一个合法的 PHP 代码字符串，否则 PHP 会在报告在包含 preg\_replace() 的行中出现语法解析错误。&#x20;
{% endhint %}

所以现在我们知道了第一个和第三个参数是我们可以输入的。preg\_replace函数会在匹配到符号正则的字符串的时候，会将第二个参数当作代码来执行。

但是这一下就有个问题了，我们看到题目中的第二个参数是固定的strtolower（"\\\1")字符串。



### ①爬坑1

所以上面的指令其实是eval（‘strtolower（"\\\1");')，因为转义字符，这个\\\1其实是\1。这个\1另有说法

> 反向引用：
>
> 对一个正则表达式模式或部分模式 **两边添加圆括号** 将导致相关 **匹配存储到一个临时缓冲区** 中，所捕获的每个子匹配都按照在正则表达式模式中从左到右出现的顺序存储。缓冲区编号从 1 开始，最多可存储 99 个捕获的子表达式。每个缓冲区都可以使用 '\n' 访问，其中 n 为一个标识特定缓冲区的一位或两位十进制数。
>
>

这里举个例子

<figure><img src="../.gitbook/assets/image (254).png" alt=""><figcaption></figcaption></figure>

从答案来看，payload是/？.\*={${phpinfo()\}}所以参数名其实是.\*

值为{${phpinfo()\}}，所以我们的正则表达式发生了变化。

```
原先的语句：
 preg_replace('/(' . $regex . ')/ei', 'strtolower("\\1")', $value);
变成了语句：
 preg_replace('/(.*)/ei', 'strtolower("\\1")', {${phpinfo()}});
```

**替换字符串 `'strtolower("\\1")'`**：\
当找到与 `$re` 匹配的内容时，这部分内容将被替换为执行 `strtolower("\\1")` 的结果。在这里，`\\1` 是一个反向引用，它引用了正则表达式中第一个括号 `()` 内匹配到的内容。`strtolower` 函数将这个匹配到的内容转换为小写。



### ②爬坑2

这个坑是GET传递参数导致的坑。

我们如果是把.\*写到程序里面，肯定可以成功执行，但是如果我们是通过GET参数传入的话，我们无法执行phpinfo函数，因为我们通过GET传递的.\*会变成\__\*，这个原因是我们传入的非法的$_\_GET数组参数名，会将其转化为下划线，所以我们正则表达式会匹配失败。

通过文章作者fuzz后发现，

当非法字符为首字母时，只有点号会被替换成下划线。对此我们有另外一种匹配方法，这里贴出来。

```python
 \S*=${phpinfo()}
```



### ③爬坑3

这里来说一下为什么是{${phpinfo()\}}或者${phpinfo()}，才能执行phpinfo函数。这是因为php可变变量的原因。在php中双引号包裹的字符串中可以解析变量，单引号就不行。${phpinfo()}中的phpinfo（）会被当做变量先执行，执行后，就变成${1}了。所以

下面的这个问题是

```php
var_dump(phpinfo()); 
// 结果：布尔 true
var_dump(strtolower(phpinfo()));
// 结果：字符串 '1'
var_dump(preg_replace('/(.*)/ie','1','{${phpinfo()}}'));
// 结果：字符串'11'

var_dump(preg_replace('/(.*)/ie','strtolower("\\1")','{${phpinfo()}}'));
// 结果：空字符串''
var_dump(preg_replace('/(.*)/ie','strtolower("{${phpinfo()}}")','{${phpinfo()}}'));
// 结果：空字符串''
这里的'strtolower("{${phpinfo()}}")'执行后相当于 strtolower("{${1}}") 又相当于 strtolower("{null}") 又相当于 '' 空字符串
```









***

## 5.getallheaders()

当我们$\_GET遇到困难的时候，可以考虑通过getallheaders（）去执行header的内容，就把需要RCE的命令写在头部。

> getallheaders — 获取全部 HTTP 请求头信息







***

## 6.shtml文件

> shtml跟html类似，也是一种用于网页设计的标记型语言，区别在于：html是一种纯静态的标记型语言，在html文档里面写的内容是什么，用户打开浏览器看到的就是什么，而shtml是一种半静态半动态的标记型语言，在shtml里面可以包含SSI命令，当用户在浏览器浏览shtml文档的时候，里面包含的SSI命令会被解析，然后再呈现内容给用户。
>
> 作者：艾逗笔 链接：https://juejin.cn/post/6844903447095951373 来源：稀土掘金 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

这里主要介绍一下ssi指令的基本格式

\<!-– 指令名称="指令参数"-->

\<!-– 指令名称="指令参数"-->

如 程序代码：

\<!--#include file="info.htm"-->

\<!--#include file="info.htm"-->

说明：1．\<!-- -->是HTML语法中表示注释，当WEB[服务器](https://baike.baidu.com/item/%E6%9C%8D%E5%8A%A1%E5%99%A8/0?fromModule=lemma\_inlink)不支持SSI时，会忽略这些信息。

2．#include 为SSI指令之一。

3．file 为include的参数，info.htm为参数值，在本指令中指将要包含的文档名。

注意：1．\<!--与#号间无空格，只有SSI指令与参数间存在空格。

2．上面的标点=""，一个也不能少。

3．SSI指令是大小写敏感的，因此参数必须是小写才会起作用。

这里有几个需要特别注意的格式

### ①exec示范

作用：将某一外部程序的输出插入到页面中。可插入CGI程序或者是常规应用程序的输入，这取决于使用的参数是cmd还是cgi。

语法：

程序代码：\<!--#exec cmd="文件名称"-->\<!--#exec cgi="文件名称"-->

参数：cmd 常规应用程序cgi CGI脚本程序

示例：程序代码：

\<!--#exec cmd="cat /etc/passwd"-->将会显示密码文件

\<!--#exec cmd="dir /b"-->将会显示当前目录下文件列表

\<!--#exec cgi="/cgi-bin/gb.cgi"-->将会执行CGI程序gb.cgi。

\<!--#exec cgi="/cgi-bin/access\_log.cgi"-->将会执行CGI程序access\_log.cgi。

### ②include示范

\#include 示范作用：

将[文本文件](https://baike.baidu.com/item/%E6%96%87%E6%9C%AC%E6%96%87%E4%BB%B6/0?fromModule=lemma\_inlink)的内容直接插入到文档页面中。

语法：

程序代码：\<!--#include file="文件名称"-->

\<!--#include virtual="文件名称"-->

file 文件名是一个相对路径，该路径相对于使用 #include 指令的文档所在的目录。被包含文件可以在同一级目录或其子目录中，但不能在上一级目录中。如表示当前目录下的的nav\_head.htm文档，则为file="nav\_head.htm"。

virtual 文件名是 Web 站点上的虚拟目录的完整路径。如表示相对于服务器文档根目录下hoyi目录下的nav\_head.htm文件；则为virtual="/hoyi/nav\_head.htm"

参数：file 指定包含文件相对于本文档的位置virtual 指定相对于服务器文档根目录的位置注意：1．文件名称必须带有扩展名。

2．被包含的文件可以具有任何文件扩展名，我觉得直接使用htm扩展名最方便，微软公司推荐使用 .inc 扩展名（这就看你的爱好了）。

示例：程序代码：\<!--#include file="nav\_head.htm"-->将头文件插入到当前页面\<!--#include file="nav\_foot.htm"-->将尾文件插入到当前页面



























### 参考门：

{% embed url="https://blog.csdn.net/senlin1202/article/details/50800009" %}

{% embed url="https://xz.aliyun.com/t/2557?time__1311=n4%2BxnieDqxg7Ki%3DD%2FWT4BIalhxRex7u%2BD" %}













