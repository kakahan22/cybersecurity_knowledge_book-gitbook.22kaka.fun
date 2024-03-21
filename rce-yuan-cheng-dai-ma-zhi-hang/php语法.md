---
description: 因为RCE执行通常会出现php代码，所以这里学习php语法，并且推荐大家搭建环境进行学习
---

# 😀 PHP语法

## <mark style="color:red;background-color:blue;">1.基本格式</mark>

以`<?php`开头，`?>结尾`，每条语句用;结尾

```php
<?php
  ?>
```

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption><p>基本格式</p></figcaption></figure>

{% hint style="warning" %}
注意，如果你没有输入；会出现报错，以下报错显示期待一个分号。
{% endhint %}

特殊情况是，如果是最后一行，可以不用分号，他会自动添加分号（这是笔者在测试的时候只写了一条语句发现仍然可以运行成功。）

<figure><img src="../.gitbook/assets/image 1 (1) (1).png" alt=""><figcaption><p>报错提醒</p></figcaption></figure>

***

## <mark style="color:red;background-color:blue;">2.输出</mark>

### <mark style="color:green;background-color:purple;">1）echo</mark>

如果我们想输出hello，world这句话，我们可以采用echo这个函数，直接输出。

1. echo " "；

```php
<?php
    echo "hello world"；
?>
```

2.当然，你也可以在echo后面加括号，将输出语句括起来。

```php
<?php
    echo('hello world') ;
?>
```

<figure><img src="../.gitbook/assets/image 2 (1) (1).png" alt=""><figcaption><p>带括号的输出</p></figcaption></figure>

3.当然，你也可以把一句完整的话，用，隔开，echo可以把他们拼接起来

```php
<?php
    echo 'hello','I','like','the','word';
?>
```

<figure><img src="../.gitbook/assets/image 3 (1) (1).png" alt=""><figcaption><p>用逗号连接输出</p></figcaption></figure>

### <mark style="color:green;background-color:purple;">2）print</mark>

`print`也是打印，可以采用上面`echo`的用双引号，括号的方式（不能用，号拼接）。但是，多了一个返回值，如果打印成功，返回1。

比如我们可以试一试

```php
<?php
    echo print 'hello world' ;
?>
```

<figure><img src="../.gitbook/assets/image 4 (1) (1).png" alt=""><figcaption></figcaption></figure>

看，在输出hello world的后面紧跟着的就是1，说明，print的返回值被echo打印了。

### <mark style="color:green;background-color:purple;">3）转义</mark>

如果我们想输入一个 Li'book，如果我们用单引号进行闭合的话，那么Li后面的单引号会和前面的引号进行闭合，就会让原本应该与前面闭合的单引号落单了，这就导致了语法错误。我们可以采取用双引号闭合，也可以用转义符\来转义Li后面的单引号。

```php
<?php
    echo "Li'book";
?>
```

<figure><img src="../.gitbook/assets/image 5 (1) (1).png" alt=""><figcaption></figcaption></figure>

```php
<?php
    echo 'Li\'book';
?>
```

<figure><img src="../.gitbook/assets/image 6 (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:red;background-color:blue;">3.变量</mark>

### <mark style="color:green;background-color:purple;">1）创建变量</mark>

用美元符加变量名，就是一个变量的创建了。（命名规则和

c语言一样）

```php
<?php
$ab='hello world';
    echo $ab;
?>
```

<figure><img src="../.gitbook/assets/image 7 (1) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
注意，不能将变量名命名为this等特定名词。
{% endhint %}

### <mark style="color:green;background-color:purple;">2）按值分配和引用</mark>

这句话可能很难理解，我们先看一个代码例子。可以看，现在这个是和c语言一样的，根据执行语句的顺序，一步一步执行下去的。

```php
<?php
$x=1;
$y=$x;
$x=2;
    echo $x ;
    echo $y;
?>
```

<figure><img src="../.gitbook/assets/image 8 (1) (1).png" alt=""><figcaption></figcaption></figure>

