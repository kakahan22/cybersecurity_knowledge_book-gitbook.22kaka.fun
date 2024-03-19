---
description: >-
  其实php的语法到这个时候就已经可以用了。我们这里就直接讲解他的一些知识点了。其实反序列化漏洞能产生的原因也就是因为反序列化的输入是用户可控的，一切输入都是有害的。
---

# 🎥 反序列化漏洞知识点

## <mark style="color:yellow;background-color:blue;">一.序列化，反序列化函数</mark>

### <mark style="color:purple;background-color:green;">①serialize()</mark>

用于序列化对象或数组，并返回一个数组。

```
serialize(mixed $value): string
```

$value是要序列化的对象或数组。

```php
<?php

$a=['abc','def','ghi','jkl'];
$data=serialize($a);
echo $data;
?>

```

<figure><img src="../.gitbook/assets/image (102).png" alt=""><figcaption></figcaption></figure>

这里解释一下返回结果的格式有哪些

* String

s：size：value

* Integer

i：value

* Boolen

b：value

* Null

N

* Array

a：size：{key definition；value definition ；（repeated per element）}

* Object

O：strlen（object name）：object name ：object size：{s：strlen（property name）：property name：property definition；（repeated per property）}



接下来我们将特意举一个序列化对象化的例子，让我们看到对象序列化后输出的内容主要是什么。

```php
<?php

class saler{
    public  $code='echo "hello,world";';
    function __destruct()
    {
        @eval ($this->code);
    }
}

$s1=new saler();
echo serialize($s1);

?>

```

<figure><img src="../.gitbook/assets/image (104).png" alt=""><figcaption></figcaption></figure>

可以观察到其实是按照下面的格式输出的。

```
O（对象）：类名字符个数：类名：对象属性个数：
{属性类型：属性名字符数：属性名；属性值的类型：属性值字符数：属性值的内容}
```

除此之外对于private，public，protected，他们的输出是有区别的，我们可以试试看。

```php
<?php

class Saler{
    public  $code='echo "hello,world";';
    public $a=123;
    protected $b=123;
    private $c=123;
    function __destruct()
    {
        @eval ($this->code);
    }
}

$a=new Saler();
echo serialize($a);
//O:5:"Saler":1:{s:4:"code";s:19:"echo "hello,world";";}hello,world

/*$obj=unserialize($_GET['data']);
print_r($obj);
*/
?>
```

<figure><img src="../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

#### （1）public

public权限就是没有变化。

#### （2）protected

属性名变成了%00\*%00属性名，我们看到就是加了个星号而已，但其实，我们可以观察到，大小还是增加了两个%00和一个\*的大小，就是增加了三个。

#### （3）private

属性名变成了%00类名%00属性名，我们看到就是在属性名前面增加了类名。但其实，大小还是增加了类名和两个%00的大小。



### <mark style="color:purple;background-color:green;">②unserialize（）</mark>

将通过 serialize() 函数序列化后的对象或数组进行反序列化，并返回原始的对象结构。

```
mixed unserialize ( string $str )
```

返回的值是转换之后的值，可以是int，float，string，array，或者object都可以。

```php

<?php

$a='a:4:{i:0;s:3:"abc";i:1;s:3:"def";i:2;s:3:"ghi";i:3;s:3:"jkl";}';
$data=unserialize($a);
print_r($data);
?>

```

<figure><img src="../.gitbook/assets/image (103).png" alt=""><figcaption></figcaption></figure>

接下来特别介绍对于对象的执行结果。

```php

<?php

class Saler{
    public  $code='echo "hello,world";';
    function __destruct()
    {
        @eval ($this->code);
    }
}
/*
$a=new Saler();
echo serialize($a);
O:5:"Saler":1:{s:4:"code";s:19:"echo "hello,world";";}hello,world
*/
$obj=unserialize($_GET['data']);
print_r($obj);
?>

```

<figure><img src="../.gitbook/assets/image (105).png" alt=""><figcaption></figcaption></figure>

返回的就是object（对象）（属性名=>属性内容）

***

## <mark style="color:yellow;background-color:blue;">二.魔法函数</mark>

这个我们在php进阶语法的时候·提到过，所以我们直接

```
__construct 当一个对象创建时被调用
__destruct  当一个对象销毁时被调用
__toString  当一个对象被当作一个字符串被调用
__wakeup()  使用unserialize时触发
__sleep()   使用serialize时触发
__destruct() 对象被销毁时触发
__call()     在对象上下文调用不可访问的方法时触发
__callStatic()  在静态上下文中调用不可访问的方法时触发
__get()          用于从不可访问的属性读取数据
__set()          用于将数据写入不可访问的属性
__isset()        在不可访问的属性上调用isset()或empty()触发
__unset          在不可访问的属性上使用unset()时触发
__invoke()       当脚本尝试将对象调用为函数时触发
```



### <mark style="color:purple;background-color:green;">①\_\_sleep()</mark>

