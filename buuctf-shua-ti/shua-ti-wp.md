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