如果我们想要让y随着x的变化而变化，那么我们要修改代码为。他的意思是，x的引用赋值给了y。

```php
<?php
$x=1;
$y=&$x;
$x=2;
    echo $x ;
    echo $y;
?>
```

<figure><img src="../.gitbook/assets/image 9 (1) (1).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:green;background-color:purple;">3）打印变量</mark>

如果我们想在语句中，打印这个变量，

1）那么我们要用双引号闭合，单引号代表里面的都是字符串。

```php
<?php
$x=1;
$y=&$x;
$x=2;
    echo 'hello$x' ;
    echo "hello$y";
    
?>
```

<figure><img src="../.gitbook/assets/image 10 (1) (1).png" alt=""><figcaption></figcaption></figure>

2）除此之外，我们也可以用大括号把这个变量单独括起来。当然也要在双引号以内。

```php
<?php
$x=1;
$y=&$x;
$x=2;
    echo 'hello{$x}' ;
    echo "hello{$y}";
?>

```

<figure><img src="../.gitbook/assets/image 11 (1) (1).png" alt=""><figcaption></figcaption></figure>

3）我们可以用.连接。

```php
<?php
$x=1;
$y=&$x;
$x=2;
    echo 'hello'.$x ;
    echo "hello".$y;
    
?>
```

<figure><img src="../.gitbook/assets/image 12 (2).png" alt=""><figcaption><p>.</p></figcaption></figure>

***

## <mark style="color:red;background-color:blue;">4.常量</mark>

### <mark style="color:green;background-color:purple;">1）创建常量</mark>

<mark style="color:yellow;background-color:green;">**①用define**</mark>，他有返回值，如果成功了，返回值是1.

`define('name','value')；`

我们一般把name，大写，这样我们便于区分变量和常量。此外，常量不要用$，并且常量的值不能被改变。

```php
<?php
define ('STATUS_PAID','paid');
    echo STATUS_PAID ;
?>
```

<figure><img src="../.gitbook/assets/image 13 (2).png" alt=""><figcaption><p>DEFINE</p></figcaption></figure>

<mark style="color:yellow;background-color:green;">**②用const**</mark>

`const name='value'；`

```php
<?php
const STATUS_PAID='paid';
    echo STATUS_PAID ;
?>

```

<figure><img src="../.gitbook/assets/image 14 (1) (1).png" alt=""><figcaption><p>CONST</p></figcaption></figure>

### <mark style="color:green;background-color:purple;">2)PHP自带常量</mark>

比如我们想知道PHP的版本，我们可以直接打印常量`PHP_VERSION`

```php
<?php

    echo PHP_VERSION ;
?>

```

<figure><img src="../.gitbook/assets/image 15 (2).png" alt=""><figcaption><p>PHP_VERSION</p></figcaption></figure>

### <mark style="color:green;background-color:purple;">3)MAGIC 常量</mark>

一些可以根据位置而改变的常量，一般是`__`**`NAME`**`__`

比如常见的`__FILE__,__LINE__`

```php
<?php

    echo __FILE__ ;
?>

```

<figure><img src="../.gitbook/assets/image 16 (2) (1).png" alt=""><figcaption><p>__FILE__</p></figcaption></figure>

```php
<?php

    echo __LINE__ ;
?>

```

<figure><img src="../.gitbook/assets/image 17 (1) (1).png" alt=""><figcaption><p>__LINE__</p></figcaption></figure>

### <mark style="color:green;background-color:purple;">4）VARIABLE VARIABLES</mark>

比如我们可以把一个变量得到的结果作为一个新的变量名。

举个例子。下面的`$$foo`其实就等于`$bar`。

```php
<?php
$foo='bar';
$$foo='baz';
$bar='baz';
    echo  $$foo;
    echo $bar;
?>

```

<figure><img src="../.gitbook/assets/image 18 (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:red;background-color:blue;">5.类型</mark>

基本的`bool，int，float，string`，就不过多介绍了，c语言都有

复合型的有`array，object，callable，iterable`。

特殊类型有`resource，null`。

