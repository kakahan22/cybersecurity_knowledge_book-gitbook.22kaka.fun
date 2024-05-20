# 🥘 信息搜集

信息收集只通过各种方式获取所需要的信息，比如目标站点的IP，中间件，脚本语言，端口，邮箱等等。

### （1）whois信息

#### ①可以搜集whois的网站：

```
国外的whois：https://who.is
站长之家：http://whois.chinaz.com
爱站:https://whois.aizhan.com
微步:https://x.threatbook.cn
```

我们主要关注：注册商，注册人，邮件，DNS解析服务器，注册人联系电话。

我们测试测试自己的域名。这里就不测试我自己的了，我毫无隐藏的手段，emmm，一查就查到了。

#### ②企业备案信息：

```
天眼查：https://www.tianyancha.com/ 

ICP备案查询网：http://www.beianbeian.com/ 

国家企业信用信息公示系统：http://www.gsxt.gov.cn/index.html 
```

{% hint style="info" %}
注意：国外的服务器一般来说是查不到的，因为他们不需要备案，国内的基本上都可以查到。
{% endhint %}

{% hint style="warning" %}
tips：如果在站长上隐藏了信息，可以在who.is上再次查看。
{% endhint %}



### （2）子域名

子域名是在顶级域名下的域名，收集的子域名越多，我们渗透的目标就越多，渗透的成功率越大，一般找不到突破口的时候，就从子域名搜集入手。

#### ①goole语法

可以用谷歌和bing这样的搜索引擎直接搜（site:www.xxx.com)

google还支持额外的减号运算符，已排除我们对“网站:wikimedia.org -www -store"不感兴趣的子域名。

比如我们要看我的域名22kaka.fun下面的子域名。我们在谷歌搜索栏输入

```
site:22kaka.fun
```

<figure><img src="../.gitbook/assets/image (58).png" alt=""><figcaption></figcaption></figure>

#### ②有许多第三方服务聚合了大量的DNS数据集，并且通过它们来检索给定域名的子域名。

网址：

```
（1）VirusTotal：https://www.virustotal.com/
（2）DNSdumpster：https://dnsdumpster.com/ 

```

第一个主要是看url，file等含不含病毒。

用第二个来试试自己的域名

<figure><img src="../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

#### ③基于SSL证书查询

查找一个域名最简单方法是使用搜索引擎来收集计算机的CT日志，并让任何搜索引擎搜索他们。前两种比较常用。



> CT：Certifictae Transparency（证书透明度)证书透明度使用户和域名持有者识别不当或恶意签发的证书，以及识别数字证书认证机构(CA)的行为。证书透明度有助于避免在瞒过域持有者的情况下为域颁发证书。证书透明度不需要侧信道通信来验证证书。他们由在线证书协议(OCSP)或Convergence等技术完成。证书透明度不需要可信赖第三方。CT 不是要替换现有的 CA 设施，而是做为补充，使之更透明、更实时
>
> 他的原理就是：
>
> #### 为什么有些证书列有多个 DNS 名称？
>
> \
> 许多组织会选择签发可在多个网站使用的单一证书。例如，大型网站经常会为其资源使用多个子网域（如 www.google.com、mail.google.com、accounts.google.com），但会以单一证书指定所有这些子网域。

```
（1）https://crt.sh/

（2）https://censys.io/

（3）https://developers.facebook.com/tools/ct/

（4）https://google.com/transparencyreport/https/ct/
```

第一个可以看到把我所有的子域名全部都找出来了，真的牛逼

<figure><img src="../.gitbook/assets/image (49).png" alt=""><figcaption></figcaption></figure>



#### ④简单的在线子域名收集（不推荐）

```
（1）http://i.links.cn/subdomain/
（2）http://z.zcjun.com/
```

其实第二个就是通过爆破去收集，emmm，反正我的他没爆出来。

#### ⑤爆破枚举

```
（1）layer子域名挖掘机

（2）subDomainsBrute

（3）K8

（4）orangescan

（5）DNSRecon
```

