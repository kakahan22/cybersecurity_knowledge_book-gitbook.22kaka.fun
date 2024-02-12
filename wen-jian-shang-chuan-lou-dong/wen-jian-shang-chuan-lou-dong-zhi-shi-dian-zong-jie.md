---
description: 我的理解是web应用允许用户上传一些头像，附件之类的。但是如果web应用上传了一句话木马等webshell，从而控制网站。
---

# 🏍 文件上传漏洞知识点总结

看网上都是分成了前端和后端来分别讲解的，我们也按照他们的思路来一起介绍咯！！！！

我们先简单建立一个前端和后端的概念，简单理解就是前端是你能看到的，就是界面上的东西，所以你也能轻易的修改。后端就是你看不到的。所以有句话说：前端是写给人看的，后端是写给服务器看到。

## <mark style="color:yellow;background-color:green;">1）前端检测</mark>

前端检测是通过一段JavaScript代码校验文件的后缀名，有白名单也有黑名单。如果后缀名不对，就会有弹窗告诉说后缀名不对。此时文件上传的数据包并没有发送到服务端，只是在客户端浏览器使用Javascript对数据包进行检测

### <mark style="color:green;">①绕过姿势一：</mark>

因为前端是用户可以自己可以修改的，所以这个绕过姿势就可以是用户自己修改前端的代码，然后再执行代码。

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:green;">②绕过姿势二：</mark>

用户还可以用bp抓包，将上传文件的后缀修改后再发送，这个时候就已经通过了js的校验。

* 首先把需要上传的文件后缀改成允许上传的文件类型，如jpg、png、gif等，绕过Javascript检测，再抓包，把后缀名改成可执行文件的后缀即可上传成功

### <mark style="color:green;">③绕过姿势三：</mark>

既然使用js代码来校验，那么我们直接删除js代码，把JavaScript给他ban了，然后上传文件，就不会有校验了。我们这里将介绍火狐和谷歌的关闭js的方法。（虽然我直接用的插件）

火狐：

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

谷歌：

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:yellow;background-color:green;">2）后端检测之后缀名检测漏洞</mark>

后端检测中对文件的后缀名进行过滤。一般是黑白名单过滤，如果不符合就上传失败了。

### <mark style="color:orange;background-color:yellow;">①黑名单检测</mark>

黑名单是不希望遇到的。

#### <mark style="color:green;">0x01：姿势一：大小写绕过：</mark>

假如php被ban了，我们可以用pHP这种。

#### <mark style="color:green;">0x02：姿势二：双写绕过：</mark>

这个双写绕过的原理其实是因为后台会把敏感词替换成空格，所以假如php是黑名单的词，我们可以用pphphp来代替。

#### <mark style="color:green;">0x03：姿势三：找漏网之鱼：</mark>

有：`asp:`​ `asa`​ `cer`​ `aspx`​ `jsp:`​ `jspx`​ `jspf`​ `php:`​ `php`​ `php3`​ `php4`​ `php5`​ `phtml`​ `pht`​ `exe:`​ `exee`​

总能找到没被ban的

#### <mark style="color:green;">0x04：姿势四：利用windows命名机制：</mark>

对windows来说，不允许后缀后面带点（.)和空格（ ），所以他会自动将点和空格都删掉。所以我们可以用这个性质来绕过。比如在后缀的后面加上点和空格。

#### <mark style="color:green;">0x05：姿势五：截断上传：</mark>

因为%00表示结束符，所以会把%00后面的所有的字符都删掉。所以如果我们要上传的是flag.php，但是要求的是jpg文件，我们就可以用flag.php%00.jpg，反正后面的jpg能被删掉。

条件：

php版本小于5.3.4,PHP的magic\_quotes\_gpc为OFF状态

#### <mark style="color:green;">0x06：姿势六：利用解析漏洞：</mark>

解析漏洞有.htaccess文件解析漏洞，apache解析漏洞，IIS7.0 | IIS7.5 | Nginx的解析漏洞，IIS6.0解析漏洞，目录解析漏洞，文件解析漏洞。

首先解释一下什么叫解析漏洞：

> 文件解析漏洞主要由于网站管理员操作不当或者 Web 服务器自身的漏洞，导致一些特殊文件被 IIS、apache、nginx 或其他 Web服务器在某种情况下解释成脚本文件执行。

接下来一个一个介绍。这里直接参考狼队的文章了，因为写的很清晰明了。

### <mark style="color:orange;background-color:yellow;">（1）目录解析漏洞</mark>

原理：（/test.asp/1.jpg)

在IIS5.x/6.0 中，在网站下建立文件夹的名字为\*.asp、_.asa、_.cer、\*.cdx 的文件夹，那么其目录内的任何扩展名的文件都会被IIS当做asp文件来解释并执行。例如创建目录 test.asp，那么 /test.asp/1.jpg 将被当做asp文件来执行。假设黑客可以控制上传文件夹路径，就可以不管上传后你的图片改不改名都能拿shell了

形式：

{% embed url="http://%2A%2A%2A%2A%2A%2A%2A%2A%2A%2A%2A/*.asp/*.jpg" %}











































## <mark style="color:red;background-color:red;">参考门：</mark>

{% embed url="https://wiki.tql.ac/Offer/%E7%A7%8B%E6%8B%9B%E7%9F%A5%E8%AF%86%E7%82%B9/%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E5%92%8C%E6%96%87%E4%BB%B6%E8%A7%A3%E6%9E%90%E6%BC%8F%E6%B4%9E" %}

{% embed url="https://wiki.wgpsec.org/knowledge/ctf/uploadfile.html" %}





