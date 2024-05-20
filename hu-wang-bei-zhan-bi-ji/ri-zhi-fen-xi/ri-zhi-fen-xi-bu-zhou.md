---
description: 日志分析需要关注的几个步骤也将在这里说一下。
---

# 🥗 日志分析步骤

## 1.字符串特征

### ①识别攻击者工具

有些常见的扫描器的字符串特征，如果在日志中发现这些字符串，可以直接确定他们的对应的攻击工具。

```
AWVS扫描器：acunetix_wvs_security_test,acunetix
Appscan扫描器:Appscan
sqlmap:User-Agent中发现sqlmap
curl：User-Agent中发现字符串curl（linux中用的多）
```

> 这里再提一下HTTP请求字段的含义！！！！！！！！！！
>
> ```
> ​Host：指定目标服务器的主机名或 IP 地址。
> 例如：Host: www.example.com
> ​User-Agent：发送请求的用户代理信息，用于描述客户端的软件应用程序。
> 例如：User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36
> ​Accept：指定客户端可以接受的响应内容类型，使用 MIME 类型。
> 例如：Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8
> ​Accept-Language：指定客户端可以接受的语言类型。
> 例如：Accept-Language: en-US,en;q=0.9
> ​Accept-Encoding：指定客户端可以接受的内容编码方式，用于压缩传输的数据。
> 例如：Accept-Encoding: gzip, deflate
> ​Connection：指定是否需要持久连接（keep-alive）。
> 例如：Connection: keep-alive
> ​Referer：指定当前请求的来源页面的 URL，用于跟踪链接来源。
> 例如：Referer: https://www.example.com/previous-page
> ​Content-Type：指定请求体的媒体类型。
> 例如：Content-Type: application/json
> ​Content-Length：指定请求体的长度（字节数）。
> 例如：Content-Length: 1024
>
> ```





***

## 2.行为特征

通过日志中的行为特征，确定攻击者可能的攻击手段

### ①漏洞扫描：

来源地址相对固定，返回结果大部分失败（参考HTTP状态码），



### ②暴力破解

来源地址相对固定，登陆页面短时间高频率发送请求，请求的url相对固定（post不会被日志记录，get请求会被日志记录。登录页面一般是post请求）



### ③webshell（大马）

如果攻击者再web服务器上发现了漏洞，并且有上传全选，就可以上传webshell，由脚本语言编写，可以在web服务器上运行。

那么：只有攻击者可以访问，来源ip地址就是攻击者的ip地址，访问时间相对集中，webshell没有内嵌页面，不会跳转其他页面。



### ④小马（一句话木马）

通常就是php哪个\<?php的代码，

所以查找搜\<?php就可以。





> HTTP状态码
>
> ```
> 1xx（信息性状态码）：表示接收到请求并且正在处理。
> 100：继续
> 101：切换协议
> 2xx（成功状态码）：表示请求已成功处理。
> 200：OK
> 201：已创建
> 204：无内容
> 3xx（重定向状态码）：表示需要采取进一步的操作才能完成请求。
> 301：永久重定向
> 302：临时重定向
> 304：未修改
> 4xx（客户端错误状态码）：表示服务器无法处理客户端的请求。
> 400：错误的请求
> 401：未授权
> 403：禁止访问
> 404：未找到
> 5xx（服务器错误状态码）：表示服务器在处理请求时遇到了问题。
> 500：服务器内部错误
> 502：错误的网关
> 503：服务不可用
> 504：网关超时
> ```





***

## 3.分析各类特征，检验，分类线索，并扩线分析。

检验线索，确保线索的准确性、可靠性

分类线索，如网站漏洞扫描、登录后台的行为、SQL注入攻击等等

扩线分析，确定被攻击影响范围、确定被利用漏洞、确定隐藏后门、确定攻击者IP

后门扩线分析：查找访问过后门的所有ip，得到攻击者的所有ip

ip扩线分析：分析攻击者的所有ip的访问路径和可疑行为，得到攻击者的所有后门&#x20;





***

## 4.常见的中间件及中间件的日志

### ①Tomcat

#### （1）目录结构：

* bin：存放命令脚本
* conf：存放配置文件
* lib：存放运行需要加载的jar包
* logs
* temp
* webapps
* work

#### （2）日志：

* 访问日志：记录访问时间，来源
* 运行日志：记录运行信息，异常信息

#### （3）配置文件：

* server.xml
* web.xml
* tomcat-user.xml

#### (4)运行日志默认路径：

```
./log文件夹下
```

* 运行日志配置文件默认路径：./conf/logging.properties，其中定义了Tomcat运行日志分类和分级
* 运行日志等级（低-高）：\[FINST | FINER | FINE | CONFIG | INFO | WARNING]
* 运行日志默认四类日志文件：
  * catelina
  * localhost
  * manager
  * host-manager
