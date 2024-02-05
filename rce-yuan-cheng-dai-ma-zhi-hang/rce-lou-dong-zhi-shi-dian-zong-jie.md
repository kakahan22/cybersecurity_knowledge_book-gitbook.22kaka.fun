---
description: 这里是CTF做题时常见的会遇见的RCE的漏洞知识点总结
---

# 😅 RCE漏洞知识点总结

## <mark style="color:blue;background-color:purple;">1.PHP常见的命令执行函数</mark>

### <mark style="color:green;background-color:blue;">1)system()</mark>

执行外部程序，<mark style="background-color:orange;">**并且返回命令输出的最后一行输出**</mark>

> `system(string [command],int [result_code]=null):string | status`

### <mark style="color:green;background-color:blue;">2）exec()</mark>

执行外部程序，但是<mark style="background-color:orange;">**输出执行结果的最后一行内容**</mark>

> `exec(string[command],array[output]=null,int[result_code]=null):string|status`

### <mark style="color:green;background-color:blue;">3）passthru()</mark>

执行外部程序，并且<mark style="background-color:orange;">**显示原始输出**</mark>

> `passthru(string[command],int[result_code]=null):null?false`

### <mark style="color:green;background-color:blue;">4)eval()</mark>

把字符串作为php代码执行，<mark style="background-color:orange;">**无回显**</mark>

> `eval(string[command]:mixed`

注意，eval不能包含打开/关闭的php tags，就是不能包含完整的，但是可以用？>xxxxxx\<?php这种。除此之外，传入的必须是有效的php代码，要以**分号**结尾。

### <mark style="color:green;background-color:blue;">5）shell\_exec()</mark>

通过shell执行命令，<mark style="background-color:orange;">**并将完整的输出以字符串的方式返回**</mark>

> `shell_exec(string[command])。`

### <mark style="color:green;background-color:blue;">6）执行运算符</mark>

反引号在php中等同于`shell_exec()`，将反引号中的内容作为shell命令来执行，并且输出信息返回。如果要看到输出的信息，需要用echo或者print来包裹他。

> `` `command` ``

### <mark style="color:green;background-color:blue;">7）escapeshellarg()</mark>

转义字符串以用作shell参数。在字符串周围添加单引号，并且转义现有的单引号（自动转义），连续的反斜杠还有会额外的反斜杠转义。返回<mark style="background-color:orange;">**转义的字符串，主要用来转义shell函数的参数**</mark>

> `escapeshellarg(string [arg]):string`

### <mark style="color:green;background-color:blue;">8)escapeshellcmd（）</mark>

就是加了个转义符和上面一样都只有转义的功能

> `escapeshellcmd(string[command]):string`

以下字符前面有一个反斜杠： `&#;|*?~<>^()[]{}$\·\x0A 和\xFF`。



{% hint style="info" %}
7和8一般是和system等这种能执行外部命令的函数一起使用。他们没有执行功能
{% endhint %}

***

## <mark style="color:blue;background-color:purple;">2.linux连接符</mark>

### <mark style="color:green;background-color:blue;">1）</mark><mark style="color:green;background-color:blue;">`&`</mark><mark style="color:green;background-color:blue;">和号操作符</mark>

`&`操作符是使命令在后台运行

> 在后台运行：就是如果我们放在前台运行，那么我们将该终端端口关掉，这个进程也会结束。如果我们放在后台运行，任务不会终止。

比如我们平常执行ping的时候

但是当我们执行下面的语句的时候

```sh
ping baidu.com &
```

<figure><img src="../.gitbook/assets/image 1 (1).png" alt=""><figcaption></figcaption></figure>

我们使用ctrl+c无法停止这个进程，说明他已经在后台进行了。

&可以一口气执行好几个命令，只要在每条命令后面加一个&就可以，并且是**同时执行的**。

### <mark style="color:green;background-color:blue;">2）分号操作符；</mark>

分号操作符可以让你一口气执行好几个命令，并且<mark style="background-color:yellow;">**按顺序执行**</mark>

```sh
apt-update;makdir test;cat 1.php
```

上述命令先执行更新，再执行创建文件夹，最后执行查看1.php文件。

### <mark style="color:green;background-color:blue;">3）与操作符&&</mark>

如果第一个命令成功才能执行第二个命令。

