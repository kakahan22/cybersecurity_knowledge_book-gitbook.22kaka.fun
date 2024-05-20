---
description: 有windows就有linux
---

# 🥙 linux应急响应

## 1.敏感文件夹分析

### ①temp文件分析

在linux下有一个特别的临时文件， /tmp，每个用户都可以对他进行读写操作，所以我们可以查看/tmp下面有没有一些特别的文件。

通过ls -alt三个参数来查看，t是time按照时间排序，a是all所有的，l是long长格式显示目录下的内容列表。

<figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

### ②/usr/bin，/usr/sbin文件分析

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>







***

## 2.开机自启动文件

恶意代码很可能在开机启动的位置

开机自启动项内容在/etc/init.d。我们可以去查看信息。

<figure><img src="../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

如果我们想查看某个文件更加详细的时间信息，可以使用指令

```
stat 文件
```

<figure><img src="../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

可以看到modify时间，birth时间，change时间和access时间。







***

## 3.新增文件

主要是查找24h之内被修改的文件。

指令：

```
find ./ -mtime 0 -name "*.php"
```

<figure><img src="../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

查找72小时之内新增的文件。

```
find ./ -ctime -2 -name “*.php”
```



> atime 意为access time 访问时间 -n 表示查询的是在n天之内的范围，+n表示n天之前 n表示正好第n天
>
> ctime 意为change time 状态的改变时间 -n 表示查询的是在n天之内的范围，+n表示n天之前 n表示正好第n天
>
> mtime 意为modify time 文件内容改变时间 -n 表示查询的是在n天之内的范围，+n表示n天之前 n表示正好第n天





***

## 4.权限过大文件

权限查找，如果某些文件有777权限就很可以。

```
find ./ -iname "*.php" -perm 777 # 其中的iname的i是ignore的意思，perm用于设定筛选文件权限
```

<figure><img src="../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>





***

## 5.网络连接分析

指令

```
netstat -lntp
```

<figure><img src="../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

如果哪个进程是未知的，我们使用 kill -9 pid然后关闭

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>





***

## 6.进程分析

### ①ps分析

我们可以用ps命令去分析进程，根据netstat得到pid，然后用ps命令分析进程。

查看所有进程信息

```
ps aux
```

<figure><img src="../../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

查看使用22端口的进程。

```
ps aux | grep "22"
```

<figure><img src="../../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

### ②lsof分析

我们可以用lsof查看隐藏的进程。

比如查看端口22的隐藏进程

```
lsof -i:22
```

<figure><img src="../../.gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure>





***

## 7.异常登录



在linux做的操作都会被记录到系统日志中，对于登录也可以查看日志信息查看是否有异常登录。

### ①last记录

last命令记录着所有的用户登录日志，他的结果来自于/var/log/wtmp文件，稍有经验的会删除掉，但是还是会有蛛丝马迹在此文件中的。

```
last
```

<figure><img src="../../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

查看登录日志，筛选非本地登录。

```
last -i | grep -v  0.0.0.0
```

<figure><img src="../../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>





***































## 参考门：

[https://www.anquanke.com/post/id/259764](https://www.anquanke.com/post/id/259764)

