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

#### 1.漏洞介绍

CRLF是“回车+换行”(\r\n)的简称。

HTTP Header与HTTP Body是用两个CRLF分割的，浏览器根据两个CRLF来取出HTTP内容并显示出来。

通过控制HTTP消息头的字符，注入一些恶意的换行，就能注入一些会话cookie或者html代码，由于Nginx配置不正确，导致注入的代码会被执行。

#### 2.漏洞修复

Nginx的配置文件/etc/nginx/conf.d/error1.conf修改为使用不解码的url跳转

### ⑤目录穿越

#### 1.漏洞介绍

Nginx反向代理，静态文件存储在/home/下，而访问时需要在url输入files，配置文件中/files没有用/闭合，导致可以穿越至上层目录。

#### 2.漏洞修复

Nginx的配置文件/etc/nginx/conf.d/error2.conf的/files/使用闭合



## （四）Tomcat

### ①Tomecat介绍

Tomcat 服务器是一个免费的开放源代码的Web 应用服务器，属于轻量级应用 服务器，在中小型系统和并发访问用户不是很多的场合下被普遍使用，是开发和调试JSP 程序的首选。对于一个初学者来说，可以这样认为，当在一台机器上配置好Apache 服务器，可利用它响应 HTML （ 标准通用标记语言下的一个应用）页面的访问请求。实际上Tomcat是Apache 服务器的扩展，但运行时它是独立运行的，所以当运行tomcat 时，它实际上作为一个与Apache 独立的进程单独运行的。

### ②远程代码执行漏洞

#### 1.漏洞介绍

Tomcat运行在Windows主机上，且启用了，HTTP PUT请求方法，可通过构造的攻击请求向服务器上传包含任意代码的JSP文件，造成任意代码执行

#### 2.漏洞修复

1）检查当前版本是否在影响范围内，并禁用PUT方法。

2）更新至最新版

### ③war后门文件部署

#### 1.漏洞介绍

Tomcat支持在后台部署war文件，可以直接将webshell部署到web目录下。

若后台管理页面存在弱口令，则可以通过爆破获得密码

#### 2.漏洞复现

1）在系统上以低权限运行Tomcat应用程序。创建一个专门的Tomcat服务用户，该用户只能拥有一组最小权限（例如不允许远程登录）

2）增加对于本地和基于证书的身份验证，部署账户所i的那个机制（对于集中式认证，目录服务也要做相应配置）

3）后台避免弱口令

4）针对manager-gui/manager-status/manager-script等目录页面设置最小权限访问限制

## （五）jBoss

### ①jboss介绍：

jBoss是一个基于J2EE的开发源代码的应用服务器。 JBoss代码遵循LGPL许可，可以在任何商业应用中免费使用。JBoss是一个管理EJB的容器和服务器，支持EJB1.1、EJB 2.0和EJB3的规范。但JBoss核心服务不包括支持servlet/JSP的WEB容器，一般与Tomcat或Jetty绑定使用。

### ②反序列化漏洞

#### 1.漏洞介绍

java序列化就是把java对象转化为字节序列。而反序列化就是把字节序列恢复为java对象的过程，然后就在一转一变的过程中，程序员的过滤不严格，就可以导致恶意构造的代码的实现。

#### 2.漏洞修复

1）升级JBOSS AS7版本

2）不需要http-invoker.sar组件的用户可以直接删除此组件

3）用于对httpinvoker组件进行访问控制。

### ③war后门文件部署

#### 1.漏洞介绍：

jBoss后台管理页面存在弱口令，通过爆破获得账号密码。登陆后台上传包含后门的war包



## （六）Weblogic

### ①weblogic介绍

WebLogic是美国Oracle公司出品的一个applicationserver，确切的说是一个基于JAVAEE架构的中间件，WebLogic是用于开发、集成、部署和管理大型分布式Web应用、网络应用和数据库应用的Java应用服务器。将Java的动态功能和Java Enterprise标准的安全性引入大型网络应用的开发、集成、部署和管理之中。

### ②反序列化漏洞

抓包改包

### ③SSRF

#### 1.漏洞介绍： weblogic中存在一个SSRF漏洞，利用该漏洞可以发送任意HTTP请求，进而攻击内网组件中脆弱组件。

#### 2.漏洞修复：

1）删除SearchPublicRegistries.jsp

2）删除uddiexplorer文件夹，限制应用内网访问





## （七）FASTCGI











## （八）PHPCGI















































## 参考门：

[https://m.freebuf.com/articles/web/192063.html](https://m.freebuf.com/articles/web/192063.html)













