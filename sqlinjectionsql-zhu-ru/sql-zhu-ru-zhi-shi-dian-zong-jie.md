---
description: 终于开这个坑了，因为实在是，sql注入不知道为什么总是在我的死点上面，真的就是完全不知道为啥。
---

# 🐮 SQL注入知识点总结

一些sql注入的基本知识还是得重新说说的，虽然现在已经理解了，但是为来者铺路。



sql注入产生的原理就不细说了，就是输入有害，可以拼接语句这种。



## <mark style="color:green;">（1）SQL的系统库</mark>

### <mark style="color:yellow;">①information\_schema</mark>

mysql里面自带了一个information\_schema库，我们利用其他系统的mysql的时候，不知道他具体的库的信息，但是我们从这个系统库里面知道一些玄机

<figure><img src="../.gitbook/assets/image (123).png" alt=""><figcaption></figcaption></figure>

我们可以看看这个库里面的一些表。

<figure><img src="../.gitbook/assets/image (124).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (125).png" alt=""><figcaption></figcaption></figure>

这里面的表也是自带的，我们将从这些表里面获取到信息。所以我们将重点介绍几个自带信息的表。

### <mark style="color:yellow;">②SCHEMATA</mark>

首先查看一下这个表里面的所有信息。

<figure><img src="../.gitbook/assets/image (126).png" alt=""><figcaption></figcaption></figure>

我们可以看到这个表里面的SCHEMA\_NAME是数据库里面所有库的库名。所以如果我们想查看库名，可以用

```sql
SELECT SCHEMA_NAME FROM SCHEMATA;
```

<figure><img src="../.gitbook/assets/image (127).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:yellow;">③TABLES</mark>

同样查看tables表的全部内容。

<figure><img src="../.gitbook/assets/image (128).png" alt=""><figcaption></figcaption></figure>

我们可以看到这里有表名，库名都有。所以我们可以从这个表里面查询到表名和库名。

这里写查库名的语句就是

```sql
SELECT TABLE_SCHEMA FROM TABLES;
```

查表名就是

```sql
SELECT TABLE_NAME FROM TABLES;
```

<figure><img src="../.gitbook/assets/image (129).png" alt=""><figcaption></figcaption></figure>

### <mark style="color:yellow;">③COLUMNS</mark>

同样查看表先

<figure><img src="../.gitbook/assets/image (130).png" alt=""><figcaption></figcaption></figure>

发现有库名，表名，列名全部都有。

那我们就直接写他们分别的查询语句。

查库名

```sql
SELECT TABLE_SCHEMA FROM COLUMNS;
```

<figure><img src="../.gitbook/assets/image (131).png" alt=""><figcaption></figcaption></figure>

查表名

```sql
SELECT TABLE_NAME FROM COLUMNS;
```

<figure><img src="../.gitbook/assets/image (132).png" alt=""><figcaption></figcaption></figure>

查列名

```sql
SELECT COLUMN_NAME FROM COLUMNS;
```

<figure><img src="../.gitbook/assets/image (133).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:green;">（2）SQL注释符</mark>

这里SQL的注释符还是要仔细说说的。他一共有三种注释方法。

### <mark style="color:yellow;">①</mark> <mark style="color:yellow;"></mark><mark style="color:yellow;">`--`</mark>&#x20;

`--` （后面有一个空格）表示注释，当然也可以把空格urlencode，最后就变成了`--%20`&#x20;

还有一些写成`--+`也可以

### <mark style="color:yellow;">②</mark><mark style="color:yellow;">`#`</mark>

就是一个单纯的`#`，不需要空格什么的，有些时候将他urlecode也是可以的，就直接一个`%23`

### <mark style="color:yellow;">③</mark> <mark style="color:yellow;"></mark><mark style="color:yellow;">`/**/`</mark>

就是语言一般用的注释符`/**/`

***

## <mark style="color:green;">（3）常用函数</mark>

这些函数主要是在注入的时候后面会用到的。

### <mark style="color:yellow;">①系统库系统版本</mark>

```sql
VERSION()
@@VERSION
@@GLOBAL.VERSION
```

### <mark style="color:yellow;">②系统库当前使用用户</mark>

```sql
USER()
CURRENT_USER()
SYSTEM_USER()
SESSION_USER()
```

### <mark style="color:yellow;">③当前使用的数据库</mark>

```sql
DATABASE()
SCHEMA()
```

### <mark style="color:yellow;">④GROUP\_CONCAT()</mark>

将group by产生的同一个分组中的值连接起来，返回一个字符串结果。简单来说就是多行数据变成一行输出。

格式是：

```sql
GROUP_CONCAT(str1,str2,…)
```

***

## <mark style="color:green;">（4）寻找注入点</mark>

### <mark style="color:yellow;">①</mark><mark style="color:yellow;">`'`</mark><mark style="color:yellow;">或者</mark><mark style="color:yellow;">`"`</mark>

一般在参数后添加单引号，或者双引号，如果报错或者长度变化，那么就可能存在sql注入。

***



















































































## 参考门：

{% embed url="https://www.cnblogs.com/1ink/p/15123921.html" %}

{% embed url="https://luckyfuture.top/sqli-summary" %}

{% embed url="https://m.freebuf.com/articles/web/339118.html" %}

