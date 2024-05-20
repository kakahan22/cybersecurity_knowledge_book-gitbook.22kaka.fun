# 🍪 渗透工具使用

## 1.nmap

这里是利用的kali自带的，就不单独下载了。

### ①端口扫描

#### （1）基本

```
namap IP地址（默认扫描1000）个端口
```

<figure><img src="../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>

可以看到这里就有22这个端口打开了。



#### （2）指定端口

可以用-p参数，可以一次扫描单个端口，多个端口，或扫描一个范围的端口

```
namp IP地址 -p 80
nmap IP地址 -p 1-80
nmap IP地址 -p 80，3389，22，21
nmap IP地址 -p 1-65535
namp IP地址 -p- # -p-等价于-p 1-65535
```

<figure><img src="../.gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (55).png" alt=""><figcaption></figcaption></figure>

可以看到是其实我们指定端口查询会能查到服务和开关状态，但是如果直接用范围的，就只能找到开放的服务。



#### （3）指定扫描方式

这里利用kali中的wireshark抓包分析不同扫描方式的请求信息，从而判断区别。

用它去抓包

<figure><img src="../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

#### 3.1.TCP全连接扫描

```
namp IP地址 -p 80 -sT
```

全连接扫描：通过使用完整的三次握手建立连接，能够建立就判定端口开放，否则判定端口关闭。

开放：

此时STATE是open的

<figure><img src="../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>



关闭：

当关闭的时候只有一次握手。STATE字段为closed

<figure><img src="../.gitbook/assets/image (38).png" alt=""><figcaption></figcaption></figure>



#### 3.2SYN半链接扫描

```
namp IP地址 -p 80 -sS
```

半链接扫描：只进行两次握手，双方返回确定帧（ACK=1）就判定端口开放，否则判定端口关闭

开放：

<figure><img src="../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

关闭：

<figure><img src="../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>



#### 3.3隐秘扫描

隐秘扫描，只适用于linux系统

隐秘扫描：向目标主机的端口发送TCP FIN句或Xmas tree包 或Null包，如果收到RST响应包，就判定端口关闭，否则就判定端口开放或屏蔽（open/filtered）

```
nmap 127.0.0.1 -p 80 -sF  # Fin扫描
nmap 127.0.0.1 -p 80 -sN  # Null扫描（所有flags都为0的TCP包）
nmap 127.0.0.1 -p 80 -sX  # Xmas扫描（flags的FIN、URG、PUSH都为1的包）
```





### ②.主机探测

扫描网段中有哪些主机在线，使用-sP参数，不扫描端口，只扫描存活主机

本质上是ping，能ping通就有回包，就判定主机在线。

```
namp -sP IP网段
```

<figure><img src="../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

（学校的你永远想不到有多忙碌）emmmm，我都不敢去扫别人，好害怕。





### ③.服务识别

扫描端口时，默认显示端口对应的服务，但不显示服务版本，如果想显示版本，可以用-sV服务，但是好像要开启才能显示version

```
nmap IP地址 -p 80 -sV
```

<figure><img src="../.gitbook/assets/image (44).png" alt=""><figcaption></figcaption></figure>





### ④.系统识别

想要识别操作系统版本，可以使用-o参数

```
nmap IP地址 -p 22 -o
```

<figure><img src="../.gitbook/assets/image (45).png" alt=""><figcaption></figcaption></figure>



{% hint style="info" %}
1. Nmap扫描出的系统版本并完全准确，仅供参考。
2. 当识别不出具体版本时，Nmap会以概率的形式列举出可能的操作系统，如上图所示。
{% endhint %}





***

## 2.御剑

安装包在这里上传一下

{% file src="../.gitbook/assets/御剑后台扫描珍藏版.zip" %}

直接把我们需要检测域名输入进去，就会显示下面的后台文件。也可以自己修改线程会快一点。

<figure><img src="../.gitbook/assets/image (37).png" alt=""><figcaption></figcaption></figure>









***

## 3.WAFW00F

kali上自带了waf检测工具。

<figure><img src="../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure>

原理：发送正常的HTTP请求并分析响应，这确定了许多WAF解决方案，如果不成功，就发送多个（可能是恶意的）HTTP请求，并使用简单逻辑来取代它时其中WAF，都说了是简单，害额。。。



### （1）支持检测的WAF类型

```
wafw00f -l
```

<figure><img src="../.gitbook/assets/image (61).png" alt=""><figcaption></figcaption></figure>

还是挺多的



### (2)检测单个URL（IP）

```
wafw00f ip（或网址）
```

<figure><img src="../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

从这里可以看到他用的服务器时BWS1.1，但是它返回的服务器服务时Apache，所以他应该是秀嘎了响应包头的返回。



### （3）测试多个

```
wafw00f ip1 ip2 ip3 ........
```

<figure><img src="../.gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

这个就显示两个都是Cloudflare的WAF





### （4）匹配所有签名特征的WAFS

```
wafw00f ip1 -a
```

<figure><img src="../.gitbook/assets/image (64).png" alt=""><figcaption></figcaption></figure>









***

## 4.hydra

具体参数：

```
-l 指定用户名
-p 指定密码
-L 指定用户名字典
-P 指定密码字典
-C 指定所用格式为“user:password”的字典文件
-e
n null，表示尝试空密码
s same，把用户名本身当做密码进行尝试
r 反向，把用户名倒叙，当做密码进行尝试。
-vV 显示执行细节
-o 保存执行结果
-s 指定非默认端口
-M 指定破解的目标文件，如果不是默认端口，后面跟上“:port”
-t 指定爆破时的任务数量（默认16）
————————————————

                            版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。
                        
原文链接：https://blog.csdn.net/wangyuxiang946/article/details/128194559
```



### ①爆破ssh协议

```
hydra -l root -p 1234567 IP地址 协议
hydra -l root -p 1234567 协议://IP地址
```

<figure><img src="../.gitbook/assets/image (72).png" alt=""><figcaption></figcaption></figure>



### ②字典爆破

大写

```
hydra -l root -P 密码字典 IP字典 协议
```

<figure><img src="../.gitbook/assets/image (73).png" alt=""><figcaption></figcaption></figure>

如果想看具体细节，可以加-vV参数在最后。



### ③远程桌面爆破（RDP）爆破：



```
hydra -l administrator -P 密码字典 192.168.31.173 rdp

```



### ④共享文件（SMB)爆破

```
hydra -l administrator -P 密码字典 192.168.31.173 smb

```



### ⑤文件传输（FTP）：



```
hydra -l 用户名 -P 密码字典 192.168.31.173 ftp	

```

### ⑥协议邮箱（POP3）



```
hydra -l 用户名 -P 密码字典 192.168.31.173 pop3

```

### ⑦MSSQL数据库

```
hydra -l sa -P 密码字典 192.168.31.173 mssql

```



### ⑧MYSQL数据库

```
hydra -l 用户名 -P 密码字典 192.168.31.173 mysql

```



### ⑨Oracle

```
hydra -l 用户名 -P 密码字典 192.168.31.173 oracle
```



### ⑩Redis数据库



```
hydra -l 用户名 -P 密码字典 192.168.31.173 redis

```



### 1①PgSQL数据库

```
hydra -l 用户名 -P 密码字典 192.168.31.173 postgresql

```







***



























## 参考门：

{% embed url="https://zhuanlan.zhihu.com/p/585377081" %}













