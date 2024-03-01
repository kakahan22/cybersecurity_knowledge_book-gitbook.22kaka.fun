---
description: 其实php的语法到这个时候就已经可以用了。我们这里就直接讲解他的一些知识点了。
---

# 🚅 序列化，反序列化知识点

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









### <mark style="color:purple;background-color:green;">②\_\_wakeup()</mark>















## <mark style="color:yellow;background-color:blue;">三.PHP反序列化漏洞分析</mark>

### <mark style="color:purple;background-color:green;">①pop链</mark>

对于pop链具体是啥我们放到后面再来解释，我们先解释一个简单的反序列化漏洞的案例。



































## 参考门：

{% embed url="https://xz.aliyun.com/t/12507?time__1311=mqmhD50I1G7D%2FD0l8Gk%2Bpr39jmfD&alichlgref=https%3A%2F%2Fwww.google.com%2F" %}

{% embed url="https://evalexp.top/p/64706/#PHP%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90" %}

{% embed url="https://www.ol4three.com/2021/01/22/CTF/Web/PHP%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96%E5%AD%A6%E4%B9%A0%E4%B8%8E%E5%AE%9E%E8%B7%B5/" %}
