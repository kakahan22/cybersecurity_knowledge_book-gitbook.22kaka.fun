---
description: 主要是面向对象的基础，在序列化知识点就需要用这个思想。
---

# ☎️ PHP语法进阶

## <mark style="color:orange;">1.面向对象关键字：</mark>

### ①类（class）：

定义面向对象主体的最外层结构，用来包裹主体的数据和功能（函数）。类是一类具有共性事务的代表，代表的是事务的共性。类里面是类成员（member）

```php
class 类名{

}
```

### ②对象（object）：

是某类事务的具体代表，也是实际数据和功能操作的具体单元，也被称之为实例（instance）

```php
$object=new 类名();
```

### ③实例化（new）：

从一个抽象的概念得到一个符合抽象概念的具体实例的过程

```php
new 类名;
new 类名(); #使用较多
```

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

所以上述中首先定义了一个类，然后类实例化产生了对象。var\_dump打印出来的信息格式是：

`对象（类名）【对象编号】 具体成员信息`

### ④类成员（member）：

指类class结构中的所有内容，直接属于大括号的内容，二级括号就不属于了。属性和方法需要用到访问限制修饰符。类成员里有三种

#### （1）方法（method）：

本质是在类class结构中 创建的函数，也称之为成员方法或成员函数

#### （2）属性（property）：

本质是在类class结构中创建的变量，也称之为成员变量

#### （3）类常量（const）：

本质是在类class结构中创建的常量。

```php
class 类名{
    #类常量（可以多个）
    const 常量名=值;
    #属性
    public $属性名[=值]; #可以赋值也可以不赋值，只声明
    #方法（可以多个）
    [public]function 方法名([形参列表])
    #方法体（返回值）
    
    }
```

***



## <mark style="color:orange;">2.类成员的访问</mark>

对于类成员的访问，有对象访问(->)和类访问（::)。属性和方法都属于对象访问，类常量属于类访问。

### ①对象访问：



```php
$object=new 类名();
#属性访问
$object->属性名; #此时不带属性本身的$（前面保存对象的变量带$符号了)
#方法访问
$object->方法名([实参列表]);
```

我们可以通过对对象的访问对类进行各种修改接下来就有一个例子。

```php

<?php 

class Buyer{
    public $name;
    public $money=0;
    function display(){
        echo __CLASS__;
    }
    const BIG_NAME='BUYER';
}

$b=new Buyer();
#查找
echo $b->money;
#修改
$b->money=1000;
#删除
unset($b->name);
#增加
$b->age=20;
?>

```

<figure><img src="../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:orange;">3.访问修饰限定符</mark>

用在属性和方法前的修饰关键字，是用来控制属性或者方法的访问位置。属性必须带有访问修饰限定符，方法可以没有访问修饰限定符（默认public）

### ①公有（public）：

类内和类外都可以访问

### ②受保护（protected）：

只允许在相关类内部访问

### ③私有（private）：

只允许在定义类内部访问

***



## <mark style="color:orange;">4.类内部对象</mark>

$this，方法内部内置的一个对象，对自动指向用来调用方法的对象。$this存在于方法内部（仅限内部使用），所以相当于在类的结构内部。

{% hint style="info" %}
可以访问任意房屋内修饰限定符修饰的成员（私有的也可以）
{% endhint %}

最开始的时候其实还是没有懂$this存在的意义直到后来发现，其实不能因为包了一层类，函数就不是函数了，也就是说，函数中引用的变量还得是函数里面定义的，不然就会报错。为了解决这个问题，让函数可以访问类里面的属性，我们引入了$this。

```php

<?php 

class Saler{
    public $count =100;
    protected $discount=0.8;
    private $money=100;

    public function getAll(){

        echo $this->count,$this->discount,$this->money;
    }
}

$s=new Saler();
$s->getAll();
?>

```

<figure><img src="../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

除此之外我们呢还可以用global（全局变量来访问）。

我们可以将对象的名字设置成全局变量，然后就可以在函数内部进行访问。

```php

<?php 

class Saler{
    public $count =100;
    protected $discount=0.8;
    private $money=100;

    public function getAll(){
        global $s;
        echo $s->count,$s->discount,$s->money;
    }
}

$s=new Saler();
$s->getAll();
?>

```

<figure><img src="../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:orange;">5.构造方法</mark>

构造方法：\_\_construct()，是一种类结构特有的特殊方法，开发人员在定义的时候只要写一遍，走了构造方法发的的类在实例化对象之后，对象就会自动调用。

> 魔术方法：是自动被触发，不需要手动调用

但是他的本质还是方法。

```php

<?php 

class saler{
    public function __construct(){
        echo __CLASS__;
    }
}
new saler();
?>

```

<figure><img src="../.gitbook/assets/image (99).png" alt=""><figcaption></figcaption></figure>

### ①构造方法的意义：

构造方法是对象实例化的时候用来初始化对象的资源的，所以通常是用来初始化对象的属性或者其他资源的初始化。

```php

class saler{
    public $count;
    public $money;

    #构造方法：初始化属性
    public function __construct(){
        $this->count=100;
        $this->money=100;
    }
}
```

一旦构造方法拥有了形参，那么对象在调用该方法的时候就需要传入对应的实参，而构造方法是自动调用的，所以需要在实例化对象的时候使用new类名（构造方法对应的实参列表来表现）

```php

<?php 

class saler{
    public $count;
    public $money;

    #构造方法：初始化属性
    public function __construct($count,$money){
        $this->count=$count;
        $this->money=$money;
        echo __CLASS__;
    }
}

$s1=new saler(100,100);
var_dump($s1);
?>

```

<figure><img src="../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:orange;">6.析构方法</mark>

析构方法：\_\_destruct()，与构造方法一样，对象在销毁时会自动调用。

析构方法是用来对象销毁时主动释放资源的。其实php脚本执行结束会释放所有资源，所以一般较少使用析构方法。

```php

<?php 

class saler{
    public function __destruct(){
        echo __FUNCTION__;
    }
}

$s1=new saler();
var_dump($s1);
?>

```

<figure><img src="../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

























