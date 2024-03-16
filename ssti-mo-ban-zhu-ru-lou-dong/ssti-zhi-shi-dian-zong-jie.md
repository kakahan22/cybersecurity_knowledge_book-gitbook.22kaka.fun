---
description: 全称服务器模块注入，说实话我之前都不知道什么叫模板，所以这个漏洞我一直不是很想写。因为我完全不知道是什么东西。
---

# 🔔 SSTI知识点总结

## 一.模板是什么

先给大家上一张图，总体来看就能知道是什么。

<figure><img src="../.gitbook/assets/image (196).png" alt=""><figcaption><p>从hello-ctf顺来的，我认为应该放在前面让大家建立总体的框架。</p></figcaption></figure>

我们接下来将一一解释里面的一些概念。

### ①静态文本和动态文本

静态文本：仅仅用来展示，不能动态改变其内容，也不能再在文本框输入文字。一般是html这种文本

动态文本：可动态改变文本框的内容，常用于储存变量，随着变量值的改变，文本框的内容也会随之改变，这种类型文本框也不能再在运行时输入文字。一般是php，jsp这种文本。



### ②占位符

占位符就是字符串中的特殊标记，用于在字符串中留出位置，并在运行时将实际的值填充到这些位置上。

这里介绍一些常见的占位符用法。

### <mark style="color:blue;">python:</mark>

#### Ⅰ.%

```python
name = "john"
age = 30
message = "My name is %s and I am %d years old" %(name,age)
print(message)
```

上述的%s是以恶搞占位符，表示字符串类型的值，%d是一个占位符，表示整数的值。通过在字符串末尾使用%运算符和一个元组，可以将实际的值填充到占位符位置。



#### Ⅱ.{}和f-string（格式化字符串字面值）



```python
name = "john"
age = 30
message = f"My name is {name} and I am {age} years old."
print(message)
```

这个地方大括号作为占位符{},并且在字符串面前加上f标记，创建一个f-string，在f-string中，可以直接在花括号中使用变量名，变量的值将自动填充到占位符的位置上。



### <mark style="color:blue;">java</mark>

#### Ⅰ.%d,%f,%b,%s

就是我们常用的各种占位符，我们只介绍一个例子了，毕竟其他是一样的。



```java
String name = "Kristen";
String str = String.format("Hello, %s!",name);
System.out.println(str);
```



### <mark style="color:blue;">php</mark>

#### Ⅰ.双引号字符串中的变量插入

```php
$name="john";
echo "My name is $name";
```

#### Ⅱ.单引号字符串中使用.连接符

```php
$name = "john";
echo ' My name is' . $name . '.';
```

#### Ⅲ.使用花括号包裹变量名

```php
$count =5;
echo “ There are {$count} apples";
```

#### Ⅳ.使用数组下标或对象属性

```php
$fruits=['apple','banana','orange'];
echo " I like {$fruits[0]}.";
```

#### Ⅴ.使用特殊的占位符

```php
$name = "john";
$age = 30;
echo sprintf(" My name is %s and I am %d years old",$name,%age);

```



### ③模板

&#x20;是一种用于生成动态内容的工具。

它们通常包含两个基本部分：静态内容和动态占位符。

我们这里也直接贴图让大家理解了。

**绿色** 部分为 **静态内容** ，而 **橙色** 部分则是 **动态占位符**

<figure><img src="../.gitbook/assets/image (197).png" alt=""><figcaption></figcaption></figure>

### ④模板引擎



模板引擎（这里特指用于Web开发的模板引擎）是为了使用户界面与业务数据（内容）分离而产生的，它可以生成特定格式的文档，用于网站的模板引擎就会生成一个标准的文档。个人的理解模板的诞生是为了将显示与数据分离，其本质是将模板文件和数据通过模板引擎生成最终的HTML代码（如图）

<figure><img src="../.gitbook/assets/image (198).png" alt=""><figcaption></figcaption></figure>



### ⑤具体例子实验

这里提供一个模板的例子。

```html
<!--login.tpl-->
<html>
    <head>
        <title>{{title}}</title>
    </head>
    <body>
        <form method="{{method}}",action={{action}}>
            <input type="text" name="user" value="{{username}}">
        </form>
        <p>
            This page took {{microtime(true) - time}} seconds to render.
        </p>
    </body>
</html>
```

对应的后端的代码逻辑可以说

```php
$templateEngine = new TemplateEngine();
$tpl = $templateEngine->loadFile(login.tpl);
$tpl->assign('title','Login');
$tpl->assign('method','post');
$tpl->assign('action','login.php');
$tpl->assign('username',getUserNameFromCookie());
$tpl->assign('time',microtime(true));
$tmp->show();
```







***

## 二.SSTI漏洞原理

### ①原理

也是基于一切输入都是有害的。

目前我们使用二一些框架比如说python的flask，php的tp，java的spring等一般都采用成熟的MVC模式，用户的输入先进入Controller控制器，然后根据请求类型和请求的指令发送给对应model业务模型进行业务逻辑判断，数据库存取，最后把结果返回给Vier视图层，经过模版渲染展示给 用户。

那么形成漏洞是因为服务器端接受了用户的恶意输入后，没有经过任何处理就将其作为应用模板的一部分，模板引擎在渲染的时候，执行了用户插入的可以破坏模板的语句（就是和RCE执行漏洞差不多的语句），就可以有敏感信息泄露，代码执行，Getshell等问题。

### ②模板类型

#### <mark style="color:blue;">python：</mark>

* jinja2
* mako
* tornado
* django

#### <mark style="color:blue;">php：</mark>

* smarty
* twig

#### <mark style="color:blue;">java：</mark>

* jade
* velocity

这里有一些触发语法。

<figure><img src="../.gitbook/assets/image (199).png" alt=""><figcaption></figcaption></figure>

举个栗子，比如：

```python
from flask import Flask
from flask import request
from flask import render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    template = '''
    <p>Hello %s </p>''' % (request.args.get('name'))
    return render_template_string(template)

if __name__ == '__main__':

    app.run()
```

当我们传入\{{9\*9\}}时，他会帮我们运算后输出81。我们就可以把这个9\*9替换为其他的执行语句。





***

## 三.python的SSTI注入

















































## 参考门：



{% embed url="https://www.jianshu.com/p/b6f1aea3a2eb" %}

{% embed url="https://cs-cshi.github.io/cybersecurity/flask%E4%B9%8Bssti%E6%A8%A1%E7%89%88%E6%B3%A8%E5%85%A5%E4%BB%8E%E9%9B%B6%E5%88%B0%E5%85%A5%E9%97%A8/" %}

{% embed url="https://www.ol4three.com/2022/01/12/WEB/SSTI%E6%A8%A1%E7%89%88%E6%B3%A8%E5%85%A5%E5%AD%A6%E4%B9%A0/" %}

{% embed url="https://tr0jan.top/archives/43/" %}

{% embed url="https://hello-ctf.com/HC_Web/ssti/" %}

{% embed url="https://exp10it.io/2022/08/python-ssti-%E6%80%BB%E7%BB%93%E7%AC%94%E8%AE%B0/" %}











