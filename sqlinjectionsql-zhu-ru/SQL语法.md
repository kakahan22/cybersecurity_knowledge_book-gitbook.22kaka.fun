---
description: 因为sql注入是在sql语法的一些基础上的，所以我们必须知道sql的一些基本语法。
---

# 🐶 SQL语法

本人使用的是kali下的mysql环境

## <mark style="color:blue;background-color:green;">1.打开mysql</mark>

**step1**：首先输入指令以打开mysql

```sql
service mysql start
```

<figure><img src="../.gitbook/assets/image (12) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

step2：输入用户名和密码以进入mysql

```sql
mysql -u root -p
```

输入之后，会出现提示要你输入密码，你就输入你的mysql密码。

<figure><img src="../.gitbook/assets/image 1 (4).png" alt=""><figcaption></figcaption></figure>

这个时候你就成功打开了mysql。

***

## <mark style="color:blue;background-color:blue;">2.relationships of databases，tables and columns</mark>

<figure><img src="../.gitbook/assets/image 2 (3).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:blue;background-color:green;">3.对库进行操作</mark>

step1：查看有哪些库

```sql
show databases;
```

<figure><img src="../.gitbook/assets/image 3 (2).png" alt=""><figcaption></figcaption></figure>

step2：使用某个数据库,这里使用的是information\_schema,如果要换成其他的，就改一下名字就行。

```sql
use information_schema（table name）;   
```

<figure><img src="../.gitbook/assets/image 4 (2).png" alt=""><figcaption></figcaption></figure>

现在可以看到，前面变成了information\_schema,说明我们已经成功地进入到了这个表里面的。

***

## <mark style="color:blue;background-color:green;">4.对表操作</mark>

step1：查看有哪些表。

```sql
show tables;
```

<figure><img src="../.gitbook/assets/image 5 (2).png" alt=""><figcaption></figcaption></figure>

step2：从表中查询列和列对应的信息。（\*号表示所有的）

我们要用的SELECT FROM 语句去查询。这里查询了ALL\_PLUGINS表的所有内容。

```sql
SELECT *（column name） FROM ALL_PLUGINS（table name）;
```

<figure><img src="../.gitbook/assets/image 6 (2).png" alt=""><figcaption></figcaption></figure>

step3：现在可以看到，这个表的信息有点多，我们可以进行筛选，比如说，我们要筛选出PLUGIN\_VERSION为1.0的信息。我们需要用到WHERE子句去筛选.

```sql
SELECT * FROM ALL_PLUGINS WHERE PLUGIN_VERSION=1.0(筛选条件）;
```

<figure><img src="../.gitbook/assets/image 7 (2).png" alt=""><figcaption></figcaption></figure>

step4:现在的结果是无序的，我们想要让他像字典一样排序，我们可以用ORDER BY子句，比如我们想根据PLUGIN\_TYPE\_VERSION对上述的表进行排序。（能看到这里是根据ASCII码进行排序）

```sql
SELECT * FROM ALL_PLUGINS WHERE PLUGIN_VERSION=1.0 ORDER BY PLUGIN_TYPE_VERSION（排序条件）;
```

<figure><img src="../.gitbook/assets/image 8 (3).png" alt=""><figcaption></figcaption></figure>

step5：如果你想让where和order by的条件都暂时没有，你可以用到注释符--。

```sql
SELECT * FROM ALL_PLUGINS -- WHERE PLUGIN_VERSION=1.0 ORDER BY PLUGIN_TYPE_VERSION;
```

注意，注释的时候会把后面所有的语句都注释掉，所以分号也会注释掉，所以这个语句现在是没有结束符分号的，我们需要再加入一个；去结束。

<figure><img src="../.gitbook/assets/image 9 (2).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image 10 (3).png" alt=""><figcaption></figcaption></figure>

现在才成功，直接在句子后面加分号，是没有用的，一样会被注释掉，不信我们可以试验一下。

<figure><img src="../.gitbook/assets/image 11 (3).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:blue;background-color:green;">5.SELECT详细运用</mark>

1）.上述\*的使用

2）.特定的列。如果我们需要某些特定的列的结果，我们也可以用select语句。比如我们只需要PLUGIN\_VERSION,PLUGIN\_AUTH\_VERSION这两个列的内容。