这里介绍常用的subDomainsBrute。

首先要下载。包就放到这里了。



<figure><img src="../.gitbook/assets/image (50).png" alt=""><figcaption></figcaption></figure>

{% file src="../.gitbook/assets/subDomainsBrute-master.zip" %}

<figure><img src="../.gitbook/assets/image (52).png" alt=""><figcaption></figcaption></figure>



### （3）IP段的收集

其实在搜索子域名的时候，就大概知道目标网站的IP段了。

```
http://ipwhois.cnnic.net.cn/
```



### （4）开放端口检测

很多时候，网站会开启CDN加速，导致我们查询出的ip不是真实的ip，所以得先查询到真实的IP地址。

```
1）通过让服务器给你发邮件(看邮箱头源 ip )找真实ip（最可靠）。

（2）通过 zmpap 全网爆破查询真实ip（可靠）。

（3）通过查询域名历史ip，http://toolbar.netcraft.com（借鉴）。

（4）通过国外冷门的DNS的查询：nslookup xxx.com国外冷门DNS地址（借鉴）。
```

当然其实上面的没多大用，我们要扫描大量IP，这里我们使用nmap。



#### ⑥端口和漏洞对应表

1.远程管理漏洞



| 端口   | 服务         | 攻击方式            |
| ---- | ---------- | --------------- |
| 22   | SSH        | 弱口令，暴力猜测，用户名枚举  |
| 23   | Telnet     | 弱口令，明文传输（用嗅探抓取） |
| 3389 | RDP        | 暴力破解            |
| 5632 | Pcanywhere | 弱口令             |
| 5900 | VNC        | 弱口令、暴力破解        |



2.web中间件/服务端口

| 端口        | 服务        | 攻击方式                                                                                                                                                                                                                                                                                                           |
| --------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1090/1099 | RMI       | 安全漏洞：JAVA RMI反序列话远程命令执行漏洞              检测工具：attackRMI.jar                                                                                                                                                                                                                                                      |
| 7001      | Weblogic  | <p>安全漏洞：弱口令、SSRF、反序列化漏洞 </p><p>利用方式：</p><p> 1、控制台弱口令上传war木马 </p><p>2、SSRF内网探测</p><p> 3、反序列化远程代码执行等</p>                                                                                                                                                                                                         |
| 8000      | jdwp      | 安全漏洞：JDWP 远程命令检测工具：https://github.com/IOActive/jdwp-shellifier                                                                                                                                                                                                                                                 |
| 8080      | Tomcat    | <p>安全漏洞：弱口令、示例目录 </p><p>利用方式：通过弱口令登录控制台，上传war包。</p>                                                                                                                                                                                                                                                            |
| 8080      | Jboss     | <p>安全漏洞：未授权访问、反序列化。</p><p> 利用方式： </p><p>1、未授权访问控制台，远程部署木马 </p><p>2、反序列化导致远程命令执行等。 </p><p>检测工具：https://github.com/joaomatosf/jexboss</p>                                                                                                                                                                        |
| 8080      | Resin     | <p>安全漏洞：目录遍历、远程文件读取 </p><p>利用方式：通过目录遍历/远程文件读取获取敏感信息，为进一步攻击提供必要的信息。</p><p>任意文件读取POC： payload1 = "/resin-doc/resource/tutorial/jndi-appconfig/test?inputFile=/etc/passwd" payload2 = "/resin-doc/examples/jndi-appconfig/test?inputFile=../../../../../../../../../../etc/passwd" payload3 = "/ ..\\web-inf"</p> |
| 8080      | Jetty     | <p>安全漏洞：远程共享缓冲区泄漏 </p><p>利用方式：攻击者可以通过精心构造headers值来触发异常并偏移到共享缓冲区，其中包含了之前其他用户提交的请求，服务器会根据攻击者的payload返回特定位置的数据。 </p><p>检测工具：https://github.com/GDSSecurity/Jetleak-Testing-Script</p>                                                                                                                             |
| 8080      | GlassFish | <p>安全漏洞：弱口令、任意文件读取 </p><p>利用方式： 1、弱口令admin/admin，直接部署shell </p><p>2、任意文件读取获取服务器敏感配置信息</p>                                                                                                                                                                                                                      |
| 8161      | ActiveMQ  | <p>安全漏洞：弱口令、任意文件写入、反序列化 </p><p>利用方式：默认密码admin/admin登陆控制台、写入webshell、上传ssh key等方式。</p>                                                                                                                                                                                                                          |
| 9043      | webSphere | <p>安全漏洞：控制台弱口令、远程代码执行 </p><p>后台地址：https://:9043/ibm/console/logon.jsp</p>                                                                                                                                                                                                                                      |
| 50000     | SAP       | <p>安全漏洞：远程代码执行</p><p> 利用方式：攻击者通过构造url请求，实现远程代码执行。 POC:http://:50000/ctc/servlet/com.sap.ctc.util.ConfigServlet?param=com.sap.ctc.util.FileSystemConfig;EXECUTE_CMD;CMDLINE=cmd.exe /c ipconfig /all</p>                                                                                                        |
| 50070     | hadoop    | <p>安全漏洞：未授权访问 </p><p>利用方式：攻击者可以通过命令行操作多个目录下的数据，如进行删除操作。</p><p> curl -i -X DELETE “http://ip:50070/webhdfs/v1/tmp?op=DELETE&#x26;recursive=true“ curl -i -X PUT “http://ip:50070/webhdfs/v1/NODATA4U_SECUREYOURSHIT?op=MKDIRS“</p>                                                                              |



