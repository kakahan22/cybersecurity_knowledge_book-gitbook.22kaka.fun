---
description: >-
  配置好环境，其实我是看不懂一点的，觉得真特么的复杂什么鬼玩意啊，无所谓，因为我会看网课，我看的黑马程序员，倒不是他讲的通俗不通俗，因为现在学到这里感觉理解方面已经没有很大的问题了。
---

# 📱 JAVA语法

## （1）hello world

应该没有人没写过hello ，world吧

```java
import java.util.Date;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main{
    public static void main(String[] args){
        System.out.println("helloworld");
    }
}
```

***

## （2）注释

### ①单行注释：//

### ②多行注释：/\*\*/

```java
import java.util.Date;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main{
    //main方法，表示程序的主入口
    public static void main(String[] args){
        //叫做输出语句
        //会把小括号里面的内容进行输出打印。
        System.out.println("helloworld");
    }
}
```

***

## （3）字面量

### 1）基本类型

#### ①**int 型**：

#### ②**float型**，double型：双引号括起来的内容，float型需要在后面加一个F，大写小写都可。

#### ③**char型**：单引号括起来的，内容只有一个

#### **④string型**

#### ⑤**boolean型**

#### ⑥**null型**

没有特别说明的，就和c语言一样。这里每个类型的输出模式如下。

```java
import java.util.Date;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main{

    public static void main(String[] args){
        System.out.println(666);
        System.out.println(-345);
        System.out.println(23.45);
        System.out.println(234.34F);
        System.out.println("fsga");
        System.out.println('c');
        System.out.println(true);
        System.out.println(false);
    }
}
```

<figure><img src="../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

⑦byte型

⑧long型：需要在数字后加一个L后缀，建议大写，虽然大写小写都可。

⑨short型

***

### 2）特殊字符

这里本来在c语言也学过，但是突然发现自己以前学的是个错的，所以才在这里在学一次。

#### ①制表符\t

它的作用是把前面的字符串长度补到8或者8的倍数，最少补一个空格，做多补8个空格。一般用于对齐。

```java
import java.util.Date;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main{

    public static void main(String[] args){
       System.out.println("avc"+'\t');
       System.out.println("aga");
    }
}
```

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## （4）变量

和c一致，不多说

***

## （5）进制

二进制：代码中以0b开头

十进制：默认

八进制：0开头

十六进制：0x开头

```java
import java.util.Date;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main{

    public static void main(String[] args){
      System.out.println(0x12);//16进制
        System.out.println(014);//8进制
        System.out.println(14);//10进制
        System.out.println(0b100);//2进制
        
    }
}
```

<figure><img src="../.gitbook/assets/image (90).png" alt=""><figcaption></figcaption></figure>

***

## （6）命名规则

变量：小驼峰命名法（第一个首字母小写，其余首字母大写）

类：大驼峰命名法（每个首字母都大写）

***

## （7）scanner类：键盘录入

java写好的一个类类叫scanner，这个类可以接受键盘输入的数字。

那么我们如何进行键盘录入呢，其实我感觉这个步骤类似于c语言的头文件和调用函数。

### step1：导包

```java
import java.util.Scanner;
```

导包的动作必须出现在类定义的上边。导包现在可以自动导入了，如果直接进入第二步，第一步会自动导入

### step2：创建对象

```java
Scanner sc=new Scanner(System.in);
```

上面的sc是变量名可以变，其他都不能变。

### step3：接收数据

```java
int i=sc.nextInt();
```

上面的i是变量名可以变，其他的都不允许变。

其实他的写法是如下的

```java
import java.util.Date;
//导包，找到scanner这个类在哪
import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main{

    public static void main(String[] args){
    //创建对象，表示我们现在准备要用这个类。
        Scanner sc=new Scanner(System.in);
        //接受数据，变量i记录了键盘录入的数据。
        int i=sc.nextInt();
        System.out.println(i);

    }
}
```

<figure><img src="../.gitbook/assets/image (91).png" alt=""><figcaption></figcaption></figure>

如果我们要继续接受数据的话，第一步和第二步可以不用写了，只要再写一个第三步就可以了。

***

## （8）运算符

#### ①+：和数字就是加法，和字符串在一起就是拼接。

#### ②-

