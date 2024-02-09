# 🏈 CTFSHOW PHP特性

## <mark style="color:purple;background-color:red;">（1）WEB 89</mark>

### <mark style="color:green;">①代码解释</mark>

```php
 <?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-16 11:25:09
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-18 15:38:51
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/


include("flag.php");
highlight_file(__FILE__);

if(isset($_GET['num'])){
    $num = $_GET['num'];
    if(preg_match("/[0-9]/", $num)){
        die("no no no!");
    }
    if(intval($num)){
        echo $flag;
    }
} 
```

<figure><img src="../.gitbook/assets/image (5) (1).png" alt=""><figcaption></figcaption></figure>

代码逻辑很简单，就是我们要让匹配$num的结果是0，然后$num变量通过intval为1就可以了。对于preg\_match匹配要是0，就说明不能是数字，但是如果是字符串的话，在下面的intval匹配中就会为0，这个时候我们要想到如果$num传入一个数组，那么对于pre\_match的特性，就会输出false然后我们就会进入else语句然后num是个数组并且不为空的话，就会输出1，也就是我们的num要通过url解析成一个不为空的数组。

### <mark style="color:green;">②思路介绍</mark>

不知道为什么网上的wp都没有解释一个事情。就是num=\["abc"]和num\[]="abc的区别。（这个地方主要是自己最开始也知道要传一个不含有数字的空的字符串去，但是后面发现其实不对。然后弄了很久才发现原来是url解析的问题。这里将讲解一下url对他们的解析的微妙的区别。）

*