```sql
SELECT PLUGIN_VERSION,PLUGIN_AUTH_VERSION（column names） FROM ALL_PLUGINS;
```

<figure><img src="../.gitbook/assets/image 12 (4).png" alt=""><figcaption></figcaption></figure>

3）对列的内容进行计算。

比如，我们想让PLUGIN\_VERSION这一列的结果都加上10的结果也输出来。我们可以用

```sql
SELECT PLUGIN_VERSION,PLUGIN_AUTH_VERSION,PLUGIN_VERSION+10 FROM ALL_PLUGINS;
```

<figure><img src="../.gitbook/assets/image 13 (4).png" alt=""><figcaption></figcaption></figure>

可以看到第三列输出了我们想要的这个结果（**乘法，除法，加法，减法，取模**都可以用）。

4）取别名，可以看到刚刚我们对PLUGIN\_VERSION这一列的结果都加上10，我们可以把这一列取一个名字。这就需要用到AS了，比如我们把他叫做PLUGIN\_VERSIONELSE。

```sql
SELECT PLUGIN_VERSION,PLUGIN_AUTH_VERSION,PLUGIN_VERSION+10 AS PLUGIN_VERSIONELSE FROM ALL_PLUGINS;
```

<figure><img src="../.gitbook/assets/image 14 (3).png" alt=""><figcaption></figcaption></figure>

注意，如果你想在名字里面加入空格，你需要用''或者”“将他引起来，不然就要用下划线代表空格。

***

## <mark style="color:blue;background-color:green;">6.多个条件连接符OR ,AND NOT</mark>

1.AND:同时都要满足。

2.OR：两者满足一个就可以输出。

3.NOT：否定条件，就是除了后面的条件以外的所有。

NOT>AND>OR

***

## <mark style="color:blue;background-color:green;">7.IN</mark>

作用和OR等价。

比如说我们要输出PLUGIN\_TYPE\_VERSION=2.2和PLUGIN\_TYPE\_VERSION=2.0的一些数据，我们用OR是这样写的。

```sql
SELECT PLUGIN_TYPE_VERSION from ALL_PLUGINS WHERE PLUGIN_TYPE_VERSION=2.2 OR PLUGIN_TYPE_VERSION=2.0;

```

<figure><img src="../.gitbook/assets/image 15 (4).png" alt=""><figcaption></figcaption></figure>

我们换成IN就是

```sql
SELECT PLUGIN_TYPE_VERSION from ALL_PLUGINS WHERE PLUGIN_TYPE_VERSION IN (2.0,2.2);
```

<figure><img src="../.gitbook/assets/image 16 (4).png" alt=""><figcaption></figcaption></figure>

输出的结果完全相等，和括号里面的结果的顺序没有关系。

前面也可以加NOT去否定这个条件。

***

## <mark style="color:blue;background-color:green;">8.BETWEEN</mark>

一般和AND一起使用，表示在某某和某某之间。

比如我们要查询PLUGIN\_VERSION在2到100000之间的结果

```sql
SELECT PLUGIN_VERSION FROM ALL_PLUGINS WHERE PLUGIN_VERSION BETWEEN 2 AND 1000000;
```

<figure><img src="../.gitbook/assets/image 17 (3).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:blue;background-color:green;">9.LIKE</mark>

顾名思义，就是查询像什么样的，比如我们想要查询b开头的单词的某个结果，可以用'b%'，**这个b是大写和小写不重要**。如果我们要查询2开头的PLUGIN\_VERSION。

```sql
SELECT PLUGIN_VERSION FROM ALL_PLUGINS WHERE PLUGIN_VERSION LIKE '2%';
```

<figure><img src="../.gitbook/assets/image 18 (3).png" alt=""><figcaption></figcaption></figure>

%可以放在任何地方，可以放在前面，中间，后面都可以，如果要表示b在中间的任何的单词，可以表示为'%b%'

如果我们想表示固定的某个位数是某个字母，我们可以使用来表示，一个下划线表示一位，比如b就表示第二位为b的单词。比如如下表示第三位为2的结果。（第几位，前面就有多少个\_)