简单介绍一下`array`和两种特殊的，另外的复合型将在后面详细介绍。

{% hint style="warning" %}
补充一个，`IFS`代表无穷大
{% endhint %}

### <mark style="color:green;background-color:purple;">1）array</mark>

这里简单介绍一下`array`，我们用中括号把我们需要的`array`的值括起来，里面可以包含各种类型，（这点和c语言不同，他更加灵活）。

<mark style="color:yellow;background-color:green;">**①打印数组**</mark>，我们需要用专门的`print_r()`打印这个数组。

```php
<?php
$array=[1,2,3,'abc','def','ghi',34.56,4343.789,true,false];
print_r($array);
?>

```

<figure><img src="../.gitbook/assets/image 19 (1) (1).png" alt=""><figcaption><p>PRINT_R</p></figcaption></figure>

但是如果是打印其中的一个，我们还是用`echo`或者`print`就可以。

比如以下这个，打印了数组的第0号位置的结果，并且，证明了数组是从0开始编号的。

```php
<?php
$programminglanguages=['php','java','python'];
echo($programminglanguages[0]);
var_dump(isset($programminglanguages[3]));
?>//isset被用来检测变量是否被声明并且它的值不为null。

```

<figure><img src="../.gitbook/assets/image 20 (1) (1).png" alt=""><figcaption></figcaption></figure>

<mark style="color:yellow;background-color:green;">**②推入元素**</mark>。如果要往数组里增加值，有两种方式，第一种用下标直接赋值，但是这样一次只能赋值一种，效率低。第二种利用`array_push`函数，一次可以推入多个值。

`array_push(array,value,value,value.....)`

```php
<?php
$programminglanguages=['php','java','python'];
$programminglanguages[]='go';
print_r($programminglanguages);
echo '<br />';

array_push($programminglanguages,'c++','c','golong','js','html');
print_r($programminglanguages);

?>

```

<figure><img src="../.gitbook/assets/image 21 (2).png" alt=""><figcaption><p>ARRAY_PUSH</p></figcaption></figure>

<mark style="color:yellow;background-color:green;">**③key-value**</mark>，数组是有键值对的，php中也可以这么做。

直接看代码吧。因为这种python里面用过。学名**关联数组**

```php
<?php
$programminglanguages=[
    'php'=>1.0,
    'java'=>2.0,
    'python'=>3.0
];

print_r($programminglanguages);
echo '<br \>';

echo $programminglanguages['php'];

?>

```

<figure><img src="../.gitbook/assets/image 22 (1).png" alt=""><figcaption></figcaption></figure>

如果我们想知道某个键是否存在，我们可以利用一个函数

`array_key_exists(key,array)`

```php
<?php
$programminglanguages=[
    'php'=>'1.0',
    'java'=>'2.0',
    'python'=>[
        'version1'=>'3.4',
        'version2'=>'4.5',
        'version3'=>'5.7',
    ],
];

var_dump(array_key_exists('python',$programminglanguages));
var_dump(array_key_exists('version1',$programminglanguages));

echo '<br \>';


?>

```

<figure><img src="../.gitbook/assets/image 23 (1).png" alt=""><figcaption><p>ARRAY_KEY_EXISTS</p></figcaption></figure>

从这里我们也可以看出来，其实键值对是对于某个特定的维数来说的，对于第二个键，其实是`$programlanguages['python']`这个数组的键值对（并且验证过了）。

<mark style="color:yellow;background-color:green;">④</mark><mark style="color:yellow;background-color:green;">**多维数组**</mark>。这个多维不像c语言一样，他的多维是通过键值对来实现的，比如这个value因为可以有多种类型的结果，当他是数组的时候，那么他又有键值对在value里面。这个时候就实现了多维数组。

```php
<?php
$programminglanguages=[
    'php'=>'1.0',
    'java'=>'2.0',
    'python'=>[
        'version1'=>'3.4',
        'version2'=>'4.5',
        'version3'=>'5.7',
    ],
];

print_r($programminglanguages);
echo '<br \>';

echo $programminglanguages['python']['version2'];

?>

```

