---
description: 专门出的关于php的特性比较，后面好像也有java的特性。
---

# 🏀 PHP特性知识点总结

## <mark style="color:purple;background-color:red;">（1）类型转换</mark>

之前提到过的是字符串转为整型。其实php手册里面提到了各种类型的转换。先把他放在这里。

[https://www.php.net/manual/zh/language.types.type-juggling.php#language.types.typecasting](https://www.php.net/manual/zh/language.types.type-juggling.php#language.types.typecasting)

我们按照php手册上的顺序来介绍，只介绍几个比较常用的。

### <mark style="color:green;">①转化为bool</mark>

<figure><img src="../.gitbook/assets/image (51).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:green;">②转化为整型int</mark>

#### 0x01：从bool转换为int

false为0，true为1

#### 0x02：从float转换为int

向下取整（直接舍去小数位）

#### 0x03：从string转换为int

如果 string 是 numeric（数字字符串） 或者前导数字， 则将它解析为相应的 int 值，否则将转换为零（`0`）

> 数字字符串：\
> 这只是一个字符串，其开头类似于数字字符串，后跟任何字符。但是如果含 e 的字符串转换成 int 类型时会被当做科学计数法处理, `123e456` 表示 123 的 456 次方。

#### 0x04：从null转换为int

为0

### <mark style="color:green;">③转换为float</mark>

0x01：从string转换为float

如果 string 是 numeric（数字字符串） 或者前导数字， 则将它解析为相应的 int 值，否则将转换为零（`0`）

0x02：其他类型转换为float

先将其他类型转换为int，再由int转换为float。（而其他类型转换为float，就在上面的②）



***

## <mark style="color:purple;background-color:red;">（2）==与===</mark>

\== 弱类型比较, 仅要求两边变量类型转换后的值相等

\=== 强类型比较, 不仅要求两个变量的值相等, 还要求变量的类型相同

同理 != 是弱类型比较, 而 !== 是强类型比较

***

## <mark style="color:purple;background-color:red;">（3）intval（）函数绕过</mark>

首先我们去php手册了解这是什么东西。

> intval（）
>
> 获取变量的整数值。下面的base是转换的进制，默认是0
>
> ```php
> intval(mixed $value, int $base = 10): int
> ```

intval主要利用有三个。

### <mark style="color:orange;background-color:yellow;">①特性一：返回值</mark>

<figure><img src="../.gitbook/assets/image (10) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

这个重点在非空的数组会返回1。

<figure><img src="../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

这里想提醒一下`['']`这个不是数组为空，这个数组有一个元素，元素为空元素。要是`[]`才是空数组

### <mark style="color:orange;background-color:yellow;">②特性二：base转化的进制</mark>

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

前提是base是0的时候，由value来决定。其他几个情况比较熟悉，0开头是8进制需要好好记忆一下。

<figure><img src="../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:orange;background-color:yellow;">③特性三：弱类型比较下的base转换开始和结束</mark>

这个是说在弱类型比较的前提下，本来在base=0的情况下，要看value的结果来判断，这个判断是<mark style="color:red;">从数字或者正负号开始才做转换，直到遇到非数字，或者字符串的结束符（\0）结束转换</mark>。开始我还理解错了。这句话的意思是比如我们要得到带4476的字符串，应该是4476abc这种。不然以abc4476是被转换为0的。

<figure><img src="../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:orange;background-color:yellow;">④不影响结果的在开头的元素</mark>



<mark style="color:blue;">**空格**</mark>和<mark style="color:blue;">**＋（表示正号）**</mark>



***

## <mark style="color:purple;background-color:red;">（4）preg\_match()函数绕过</mark>

> preg\_match():\
> 执行匹配正则表达式
>
> ```php
> preg_match(
>     string $pattern,
>     string $subject,
>     array &$matches = null,
>     int $flags = 0,
>     int $offset = 0
> ): int|false
> ```

### <mark style="color:orange;background-color:yellow;">①特性一：传递数组</mark>

<figure><img src="../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

上面显示subject得是字符串，也就是说如果是数组，会返回false。

### <mark style="color:orange;background-color:yellow;">②特性二：换行符绕过</mark>

换行符这个大部分都只有一个，但是其实在做题之类的看到了两个。

#### 1）/m

首先我们需要知道这个/m是什么

> 手册上太复杂了，所以我直接用自己的理解来理解吧。就是m代表multiline mode，是多行模式。这个多行模式是什么意思呢。我们在正则表达式里面有说过^代表匹配开头，$代表匹配结尾。但是如果没有/m就是单纯的单行的匹配，如果我们开启了/m就是可以多行的匹配。就是每一行都可以匹配由^开头，以$结尾的。

我们接下来继续举例理解。比如我们有字符串

```php
line1
line2
line3
```

我们如果用正则表达式/^line/m，如果开启了多行，就每一行都可以匹配，就是能匹配到line1，line2，line3，如果我们没开就是只能匹配搭配line1。

但是我们可以截断这个m的作用。<mark style="color:red;">利用%0a</mark>

当出现%0a的时候它会被认为是一个换行符，是什么意思呢，就是从字符串的开头到%0a作为了第一行，从%0a到字符串末尾变成了第二行。就是说我们如果第一行匹配不了，但是第二行匹配成功了也行。

```php
<?php
$a=$_GET['a'];
if(preg_match('/^php$/im',$a))
{
    echo "hacking attempt .....";
}
else
{
    echo "success";
}
```

<figure><img src="../.gitbook/assets/image (8) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### 2）.

.也是截断输入，这个输入的原理是因为。.可以匹配除换行符（\n）之外的任意单个字符。举个例子，我们比如我们有一个字符串/hello\nworld这个字符串，然后我们正则表达式/h.llo/会得到的是hello，这个.匹配到了一个e。但是他不能匹配\n。这个\n我们要用%0a来表示。

我们可以实验一下。

```php
<?php
$a=$_GET['a'];
if(preg_match('/^.*(flag).*$/',$a))
{
    echo "hacking attempt .....";
}
else
{
    echo "success";
}
```

所以我们传入%0aflag之后

<figure><img src="../.gitbook/assets/image (7) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:orange;background-color:yellow;">③回溯绕过</mark>

p神的讲解我放在最后的传送门了。

#### <mark style="color:green;">0X01：</mark>

这里推荐一个工具[https://blog.robertelder.org/regular-expression-visualizer/](https://blog.robertelder.org/regular-expression-visualizer/)

这个工具可以展示正则表达式的详细匹配过程。我们就用这个工具来理解p神的回溯过程也不失为一种高效的办法。

所以回溯绕过就是利用的PHP的PCRE库也是利用的NFA为正则引擎，这样就要回溯找到其他状态。

同样的正则表达式`<?.*`_``[(`;?>].* ,要匹配的字符串是<?php phpinfor();//aaaa``_

自行利用上面的工具进行测试。

* 可以看到当执行到\*的时候他分成了两条路，一条是greedy的，就是把后面所有的都匹配了，还有一条是懒惰的，匹配到后面有(\`;?>就不匹配了。

<figure><img src="../.gitbook/assets/image (12) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* 直接进行lazy的path的就是p神文章里提到的DFA模式，而且我们说的NFA模式，就是先greedy，也就是把整个字符串都先匹配了。like this

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* 这个时候他匹配进入到了failure的步骤，失败了，我们就要去看看能不能走lazy path了，发现到了末尾了，走不了。

<figure><img src="../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* 这个时候我们就尝试一种新的路径。

<figure><img src="../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* 另一种路径当然是lazy 路径，我们就在元素列表里看看能不能找到匹配lazy path的元素，发现不行，因为已经到末尾了，所以这个时候我们就可以弹出栈顶元素然后看看能不能尝试lazy path。发现还是因为a不能匹配(·；？>中的一个，所以我们就继续吐出来。

<figure><img src="../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* 吐着吐着吐到了;发现匹配成功了。我们就继续下一个任意匹配了。又是从greedy开始。这样。

<figure><img src="../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

以上一共回溯了7次。

#### <mark style="color:green;">0X02：</mark>

接下来我们将讲解一个php配置里面的pcre.backtrack\_limit

<figure><img src="../.gitbook/assets/image (7) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

p神的文章里也说了，中文版和英文版不一样，英文版是1000000，我们以1000000为准。我们可以通过下面的代码去查看当前环境的限制值

```php
<?php

$c=ini_get('pcre.backtrack_limit');
var_dump($c);
?>
```

<figure><img src="../.gitbook/assets/image (9) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### <mark style="color:green;">0X03：</mark>

现在我们将试验一下如果超过这个回溯限制的话，会发生什么情况呢。

```php
<?php

$c=preg_match('/<\?.*[(`;?>].*/is','<?php phpinfo()://'.str_repeat('c',10000000));
var_dump($c);
?>
```

<figure><img src="../.gitbook/assets/image (8) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

可以看到返回的是bool值false。正则执行失败。

#### <mark style="color:green;">0X04</mark>

所以这个绕过脚本大致是

```python
import requests

url = ''

data = {}

reponse = requests.post(url,data=data)

print(reponse.text)
```

***

## <mark style="color:purple;background-color:red;">（5）strpos绕过</mark>

<figure><img src="../.gitbook/assets/image (52).png" alt=""><figcaption></figcaption></figure>

需要特别注意的是，顺序是从0开始的。如果找到了就返回位置。如果没有找到就是返回false。

### <mark style="color:orange;background-color:yellow;">①特性一：八进制首位绕过</mark>

如果对八进制（首位是0）遇到了if（!strpos($string,0))进行过滤，我们想让八进制还能成功通过的话，需要在首位想想办法。一般是在前面加<mark style="color:red;">空格和加号</mark>。我们可以进行实验

```php
<?php 
$string=$_GET["string"];
if(!strpos($string,0))
{
    echo "hello,world";
}
else
{
    echo "success";
}
```

<figure><img src="../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure>

并且空格还可以用%20，%0a，%09来代替，加号可以用%2b代替。

### <mark style="color:orange;background-color:yellow;">②特性二：传递数组</mark>

对于如果strpos传递的不是字符串，而是数组的话，返回值为null。

{% hint style="warning" %}
结论对`strrpos() stripos() strripos()` 同理
{% endhint %}

***

## <mark style="color:purple;background-color:red;">（6）is\_numeric()函数绕过</mark>

<figure><img src="../.gitbook/assets/image (55).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:orange;background-color:yellow;">①特性一：科学计数法绕过</mark>

我们知道科学计数法是含有e的数字字符串，对于is\_numeric来说，他是能识别科学计数法的，并且能返回true。试验一下

```php

<?php 
$string= 11e11;
if(is_numeric($string))
{
    echo "hello,world";
}
else
{
    echo "failure";
}
```

<figure><img src="../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

所以，对于某些字符串，我们可以尝试利用 base64 + bin2hex 找到一些只含 e 和数字的 payload

### <mark style="color:orange;background-color:yellow;">②特性二：开头加特殊字符</mark>

在数字前面加上/n，/t等这种特殊字符仍然可以返回true，但是放在数字后面就不行了。

```php
<?php 
$string="\t123" ;
if(is_numeric($string))
{
    echo "hello,world";
}
else
{
    echo "failure";
}
?>

```

<figure><img src="../.gitbook/assets/image (57).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:purple;background-color:red;">（7）in\_array()函数</mark>

<figure><img src="../.gitbook/assets/image (58).png" alt=""><figcaption></figcaption></figure>

如果找到了返回true，没找到返回false。

### <mark style="color:orange;background-color:yellow;">①特性一：自动转换</mark>

函数在作用时会将needle的值自动转化为和array一个类型。

其实这个实验在我的环境下失败了，这结论也不在成立。后面我看了手册，发现了还是版本问题。

<figure><img src="../.gitbook/assets/image (59).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:purple;background-color:red;">（8）trim（）函数</mark>

<figure><img src="../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure>

返回值是过滤后的字符串。

### <mark style="color:orange;background-color:yellow;">①特性一：不过滤/f</mark>

我们可以看到，上面写了去除\t,\n,\r,\0,\v但是他没有过滤<mark style="color:red;">\f(换页符），他的url编码是%0c36</mark>

***

## <mark style="color:purple;background-color:red;">（9）md5（）和sha1（）</mark>

<figure><img src="../.gitbook/assets/image (61).png" alt=""><figcaption></figcaption></figure>

返回值sha1的散列值的字符串形式。

<figure><img src="../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

以 32 字符的十六进制数形式返回散列值。

{% hint style="info" %}
两函数的性质啥的都是一样的。所以我们直接一起说了，有些情况只列举了一个，但是对两个函数都是一样的。
{% endhint %}

### <mark style="color:orange;background-color:yellow;">①特性一：比较缺陷（或者说0e漏洞）</mark>

`PHP`在处理哈希字符串时，通过`!=`或`==`来对哈希值进行比较，它把每一个以`0e`开头的哈希值都解释为`0`，所以如果两个不同的密码经过哈希以后，其哈希值都是以`0e`开头的，那么`PHP`将会认为他们相同，都是`0。这个通常是对于科学计数法的时候会遇到0e漏洞。`

可以实验一下。

```php
<?php 
$a="0e123";
$b="0e456";
if($a==$b)
{
    echo "equal";
}
else
{
    echo "wrong";
}

?>
```

<figure><img src="../.gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

可以看到在php解释其中，他们会认为0e开头的都相等。

所以我们如果如果我们要绕过if(md5($a)==md5($b))这个条件的话。我们可以选择一些md5编码后都为0e的a，b字符串。

所以这里介绍一些。

* [ ] _**md5加密后以0e开头的字符串**_

<pre class="language-php"><code class="lang-php">1.   QNKCDZO             ----------0e830400451993494058024219903391
<strong>2.   s878926199a         ----------0e545993274517709034328855841020
</strong>3.   s155964671a         ----------0e342768416822451524974117254469
4.   s214587387a         ----------0e848240448830537924465865611904
5.   s214587387a         ----------0e848240448830537924465865611904
6.   s878926199a         ----------0e545993274517709034328855841020
7.   s1091221200a        ----------0e940624217856561557816327384675
</code></pre>

* [ ] _**sha1加密后以0e开头的字符串**_

<pre class="language-php"><code class="lang-php">1.   aaroZmOk            ----------0e66507019969427134894567494305185566735
2.   aaK1STfY            ----------0e76658526655756207688271159624026011393
3.   aaO8zKZF            ----------0e89257456677279068558073954252716165668
4.   aa3OFF9m            ----------0e36977786278517984959260394024281014729
5.   0e1290633704        ----------0e19985187802402577070739524195726831799
<strong>6.   10932435112         ----------0e07766915004133176347055865026311692244
</strong>
</code></pre>

{% hint style="info" %}
注意这个特性是在**弱类型的条件**下。
{% endhint %}

### <mark style="color:orange;background-color:yellow;">②特性二：数组绕过</mark>

在强类型的条件下，我们特性一就失效了，这时候我们可以用数组绕过。我们知道md5和sha1是对字符串起的作用，如果我们传入的是数组：

* `md5()`函数获取不到数组的值，默认数组为0
* `sha1()`函数无法处理数组类型，将报错并返回false

所以我们可以对于if(md5($a)===md5($b))，可以用<mark style="color:red;">**`取a，b为数组`**</mark>来绕过。

{% hint style="info" %}
这个对于强类型和弱类型比较都可以成功。
{% endhint %}

{% hint style="warning" %}
这个应该有版本要求，我是8.3的版本实验的时候发现全部都是报错，无法执行我最后预期的结果。
{% endhint %}

***

## <mark style="color:purple;background-color:red;">（10）路径穿越</mark>

### <mark style="color:orange;background-color:yellow;">①特性一：利用绝对路径和相对路径</mark>

路径绕过就是通过绝对路径或者相对路径去绕过正则对文件名的检测。比如`preg_match('/flag.php/', $str)`

（关于路径的知识忘记的，可以去看我们当时在讲file：//协议中讲过的。这里放一个传送门  [#id-1file](../rce-yuan-cheng-dai-ma-zhi-hang/代码执行知识点总结.md#id-1file "mention")   )

我们可以写

```url
./flag.php
/var/www/html/flag.php
./ctfshow/../flag.php
```

### <mark style="color:orange;background-color:yellow;">②特性二：利用linux下的软链接绕过</mark>



我们首先介绍一下什么叫软链接。

> 软链接：软链接文件有类似于 Windows 的快捷方式。它实际上是一个特殊的文件。在符号连接中，文件实际上是一个文本文件，其中包含的有另一文件的位置信息。其实我的理解是他很像c语言的指针的作用，软链接是一个指向某个特定文件的指针，指针的数据块内包含的是文件的位置信息。如果文件被删除了，但是指针还存在，只是指向的位置是个无效的罢了。
>
>

其实这个博主的解答这个地方我没有看懂，有看懂的小伙伴可以解答一下

```url
/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/p
roc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/pro
c/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/
self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/se
lf/root/proc/self/root/var/www/html/flag.php
```

***

## <mark style="color:purple;background-color:red;">（11）运算优先级</mark>

没啥好讲的，直接贴图

<figure><img src="../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:purple;background-color:red;">（12）三目运算符</mark>

构造不带分号的payload需要用到

```php
return 1?phpinfo():1;
```

这样就永远都会执行phpinfo（），这个phpinfo可以替换为其他的代码。

***

## <mark style="color:purple;background-color:red;">（13）函数与数字运算</mark>

在php中，函数和数字一起运算，函数能被正常执行。比如

```php
1+phpinfo()+1;
```

phpinfo（）能被正常执行。以下符号都能够正常执行。

```
+ - * / && ||
```

***



























































## <mark style="color:red;">参考门</mark>

{% embed url="https://www.anquanke.com/post/id/231507#h2-3" %}

{% embed url="https://www.cnblogs.com/20175211lyz/p/12198258.html" %}

{% embed url="https://www.leavesongs.com/PENETRATION/use-pcre-backtrack-limit-to-bypass-restrict.html" %}

{% embed url="https://exp10it.io/2022/08/php-%E7%89%B9%E6%80%A7%E6%80%BB%E7%BB%93%E7%AC%94%E8%AE%B0/#%E7%B1%BB%E5%9E%8B%E8%BD%AC%E6%8D%A2" %}
