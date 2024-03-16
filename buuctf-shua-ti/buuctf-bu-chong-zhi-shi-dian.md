# 💘 BUUCTF补充知识点

## 1.php网站备份

网站备份有两部分，一部分是数据库内容，另一部分是网站的源码。

常用的备份文件的后缀有



| 常见备份文件后缀                                                                      |
| ----------------------------------------------------------------------------- |
| .git                                                                          |
| .svn                                                                          |
| .swp                                                                          |
| .bak                                                                          |
| .bash\_history                                 .\~                       .bkf |

***

## 2.传参不允许含有字母

当传入的参数不允许含有字母，但是我们执行命令，查找命令这种的都需要传入字母的，这个时候的处理方法就是往变量面前加一个空格。比如$\_GET\['name']，我们在url输入的是?  name=。在？后面有一个空格。这个常用来绕过一个waf。

它的原理是

> 现在的变量叫（空格）name，不是name，但是php解析器在处理的时候会把空格去掉，这样就能够成功了，并且还上传的字母。

***

## 3.联合注入可以自己创建结果

联合注入有个小技巧，就是当联合查询不存在的数据的时候，他会自动创建这个不存在的数据，会创建一个虚拟数据让你找到。所以如果我们有时候不知道一个密码的时候可以自动创建一个密码或者用户名之类的去绕过

<figure><img src="../.gitbook/assets/image (169).png" alt=""><figcaption></figcaption></figure>





***



## <mark style="color:red;">※4.preg\_replace与RCE</mark>

这个是做题说的preg\_replace与RCE漏洞的问题。

我们是按照先知社区的来学习，因为这个完全没有遇到过，第一次看到别人这么说。

### ①案例引入

这例子他也是用的我碰到题目的例子。真是让人sad。但是他说案例简单，我哭死。

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

这里解释一下这个/e模式究竟是什么吧。











































### 参考门：



{% embed url="https://xz.aliyun.com/t/2557?time__1311=n4%2BxnieDqxg7Ki%3DD%2FWT4BIalhxRex7u%2BD" %}