<figure><img src="../.gitbook/assets/image 24 (1).png" alt=""><figcaption><p>多维数组</p></figcaption></figure>

{% hint style="info" %}
到这里，我们对下标有一种另外的理解，他是一种自动分配的键值对，键是数字。
{% endhint %}

<mark style="color:yellow;background-color:green;">**⑤删除元素**</mark>。需要用到一个函数`array_pop（）`一次弹出一个。并且是从后面开始。

`array_pop（array）`

如果我们想从前面开始删除，那么我们需要用`array_shift`函数，一次出来一个，从前面开始。

`array_shift(array)`

```php
<?php
$programminglanguages=[
    'php'=>'1.0',
    'java'=>'2.0',
    'python'=>[
        'version1'=>'3.4',
        'version2'=>'4.5',
        'version3'=>'5.7',
    ],
];

print_r($programminglanguages);
echo '<br \>';

array_pop($programminglanguages);
print_r($programminglanguages);
echo '<br \>';

array_shift($programminglanguages);
print_r($programminglanguages);
echo '<br \>';

?>

```

<figure><img src="../.gitbook/assets/image 25 (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
其实这个和数据结构的栈和队列的操作已经很相似了，可以用这两个函数来实现他们的操作。
{% endhint %}

此外，其实在删除元素的时候，php的下标会重新编号，如果是数字键值（就是用下标来表示的），那么我们的结果会发生改变，会变成从0开始。

### <mark style="color:green;background-color:purple;">2）STRING</mark>

这里补充一下`heredoc`和`nowdoc`，如果我们要输出长文字，并且要换行的话，像这样

<mark style="color:yellow;background-color:green;">1）</mark><mark style="color:yellow;background-color:green;">**heredoc**</mark>：需要用`<<<TEXT`开头，`TEXT`结尾，中间是文本内容，并且是可以换行的。里面的文本，可以识别变量以及一切特殊的符号，比如$,

这种标签也可以。除此之外，它能够读到空格，虽然在格式上表示不出来，但是我们用`var_dump`可以自行验证。

```php
<?php
$x=1;
$y=2;

$abc=<<<TEXT
LINE 1
LINE2 $x
LIEN3         $y
LIEN4
LINE5 
AAAAAA
TEXT;
echo $abc;
?>

```

<figure><img src="../.gitbook/assets/image 26 (1).png" alt=""><figcaption><p>HEREDOC</p></figcaption></figure>

<mark style="color:yellow;background-color:green;">**2）nowdoc**</mark>，格式是`<<<'TEXT'`开头，`TEXT`结尾，并且它里面的任何的文字都是只是字符串，就是说，他识别不了里面的特殊的一些符号代表的意思。

```php
<?php
$x=1;
$y=2;

$abc=<<<'TEXT'
LINE 1
LINE2 $x
LIEN3         $y
LIEN4
LINE5 
AAAAAA
TEXT;
echo $abc;
?>

```

<figure><img src="../.gitbook/assets/image 27 (1).png" alt=""><figcaption><p>NOWDOC</p></figcaption></figure>

### <mark style="color:green;background-color:purple;">3）var\_dump()</mark>

如果我们想知道变量的类型，我们可以用一个函数\*\*`var_dump()`\*\*。

```php
<?php
$a=1;
$b=1.234;
$c='string';
$d=true;
    var_dump($a);
    var_dump($b);
    var_dump($c);
    var_dump($d);
?>

```

<figure><img src="../.gitbook/assets/image 28 (1).png" alt=""><figcaption><p>VAR_DUMP</p></figcaption></figure>

我们可以看到，`var_dump（）`输出了，路径，行数，以及类型，还有变量结果，特殊的对于字符串来说，还输出了字符串的长度。

### <mark style="color:green;background-color:purple;">4)强制转换</mark>

我们根据前面已经知道php会自动转换数据类型，但是他其实不单单是根据数据判断，他也会根据上下文进行强制转换，这个和c语言一样，如果他强制转换失败了，那么他就会报错。