```sh
ping -c3 www.baidu.com && links www.baidu.com
```

在上述语句中，只有主机先在线了，我们在终端中访问网站www.baidu.com

### <mark style="color:green;background-color:blue;">4）或操作符||</mark>

或操作符就像**if else**语句，上面的操作符允许你在第一个命令失败的情况下执行第二个命令，不然就只会执行第一个命令。

```sh
apt-get update || links baidu.com
```

如果更新执行成功了，那么就不会执行访问百度的指令，如果用户不允许更新，也就是失败了，那么才能执行访问baidu的指令。

### <mark style="color:green;background-color:blue;">5）|管道操作符</mark>

管道操作符就相当于是<mark style="background-color:yellow;">**将第一个命令的输出作为了第二个命令的输入**</mark>

```sh
ls -l | less
```

比如说，在上述片段中，我们将ls输出的当前目录下的结果，用less输出。

***

## <mark style="color:blue;background-color:purple;">3.过滤姿势</mark>

这里参照的freebuf上面的一篇文章。那我们就按照他的进行学习。

### <mark style="color:green;background-color:blue;">1）过滤关键词，如cat，more等</mark>

#### <mark style="color:red;background-color:orange;">**①method one：替换法**</mark>

我们可以同义词替换，比如cat的指令相同的有

**`more`**：把文本一页一页地显示在界面上。

**`less`**：和more很像，但是more只能从前往后看，但less也可以从后往前看。

**`head`**：只看前几行

**`tac`**：从最后一行开始看（是cat反过来）

**`tail`**：只看最后几行

**`nl`**：显示的时候顺便显示行号

**`sort`**：对文本内容进行排序

#### <mark style="color:red;background-color:orange;">**②method two：进行转义**</mark>

为了验证这个，我们最好在自己的虚拟机上进行验证。对cat 1.php进行转义

（一）：就是添加\，在任何地方都可以被过滤掉的地方添加就行

```sh
ca\t 1.php
```

<figure><img src="../.gitbook/assets/image 2 (1).png" alt=""><figcaption></figcaption></figure>

（二）：**添加双引号**，转化为字符串

（对于这个，我在自己虚拟机上实验的时候发现别人写的好像实现不了，所以我在自己的虚拟机上实验过后，发现应该是在任何地方加一对双引号，不是只有单个的一个）

```sh
ca"t" 1.php

```

<figure><img src="../.gitbook/assets/image 3 (1).png" alt=""><figcaption></figcaption></figure>

（三）：**添加单引号**，转化为字符串

```sh
c'at' 1.php

```

<figure><img src="../.gitbook/assets/image 4 (1).png" alt=""><figcaption></figcaption></figure>

#### <mark style="color:red;background-color:orange;">**③method three：拼接法**</mark>

将某个完整的部分分成几个部分用变量代替。

比如以下的

```sh
a=1.;b=php;cat $a$b
```

<figure><img src="../.gitbook/assets/image 5 (1).png" alt=""><figcaption></figcaption></figure>

#### <mark style="color:red;background-color:orange;">**④method four：空变量绕过**</mark>

空变量有:`$*,$@,$x,${X}`

```sh
ca$*t 1.php

```

<figure><img src="../.gitbook/assets/image 6 (1).png" alt=""><figcaption></figcaption></figure>

```sh
ca$@t 1.php 
```

<figure><img src="../.gitbook/assets/image 7 (1).png" alt=""><figcaption></figcaption></figure>

```sh
ca$1t 1.php
```

<figure><img src="../.gitbook/assets/image 8 (1).png" alt=""><figcaption></figcaption></figure>



{% hint style="info" %}
通过实验发现，上述的x需要与后面的字符不是同一类型，比如后面是字母，那么x就只能是数字。
{% endhint %}

```sh
ca${1}t 1.php
```

<figure><img src="../.gitbook/assets/image 9 (1).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:green;background-color:blue;">2）反引号执行，$()执行</mark>

