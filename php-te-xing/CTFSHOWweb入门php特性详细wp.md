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

<figure><img src="../.gitbook/assets/image (5) (1) (1).png" alt=""><figcaption></figcaption></figure>

代码逻辑很简单，就是我们要让匹配$num的结果是0，然后$num变量通过intval为1就可以了。对于preg\_match匹配要是0，就说明不能是数字，但是如果是字符串的话，在下面的intval匹配中就会为0，这个时候我们要想到如果$num传入一个数组，那么对于pre\_match的特性，就会输出false然后我们就会进入else语句然后num是个数组并且不为空的话，就会输出1，也就是我们的num要通过url解析成一个不为空的数组。

### <mark style="color:green;">②思路介绍</mark>

不知道为什么网上的wp都没有解释一个事情。就是num=\["abc"]和num\[]="abc的区别。（这个地方主要是自己最开始也知道要传一个不含有数字的空的字符串去，但是后面发现其实不对。然后弄了很久才发现原来是url解析的问题。这里将讲解一下url对他们的解析的微妙的区别。）

{% hint style="info" %}
URL解析差异！！！！！！！！！
{% endhint %}

* 对于num\[]=1 ，num被解释为一个数组，其第一个元素为1。这个时候数组的键值是动态生成的索引，例如num\[0]=1\&num\[1]=2。这个时候表达的意思其实是num是个数组，包含一个元素为1的数组。
* 对于num=\["1"]，其实num被解释成为了一个字符串，其值为\["1"].

所以在弄清楚这个后，我们能写出绕过方案

```url
http://65b4d1c3-5cc4-426c-b856-e5c14d755ef0.challenge.ctf.show/?num[]="abc"
```

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>



***

## <mark style="color:purple;background-color:red;">（2）web 90</mark>

```php
 <?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-16 11:25:09
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-18 16:06:11
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/


include("flag.php");
highlight_file(__FILE__);
if(isset($_GET['num'])){
    $num = $_GET['num'];
    if($num==="4476"){
        die("no no no!");
    }
    if(intval($num,0)===4476){
        echo $flag;
    }else{
        echo intval($num,0);
    }
}

```

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:green;">①代码解释</mark>

其实这个代码的意思也很明确，就是$num不能完全等于4476，但是在intval函数作用后，要等于4476，就能输出flag。

### <mark style="color:green;">②思路介绍</mark>

其实这一题我们看到intval函数的base为0，就应该想到intval的特性。所以我们可以让num是前面带有字母的，但是开头的数字是4476就行。类似4476ba这种。或者你想麻烦点，把他们进行进制转换也可以。

所以我们的方案就是

```url
http://f855998e-1508-4b60-9956-e03eadde4e40.challenge.ctf.show/?num=4476ab
```

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>



***

## <mark style="color:purple;background-color:red;">（3）web 91</mark>

```php

/*
# -*- coding: utf-8 -*-
# @Author: Firebasky
# @Date:   2020-09-16 11:25:09
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-18 16:16:09
# @link: https://ctfer.com

*/

show_source(__FILE__);
include('flag.php');
$a=$_GET['cmd'];
if(preg_match('/^php$/im', $a)){
    if(preg_match('/^php$/i', $a)){
        echo 'hacker';
    }
    else{
        echo $flag;
    }
}
else{
    echo 'nonononono';
}

Notice: Undefined index: cmd in /var/www/html/index.php on line 15
nonononono
```

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:green;">①代码解释</mark>

字符串a在开启了多行模式下满足正则表达式/^php$/，但是在非多行模式下，不满足正则表达式了。正则表达式的意思简单翻译就是转化后的字符串是php。

### <mark style="color:green;">②思路解释</mark>

这个就是我们讲过preg\_match含有的特性是绕过多行问题。我们采用的是%0a来解决的。

```url
http://4e1772d9-0414-4f78-a71b-8b49260e5e5e.challenge.ctf.show/?cmd=%0aphp
```

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:purple;background-color:red;">（4）web 92</mark>

```php
<?php

/*
# -*- coding: utf-8 -*-
# @Author: Firebasky
# @Date:   2020-09-16 11:25:09
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-18 16:29:30
# @link: https://ctfer.com

*/

include("flag.php");
highlight_file(__FILE__);
if(isset($_GET['num'])){
    $num = $_GET['num'];
    if($num==4476){
        die("no no no!");
    }
    if(intval($num,0)==4476){
        echo $flag;
    }else{
        echo intval($num,0);
    } 
```

<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:green;">①代码解释</mark>

代码的意思就是$num弱类型比较之后的值不能等于4476，并且通过intval函数作用后，在弱类型比较下要等于4476。

### <mark style="color:green;">②思路解释</mark>

我们之前用的直接在后面加字母不能用了，因为在弱类型比较下那样num会被认为是4476。所以我们只能使用intval的进制转换的特性了。我们这里用的是转16进制。（4476的16进制结果是117c）

```url
http://33ebd11e-67ab-47ec-af2f-b2571baba355.challenge.ctf.show/?num=0x117c
```

<figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>



***

## <mark style="color:purple;background-color:red;">（5）web 93</mark>

```php
 <?php

/*
# -*- coding: utf-8 -*-
# @Author: Firebasky
# @Date:   2020-09-16 11:25:09
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-18 16:32:58
# @link: https://ctfer.com

*/

include("flag.php");
highlight_file(__FILE__);
if(isset($_GET['num'])){
    $num = $_GET['num'];
    if($num==4476){
        die("no no no!");
    }
    if(preg_match("/[a-z]/i", $num)){
        die("no no no!");
    }
    if(intval($num,0)==4476){
        echo $flag;
    }else{
        echo intval($num,0);
    }
} 
```

<figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:green;">①代码解释</mark>

这里比上一题就是添加了一个条件，多了一个num里面不能含有字母。

### <mark style="color:green;">②思路解释</mark>

不能用字母是ban了16进制和二进制，但是8进制，只要开头是0就行了，还是能用的。所以这里我们直接用8进制的写法。4476的八进制结果是10574

```url
http://8e3950a6-590f-4e78-89d3-327e81f2a858.challenge.ctf.show/?num=010574
```

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>



***

## <mark style="color:purple;background-color:red;">（6）web 94</mark>

```php
 <?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-16 11:25:09
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-18 16:46:19
# @link: https://ctfer.com

*/

include("flag.php");
highlight_file(__FILE__);
if(isset($_GET['num'])){
    $num = $_GET['num'];
    if($num==="4476"){
        die("no no no!");
    }
    if(preg_match("/[a-z]/i", $num)){
        die("no no no!");
    }
    if(!strpos($num, "0")){
        die("no no no!");
    }
    if(intval($num,0)===4476){
        echo $flag;
    }
} 
```

<figure><img src="../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:green;">①代码解释</mark>

这个比上一题又多加了一个条件。为了理解这个条件，我们先了解一下这个函数。

> strpos（）：查找字符串首次出现的位置

<figure><img src="../.gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure>

所以这个条件的意思就是要求我们的第一位不能是0。但是目前我们用进制转换的8进制首位得是0，那么我们就得在前面添加一些不影响我们结果的非0得一些东西。

### <mark style="color:green;">②思路解释</mark>

























































































































