---
description: 我的理解是web应用允许用户上传一些头像，附件之类的。但是如果web应用上传了一句话木马等webshell，从而控制网站。
---

# 🏍️ 文件上传漏洞知识点总结（包含了文件解析漏洞）

看网上都是分成了前端和后端来分别讲解的，我们也按照他们的思路来一起介绍咯！！！！

我们先简单建立一个前端和后端的概念，简单理解就是前端是你能看到的，就是界面上的东西，所以你也能轻易的修改。后端就是你看不到的。所以有句话说：前端是写给人看的，后端是写给服务器看到。

## <mark style="color:yellow;background-color:green;">1）前端检测</mark>

前端检测是通过一段JavaScript代码校验文件的后缀名，有白名单也有黑名单。如果后缀名不对，就会有弹窗告诉说后缀名不对。此时文件上传的数据包并没有发送到服务端，只是在客户端浏览器使用Javascript对数据包进行检测

### <mark style="color:green;">①绕过姿势一：</mark>

因为前端是用户可以自己可以修改的，所以这个绕过姿势就可以是用户自己修改前端的代码，然后再执行代码。

<figure><img src="../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:green;">②绕过姿势二：</mark>

用户还可以用bp抓包，将上传文件的后缀修改后再发送，这个时候就已经通过了js的校验。

* 首先把需要上传的文件后缀改成允许上传的文件类型，如jpg、png、gif等，绕过Javascript检测，再抓包，把后缀名改成可执行文件的后缀即可上传成功

### <mark style="color:green;">③绕过姿势三：</mark>

既然使用js代码来校验，那么我们直接删除js代码，把JavaScript给他ban了，然后上传文件，就不会有校验了。我们这里将介绍火狐和谷歌的关闭js的方法。（虽然我直接用的插件）

火狐：

<figure><img src="../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

谷歌：

<figure><img src="../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:green;">④绕过姿势四：</mark>

可以使用畸形后缀

phtml，php4，php5，pht，php3



***

## <mark style="color:yellow;background-color:green;">2）后端检测之后缀名检测漏洞</mark>

后端检测中对文件的后缀名进行过滤。一般是黑白名单过滤，如果不符合就上传失败了。

### <mark style="color:orange;background-color:yellow;">①黑名单检测</mark>

黑名单是不希望遇到的。

#### <mark style="color:green;">0x01：姿势一：大小写绕过：</mark>

假如php被ban了，我们可以用pHP这种。

#### <mark style="color:green;">0x02：姿势二：双写绕过：</mark>

这个双写绕过的原理其实是因为后台会把敏感词替换成空格，所以假如php是黑名单的词，我们可以用pphphp来代替。

#### <mark style="color:green;">0x03：姿势三：找漏网之鱼：</mark>

有：`asp:`​ `asa`​ `cer`​ `aspx`​ `jsp:`​ `jspx`​ `jspf`​ `php:`​ `php`​ `php3`​ `php4`​ `php5`​ `phtml`​ `pht`​ `exe:`​ `exee`​

总能找到没被ban的

#### <mark style="color:green;">0x04：姿势四：利用windows命名机制：</mark>

对windows来说，不允许后缀后面带点（.)和空格（ ），所以他会自动将点和空格都删掉。所以我们可以用这个性质来绕过。比如在后缀的后面加上点和空格。

#### <mark style="color:green;">0x05：姿势五：截断上传：</mark>

因为%00表示结束符，所以会把%00后面的所有的字符都删掉。所以如果我们要上传的是flag.php，但是要求的是jpg文件，我们就可以用flag.php%00.jpg，反正后面的jpg能被删掉。

条件：

php版本小于5.3.4,PHP的magic\_quotes\_gpc为OFF状态

#### <mark style="color:green;">0x06：姿势六：利用解析漏洞：</mark>

解析漏洞有.htaccess文件解析漏洞，apache解析漏洞，IIS7.0 | IIS7.5 | Nginx的解析漏洞，IIS6.0解析漏洞，目录解析漏洞，文件解析漏洞。