* 访问呢日志配置文件默认路径（Tomcat默认不记录访问日志，需要手动启动运行日志）：编辑./conf/server.xml文件，去掉头尾的注释，开启访问日志记录。
* 访问日志默认路径：./log
* 访问日志命名规则:localhost\_access\_log.日期.txt





### ②Weblogic

#### （1）目录结构：

* coherence
* jrockit
* logs
* modules
* user\_projects
* utiles
* wlserver

#### (2)日志：

* access.log(访问日志，记录http相关信息）
* server.log(服务器日志，记录Server运行状态，包括admin server和app server)
* domain.log(记录一个domain的运行情况）

#### （3）日志默认路径

weblogic8.x:

* access.log($MW\_HOME\user\_projects\domains \ \<domain\_name> \ \<server\_name>\access.log)
* server.log($MW\_HOME\user\_projects\domains \ \<domain\_name> \ \<server\_name>\ \<server\_name>.log)
* domain.log($MW\_HOME\user\_projects\domains \ \<domain\_name> \ \<server\_name> \ \<domain\_name>.log)

weblogic9:

* access.log($MW\_HOME\user\_projects\domains \ \<domain\_name> \ servers \ \<server\_name> \logs\access.log)
* server.log($MW\_HOME\user\_projects\domains \ \<domain\_name> \ \<server\_name>\ servers \ \<server\_name> \logs\ \<server\_name>.log)
* domain.log($MW\_HOME\user\_projects\domains \ \<domain\_name> \ servers \ \<server\_name> \logs\ \<domain\_name>.log)



### ③Nginx

#### （1）目录结构：

* conf 配置文件
* html 默认web根目录
* logs 日志

#### （2）配置文件：

* nginx.conf

#### （3）fastcgi配置文件：

* fastcgi.conf

#### （4）日志：

* access\_log(访问日志，记录客户端的请求信息）
* error\_log(错误日志，记录服务器和请求处理过程中的错误信息）

#### （5）访问日志默认路径

* ./logs/access\_log或者/var/log/nginx/access

#### （6）Nginx访问日志配置文件默认路径

* ./conf/nginx.conf

#### （7）错误日志默认路径

* ./logs/error\_log或/var/log/nginx/error\_log

#### （8）Nginx错误日志配置文件默认路径

* ./conf/nginx.conf

#### （9）Nginx错误日志级别:\[debug | info | notice | warn | error | crit | alter | emerg]





### ④Apache

#### （1）目录结构：

* bin
* build
* cgi-bin
* conf
* error
* htdocs
* icons
* include
* lib
* logs
* man
* manual
* modules

#### （2）配置文件：

* http.conf

#### （3）日志：

* access\_log
* error\_log
* ssl\_access\_log
* ssl\_error\_log
* ssl\_request\_log

#### （4）日志默认路径

* ./logs

#### （5）日志配置文件默认路径：

* Apache/conf/httd.conf



### ⑤IIS

#### （1）IIS6.0目录结构

* C:\InetPub 站点根目录
* C:\WINDOWS\Help\IISHELP 帮助文档
* C:\WINDOWS\System32\InetSrv  IIS安装文件夹的路径
* C:\WINDOWS\System32\InetSrv\MetaBack 初始配置数据库配置的备份文件

#### （2）IIS6.0站点配置文件

* C:\WINDOWS\System32\inetSrv\MetaBack.xml

#### （3）IIS6.0日志默认路径

* C:\WINDOWS\System32\LogFiles\W3CSV+标识符

#### （4）IIS7.0目录结构

* AdminScripts 存放虚拟目录的脚本文件
* custerr 存放各种语言的网站错误页面
* ftproot ftp根目录，添加ftp组件后有用
* history 存放历史配置文件
* logs 存放日志文件
* temp 存放临时文件
* wwwroot 存放IIS默认网站源码网页。

#### （5）IIS7.0站点配置文件

* C:\WINDOWS\System32\inetSrv\config\applicationHost.config

#### （6）IIS7.0日志默认路径

* C:\inerpub\logs\W3CSV+标识符



### ⑥MYSQL

























1、事件查看器 在Windows上，使用win+R输入eventvwr.msc进入事件查看器

2、常见事件ID 4624：登陆成功

4625：登录失败

4634：注销成功

4672：使用超级用户（如管理员）进行登录

4720：创建用户

3、Linux系统日志 存放在 /var/log目录

系统日志：/var/log/message

cron日志：/var/log/cron

安全日志：/var/log/secure&#x20;



















































































## 参考门：

[https://blog.csdn.net/m0\_59302403/article/details/131466352](https://blog.csdn.net/m0\_59302403/article/details/131466352)