> serialize() 函数会检查类中是否存在一个魔术方法 \_\_sleep()。如果存在，该方法会先被调用，然后才执行序列化操作。此功能可以用于清理对象，并返回一个包含对象中所有应被序列化的变量名称的数组。如果该方法未返回任何内容，则 NULL 被序列化，并产生一个 E\_NOTICE 级别的错误。

对象被序列化之前触发，返回需要被序列化存储的成员属性，删除不必要的属性。

### <mark style="color:purple;background-color:green;">②\_\_wakeup()</mark>

> unserialize() 会检查是否存在一个 \_\_wakeup() 方法。如果存在，则会先调用 \_\_wakeup 方法，预先准备对象需要的资源。

预先准备对象资源，返回void，常用于反序列化操作中重新建立数据库连接或执行其他初始化操作。

所以这里直接借用青叶大佬里面的例子进行实验

```php
<?php 
class Caiji{
    public function __construct($ID, $sex, $age){
        $this->ID = $ID;
        $this->sex = $sex;
        $this->age = $age;
        $this->info = sprintf("ID: %s, age: %d, sex: %s", $this->ID, $this->sex, $this->age);
    }

    public function getInfo(){
        echo $this->info . '<br>';
    }
    /**
     * serialize前调用 用于删选需要被序列化存储的成员变量
     * @return array [description]
     */
    public function __sleep(){
        echo __METHOD__ . '<br>';
        return ['ID', 'sex', 'age'];
    }
    /**
     * unserialize前调用 用于预先准备对象资源
     */
    public function __wakeup(){
        echo __METHOD__ . '<br>';
        $this->info = sprintf("ID: %s, age: %d, sex: %s", $this->ID, $this->sex, $this->age);
    }
}

$me = new Caiji('twosmi1e', 20, 'male');

$me->getInfo();
//存在__sleep(函数，$info属性不会被存储
$temp = serialize($me);
echo $temp . '<br>';

$me = unserialize($temp);
//__wakeup()组装的$info
$me->getInfo();

?>
```

<figure><img src="../.gitbook/assets/image (9) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

其实对于结果分析我们就能看到，在调用serialize的时候，自动调用了\_\_sleep，然后因为sleep里面没有准备info，所以后面的输出，其实就没有info了。在调用unserialize的时候，自动调用了\_\_wakeup，里面又重构了了info，所以后面成功输出了info。

### <mark style="color:purple;background-color:green;">③\_\_toString()</mark>

> \_\_toString()方法用于一个类被当成字符串时应怎样回应。例如echo $obj; 应该是显示些什么。此方法必须返回一个字符串，否则将发出一条E\_RECOVERABLE\_ERROR级别的致命错误

举个栗子：

```php
<?php 
class Caiji{
    public function __construct($ID, $sex, $age){
        $this->ID = $ID;
        $this->sex = $sex;
        $this->age = $age;
        $this->info = sprintf("ID: %s, age: %d, sex: %s", $this->ID, $this->sex, $this->age);
    }

    public function __toString(){
        return $this->info;
    }
}

$me = new Caiji('ol4three', 18, 'male');
echo '__toString:' . $me . '<br>';
?>

```

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:yellow;background-color:blue;">三.PHP反序列化漏洞分析（未完）</mark>

### <mark style="color:purple;background-color:green;">①wakeup（）绕过</mark>

很多对这个解释都是说，因为在使用unserilize（）之前会使用wakeup（），但是如果序列化字符串中表示对象属性个数的值大于真实的属性个数会跳过\_\_wakeup()的执行。

举个栗子：

```php
<?    
    class A{
        public $target = "test";
        function __wakeup(){
            $this->target = "wakeup!";
        }
        function __destruct(){
            $fp = fopen("/Library/WebServer/Documents/hello.php","w");
            fputs($fp,$this->target);
            fclose($fp);
        }
    }
    $a = $_GET['test'];
    $b = unserialize($a);
    echo "hello.php"."<br/>";
    include("./hello.php");
?>
```

正常情况下在这个下面$target的结果会被覆盖为wakeup，但是如果我们test传入的属性个数从1转化为2的时候，$target就不会被覆盖。

### <mark style="color:purple;background-color:green;">②session反序列化漏洞</mark>

其实之前我们有讲过session，但是当时是因为文件包含所以讲解的，这里我们为了反序列化再讲一次。

#### （1）session介绍

基础部分我们还是引用之前讲过的。可以从下面的link跳转。

&#x20;[#id-5.-bao-han-session](../lfi-he-rfl-wen-jian-bao-han-lou-dong/文件包含漏洞知识点总结.md#id-5.-bao-han-session "mention")

#### （2）session工作流程

第一次访问网站时，session\_start()会创建一个session id，并且通过http的响应头，将这个session id保存到客户端的cookie里面。同时也在服务器端创建一个以session\_id命名的文件用于保存用户信息。当再次访问这个网站的时候，会自动通过http头讲cookie保存的session id再携带过来，这时的session id不会修改。

#### （3）handler

php对session有不同的handler

