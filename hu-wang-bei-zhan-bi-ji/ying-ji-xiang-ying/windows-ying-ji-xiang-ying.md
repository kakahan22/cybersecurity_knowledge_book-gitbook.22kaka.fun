---
description: >-
  第一个就是windows的应急响应，毕竟用win系统的人还是多数。这里是用自己的win11系统，可能有些是win10所以版本不一样，但是这里会写的是自己的win11
---

# 🍳 windows应急响应

## 1.开机自启动文件

一般被植入的木马病毒，恶意文件都会在计算机启动时自行启动。在windows下可通过以下几种方式查看开机自启动项。

### ①操作系统中的启动菜单。

```
C:\Users\cyh17\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
```



<figure><img src="../../.gitbook/assets/image (26).png" alt=""><figcaption></figcaption></figure>

### ②利用cmd的msconfig

<figure><img src="../../.gitbook/assets/image (27).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (28).png" alt=""><figcaption></figcaption></figure>

### ③利用注册表regedit

win+R->regedit打开注册表

然后找到

```
计算机\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
```

<figure><img src="../../.gitbook/assets/image (29).png" alt=""><figcaption></figcaption></figure>



<figure><img src="../../.gitbook/assets/image (30).png" alt=""><figcaption></figcaption></figure>







***

## 2.temp临时异常文件

临时文件里面也有可能有异常文件，比如临时编辑的文件，浏览的页面，很多网上的清理c盘的教程，就让我们删除temp的所有文件。

这里有两种方式查看临时异常文件。

### ①操作系统的temp文件夹

```
C:\Users\cyh17\AppData\Local\Temp
```

<figure><img src="../../.gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>



### ②运行%temp%

WIN+R->%temp%

<figure><img src="../../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

接下来我们需要注意这些临时文件的什么地方呢？

### ③排查对象：

查看temp文件夹PE文件（exe，dll，sys），或者特别大的temp文件。

可疑文件可以放到微步云沙箱去验证

[https://s.threatbook.com/](https://s.threatbook.com/)

<figure><img src="../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

比如我的目录下，暂时没找到不认识的exe或者dll文件

<figure><img src="../../.gitbook/assets/image (18).png" alt=""><figcaption></figcaption></figure>



{% hint style="info" %}
为什么要排查Temp文件夹？

使用Temp文件夹有几个优点。在某些系统中，Temp文件夹位于RAM DISK上。与通常的磁盘文件系统相比，写入操作和文件操作要快的很多。

另一个优点是Temp文件夹对当前登录的用户具有读写访问权限，从而解决了恶意软件安装程序在没有适当权限的情况下尝试将恶意软件安装在目标位置时出现的任何文件系统权限错误。一旦恶意软件安装程序或恶意软件本身具有升级的特权，Temp文件夹通常用作暂存点。

操作系统还具有清理Temp文件夹中临时文件的不完整写入的优点，因此在恶意软件安装失败的情况下，操作系统负责删除文件的任何痕迹，从而防止恶意软件的任何部分或版本损坏它的主要可执行文件。所以恶意软件安装程序通常在恶意软件感染期间利用TMP文件和Windows Temp文件夹。
{% endhint %}





***

## 3.浏览器分析

如果服务器被攻击者拿下了，攻击者可能会使用服务器的流浪其进行访问网站去下载一些东西，可以排查浏览器看是否被下载恶意代码了。

### ①浏览器浏览痕迹查看

就是历史记录，应该没有人不会看吧。

<figure><img src="../../.gitbook/assets/image (19).png" alt=""><figcaption></figcaption></figure>

### ②浏览器文件下载记录查看



<figure><img src="../../.gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure>



### ③浏览器cookie信息查看。

<figure><img src="../../.gitbook/assets/image (21).png" alt=""><figcaption></figcaption></figure>





***

### 4.文件属性时间分析

我们主要是看创建时间和修改时间。

<figure><img src="../../.gitbook/assets/image (22).png" alt=""><figcaption></figcaption></figure>

如果文件的修改时间早于创建时间，那么异常的时间很可能是攻击者进行恶意修改的不正查文件。







***

### 5.最近打开文件

也有两种方法打开。

### ①运行指令

WIN+R->%UserProfile%/Recent

<figure><img src="../../.gitbook/assets/image (23).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (24).png" alt=""><figcaption></figcaption></figure>

### ②系统文件

文件路径

```
C:\Users\cyh17\Recent
```

<figure><img src="../../.gitbook/assets/image (25).png" alt=""><figcaption></figcaption></figure>





***

## 6.可疑进程发现与关闭。

可以查看木马与外部进行通信的连接状态，然后找到对应的进程ID，然后关闭进程ID进行断开木马的通信连接。

```
netstat -ano | find "ESTABLISHED"  查看网络建立连接的状态
tasklist /svc | find "PID" 查看具体PID进程对应的程序
taskkill /PID xxx /T 关闭进程
```

<figure><img src="../../.gitbook/assets/image (84).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (85).png" alt=""><figcaption></figcaption></figure>





***

## 7.windows分析排查-系统信息排查

### ①异常计划任务排查

一般攻击设定了计划任务在固定时间内执行恶意代码，可以达到隐藏的效果，所以我们使用schtasks命令可以对计划任务进行管理，查看计算机中保存的计划任务

<figure><img src="../../.gitbook/assets/image (86).png" alt=""><figcaption></figcaption></figure>

或者我们可以从任务管理器中查看

<figure><img src="../../.gitbook/assets/image (87).png" alt=""><figcaption></figcaption></figure>

### ②隐藏账户的发现与删除

隐藏账户可能是攻击者入侵服务器后为了能长时间保持对计算机的访问，所以建立了一个隐藏账户。

我们可以通过下面的指令去查看目前的账户有哪些

```
net user
```

<figure><img src="../../.gitbook/assets/image (88).png" alt=""><figcaption></figcaption></figure>

这种是比较容易看出来的隐藏账户，有种难看出来的是在注册表里面。可能你一开始不能看到sam下面还有其他的目录，我们需要改变我们的权限。然后重新启动。

<figure><img src="../../.gitbook/assets/image (90).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (89).png" alt=""><figcaption></figcaption></figure>

然后查看下面的目录下面的结果

```
计算机\HKEY_LOCAL_MACHINE\SAM\SAM\Domains\Account\Users\Names
```

<figure><img src="../../.gitbook/assets/image (91).png" alt=""><figcaption></figcaption></figure>































## 参考门：

[https://www.anquanke.com/post/id/287417](https://www.anquanke.com/post/id/287417)