首先解释一下什么叫解析漏洞：

> 文件解析漏洞主要由于网站管理员操作不当或者 Web 服务器自身的漏洞，导致一些特殊文件被 IIS、apache、nginx 或其他 Web服务器在某种情况下解释成脚本文件执行。

接下来一个一个介绍。这里直接参考狼队的文章了，因为写的很清晰明了。

\---------------------------------------------------------------------------------------------------------------

## <mark style="color:purple;">一.IIS解析漏洞</mark>

### <mark style="color:orange;background-color:yellow;">（1）目录解析漏洞</mark>

原理：（/test.asp/1.jpg)

在IIS5.x/6.0 中，在网站下建立文件夹的名字为\*.asp、_.asa、_.cer、\*.cdx 的文件夹，那么其目录内的任何扩展名的文件都会被IIS当做asp文件来解释并执行。例如创建目录 test.asp，那么 /test.asp/1.jpg 将被当做asp文件来执行。假设黑客可以控制上传文件夹路径，就可以不管上传后你的图片改不改名都能拿shell了

形式：

```url
www.xxx.com/xxx.asp/xxx.jpg
```

### <mark style="color:orange;background-color:yellow;">（2）文件名解析漏洞</mark>

原理：（test.asp;.jpg)

在IIS5.x/6.0 中， 分号后面的不被解析，也就是说 xie.asp;.jpg 会被服务器看成是xie.asp。还有IIS6.0默认的可执行文件除了asp还包含这两种 .asa .cer 。而有些网站对用户上传的文件进行校验，只是校验其后缀名。所以我们只要上传 _.asp;.jpg、_.asa;.jpg、\*.cer;.jpg 后缀的文件，就可以通过服务器校验，并且服务器会把它当成asp文件执行

形式：

```url
www.xxx.com/xxx.asp;.jpg
```

### <mark style="color:orange;background-color:yellow;">（3）畸形解析漏洞</mark>

原理：(/test.jpg/\*.php)

在 IIS7.0中，在默认Fast-CGI开启状况下，我们往图片里面写入下面的代码

```
<?php fputs(fopen('shell.php','w'),'<?php @eval($_POST[x])?>')?>
```

将文件保存成test.jpg格式，上传到服务器，假设上传路径为/upload，上传成功后，直接访问/upload/test.jpg/x.php，此时神奇的畸形解析开始发挥作用啦。test.jpg将会被服务器当成php文件执行，所以图片里面的代码就会被执行。我们会神奇的发现在 /upload 目录下创建了一个一句话木马文件 shell.php 。

形式：

```url
www.xxx.com/upload/test.jpg/x.php
```

这个漏洞和接下来介绍的Nginx漏洞是一样的。

## <mark style="color:purple;">二.Nginx解析漏洞</mark>

### <mark style="color:orange;background-color:yellow;">(1)畸形解析漏洞</mark>

原理：（test.jpg/\*.php)

在nginx<0.8.03环境中，我们新建一个文件，内容为：\<?php phpinfo() ?> ，然后将其名字修改为: test.jpg

在浏览器中访问http://192.168.10.139/test.jpg 显示图片解析错误。在浏览器中访问 http://192.168.10.139/test.jpg/test.php ，显示：Access denied. 。这就奇怪了，test.jpg是文件不是目录，test.php更是根本就不存在的文件，访问/test.jpg/test.php没有报404，而是显示 Access denied. 。这是到底为啥？

原因在于，Nginx拿到文件路径（更专业的说法是URI）/test.jpg/test.php 后，一看后缀是.php，便认为该文件是php文件，于是转交给php去处理。php一看 /test.jpg/test.php 不存在，便删去最后的/test.php，又看/test.jpg存在，便把/test.jpg当成要执行的文件了，又因为后缀为.jpg，php认为这不是php文件，于是返回 Access denied. 。

条件：

cgi.fix\_pathinfo=1，一般默认都开启的。\
形式：

```url
www.xxx.com/upload/test.jpg/test.php
```

