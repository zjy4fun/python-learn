# python

## 01-基础

### 数据类型和变量

**字符串**可以使用双引号和单引号括起来，如果既包含双引号也包含单引号，可以使用转义字符`\`来表示

如果有很多字符需要转义，使用`r''`表示引号中的字符串默认不转义

Python允许用`'''...'''`的格式表示多行内容

**空值**使用 None 表示

同一个变量可以反复赋值，而且是不同类型的变量（动态语言）

### 字符串和编码

ASCII：对字符进行编码

Unicode：解决乱码问题

UTF-8：可变长（解决了Unicode占用存储空间大的缺点）

在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码

由于Python的字符串类型是`str`，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把`str`变为以字节为单位的`bytes`

Python对`bytes`类型的数据用带`b`前缀的单引号或双引号表示

```
decode: bytes => str 
encode: str => bytes
```

计算`str`包含多少个字符，可以使用len()函数

如果换成bytes，len()统计的就是字节数

指定使用UTF-8编码保存文件

```
# -*- coding: utf-8 -*-
```

格式化方式和C语言一致，使用 % 实现

占位符`%s`会把任何数据类型转换为字符串

使用%对%进行转义

使用format方法进行转义

使用f-string格式化

python3的字符串使用Unicode，直接支持多语言。

当 str 和 bytes 互相转换时，需要指定编码，最常用的编码是UTF-8

### list

有序列表

可使用负数索引访问倒数的元素

其他类似于其他语言种的list

### tuple

一旦初始化，就不能修改（安全）

### 条件判断

if-elif-else

input返回值是字符串

### 循环

for-in

range()可以生成一个整数序列

再通过list()函数可以转换为list

while

### dict

类似于map，使用key-value存储，具有极快的查找速度

删除一个key，使用`pop(key)`，对应的 value 也会从 dict 中删除

dict是用空间来换取时间的一种方法。

dict的key必须是**不可变对象**。

### set

要创建一个set，需要提供一个list作为输入集合：

## 02-函数

使用 def 创建

### 空函数

```
def nop():
	pass
```

pass是一个占位符，如果还没想好怎么写代码，可以先放下一个pass，让代码能够跑起来

### 参数检查

数据类型检查可以用内置函数`isinstance()`实现：

### 返回多个值

其实返回的是一个tuple

### 函数参数

位置参数，默认参数（调用的时候可以不提供）

默认参数必须指向的是不变对象，否则下一次调用的时候，初始值会因为上一次调用而发生改变。

可变参数：传入的参数个数是可变的，调用的时候，需要先组装出一个list或tuple

在参数前面加一个*号，该参数就是一个list或者tuple，然后使用泛型迭代的方法进行遍历

关键字参数：函数内部会把关键字参数组合成一个dict，以实现扩展函数的功能

也可以把参数组合成一个dict再传进去

### 参数组合

5种参数都可以组合使用，但是参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

## 03-对象

self 类似于其他语言中的 this
重写 __str__ 类似于 java 里面的 toString()



## 04-模块

每个py文件被称之为模块，每个具有_init_.py文件的目录被称为包

只要模块或者包所在的目录在sys.path中，就可以使用import模块或者import包来使用。

如果要使用的模块(py文件)和当前模块在同一目录，只要import相应的文件名即可

sys.path是python的搜索模块的路径集，是一个list；可以在python环境下使用sys.path.append(path)添加相关的路径，但在退出python环境后添加的路径就会自动消失了。

ImportError: No module named ‘xxx’：模块不在搜索路径里，从而导致路径搜索失败。



## 05-Stream

　　流是用于处理网络连接的高级async/await-ready原语。流允许发送和接收数据，而不需要使用回调或低级协议和传输。（待补充）



## 高级特性

### 生成器

Python中，一边循环一边计算的机制，称为生成器：generator

创建 generator 的方法：

- 第一种是把列表生成式的`[]`换成`()`，就创建了一个generator
  - 可以使用next来一个一个访问generator生成的值
  - 使用for循环迭代generator
- 使用yield关键字，包含yield关键字的函数就是一个generator函数，调用一个generator函数将返回一个generator
  - 普通函数是顺序执行，遇到 return 语句或者最后一行函数语句就返回，而变成 generator 的函数，在每次调用 next() 的时候执行，遇到yield语句返回，再次执行时从上次返回的 yield 语句处继续执行
  - 调用generator函数会创建一个generator对象，多次调用generator函数会创建多个相互独立的generator
  - 使用for循环调用generator时，如果想要拿到返回值，必须捕获`StopIteration`错误，返回值包含在`StopIteration`的`value`中

### 迭代器

能够使用`for`循环的对象统称为可迭代对象：`Iterable`

可以被`next()`函数调用并不断返回下一个值的对象称为迭代器：`Iterator`

生成器都是`Iterator`对象，但`list`、`dict`、`str`虽然是`Iterable`，却不是`Iterator`

把list，dict，str等Iterable变成Iterator可以使用iter()函数

Iterator的计算是惰性的，只有在需要返回下一个数据它才会计算

Python的for循环本质上就是通过不断调用 `next()` 函数实现的



## 补充

### 属性私有化问题

1. 没有下划线：一般情况下使用的变量

2. 一个下划线：

   - import 模块名 变量可以正常使用

   - from 模块名 import * 的方式，变量无法使用

3. 双下划线

   类的私有属性/类的私有方法，只能在类的内部访问；

   不能在类的外部直接访问，但是可以间接访问；

   python解释器会对私有属性和私有方法进行名字重整（改名）

   重整原则：_类名__私有属性名或私有方法名

4. `__xx__`主要用于方法

   初始化方法，str 方法，del 方法，new 方法

   这些方法不需要自己调用，例如创建对象的时候，会自动先执行new方法，再执行初始化方法

   注意：自定义方法要避免与这些内置的方法重名

5. `xx_`主要用来区分变量名或者方法名（一般情况下不常用）

6. 使用 property 简化私有属性的访问方式

7. 使用@property简化私有属性的访问方式



