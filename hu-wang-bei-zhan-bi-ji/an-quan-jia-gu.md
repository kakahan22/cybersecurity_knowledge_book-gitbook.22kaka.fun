---
description: >-
  分为windows安全加固和linux安全加固，其实后面发现安全加固这个微专业老师好像也刚好在学这个，我了个豆，原来学过的东西都会以不同的形式再回到你脑子里/(ㄒoㄒ)/~~,所以这里就结合网上的文章和老师ppt一起来写这一篇知识总结。
---

# 🌮 安全加固

## 1.linux安全加固手册

接下来从用户及权限安全排查 ，远程连接安全配置， SUID/SGID文件权限排查， Linux系统不安全服务排查 ，敏感数据排查与防护这几个方面来进行安全加固。

### ①用户权限安全排查

前置知识：

> Linux系统是多用户操作系统；&#x20;
>
> 并不能识别用户输入的用户名称，而是识别用户名称对应的ID号；&#x20;
>
> 每个用户的ID号分为两种，分别是用户ID（UID），组ID（GID）；&#x20;
>
> 所有用户的名称与ID的对应关系都存储在/etc/passwd文件中；
>
> &#x20;UID由一个32位的无符号型整数表示，用于唯一标识系统中的用户；&#x20;
>
> root的UID为0；&#x20;
>
> GID也是一个32位的无符号整数表示，用于定义该用户所在的组；
>
> &#x20;root:         x:               0:       0:          root:               /root:                  /bin/bash&#x20;
>
> 用户名称 用户密码    UID    GID      信息描述       用户主目录         默认shell

<figure><img src="../.gitbook/assets/image (33).png" alt=""><figcaption></figcaption></figure>

这里密码都是x是因为真正的密码存在/etc/shadow里面。



#### （1）查询当前系统新增的用户名

首先新增一个用户test1，

```
useradd test1
```

<figure><img src="../.gitbook/assets/image (34).png" alt=""><figcaption></figcaption></figure>

可以看到添加成功。



```
awk -F : '($3>=500||$3==0){print $1}' /etc/passwd
```

<figure><img src="../.gitbook/assets/image (35).png" alt=""><figcaption></figcaption></figure>

#### （2）查询系统中是否存在特权用户

UID为0的用户拥有系统的最高权限

```
awk -F : '($3==0){print $1}' /etc/passwd
```

<figure><img src="../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>



#### (3)查询密码为空的用户

在passwd中，用户密码是被保护的的状态，都是使用x来隐藏的，真正的密码内容保存在/etc/shadow文件中，而shadow只有root才能查看。 如果该文件中密码对应字段长度为0，则表明该用户密码为空。

```
awk -F : '($2==""){print $1}' /etc/shadow
```

<figure><img src="../.gitbook/assets/image (71).png" alt=""><figcaption></figcaption></figure>



#### 4)检测系统中是否存在弱口令的用户

对于弱口令爆破，这里使用的是hydra，对于工具的使用我们在工具里面具体介绍。

```
hydra -l hanhan -p 123456 192.168.29.128 ssh
```

<figure><img src="../.gitbook/assets/image (74).png" alt=""><figcaption></figcaption></figure>



#### （5）禁用/解锁不安全的用户账号。

禁用：

```
passwd -l 用户名
```

<figure><img src="../.gitbook/assets/image (75).png" alt=""><figcaption></figcaption></figure>

解禁unlock

```
passwd -u root
```



#### (6)删除不安全的的用户账户

```
userdel 删除账号
useradd 添加账号
```

<figure><img src="../.gitbook/assets/image (76).png" alt=""><figcaption></figcaption></figure>

#### （7）更改用户弱口令等，也可以修改i。

```
passwd 用户名
```

<figure><img src="../.gitbook/assets/image (77).png" alt=""><figcaption></figcaption></figure>







### ②远程连接安全配置

传统的远程传输协议（如FTP、Telnet）本质上都是不安全的，传输内容是明文，容易遭受“中间人”攻击，因此，在管理远程服务器时，最常使用的是SSH远程连接协议。 SSH传输的数据是加密的，但SSH的不安全配置也会造成一系列的安全问题，如弱口令枚举、特权用户登录等。



#### （1）修改ssh默认端口

首先我们先看ssh能否远程连接上，可以连接成功的。

<figure><img src="../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

ssh的默认文件是 /etc/ssh/sshd\_config ，所以我们将编辑文件修改端口号，例如改成20022

<figure><img src="../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

```
cat /etc/ssh/sshd_config | grep -i port
修改port为其他的端口
重启服务
systemctl restart sshd
```

然后访问，我们远程访问ssh协议的指令是

```
ssh username@ip_address -p 端口号
```

但是我们改变了端口之后，需要关掉虚拟机的ufw防火墙，不然其他的端口无法连接。

<figure><img src="../.gitbook/assets/image (81).png" alt=""><figcaption></figcaption></figure>

然后再连接就可以成功了

<figure><img src="../.gitbook/assets/image (82).png" alt=""><figcaption></figcaption></figure>



#### （2)防止端口探测工具进行服务版本识别。

首先查看目前ssh的指纹信息

```
nmap 192.168.29.128 -p 20022 -sS -Pn -A
```

<figure><img src="../.gitbook/assets/image (83).png" alt=""><figcaption></figcaption></figure>







































## 参考门：

[https://www.cnblogs.com/skkip/p/10074096.html](https://www.cnblogs.com/skkip/p/10074096.html)















