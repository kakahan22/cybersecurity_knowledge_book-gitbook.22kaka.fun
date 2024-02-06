---
description: 这里将通过参考文章和做题一起进行总结，并且文件包含漏洞，很多都利用了文件上传漏洞，所以这里也会总结一些文件上传漏洞的知识。
---

# 🍉 FL漏洞知识点总结

## <mark style="color:blue;background-color:green;">1.include/require/include\_one/require\_one</mark>

在PHP语法篇的10.文件里面我们讲了include和require和include\_one和require\_one这些，如果大家忘记了，可以返回去看看。

{% content-ref url="../rce-yuan-cheng-dai-ma-zhi-hang/php-yu-fa.md" %}
[php-yu-fa.md](../rce-yuan-cheng-dai-ma-zhi-hang/php-yu-fa.md)
{% endcontent-ref %}

***

## <mark style="color:blue;background-color:green;">2.allow\_url\_include/allow\_url\_fopen</mark>

其实我看到老师写的书上也还在说这个，但是我看官方手册上面allow\_url\_include自php7.4就废除了，还发现就算是再新的书都有一定的滞后性，大家还是以手册为主。虽然废除了，但是我们还是讲解这两个在php.ini配置文件中的作用

### <mark style="color:purple;background-color:yellow;">1）allow\_url\_include</mark>

这个选项允许include,require,include\_one和require四个函数的使用。

{% hint style="info" %}
这个设置项需要开启 allow\_url\_fopen 。
{% endhint %}

### <mark style="color:purple;background-color:yellow;">2）allow\_url\_fopen</mark>

本选项激活了 URL 形式的 fopen 封装协议使得可以访问 URL 对象例如文件。默认的封装协议提供用 ftp 和 http 协议来访问。

***

## <mark style="color:blue;background-color:green;">3.php伪协议</mark>

我们在RCE漏洞知识点总结的5.php伪协议里面讲了php伪协议，忘记了也可以去看看

{% content-ref url="../rce-yuan-cheng-dai-ma-zhi-hang/rce-lou-dong-zhi-shi-dian-zong-jie.md" %}
[rce-lou-dong-zhi-shi-dian-zong-jie.md](../rce-yuan-cheng-dai-ma-zhi-hang/rce-lou-dong-zhi-shi-dian-zong-jie.md)
{% endcontent-ref %}

{% hint style="info" %}
这里总结一下四个主要的协议是用在哪些方面。

```php
1.php://filter              主要用于读取源码
2.php://input               经常使用file_get_contents获取php://input内容
3.data://                   执行命令
4.file://                   访问本地文件系统
```
{% endhint %}

***

在有以上的知识的基础上我们要介绍这个FL漏洞了。主要是分为本地文件包含漏洞和远程文件包含漏洞。

## <mark style="color:blue;background-color:green;">1.本地文件包含漏洞</mark>























## <mark style="color:red;background-color:orange;">参考门：</mark>

[https://www.freebuf.com/articles/web/182280.html](https://www.freebuf.com/articles/web/182280.html)