如果我们想要禁止掉动态转换类型的话，我们可以加一句

**`declare(strict_types=1)；`**

（但是这个还是可以让int和float转换，就挺离谱的）

> <mark style="color:purple;background-color:orange;">弱类型转换</mark>
>
> 在这个地方想要提一句弱类型转换，因为这个地方，上次刷ctf题目的时候刷到了。
>
> php属于弱类型语言，所以当我们用字符串a和数字0做判断的时候，字符串a会转化为0，当我们用字符串1a和数字0作比较的时候，字符串1a就会转换为1.
>
> 我们可以实验一下。
>
> ```php
> <?php
> $x='a';
> $y='1a';
> var_dump((int)$x);
> var_dump((int)$y);
>
> ?>
> ```

<figure><img src="../.gitbook/assets/image 29 (1).png" alt=""><figcaption><p>弱类型</p></figcaption></figure>

##

{% hint style="info" %}
![](data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==)总结就是：当string转化为int的时候，字符串没有数字开头就转换为0，有数字开头，就转换为第一位数字。如果数字中间有其他东西分隔了，转换为分割前的数字。
{% endhint %}

***

## <mark style="color:red;background-color:blue;">6.运算符</mark>

### <mark style="color:green;background-color:purple;">1）数学运算符</mark>：

`+，-，`**`，/，%，`**`*`

（最后一个\*\*是幂运算，比如a\*\*\*\*b，就是a的b次方的意思）

### <mark style="color:green;background-color:purple;">2）赋值运算符</mark>

就是上述的后面都加个等号，和c语言一样，就不多说了。

### <mark style="color:green;background-color:purple;">3）字符运算符</mark>

`. ,.=`

就是字符串连接符，之前在echo的输出有用到过。

### <mark style="color:green;background-color:purple;">4）比较运算符</mark>

#### <mark style="color:yellow;background-color:green;">①\*\*==和===\*\*</mark>

\==在运算时，会先进行类型转换，再比较相等不相等。

\===在运算时，直接比较相等不相等，不进行类型转换。

```php
<?php
$x=1;
$y='1';
var_dump($x==$y);
var_dump($x===$y);

?>

```

<figure><img src="../.gitbook/assets/image 30.png" alt=""><figcaption></figcaption></figure>

#### <mark style="color:yellow;background-color:green;">**②≠，！ ==，<>**</mark>

`≠`如果不等于，就是true。只比较值

`！ ==`如果不全等于，就是true。值和类型都比较

`<>`表示不等于。

```php
<?php
$x=1;
$y='1';
var_dump($x!=$y);
var_dump($y!==$y);

?>

```

<figure><img src="../.gitbook/assets/image 31.png" alt=""><figcaption></figcaption></figure>

#### <mark style="color:yellow;background-color:green;">**③≥,≤,≤=>**</mark>

这里就讲一下≤=>就可以了，他用一个符号的返回值，可以表示大于，等于，小于，三种关系。

如果左边<右边 ------------------ -1

左边=右边----------------------- 0

左边>右边---------------------- 1

```php
<?php
$x=1;
$y=2;
$z=2;
var_dump($y<=>$z);
var_dump($x<=>$y);
var_dump($y<=>$x);

?>

```

<figure><img src="../.gitbook/assets/image 32.png" alt=""><figcaption></figcaption></figure>

#### <mark style="color:yellow;background-color:green;">**④？？， ?:**</mark>

这是三元运算符`，？：`我们在c语言已经见过了，如果条件成立，返回？后面的结果，否则返回：后面的结果。

`？？`是空合并符，比如`y=x ?? "hello"`,这个式子，就是如果x不为null，y的值就是x，如果x为空，y的值，就是`”hello”`。

{% hint style="danger" %}
接下来的是RCE要用到的一些符号。
{% endhint %}

#### <mark style="color:yellow;background-color:green;">5）错误控制符@</mark>

英文翻译是ERROR control operators，其实应该称为错误抑制符比较合适。因为平常如果我们输出的php语句有错误，屏幕上会报错，但是如果我们使用了@，那么我们就看不到报错了。

