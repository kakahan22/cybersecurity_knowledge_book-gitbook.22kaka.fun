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

## <mark style="color:green;">（4）数字型注入</mark>

### <mark style="color:yellow;">①加</mark> <mark style="color:yellow;"></mark><mark style="color:yellow;">`'`</mark><mark style="color:yellow;">或者</mark><mark style="color:yellow;">`"`</mark>

```url
http://xxxxxxxx?id=3'
```

这个时候sql语句的语法是错误的，程序根本就不执行，所以会报错。这个时候执行的sql逻辑是

```sql
select * from table where id =3'
```

### <mark style="color:yellow;">②加and 1=1</mark>

```
http://xxxxxxxxxxxx?id =3 and 1=1 
```

如果这个时候执行结果是与原页面没有差异的话，就说明这一步是成功的。因为这个sql语句是正确的，所以没有差异。这个时候执行的sql逻辑是

```sql
select * from table where id=3 and 1=1
```

### <mark style="color:yellow;">③加and 1=2</mark>

```
http://xxxxxxxxxxx?id=3 and 1=2
```

这个时候语句执行是正常的，没有语法错误，但是无法查询出结果，所以返回的数据与原页面存在一定的差异。这个时候执行的sql逻辑是

```sql
select * from table where id=3 and 1=2
```

以上这些步骤说明URL存在数字型注入

***

## <mark style="color:green;">(5)字符型注入</mark>

字符型比数字型稍微复杂一点，他需要考虑到闭合单（双）引号的问题，就需要加一个引号并且注释后面的引号。

### <mark style="color:yellow;">①加'</mark> <mark style="color:yellow;">或者"</mark>

```
http://xxxxxxxxxxxx?username='admin
```

这个时候会报错，因为字符型本身就带有一对引号，所以额外加了一个引号之后其实无法闭合了，就会报错。这个时候sql逻辑语句是

```
select * from table where username= ''admin'
```

### <mark style="color:yellow;">②加 ' and 1=1 #</mark>

```
http://xxxxxxxxx?username=admin'and 1=1 #
```

如果这个时候成功执行并且返回了正确的结果的话，那么就说明字符型注入成功了。因为相当于admin'和前面的’进行了闭合，然后后面的单引号又被注释了，所以其实拼接的语句就是

```sql
select * from table where username='admin' and 1=1 #
```

### <mark style="color:yellow;">③加 ‘ and 1=2#</mark>

```
http://xxxxxxxxxxxx?username=admin' and 1=2#
```

这个时候执行了但是会报错，语法没有错误，但是

































































## 参考门：

{% embed url="https://www.cnblogs.com/1ink/p/15123921.html" %}

{% embed url="https://luckyfuture.top/sqli-summary" %}

{% embed url="https://m.freebuf.com/articles/web/339118.html" %}

