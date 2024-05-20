# 🥘 中间件漏洞

## （一)IIS

### ①IIS介绍：

IIS是Internet Information Services的缩写，意为互联网信息服务，是由微软公司提供的基于运行Microsoft Windows的互联网基本服务。最初是Windows NT版本的可选包，随后内置在Windows 2000、Windows XP Professional和Windows Server 2003一起发行，但在Windows XP Home版本上并没有IIS。IIS是一种Web（网页）服务组件，其中包括Web服务器、FTP服务器、NNTP服务器和SMTP服务器，分别用于网页浏览、文件传输、新闻服务和邮件发送等方面，它使得在网络（包括互联网和局域网）上发布信息成了一件很容易的事。

### ②PUT漏洞

#### 1.漏洞介绍及成因： 

IIS server在web服务扩展中开启了WebDAV，配置了可以写入的权限，造成任意文件上传

版本: IIS6.0

#### 2.修复建议：

关闭WebDAV和写权限

### ③短文件名猜解

#### 1.漏洞介绍及成因

IIS的短文件名机制，可以暴力猜解短文件名，访问构造的某个存在的短文件名，会返回4.4，访问不存在的访问400.

#### 2.修复建议

1）升级.net framework

2）修改注册表禁用短文件名功能

WIN+R->regedit->HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem,将其中的NtfsDisable8dot3NameCreation这一项设置为1，1代表不创建短文件名格式，修改完成后，需要重启系统生效。

3）CMD关闭NTFS8.3文件格式的支持。

### ④远程代码执行

#### 1：漏洞成因：

在IIS6.0处理PROPFIND指令的时候，由于对URL长度没有进行有效的长度控制和检查，导致执行memcpy对虚拟路径进行构造的时候，引发栈溢出，从而导致代码执行。

2.漏洞修复：

1）关闭WebDAV服务，

2）使用相关防护设备

### ⑤解析漏洞

#### 1.漏洞介绍及成因：

IIS 6.0在处理含有特殊符号的文件路径时出现逻辑错误，从而造成文件解析漏洞

#### 2.利用方式：

```
/test.asp/test.jpg

test.asp;.jpg
```

#### 3.漏洞修复

1）对新建目录名进行过滤，不允许新建包含'.'文件

2）曲线网站后台新建目录功能，不允许新建目录。

3）限制上传的脚本执行权限，不允许执行脚本

4）过滤.asp/xm.jpg，通过ISApi组件过滤



## （二）Apache

### ①Apache介绍：

Apache 是世界使用排名第一的Web 服务器软件。它可以运行在几乎所有广泛使用的 计算机平台上，由于其 跨平台 和安全性被广泛使用，是最流行的Web服务器端软件之一。它快速、可靠并且可通过简单的API扩充，将 Perl/ Python等 解释器编译到服务器中。

### ② 解析漏洞

#### 1.漏洞成因

Apache文件解析漏洞与用户的配置有密切关系，严格来说属于用户配置问题

ApacheW文件解析漏洞涉及到一个解析文件的特性：

Apache默认一个文件可以有多个以点分隔的后缀，当后边的后缀无法识别（不在mime.tyoes内），则继续向左识别，当我们请求这样一个文件：shell.xxx.yyy

```
yyy->无法识别，向左
xxx->无法识别，向左
```

#### 2.漏洞修复：

将AddHandler application/x-httpd-php.php的配置文件删除。

### ③目录遍历

#### 1.漏洞成因

由于配置错误导致目录遍历

#### 2.漏洞修复

修改apache配置文件，httpd.conf

找到Options+Indexes+FollowSymLinks+ExecCGI并修改成Options-Indexes+FollowSymLinks+ExecCGI



## （三）Nginx

### ①Nginx介绍

Nginx 是一款 轻量级的 Web 服务器、 反向代理 服务器及 电子邮件（IMAP/POP3）代理服务器，并在一个BSD-like 协议下发行。其特点是占有内存少， 并发能力强，事实上nginx的并发能力确实在同类型的网页服务器中表现较好

### ②文件解析

#### 1.漏洞介绍：

对任意文件名，在后面添加/任意文件名.php的解析漏洞，比如原本文件名时test.jpg，可以添加test.jpg/x.php进行解析攻击

#### 2.漏洞复现

1）将php.ini文件中的cgi.fix\_pathinfo的值设置为0.这样php在解析1.php/1.jpg这样的目录时，只要1.jpg不存在就会显示404

2）将/etc/php5/fpm/pool.d/www/conf中security.limit\_ectensions后面的值设置.php



### ③目录遍历

#### 1.漏洞简介及成因：

Nginx目录遍历和Apache一样，都是配置方面的问题，错误的配置可导致目录遍历与源码泄露。

#### 2.漏洞修复：

将/etc/nginx/sites-avaliable/default里的autoindex on改为autoindex off。



### ④CRLF注入





## （四）Tomcat











## （五）jBoss









## （六）Weblogic











## （七）FASTCGI











## （八）PHPCGI















































## 参考门：

[https://m.freebuf.com/articles/web/192063.html](https://m.freebuf.com/articles/web/192063.html)