我们将会对比一下。因为我们要打开的是一个不存在的一个txt文件，正常情况下，会报错。

<figure><img src="../.gitbook/assets/image 33.png" alt=""><figcaption></figcaption></figure>

但是如果我们加上了@符在file前面，我们可以看到屏幕什么都没有显示。有时候我们利用rce的时候，不想要目标看到我们的显示，就可以用这个。

<figure><img src="../.gitbook/assets/image 34.png" alt=""><figcaption></figcaption></figure>

#### <mark style="color:yellow;background-color:green;">6）自增自减运算符++，--</mark>

和c语言一样，就不介绍了。

#### <mark style="color:yellow;background-color:green;">7）逻辑运算符</mark> <mark style="color:yellow;background-color:green;">`&&， ||， and ， or，xor`</mark>

`&&`:两个都为真，结果才为真。

`||`：任一为真，就为真

`and`：和&&一样，但是&&的优先级高于&&

`or`：和||一样

`xor`：（异或），如果两个任意一个为真，但是不同时为真，就为真。（相异为真，相同为假）

这里需要特别提到**逻辑短路**的特性。对于逻辑运算符&&和||来说。如果是&&，如果前面为假，那么后面的部分不会执行了，就直接输出为假。对于||来说，如果前面为真了，后面的也不会执行了，直接输出为真。

#### <mark style="color:yellow;background-color:green;">8）按位运算符& ,|,^,\~,<<,>></mark>

因为之前学过的位运算差不多忘光了，这里就再补充一下

①`&`:转化为2进制数之后，都为1输出1，其他情况都输出0.

②`|`:转化为二进制之后，如果有1，则出1。

③`^`：转化为二进制后异或每一位。

④`~`：转化为二进制之后每一位取反

⑤`<<：`往左是\*2.

⑥`>>`:往右是/2

#### <mark style="color:yellow;background-color:green;">9）PHP运算符优先级</mark>

这里直接用手册里面的来作为讲解了，就不细讲了，因为c语言里面也有。

<figure><img src="../.gitbook/assets/image 35.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image 36.png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:red;background-color:blue;">7.if/else/elseif/else if</mark>

这里`if/else`语句和`if/elseif/else`语句也是和

c语言一样的。`elseif`和`else if`其实是相同的使用，没有区别，就是是否有空格。

```php
<?php
 $a=100;
 if($a>50 && $a<100)
 {
    echo 'A';
 }
 else
 {
    echo 'B';
 }
?>

```

<figure><img src="../.gitbook/assets/image 37.png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:red;background-color:blue;">8.While/do while/for/foreach</mark>

### <mark style="color:green;background-color:purple;">1）while/do while</mark>

`while`和`do while`的语法和c语言一样。

```php
<?php
 $a=0;
 while($a<10)
 {
    echo $a++;
    echo '<br \>';
 }
?>

```

<figure><img src="../.gitbook/assets/image 38.png" alt=""><figcaption></figcaption></figure>

```php
<?php
 $a=0;
 do
 {
    echo $a++;
    echo '<br \>';
 }while($a <20);
?>

```

<figure><img src="../.gitbook/assets/image 39.png" alt=""><figcaption></figcaption></figure>

在循环里面，我们可以加入`break`和`continue`这两个去跳出循环。这两个的使用也是和c语言一样，`break`是跳出循环，`continue`是跳出当前循环。一个是全部跳出，一个是跳出当前一个。

我们可以试验一下。

```php
<?php
 $a=0;
 $b=9;

 while($a <20)
 {
    echo 'a='.$a++;
    echo 'b='.$b++;
    echo '<br \>';
    if($b>9)
    {
        break;
    }
   
 }
?>

```

<figure><img src="../.gitbook/assets/image 40.png" alt=""><figcaption><p>BREAK</p></figcaption></figure>

可以看到，`break`直接执行一次之后结束了循环。