3.数据库端口



| 端口    | 服务            | 攻击方式                                                                                                                                                                                                                  |
| ----- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 389   | ldap          | <p>安全漏洞：未授权访问 、弱口令 </p><p>利用方式：通过LdapBrowser工具直接连入。</p>                                                                                                                                                               |
| 1433  | Mssql         | <p>安全漏洞：弱口令、暴力破解 </p><p>利用方式：差异备份getshell、SA账户提权等</p>                                                                                                                                                                 |
| 1521  | Oracle        | <p>安全漏洞：弱口令、暴力破解 </p><p>利用方式：通过弱口令/暴力破解进行入侵。</p>                                                                                                                                                                      |
| 3306  | MySQL         | <p>安全漏洞：弱口令、暴力破解 </p><p>利用方式：利用日志写入webshell、udf提权、mof提权等。</p>                                                                                                                                                         |
| 5432  | PostgreSQL    | <p>安全漏洞：弱口令、高权限命令执行 </p><p>利用方式：攻击者通过弱口令获取账号信息，连入postgres中，可执行系统命令。 </p><p>PoC参考： DROP TABLE IF EXISTS cmd_exec; CREATE TABLE cmd_exec(cmd_output text); COPY cmd_exec FROM PROGRAM 'id'; SELECT * FROM cmd_exec;</p> |
| 5984  | CouchDB       | <p>安全漏洞：垂直权限绕过、任意命令执行 </p><p>利用方式：通过构造数据创建管理员用户，使用管理员用户登录，构造恶意请求触发任意命令执行。 后台访问：http://:5984/_utils</p>                                                                                                                |
| 6379  | Redis         | <p>安全漏洞：未授权访问 </p><p>利用方式：绝对路径写webshell 、利用计划任务执行命令反弹shell、 公私钥认证获取root权限、主从复制RCE等。</p>                                                                                                                               |
| 9200  | elasticsearch | 安全漏洞：未授权访问、命令执行 检测方式： 1、直接访问如下url，获取相关敏感信息。   http://:9200/\_nodes   查看节点数据   http://:9200/\_river  查看数据库敏感信息 2、通过构造特定的数据包，执行任意命令。                                                                                    |
| 11211 | MemCache      | <p>安全漏洞：未授权访问 </p><p>检测方式：无需用户名密码，可以直接连接memcache 服务的11211端口。 nc -vv 11211</p>                                                                                                                                         |
| 27017 | Mongdb        | <p>安全漏洞：未授权访问、弱口令 </p><p>利用方式：未授权访问/弱口令，远程连入数据库，导致敏感信息泄露。</p>                                                                                                                                                         |