当执行函数比如`system，eval，exec`这些都被过滤了，我们可以考虑执行符反引号\`\`

除此之外，我们也可以用$()来包含要执行的指令

### <mark style="color:green;background-color:blue;">3）Base64编码</mark>

我们可以把关键词，比如cat，或者ls用先用base64编码，再解码执行。

这个步骤可以参考下述代码

```sh
echo 'cat' | base64  //对cat进行base64编码
echo 'Y2F0Cg==' | base64 -d//对Y2F0Cg==进行解码，和cat对上了，说明没有错误
`echo 'Y2F0Cg=='|base64 -d ` 1.php//得出最后的执行代码是这个
```

<figure><img src="../.gitbook/assets/image 10 (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image 11 (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image 12 (1).png" alt=""><figcaption></figcaption></figure>



{% hint style="info" %}
这里补充一个，那个对于base64编码的最后的执行语句还能写成下面的形式，主要是对于反引号\`\`被过滤的情况。
{% endhint %}

```sh
echo 'Y2F0Cg=='|base64 -d | bash
$(echo 'Y2F0Cg=='|base64 -d)
```

### <mark style="color:green;background-color:blue;">4）通配符绕过</mark>

> 通配符
>
> 通配符是一种特殊符号，主要有\*和？两种，用来模糊搜索文件
>
> \*:代表任何字符串
>
> ？：代表单个字符串

所以我们可以写出如下的shell。

```sh
cat 1*
cat 1??hp
```

<figure><img src="../.gitbook/assets/image 13 (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image 14 (1).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:green;background-color:blue;">5)hex编码</mark>

介绍hex编码，就需要介绍一个linux指令xxd（这个指令linux好像不自带，反正我的kali就不含这个指令，还得下载）

> xdd命令的功能是用于**以十六进制形式显示文件内容**，亦可以将十六进制内容转换回原始二进制的形式。

```sh
echo '63617420312e706870'|xxd -r -p |bash 
```

<figure><img src="../.gitbook/assets/image 15 (1).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:green;background-color:blue;">6）空格过滤</mark>

我们可以用`<>,%20,%09,$IFS,${IFS},(cat,flag)`,这些去过滤

### <mark style="color:green;background-color:blue;">7）括号过滤</mark>

#### **①method one：**

我们需要去积累一些不需要用括号的函数，因为有时候括号被过滤了，但是一些函数还是可以使用

`（一）echo ，print`

`（二）require，include，require_one,include_one`

`（三）die`

***

## <mark style="color:blue;background-color:purple;">4.反弹shell</mark>

之前老师上课的时候分享过一个反弹shell一件生成器。直接把他放在这里了。

[https://forum.ywhack.com/shell.php](https://forum.ywhack.com/shell.php)

反弹shell的目的是为了让受害者（也就是目标机）自己来连接攻击机，因为攻击机如果正向连接，需要突破防火墙，防火墙一般是防进不防出，所以我们可以通过命令执行去让受害者来自己连接我们。

***

## <mark style="color:blue;background-color:purple;">5.PHP伪协议</mark>

对于伪协议的具体含义，我们需要从几个与文件处理相关的函数来了解，除了我们之前提到的include，require之外的。

### <mark style="color:green;background-color:blue;">1）文件系统函数</mark>

#### <mark style="color:red;background-color:orange;">**①fopen()**</mark>

打开文件或者url。并且将filename指定的资源绑到一个流上。

```php
fopen(string[filename],string[mode],bool[use_include_path]=false,?resource[content]=null):resource|false
```

#### <mark style="color:red;background-color:orange;">**②copy()**</mark>

作用和名字一样，就是拷贝文件。

```php
copy(string[from],string[to],?resource[content]=null):bool
```

#### <mark style="color:red;background-color:orange;">**③file\_exists(）**</mark>

检验文件是否存在

```php
file_exists(string[filename]):bool
```

#### <mark style="color:red;background-color:orange;">**④filesize()**</mark>

取得文件大小

```PHP
filesize(string[filename]):int|false
```



{% hint style="info" %}
封装协议的url语法支持schema://....语法，其他的语法是不支持的。
{% endhint %}

### <mark style="color:green;background-color:blue;">2）支持的协议和封装协议</mark>

#### <mark style="color:red;background-color:orange;">**①file://**</mark>

作用：访问本地文件系统

> 文件系统：是php默认的文件系统，指定了本地文件系统。当指定了相对路径（不以/,\，\\,或windows的盘开头的）提供的路径将基于当前的工作目录。

这里展现一些路径的写法

* 文件路径
  * `/path/to/file.ext`
  * 【这是一个unix路径，从/根目录开始，然后指定了路径】
  * `relative/path/to/file.ext`
  * 【这是一个相对路径，从当前目录的子目录relative开始，然后进入到file.ext】
  * `fileInCwd.ext`
  * 【直接指向当前目录下的fileInCwd.ext文件】
  * `C:/path/to/winfile.ext`
  * 【win下面的路径】
  * `C:\path\to\winfile.ext`
  * 【和上面同理】
  * `\\smbserver\share\path\to\winfile.ext`
  * 【这是一个UNC（universal naming convention）通用命名路径，win环境中使用，smbserver是服务器或者ip名字，比如127.0.0.1,share是共相文件夹名称，path/是路径。】
  * `file:///path/to/file.ext`
  * 【这一下个就清晰多了，除去file://，这个代表的是文件系统，然后就是/path/to/file.ext这个是文件路径】

