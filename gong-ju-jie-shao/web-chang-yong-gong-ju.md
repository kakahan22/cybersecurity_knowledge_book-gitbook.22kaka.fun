# 🚩 web常用工具

## <mark style="color:blue;">1.dirsearch</mark>

### <mark style="color:orange;">①作用</mark>

kali下面自带了我记得，所以我这里直接记录使用方法了。

> 用python编写的Dirsearch是一个命令行网站目录扫描程序。

我们可以用它来扫描当前目录下面的目录，备份文件，隐藏文件之类的。

### <mark style="color:orange;">②用法</mark>

常用的语句就是

```
dirsearch -u http://*************** 
```

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

当然也可以以指定我们需要的语言，比如我们需要的是php语言

```
dirsearch -u http://*********** -e php
```

如果什么语言都可以的话，我们可以将后面的 -e php改为 -e\*

<figure><img src="../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

还可以开通多个线程，比如我们可以设置5个线程对他扫描。

```
dirsearch -u http://xxxxxxxxx -t 5
```

<figure><img src="../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

此外还可以在请求中使用自定义的HTTP头，比如在每个请求中包含自定义的HTTP头，如 `X-Custom-Header` 和 `Authorization`

```
dirsearch -u http://example.com -H "X-Custom-Header: Value" -H "Authorization: Bearer token"
```

***

## （2）phpggc