#### ③\*

#### ④/

#### ⑤%

计算规则和运行结果和c语言一样不多说。不过小数参与计算，计算结果可能不精确。

```java
import java.util.Date;
import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main{

    public static void main(String[] args){
        System.out.println(4+3);
        System.out.println(4.5+6.7);
        System.out.println(4*3);
        System.out.println(4.5*5.6);
        System.out.println(5/2);
        System.out.println(5.5/5);
        System.out.println(4%2);

    }
}
```

<figure><img src="../.gitbook/assets/image (92).png" alt=""><figcaption></figcaption></figure>

⑥++

⑦--

⑧=

⑨+=，-=，\*=，/=

1①==，!=,>=,<=,<,>,

1②?  ：



***

## （9）字符串和+

若+两边的运算数包含了字符串，那么这个+就是拼接的意思。

但是如果有一个是变量，那么变量先替换为变量值再进行运算。

```java
import java.util.Date;
import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main{

    public static void main(String[] args){
       System.out.println(123+"124"+124);
       System.out.println(124+123+"124");
       int age=123;
       System.out.println(age+"124");


    }
}
```

<figure><img src="../.gitbook/assets/image (93).png" alt=""><figcaption></figcaption></figure>

如果是char类型用+则会先转化为ascii码再计算。

```java
import java.util.Date;
import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main{

    public static void main(String[] args){
       System.out.println('a'+1);
       System.out.println('a'+"1");


    }
}
```

<figure><img src="../.gitbook/assets/image (94).png" alt=""><figcaption></figcaption></figure>

***

## （10）逻辑运算符

#### ①&&

#### ②||

#### ③^

#### ④！

***

## （11）判断和循环

### 1）判断

#### ①if -else

其实它的语法格式和c语言也差不多，我这里直接上代码了。

```java
import java.util.Date;
import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main{

    public static void main(String[] args){
       Scanner sc=new Scanner(System.in);
       System.out.println("请输入酒量");
       int wine=sc.nextInt();
       if(wine>100&&wine<200) {
           System.out.println("小伙子不错哦");
       }
       else if(wine>200){
           System.out.println("小伙子太棒了");
        }
       else {
           System.out.println("小伙子再去练练吧");
       }
    }
}
```

<figure><img src="../.gitbook/assets/image (95).png" alt=""><figcaption></figcaption></figure>

#### ②switch

同c语言，其实在学了很多很多的语言之后，感觉语法确实是最不值得花时间的。

```java
import java.util.Date;
import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main{

    public static void main(String[] args){
       Scanner sc=new Scanner(System.in);
       System.out.println("请输入课程编号");
       int classorder=sc.nextInt();
       switch(classorder)
       {
           case 1:
               System.out.println("计算机");
               break;
           case 2:
               System.out.println("高等数学");
               break;
           case 3:
               System.out.println("大学物理");
               break;
           case 4:
               System.out.println("线性代数");
               break;
           default:
               System.out.println("没有");
       }
    }
}
```

<figure><img src="../.gitbook/assets/image (96).png" alt=""><figcaption></figcaption></figure>

当然java这里和c语言有了一点区别了哦，有一种省略break的写法。将冒号用->代替，将break用{}代替

```java
import java.util.Date;
import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main{

    public static void main(String[] args){
       Scanner sc=new Scanner(System.in);
       System.out.println("请输入课程编号");
       int classorder=sc.nextInt();
       switch(classorder) {
           case 1 -> {
               System.out.println("计算机");
           }
           case 2 -> {
               System.out.println("高等数学");
           }
           case 3 -> {
               System.out.println("大学物理");
           }
           case 4->{
               System.out.println("线性代数");
           }
           default->{
               System.out.println("没有");
           }
       }
    }
}
```

<figure><img src="../.gitbook/assets/image (97).png" alt=""><figcaption></figcaption></figure>

### 2）循环

#### ①for：

和c语言语法还是一样的，没啥区别。直接上代码

```java
import java.util.Date;
import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main{

    public static void main(String[] args) {
        int i;
        for(i=5;i<=10;i++)
        {
            System.out.println(i);
        }
    }
}
```

<figure><img src="../.gitbook/assets/image (98).png" alt=""><figcaption></figcaption></figure>

#### ②while





