```sql
SELECT PLUGIN_VERSION FROM ALL_PLUGINS WHERE PLUGIN_VERSION LIKE '__2%';
```

<figure><img src="../.gitbook/assets/image 19 (3).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:blue;background-color:green;">10.REGEXP（正则表达式）</mark>

1）.^表示开头，$表示结尾。

比如我们想要以2开头可以写成

```sql
SELECT PLUGIN_VERSION FROM ALL_PLUGINS WHERE PLUGIN_VERSION REGEXP '^2';
```

<figure><img src="../.gitbook/assets/image 20 (3).png" alt=""><figcaption></figcaption></figure>

以2结尾为

```sql
SELECT PLUGIN_VERSION FROM ALL_PLUGINS WHERE PLUGIN_VERSION REGEXP '2$';
```

<figure><img src="../.gitbook/assets/image 21 (4).png" alt=""><figcaption></figcaption></figure>

含有2

```sql
SELECT PLUGIN_VERSION FROM ALL_PLUGINS WHERE PLUGIN_VERSION REGEXP '2';
```

<figure><img src="../.gitbook/assets/image 22 (2).png" alt=""><figcaption></figcaption></figure>

2） |表示或者，比如以2开头或者以2结尾。

```sql
SELECT PLUGIN_VERSION FROM ALL_PLUGINS WHERE PLUGIN_VERSION REGEXP '^2|2$';
```

<figure><img src="../.gitbook/assets/image 23 (2).png" alt=""><figcaption></figcaption></figure>

3）\[]表示匹配。比如我们要1.2或者2.2那么我们只需要前面的第一位是1或者2与.2进行匹配就行。

```sql
SELECT PLUGIN_VERSION FROM ALL_PLUGINS WHERE PLUGIN_VERSION REGEXP '[12].2';
```

<figure><img src="../.gitbook/assets/image 24 (2).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:blue;background-color:green;">11.ORDER BY</mark>

***

DESC降序，放在内容之后。

## <mark style="color:blue;background-color:green;">12.LIMIT</mark>

如果我们只要前几行，我们可以用 LIMIT 行数。

比如我们要前三行。

```sql
SELECT PLUGIN_VERSION FROM ALL_PLUGINS LIMIT 3;
```

<figure><img src="../.gitbook/assets/image 25 (2).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:blue;background-color:green;">13.INNER JOIN</mark>

1\)同一个数据库里的不同表

将两个表的某些列拼在一起，可以跨表进行数据操作。

比如我们需要让users表和stagers这两个表里面的id相等的行的信息输出。

```sql
SELECT * FROM users JOIN stagers ON stagers.id=users.id;
```

<figure><img src="../.gitbook/assets/image 26 (2).png" alt=""><figcaption></figcaption></figure>

2）不同数据库的不同表

将不同数据库的表连接在一起，可以跨数据库进行操作，只要指明了特定的数据库下的表就可以。

```sql
 SELECT * from TABLES oi JOIN empire.user_id_seq  q ON oi.DATA_FREE =q.cycle_count;
```

<figure><img src="../.gitbook/assets/image 27 (2).png" alt=""><figcaption></figcaption></figure>

3）同一个数据库的同一个表（SELF JOIN）

操作一样，只不过要给自己的两个相同的表取一个别名。

比如我们要将user表的Update\_priv和Create\_priv作为条件连接，只要将第一个命名为a，第二个命名为b就行。

```sql
SELECT a.Update_priv,b.Create_priv FROM user a JOIN user b ON a.Update_priv=b.Create_priv;
```

<figure><img src="../.gitbook/assets/image 28 (2).png" alt=""><figcaption></figcaption></figure>

4）多个表连接

将多个表连接，就是在后面添加JOIN ON语句

比如我们这里要将3个自己的表连接。

```sql
SELECT a.Update_priv,b.Create_priv,c.Drop_priv FROM user a JOIN user b ON a.Update_priv=b.Create_priv JOIN user c ON a.Update_priv=c.Drop_priv;
```

<figure><img src="../.gitbook/assets/image 29 (2).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:blue;background-color:green;">14.OUTER JOIN</mark>

1）左连接，右连接。

