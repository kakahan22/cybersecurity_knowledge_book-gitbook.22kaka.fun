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

<figure><img src="../.gitbook/assets/image (10) (1).png" alt=""><figcaption></figcaption></figure>

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































### 参考门：

{% embed url="https://blog.csdn.net/senlin1202/article/details/50800009" %}

{% embed url="https://xz.aliyun.com/t/2557?time__1311=n4%2BxnieDqxg7Ki%3DD%2FWT4BIalhxRex7u%2BD" %}