除此之外好像还要掌握封装协议的概要，这里就直接贴图了，反正是yes或者no也没什么好解释的。



<figure><img src="../.gitbook/assets/image 16 (1) (1).png" alt=""><figcaption></figcaption></figure>

#### <mark style="color:red;background-color:orange;">**②http:// https://**</mark>

这个就很熟悉了，访问网址。

> 这个用的是http/1.0 GET。

不多说了，直接上用法

* 用法
  * `http://example.com`
  * 【就是访问example.com域上的内容】
  * `http://example.com/file.php?var1=val1&var2=val2`
  * 【指向example.com域上的file.php内容，并且传入了两个参数】
  * `http://user:password@example.com`
  * 【包含用户名，密码的url】
  * `https://example.com https://example.com/file.php?var1=val1&var2=val2 https://user:password@example.com`
  * 【利用了https协议，更安全】

<figure><img src="../.gitbook/assets/image 17 (1).png" alt=""><figcaption></figcaption></figure>

#### <mark style="color:red;background-color:orange;">**③ftp:// ftps://**</mark>

和http差不多，只不过访问的是ftp远程服务器。而且允许读取文件，创建文件。

*   用法

    `ftp://example.com/pub/file.txt ftp://user:password@example.com/pub/file.txt ftps://example.com/pub/file.txt ftps://user:password@example.com/pub/file.txt`

<figure><img src="../.gitbook/assets/image 18 (1).png" alt=""><figcaption></figcaption></figure>

#### <mark style="color:red;background-color:orange;">**④php://**</mark>

作用就是访问输入输出流（i/o流）

#### **（1）php://input**

访问请求的原始数据的只读流。

```php
php://input + [POST DATA]执行php代码
```

以上这个代码主要是用于写入木马。

如果启用了 `enable_post_data_reading` 选项， `php://input` 在使用 `enctype="multipart/form-data"` 的 POST 请求中不可用。

#### **（2）php：//output**

只写的数据流，允许以print和echo的方式写入。

#### **（3）php://filter ！！！！**

是一种元封装器，设计用于数据流打开时的筛选过滤应用。

我们需要掌握他参数的具体写法。

<figure><img src="../.gitbook/assets/image 19 (1).png" alt=""><figcaption></figcaption></figure>

可选项也要了解一下

<figure><img src="../.gitbook/assets/image 20 (1).png" alt=""><figcaption></figcaption></figure>

我们这里主要详细讲解一下常用的几个语句的解释。

```php
php://filter/read=convert.base64-encode/resource=[文件名]读取文件源码（针对php文件需要base64编码）
```

`php://filter/read=convert.base64-encode/resource=` 是一种可以用于读取和编码文件内容的 PHP 文件包装器（PHP file wrapper）。该方法通常用于查看 PHP 文件的源代码，特别是在通过 HTTP 请求传递文件名时。这样是为了用base64的方法返回。

#### <mark style="color:red;background-color:orange;">**⑤data://**</mark>

就连手册上都是直接简单的数据流封装器。一般和include一起用，因为会被当成文件执行。

直接掌握下面两个语句,直接将text的内容转换为php代码。

```php
data://text/plain;base64,[text]
```

```php
data://text/plain,【text】
```

***

### <mark style="color:blue;background-color:purple;">6.无参数读文件</mark>

当我们的过滤限制非常大的时候，如以下情况

<figure><img src="../.gitbook/assets/image 21 (1).png" alt=""><figcaption></figcaption></figure>

我们就需要考虑无参数读文件了。