4.常见协议端口



| 端口   | 服务        | 攻击方式                                                                                                                                                                                                                                                                           |
| ---- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 21   | FTP       | <p>安全漏洞：1、配置不当    2、明文传输    3、第三方软件提权 </p><p>利用方式： </p><p>1、匿名登录或弱口令 </p><p>2、嗅探ftp用户名和密码 3、Serv-U权限较大的账号可导致系统命令执行。 FTP提权命令： # 增加系统用户 Quote site exec net user 4567 4567 /add</p><p>提升到管理员权限</p><p>Quote site exec net localgroup administrators 4567 /add</p>                 |
| 25   | SMTP      | <p>攻击方式：1、匿名发送邮件 2、弱口令 3、SMTP用户枚举 </p><p>利用方式： </p><p>1、SMTP服务器配置不当，攻击者可以使用任意用户发送邮件。</p><p> 2、SMTP弱口令扫描，获取用户账号密码，发送邮件钓鱼。</p><p> 3、通过SMTP用户枚举获取用户名： nmap -p 25 -- smtp-enum-users.nse</p>                                                                                       |
| 53   | DNS       | <p>安全攻击：1、DNS域传送漏洞、DNS欺骗、DNS缓存投毒 </p><p>检测方式：</p><p> 1、DNS域传送漏洞，Windows下检测使用nslookup命令，Linux下检测使用dig命令，通过执行命令可以清楚的看到域名解析情况。</p><p> 2、DNS欺骗就是攻击者冒充域名服务器的一种欺骗行为。</p><p> 3、DNS缓存投毒是攻击者欺骗DNS服务器相信伪造的DNS响应的真实性。</p>                                                                 |
| 161  | SNMP      | <p>安全漏洞：默认团体名/弱口令访问 </p><p>利用方式：通过nmap自带的审计脚本进行检测，可能导致敏感信息泄露。</p><p>1、弱口令检测：nmap –sU –p161 –script=snmp-brute 2、获取系统信息：nmap –sU –p161 –script=snmp-sysdescr</p><p> 3、获取用户信息：nmap -sU -p161 --script=snmp-win32-user </p><p>4、获取网络端口状态：nmap -sU -p161 --script=snmp-netstat</p> |
| 443  | SSL       | <p>安全漏洞：OpenSSL 心脏出血 </p><p>利用方式：攻击者可以远程读取存在漏洞版本的openssl服务器内存中长大64K的数据。 </p><p>扫描脚本：nmap -sV --script=ssl-heartbleed</p>                                                                                                                                                       |
| 445  | SMB       | <p>安全漏洞：信息泄露、远程代码执行 </p><p>利用方式：可利用共享获取敏感信息、缓冲区溢出导致远程代码执行，如ms17010。</p>                                                                                                                                                                                                        |
| 873  | Rsync     | <p>安全漏洞：匿名访问、弱口令 </p><p>利用方式：攻击者可以执行下载/上传等操作，也可以尝试上传webshell。 </p><p>1、下载：#rsync -avz a.b.c.d::path/file path/filiname<br>2、上传：#rsync -avz path/filename a.b.c.d::path/file</p>                                                                                                |
| 2181 | Zookeeper | <p>安全漏洞：未授权访问 </p><p>检测方式：攻击者可通过执行envi命令获得系统大量的敏感信息，包括系统名称、Java环境。 </p><p>echo envi | nc ip port</p>                                                                                                                                                                           |
| 2375 | Docker    | <p>安全漏洞：未授权方式 </p><p>检测方式：通过docker daemon api 执行docker命令。 #列出容器信息，效果与docker ps -a 一致。</p><p>curl http://:2375/containers/json   </p><p>docker -H tcp://:2375 start &#x3C;Container Id></p>                                                                                     |