### <mark style="color:orange;background-color:yellow;">(2)%00空字节代码解析漏洞</mark>

原理：(xxx.jpg%00.php)

在nginx0.5,0.6,0.7（<0.7.65),0.8(<0.8.37)的版本里面,Ngnix在遇到%00空字节时与后端FastCGI处理不一致，导致可以在图片中嵌入PHP代码然后通过访问xxx.jpg%00.php来执行其中的代码

形式：

```url
www.xxx.com/upload/test.jpg%00.php
```

### <mark style="color:orange;background-color:yellow;">(3)%20%00代码解析漏洞</mark>

原理：(xxx.jpg/%20\0.php)

这一漏洞的原理是非法字符空格和截止符（%00）会导致Nginx解析URI时的有限状态机混乱，危害是允许攻击者通过一个非编码空格绕过后缀名限制。

形式：

```url
www.xxxx.com/Upload/1.jpg/%20\0.php
```

## <mark style="color:purple;">三.apache解析漏洞</mark>

原理：（shell.php.qwe.asd)

`Apache`​ 解析文件的规则是`从右到左`​开始判断解析，如果`后缀名`​为`不可识别`​文件解析，就再往左判断。比如`test.php.a.b`​的“`.a`​”和“`.b`​”这两种后缀是`apache`​不可识别解析，`apache`​就会把`test.php.a.b`​解析成`test.php`​。

形式：

```
shell.php.qwe.asd
```

## <mark style="color:purple;">四..htaccess文件攻击</mark>

首先介绍一下.htaccess文件是什么吧

> htaccess文件是Apache服务器中的一个配置文件，它负责相关目录下的网页配置。通过 htaccess文件，可以实现：网页301重定向、自定义404错误页面、改变文件扩展名、允许/阻止特定的用户或者目录的访问、禁止目录列表、配置默认文档等功能IIS平台上不存在该文件，该文件默认开启，启用和关闭在 httpd.conf 文件中配置

形式：

一般来说.htaccess文件能用来留后门和针对黑名单的绕过，只要在上传网站的根目录下，上传一个.htaccess文件即可

绕过方法：

* 针对黑名单绕过：

编写一个txt文件，然后将后缀名改为.htaccess ，这个内容主要是将png文件解析为php文件

```
AddType  application/x-httpd-php    .png
```

* 留后门

在`.htaccess` 内写入`php`解析规则，这个的内容主要是把文件名包含`s`的解析成`php`文件

```
<FilesMatch "s">
SetHandler application/x-httpd-php
</FilesMatch>
```

* 利用.htaccess进行文件包含

使用#注释使得.htaccess能够成功解析

```
php_value auto_prepend_file ".htaccess"
#<?php eval($_POST[cmd]);?>
```

\---------------------------------------------------------------------------------------------------------------------

### <mark style="color:orange;background-color:yellow;">②白名单检测</mark>

白名单就是希望有的，里面会包含允许通过的。

#### <mark style="color:green;">0x01：姿势一：解析漏洞</mark>

就是上面提到的那些，不多写了。

#### <mark style="color:green;">0x02：姿势二：截断上传</mark>

就是上面提过的%00截断上传。

***

## <mark style="color:yellow;background-color:green;">3）后端检测之00截断</mark>

就是之前提到的%00截断，也不多说了。

***

## <mark style="color:yellow;background-color:green;">4）后端检测之MIME检测</mark>

首先还是解释mime type是什么

> `MIME(Multipurpose Internet Mail Extensions)`​多用途互联网邮件扩展类型。是设定某种扩展名的文件用一种应用程序来打开的方式类型，当该扩展名文件被访问的时候，浏览器会自动使用指定应用程序来打开。

也就是我们在用bp抓包时会看到content-type。

### <mark style="color:orange;background-color:yellow;">①常见的mime-type</mark>

