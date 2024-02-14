---
description: >-
  配置好环境，其实我是看不懂一点的，觉得真特么的复杂什么鬼玩意啊，无所谓，因为我会看网课，这里就简单的介绍一点java的语法。虽然人家的视频只有几个小时，但是我估计我得花double的时间去学，这里放一个他的链接。他讲的超级👌。
---

# 📱 JAVA语法

{% embed url="https://youtu.be/eIrMbAQSU34?si=ZlgWKzFPLO4M9KQs" %}

## （1）组成

### ①functions：函数

最小的组成部分，就是我们c语言学的函数一个概念。

```java
ReturnType Name(){
...
}
```

{% hint style="info" %}
这里有一个特别需要区别的是，在c语言中我们通常将括号中的左括号另作一行，但是在java中我们不这么做，我们是将它放在定义函数一行上，不新起一行
{% endhint %}

当然在java中也有main（主函数）的概念，他是我们程序的入口，

```java
void main(){
...
}
```

### ②class：类

类是a container for related functions，就是说，类是用来装相关联的函数的。就像超市里面，我们有各种产品，但是产品分为水果类，蔬菜类这种不同的类型。

这个时候在class中的function我们称为method（方法）。此外，我们一般在class前和method前使用（access modify）访问修饰符，比如private和public这种。

<pre class="language-java"><code class="lang-java"><strong>public class Main() {
</strong>	public void main() {
		...
	}
}

</code></pre>

{% hint style="info" %}
在一个java程序中，至少有一个主类。
{% endhint %}

#### ps：命名规则：

我们在这里可以看到，我们类的main的首字母大写了。这是因为我们为了区分类和函数，我们会将类的每个单词的首字母大写。

Classes：(所有单词首字母都大写）

```
PascalNamingConvention
```

Methods：（驼峰命名法，除了第一个首字母小写，其他单词首字母大写）

```
camelNamingconvention
```