<table><thead><tr><th width="201">Handler</th><th>存储格式</th></tr></thead><tbody><tr><td>php</td><td>键名+竖线+serialize数据</td></tr><tr><td>php_binary</td><td>键名的长度对应的ASCII字符+键名+serialize数据</td></tr><tr><td>php_serialize</td><td>serialize数据</td></tr></tbody></table>

举个例子：

一段代码

```php
session_start();
$_SESSION['name'] = 'evalexp';
```

| Handler        | 存储结果                            |
| -------------- | ------------------------------- |
| php            | name\|s:7:"evalexp";            |
| php\_binary    | names:7:"evalexp";              |
| php\_serialize | a:1:{s:4:"name";s:7:"evalexp"}; |

#### (4)session漏洞形成原理

如果开发者在存储Session数据和读取Session数据时所使用的Handler不一致，就将导致无法正确地反序列化，从而导致被反序列化攻击。

借鉴一个例子

```php
$_SESSION['hello'] = '|O:8:"stdClass":0:{}';
```

如果使用php\_serialize进行序列化，得到的session是

```shell-session
a:1:{s:5:"hello";s:20:"|O:8:"stdClass":0:{}";}
```

如果处理器是php，那么会以竖线为分隔符，就会导致不正确的序列化

```shell-session
$_SESSION['a:1:{s:5:"hello";s:20:"'] = object(stdClass){}
```

### ③字符逃逸

当出现首先对对象进行序列化，然后再进行反序列化的时候就会出现字符逃逸。

出现的原因主要是因为，反序列化底层代码是以 ; 作为字段的分隔，以 } 作为结尾，并且是根据长度判断内容的 ，同时反序列化的过程中必须严格按照序列化规则才能成功实现反序列化 ，超出的部分并不会被反序列化成功，这说明反序列化的过程是有一定识别范围的，在这个范围之外的字符都会被忽略，不影响反序列化的正常进行。而且可以看到反序列化字符串都是以_**";}**_结束的，那如果把_**";}**_添入到需要反序列化的字符串中（除了结尾处），就能让反序列化提前闭合结束，后面的内容就相应的丢弃了。

并且长度不对劲的时候会报错。

#### （1）替换修改后导致序列化字符串变长

这里用先知社区的代码作为例子。

```php
<?php
function filter($str)
{
    return str_replace('bb', 'ccc', $str);
}
class A
{
        public $name = 'aaaabb';
        public $pass = '123456';
}
$AA = new A();
echo serialize($AA) . "\n";
$res = filter(serialize($AA));
echo $res."\n";
$c=unserialize($res);
var_dump($c);
?>

```

<figure><img src="../.gitbook/assets/image (8) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

很显然报错了，但是要的就是这个效果。我们还是先解释一下这个代码，我们首先对他进行序列化，这个时候没有问题，然后我们进行字符串替换了，这个时候，bb替换为ccc，这个时候，nameccc是7个字符，但是我们的序列化的结果不能自动更新，所以它还是显示6个字符，这个时候就出问题了。我们再在这个时候落进下石的话，进行反序列化，就会报错。

#### （6）pop链

POP链：

> POP（Property-Oriented Programing）面向属性编程，常用于上层语言构造特定调用链的方法，与二进制利用中的ROP（Return-Oriented Programing）面向返回编程的原理相似，都是从现有运行环境中寻找一系列的代码或者指令调用，然后根据需求构成一组连续的调用链。在控制代码或者程序的执行流程后就能够使用这一组调用链做一些工作了。

这个暂时看不懂，所以不写。但是做了一道这样的题，发现其实就是看懂代码然后利用，我是不知道有啥需要我特别总结的。









***

## 四.对于private，procted的空格绕过

首先我们知道private和procted在反序列化的时候，protected会变成%00\*%00属性名，private会变成%00类名%00属性名。这个%00是url后的结果，没有经过url的结果其实是

```
\x00*\x00属性名
\x00类名\x00属性名。
```

这个时候我们可能会发生截断，在这个空格的地方。

为了解决这个问题，我们有两种解决方法。

### （1）方法一：

就是让Payload能够显示这个空格，我们一般会在属性的位置将用大写的S代替小写的s，具体的原因可以看p神的这个例子。

<figure><img src="../.gitbook/assets/image (4) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### （2）方法二

直接将protected和private用public代替，就是换成public，因为php7.1以上的版本对属性类型不敏感。就是直接换成public了，真是直接！











## 参考门：

{% embed url="https://xz.aliyun.com/t/12507?time__1311=mqmhD50I1G7D%2FD0l8Gk%2Bpr39jmfD&alichlgref=https%3A%2F%2Fwww.google.com%2F" %}

{% embed url="https://evalexp.top/p/64706/#PHP%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90" %}

{% embed url="https://www.ol4three.com/2021/01/22/CTF/Web/PHP%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96%E5%AD%A6%E4%B9%A0%E4%B8%8E%E5%AE%9E%E8%B7%B5/" %}
