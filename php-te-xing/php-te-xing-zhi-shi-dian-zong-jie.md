---
description: 先说什么叫弱类型比较吧。就是==和！=
---

# 🏀 PHP特性知识点总结

## <mark style="color:purple;background-color:red;">（1）intval（）函数绕过</mark>

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

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

这个重点在非空的数组会返回1。

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

这里想提醒一下`['']`这个不是数组为空，这个数组有一个元素，元素为空元素。要是`[]`才是空数组

### <mark style="color:orange;background-color:yellow;">②特性二：base转化的进制</mark>

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

前提是base是0的时候，由value来决定。其他几个情况比较熟悉，0开头是8进制需要好好记忆一下。

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>



### <mark style="color:orange;background-color:yellow;">③特性三：弱类型比较下的base转换开始和结束</mark>

这个是说在弱类型比较的前提下，本来在base=0的情况下，要看value的结果来判断，这个判断是<mark style="color:red;">从数字或者正负号开始才做转换，直到遇到非数字，或者字符串的结束符（\0）结束转换</mark>。

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:purple;background-color:red;">（2）preg\_match()函数绕过</mark>

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

<figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

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

当出现%0a的时候它会被认为是一个换行符，是什么意思呢，就是从字符串的开头到%0a作为了第一行，从%0a到字符串末尾变成了第二行。这个就打破了/m。这个时候就只能匹配第一行，就是从字符串的开头到%0a。

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

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

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

<figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:orange;background-color:yellow;">③回溯绕过</mark>



p神的讲解我放在最后的传送门了。

































































## <mark style="color:red;">参考门</mark>

{% embed url="https://www.anquanke.com/post/id/231507#h2-3" %}

{% embed url="https://www.cnblogs.com/20175211lyz/p/12198258.html" %}

{% embed url="https://www.leavesongs.com/PENETRATION/use-pcre-backtrack-limit-to-bypass-restrict.html" %}