```php
<?php
 $a=0;
 $b=9;

 while($a <20)
 {
    echo 'a='.$a++;
    echo 'b='.$b++;
    echo '<br \>';
    if($b>9)
    {
        continue;
    }
   
 }
?>

```

<figure><img src="../.gitbook/assets/image 41.png" alt=""><figcaption><p>CONTINUE</p></figcaption></figure>

可以看到，`continue`执行后只是结束了这一次的循环，但是没有结束掉全部的循环。

### <mark style="color:green;background-color:purple;">2）for</mark>

格式和c语言一样

```php
<?php
 $a=0;
 $b=9;

for($a=2;$a<8;$a++)
{
    echo $a;
    echo '<br \>';
}
?>

```

<figure><img src="../.gitbook/assets/image 42.png" alt=""><figcaption><p>FOR</p></figcaption></figure>

### <mark style="color:green;background-color:purple;">3)foreach</mark>

用于数组和对象当中的循环。

比如我们要循环数组`$programminglanguages`，那么我们可以写成

```php
<?php
 $programminglanguages=['php','java','python'];
 foreach($programminglanguages as $language)
 {
    echo $language.'<br \>';
 }
?>

```

<figure><img src="../.gitbook/assets/image 43.png" alt=""><figcaption><p>FOREACH</p></figcaption></figure>

### <mark style="color:green;background-color:purple;">4）switch/match</mark>

`switch`也是和c语言一样的格式，这里就不多赘述了。

`match`地作用也是和`switch`差不多，但是写法不同。

比如我们用`switch`和`match`实现同一个功能。我们可以写

```php
<?php
 $paymentstatus=1;
 switch($paymentstatus)
 {
    case 1:
        echo 'paid';
        break;
        
    case 2:
    case 3:
        echo 'palyment declined';
        break;
 }
 echo '<br \>';
 match($paymentstatus)
 {
    1 => print 'paid',
    2 => print 'payment declined',
 }

?>

```

<figure><img src="../.gitbook/assets/image 44.png" alt=""><figcaption></figcaption></figure>

注意对于match中间的写法和键值对差不多，需要用,连接。

match和switch最大的区别应该是，当switch不用break去隔断执行的时候，会一直执行下去，但是对于match来说，一次只返回一个结果，也就是说。

***

## <mark style="color:red;background-color:blue;">9.函数</mark>

函数的表达方式和c语言一样，这里就是直接展示一下，不多说了。事实证明在c语言的加持下，学习一门语言真的飞快。

```php
<?php

function sum(int $x,int $y)
{
    return $x+$y;
}

$a=30;
$b=79;
echo sum($a,$b);


?>

```

<figure><img src="../.gitbook/assets/image 45.png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:red;background-color:blue;">10.文件</mark>

`require/require_once/include/include_one`

这四个关键词直接将我们的文件包含进我们现在的php文件中

include和require的区别就是找不到文件时，`include`会导致`warning`，但是`require`会导致`error`，并且会停止脚本。

比如：

```php
<?php


include 'file.php';
echo "hello,world";


?>

```

<figure><img src="../.gitbook/assets/image 46.png" alt=""><figcaption></figcaption></figure>

可以看到，虽然报了错，找不到文件，但是还是执行了hello，world。

我们使用require来看看

```php
<?php


require 'file.php';
echo "hello,world";


?>

```

<figure><img src="../.gitbook/assets/image 47.png" alt=""><figcaption><p>REQUIRE</p></figcaption></figure>

很明显，直接报错。甚至hello，world都没有执行了。

如果我们没有写绝对路径，那么他就会去到和我们现在的php文件的同一目录下去寻找我们所要的文件。

对于require\_one和require的区别，就是我们利用文件是否是同一个，比如，我们先利用了file.php文件进行了操作，如果我们用带有的是once的对他进行引用的话，那么我们下一次利用这个文件的时候，我们是引用的进行了操作的文件，但是如果我们用的是不带once的，那么我们是重新引用了那个文件，我们的操作就没有在下一次保存了。

***

### <mark style="color:red;background-color:blue;">11.PHP封装协议</mark>