* `text/plain`​ （纯文本）&#x20;
* `text/html`​ （HTML文档）&#x20;
* `text/javascript`​ （js代码）
* &#x20;`application/xhtml+xml`​ （XHTML文档）&#x20;
* `image/gif`​ （GIF图像）
* &#x20;`image/jpeg`​ （JPEG图像）&#x20;
* `image/png`​ （PNG图像）&#x20;
* `video/mpeg`​ （MPEG动画）
* &#x20;`application/octet-stream`​ （二进制数据）&#x20;
* `application/pdf`​ （PDF文档）

### <mark style="color:orange;background-color:yellow;">②判断方法</mark>

一般是通过源代码来判断的。

### <mark style="color:orange;background-color:yellow;">③绕过方法</mark>

bp抓包修改content-type的字段就可以了。

***

## <mark style="color:yellow;background-color:green;">5）后端检测之文件头检测绕过</mark>

在每一个文件（包括图片，视频或其他的非ASCII文件）的开头（十六进制表示）实际上都有一片区域来显示这个文件的实际用法，这就是文件头标志。我们可以通过16进制编辑器打开文件，添加服务器允许的文件头以绕过检测。

### <mark style="color:orange;background-color:yellow;">①常见的文件头</mark>

* GIF：`47 49 46 38 39 61`​                         ----`GIF89a`
* png：`89 50 4E 47 0D 0A 1A 0A`​&#x20;
* JPG：`FF D8 FF E0 00 10 4A 46 49 46`​

### <mark style="color:orange;background-color:yellow;">②利用方法：</mark>

通过利用16进制编辑器直接添加，这里推荐有notepad++还有010editor，winhex都可以。

把安装包也放在这里了，大家自取就行。使用也很简单，直接把要分析的拖进去就可以。

{% file src="../.gitbook/assets/winhex.zip" %}

***

## <mark style="color:yellow;background-color:green;">（6）后端检验之user.ini文件配置</mark>

user.ini文件配置和.htaccess文件配置很相似，但是用途更广泛。这里也是参考p神的文章，友链放在下面了，谁懂啊，这个大佬怎么总是能钻研出这么多东西/(ㄒoㄒ)/\~\~。

首先简单介绍一下什么是user.ini

> 我们知道php.ini是php的配置文件，`.user.ini`实际上就是一个可以由用户“自定义”的php.ini，实际上，除了`PHP_INI_SYSTEM`以外的模式（包括PHP\_INI\_ALL）都是可以通过.user.ini来设置的。比如`“PHP_INI_PERDIR 、 PHP_INI_USER”。`而且，和`php.ini`不同的是，`.user.ini`是一个能被动态加载的ini文件。也就是说我修改了`.user.ini`后，不需要重启服务器中间件，只需要等待`user_ini.cache_ttl`所设置的时间（默认为300秒），即可被重新加载。

* 制造后门：

php配置项中有两个选项可以用来包含后门。一个是auto\_append\_file,还有一个是auto\_append\_file。

<figure><img src="../.gitbook/assets/image (7) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (9) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

就类似于require（）的作用，直接包含一个文件。

格式就是：

```
auto_prepend_file=*****
```

```
auto_append_file=*******
```

这个文件就是我们的木马文件。所以再.user.ini上传的文件夹下的每个php文件都会添加一个include（"\*\*\*\*\*\*\*"),每个php文件都会包含木马文件。

并且这个时候包含的文件可以不是php后缀，只要含有php代码就可以了。

***







## <mark style="color:red;background-color:red;">参考门：</mark>

{% embed url="https://wiki.tql.ac/Offer/%E7%A7%8B%E6%8B%9B%E7%9F%A5%E8%AF%86%E7%82%B9/%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E5%92%8C%E6%96%87%E4%BB%B6%E8%A7%A3%E6%9E%90%E6%BC%8F%E6%B4%9E" %}

{% embed url="https://wiki.wgpsec.org/knowledge/ctf/uploadfile.html" %}

{% embed url="https://zhuanlan.zhihu.com/p/399452532" %}

{% embed url="https://wooyun.js.org/drops/user.ini%E6%96%87%E4%BB%B6%E6%9E%84%E6%88%90%E7%9A%84PHP%E5%90%8E%E9%97%A8.html" %}