### （5）网站构架探测

网站构架有：操作系统，中间件，脚本语言，数据库，服务器，web容器等等

<pre><code>（1）wappalyzer插件——火狐插件

（2）云悉：http://www.yunsee.cn/info.html

（3）查看数据包响应头

（4）CMS指纹识别：http://whatweb.bugscaner.com/look/ 
<strong>                御剑指纹识别、
</strong>                Webrobot工具、
                whatweb工具、
                还有在线查询的网站等等。
</code></pre>

<figure><img src="../.gitbook/assets/image (46).png" alt=""><figcaption></figcaption></figure>





### （6）敏感文件，敏感目录探测

我们常说的敏感的文件，敏感目录有以下几种

<pre><code><strong>（1）Git
</strong>
（2）hg/Mercurial

（3）svn/Subversion

（4）bzr/Bazaar

（5）Cvs

（6）WEB-INF泄露

（7）备份文件泄露、配置文件泄露
</code></pre>

对于敏感文件我们是靠工具，脚本来找，一般有

```
（1）御剑

（2）爬虫（AWVS、Burpsuite等）

（3）搜索引擎（Google、Github等）

（4）wwwscan

（5）BBscan（一位巨佬写的python脚本：https://github.com/lijiejie/BBScan ）

（6）GSIL（也是一位巨佬写的python脚本：https://github.com/FeeiCN/GSIL ）
```

我们用御剑去尝试一下百度

<figure><img src="../.gitbook/assets/image (59).png" alt=""><figcaption></figcaption></figure>



### （7）目标域名邮箱收集

一定要养成收集站点邮箱账号收集的习惯（因为好多官方后台都是用内部邮箱账号登陆的，指不定哪天你就装库登录进去了）

<pre><code><strong>（1）通过说明文档以及网站页面收集，或者网站发表者以及留言板信息处收集账号
</strong>
（2）通过 teemo，metago，burpusit，awvs，netspker 或者 google 语法收集

（3）搜索相关 QQ 群收集相关企业员工的社交账号
</code></pre>



### （8）WAF探测

waf就是web应用防火墙，waf是可以被绕过的，emmmm，之前微专业上课的时候就有waf绕过，但是我没有听懂，因为好难/(ㄒoㄒ)/\~\~，回旋镖这下飞自己身上了。

```
（1）手工（提交恶意数据，简单粗暴）

（2）Kaili工具（WAFW00F）
```

这里试验一下WAFW00F和Nmap这两个工具。在渗透工具那个地方仔细介绍工具。



### （9）旁站，C段

**旁站**：是和目标网站在同一台服务器上的其它的网站。

**C端**：是和目标服务器ip处在同一个C段的其它服务器。

```
（1）利用Bing.com，语法为：http://cn.bing.com/search?q=ip:111.111.111.111 

（2）站长之家：http://s.tool.chinaz.com/same 

（3）利用Google，语法：site:125.125.125.*

（4）利用Nmap，语法：nmap  -p  80,8080  --open  ip/24

（5）K8工具、御剑、北极熊扫描器等

（6）在线：http://www.webscan.cc/ 
```

<figure><img src="../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>



### （10）搜索引擎

```
ZoomEy：https://www.zoomeye.org/ 

FoFa：https://fofa.so/ 
```

这里详细介绍一下fofa的语法。

### （11）fofa

fofa的语法分为：检索字段以及运算符，所有的查询语句都是由这两种元素组成的。

目前支持的检索字段包括：

支持的逻辑运算符：

```
= ：匹配，=""时，可查询不存在字段或者值为空的情况。
==：完全匹配，==""时，可查询存在且值为空的情况。
!= ：不匹配，!=""时，可查询值不为空的情况
&&：与
||：或
*=：模糊匹配，使用*或者?进行搜索，比如banner*="mys??" (个人版及以上可用)。
```

具体的语法在页面会有的。我们这里演示几个

<figure><img src="../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>



















