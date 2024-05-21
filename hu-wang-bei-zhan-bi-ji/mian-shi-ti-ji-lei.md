---
description: 这里就看一些网上能搜到的和他们发的资料的面试题，相当于真题的刷题策略吧。
---

# 🍟 面试题积累

## 1.渗透：

### （1）渗透的思路是什么：

信息搜集->漏洞挖掘->权限提升->清除数据，输出报告

#### ①信息搜集：

1.服务器信息（真实ip，系统类型，版本，开放端口，WAF）

2.网站指纹识别（包括cms，cdn，证书），dns记录

3.whois信息，姓名，备案，邮箱，电话反查

4.子域名收集，旁站，c段。

5.google hack探测网站的信息，后台，敏感文件

6.扫网站目录结构，爆后台，网站banner，测试文件，备份等敏感文件。

7.传输协议，通用的漏洞，exp，github源码。

8.查看IP，进行IP端口扫描，对对应端口的漏洞进行探测。

#### ②漏洞挖掘

1.浏览网站，查看网站规模，功能，特点

2.端口，弱口令，目录等扫描。

3.XSS,SQL注入，命令注入，CSRF,cookie安全检测，敏感信息，通信数据传输，暴力破解，任意文件上传，越权访问，未授权访问，目录遍历，文件包含，重放攻击，服务器漏洞检测，最后用扫描工具之后是漏洞利用，拿到webshell或者其他权限。

#### ③权限提升

mysql提权，serv-u提权，linux内核版本提权，提权服务器等，比如windows下面mysql的udf提权，windwos低版本漏洞，linux脏牛漏洞，linux的oracle低权限漏洞。

#### ④清楚测试数据|输出报告

1.日志测试数据读到清理

2.总结，输出报告，给出修复建议

图是网上找的，写的很清晰，可以借鉴，参考门在下面，表示感谢。

<figure><img src="../.gitbook/assets/image (32).png" alt=""><figcaption></figcaption></figure>

### （2）信息搜集的思路

上面其实已经回答了，看上面吧。



### （3）cdn绕过

















































## 参考门：

微信公众号：2024Hw蓝队初级面试押题 Zacarx

[https://forum.butian.net/question/129](https://forum.butian.net/question/129)

[https://blog.csdn.net/ka\_ka11/article/details/137559520](https://blog.csdn.net/ka\_ka11/article/details/137559520)

直接看别人总结好的所有的！！！！！！！！！！！！！

[https://y5neko.github.io/2022/10/21/%E6%8A%A4%E7%BD%91%E9%9D%A2%E8%AF%95%E9%97%AE%E9%A2%98/#%E7%AC%AC%E4%B8%83%E5%B1%82-%E5%BA%94%E7%94%A8%E5%B1%82](https://y5neko.github.io/2022/10/21/%E6%8A%A4%E7%BD%91%E9%9D%A2%E8%AF%95%E9%97%AE%E9%A2%98/#%E7%AC%AC%E4%B8%83%E5%B1%82-%E5%BA%94%E7%94%A8%E5%B1%82)