作用：当单纯使用JOIN ON语句时，只会显示ON后面条件成立的数据，不成立的数据将显示不出来，如果我们想让他显示出来，并且表示为NULL，就需要用LEFT JOIN ON语句（左连接）。

```sql
SELECT * FROM users LEFT JOIN stagers ON users.username=stagers.name;
```

<figure><img src="../.gitbook/assets/image 30 (1).png" alt=""><figcaption></figcaption></figure>

可以看到左连接会显示users的完整的表。

我们可以试试右连接。

```sql
SELECT * FROM users RIGHT JOIN stagers ON users.username=stagers.name;

```

<figure><img src="../.gitbook/assets/image 31 (1).png" alt=""><figcaption></figcaption></figure>

可以看到是按照了stagers表的结果输出的。

如果我们不用外连，我们可以看看会显示什么。

```sql
SELECT * FROM users JOIN stagers ON users.username=stagers.name;

```

<figure><img src="../.gitbook/assets/image 32 (1).png" alt=""><figcaption></figcaption></figure>

很显然是个空，因为没有结果成立。

2）多个表的外连，和内连一样，这里就不叙述了。

3）SELF OUTER JOIN也是和内联一样，不叙述了。

***

## <mark style="color:blue;background-color:green;">15.UNION</mark>

union可以连接两个查询的结果，使得两个查询的结果都输出。（并且两个查询可以不同表）

```sql
SELECT id FROM users UNION SELECT name FROM stagers;
```

<figure><img src="../.gitbook/assets/image 33 (1).png" alt=""><figcaption></figcaption></figure>

可以观察到，这个列名是id，所以如果我们交换一下，可以发现位置发生了改变。

```sql
SELECT name FROM stagers UNION SELECT id FROM users;
```

<figure><img src="../.gitbook/assets/image 34 (1).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:blue;background-color:green;">16.INSERT</mark>

1）插入新数据，我们可以用INSERT INTO关键词。

比如，我们要在users表中插入一行新的数据，我们可以写成。

```sql
INSERT INTO users VALUES(2,'test','test',NULL,1,1,NULL,'2024-4-2 06:34:23','2024-4-4 05:45:23');
```

<figure><img src="../.gitbook/assets/image 35 (1).png" alt=""><figcaption></figcaption></figure>

如果有默认的结果，我们可以将他的VALUE值替换为DEFAULT，这里面是没有DEFAULT值，所以不能替换。

2）如果我们想按照我们的顺序插入某些数据，我们可以在INSERT INTO后面添加输入的顺序。

```sql
INSERT INTO users(username,hashed_password,id,api_token,admin,enabled,notes,updated_at,created_at) VALUES('test2','test',3,NULL,1,1,NULL,'2024-4-2 06:34:23','2024-4-4 05:45:23');

```

<figure><img src="../.gitbook/assets/image 36 (1).png" alt=""><figcaption></figcaption></figure>

3）一次性添加多组数据。

我们只要将values的值，多几个括号，一起输入就行。中间用，隔开。

```sql
INSERT INTO users VALUES(4,'test','test',NULL,1,1,NULL,'2024-4-2 06:34:23','2024-4-4 05:45:23'),(5,'test','test',NULL,1,1,NULL,'2024-4-2 06:34:23','2024-4-4 05:45:23');
```

<figure><img src="../.gitbook/assets/image 37 (1).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:blue;background-color:green;">17.UPDATE</mark>

1）更新某一行的数据，我们需要用UPDATE SET语句

比如我们要把id=3修改成id=6

我们可以写

```sql
UPDATE users SET id=6 WHERE id=3;
```

<figure><img src="../.gitbook/assets/image 38 (1).png" alt=""><figcaption></figcaption></figure>

2）更新多个数据，我们只要在set后面增加就行。

```sql
UPDATE users SET id=6,username='hanhan',enabled=0 WHERE id=6;
```

<figure><img src="../.gitbook/assets/image 39 (1).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:blue;background-color:green;">18.DELETE</mark>

使用DELETE FROM 语句删除，比如我们要把刚刚的全部删除。

```sql
DELETE FROM users WHERE id IN (2,4,5,6);
```

<figure><img src="../.gitbook/assets/image 40 (1).png" alt=""><figcaption></figcaption></figure>

***
