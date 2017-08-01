'''

一、UserDict概述
UserDict 模块中的 UserDict 类是在python中经常使用的类，保存在Python 安装目录的 lib 目录下UserDict.py。其高仿字典(Dictionary)打开之后可见如下：

复制代码
 1 ""A more or less complete user-defined wrapper around dictionary objects."""
 2
 3 class UserDict:　　　　　　　　　　　　　　　　　　　　[1]
 4     def __init__(self, dict=None, **kwargs):　　　[2]
 5         self.data = {}　　　　　　　　　　　　　　　　[3]
 6         if dict is not None:　　　　　　　　　　　　 [4]
 7             self.update(dict)　　　　　　　　　　　　[5]
 8         if len(kwargs):
 9             self.update(kwargs)
10     def __repr__(self): return repr(self.data)
11     def __cmp__(self, dict):
12         if isinstance(dict, UserDict):
13             return cmp(self.data, dict.data)
14         else:
15             return cmp(self.data, dict)
16     def __len__(self): return len(self.data)
..................省略

复制代码
 注意：
[1]. UserDict 是一个基类，不是从任何其他类继承而来
[2].通过在 dict 参数中传入一个字典来定义初始值
[3].Python 支持数据属性，如上的 data （在C#、C++叫数据成员，java中叫实例变量）。它是由某个特定的类实例所拥有的数据，在本例中，每个 UserDict 实例将拥有一个 data 数据属性。
　　引用：(1).要从类外的代码引用这个属性，需要用实例的名字限定它，instance.data，限定的方法与你用模块的名字来限定函数一样
　　　　　(2).要在类的内部引用一个数据属性，我们使用 self 作为限定符

习惯上，所有的数据属性都在 __init__ 方法中初始化为有意义的值。然而，这并不是必须的，因为数据属性，象局部变量一样，当你首次赋给它值的时候突然产生。
[4].if ....is...语法
[5].update 方法是一个字典复制器：它把一个字典中的键和值全部拷贝到另一个字典。 这个操作 并不 事先清空目标字典，如果一些键在目标字典中已经存在，则它们将被覆盖，那些键名在目标字典中不存在的则不改变。应该把 update 看作是合并函数，而不是复制函数。

二、UserDict 常规方法

复制代码
 1 def clear(self):                        #[1]
 2     self.data.clear()                   #[2]
 3 def copy(self):                         #[3]
 4     if self.__class__ is UserDict:   　　#[4]
 5         return UserDict(self.data)
 6     import copy
 7     return copy.copy(self)           　　#[5]
 8 def keys(self):
 9     self.data.keys()
10 def items(self):
11     self.data.items()
12 def values(self):
13     self.data.values()
复制代码
注意：封装类的基本技术：
将一个真正的字典 (data) 作为数据属性保存起来，定义所有真正字典所拥有的方法，并且将每个类方法重定向到真正字典上的相应方法。（如上的clear，对应dictionary中的clear()方法）

复制代码
 1  从 dictionary 中删除元素
 2 >>> d
 3 {'server': 'mpilgrim', 'uid': 'sa', 'database': 'master',42: 'douglas', 'retrycount': 3}
 4 >>> del d[42]
 5 >>> d
 6 {'server': 'mpilgrim', 'uid': 'sa', 'database': 'master', 'retrycount': 3}
 7 >>> d.clear()
 8 >>> d
 9
10    del 允许您使用 key 从一个 dictionary 中删除独立的元素。
11   clear 从一个 dictionary 中清除所有元素。注意空的大括号集合表示一个没有元素的 dictionary。
复制代码


[1].clear 是一个普通的类方法，可以在任何时候被任何人公开调用。注意，clear 象所有的类方法一样（常规的或专用的），使用 self 作为它的第一个参数。（记住，当你调用方法时，不用包括 self；这件事是 Python 替你做的。）

[2].真正字典的 copy 方法会返回一个新的字典，它是原始字典的原样的复制（所有的键-值对都相同）。但是 UserDict 不能简单地重定向到 self.data.copy，因为那个方法返回一个真正的字典，而我们想要的是返回同一个类的一个新的实例，就象是 self。

[3].我们使用 __class__ 属性来查看是否 self 是一个 UserDict，如果是，太好了，因为我们知道如何拷贝一个 UserDict：只要创建一个新的 UserDict ，并传给它真正的字典，这个字典已经存放在 self.data 中了。 然后你立即返回这个新的 UserDict，你甚至于不需要再下面一行中使用 import copy。

[4].如果 self.__class__ 不是 UserDict，那么 self 一定是 UserDict 的某个子类（如可能为 FileInfo），生活总是存在意外。 UserDict 不知道如何生成它的子类的一个原样的拷贝，例如，有可能在子类中定义了其它的数据属性，所以我们只能完全复制它们，确定拷贝了它们的全部内容。幸运的是，Python 带了一个模块可以正确地完成这件事，它叫做 copy。能够拷贝任何 Python 对象.

[5].其余的方法是直截了当的重定向到 self.data 的内置函数上。

三、 直接继承自内建数据类型 dict

注意：dict是内建的数据类型，如同内建函数一般，可以在任何地方使用。在python中，可以直接继承自内建数据类型dict，如下：
1.继承自UserDict.UserDict

复制代码
1 #继承自 UserDict.UserDict
2 #import UserDict 这个错误，一定要导入UserDict模块的UserDict类
3 from UserDict import UserDict
4 class FileInfo(UserDict):
5     "store file metadata"
6     def __init__(self, filename=None):
7         UserDict.__init__(self)
8         self["name"] = filename
复制代码
2.直接继承自内建数据类型 dict

1 #直接继承自内建数据类型 dict
2 class demo(dict):
3     def __init__(self,test=None):
4         self["name"]=test
我们发现第二种精简了许多。它们之间的区别如下3点：

（1）不需要导入 UserDict 模块，因为 dict 是已经可以使用的内建数据类型
（2）继承方式不同，一个是继承自 UserDict.UserDict ，另一个直接继承自 dict
（3）UserDict 内部的工作方式要求你手工地调用它的 __init__ 方法去正确初始化它的内部数据结构。 dict 并不这样工作，它不是一个封装所以不需要明确的初始化。

四、python类的深入[1]

1.关于重载
在各编程语言中大致分为两种重载方式:
　　(1).通过参数列表的重载，一个类可以有同名的多个方法，但这些方法它们参数个数不同，或参数的类型不同，如java
　　(2).支持通过参数名的重载，一个类可以有同名的多个方法，这些方法有相同类型，相同个数的参数，但参数名不同如（PL/SQL）

不过注意：Python 两种都不支持！
总之是没有任何形式的函数重载。一个 __init__ 方法就是一个 __init__ 方法，不管它有什么样的参数。每个类只能有一个 __init__ 方法，并且如果一个子类拥有一个 __init__ 方法，它总是覆盖父类的 __init__ 方法，甚至子类可以用不同的参数列表来定义它。子类可以覆盖父类中的方法。

2.关于数据属性
应该总是在 __init__ 方法中给一个实例的所有数据属性赋予一个初始值。这样做将会节省你在后面调试的时间，不必为捕捉因使用未初始化（也就是不存在）的属性而导致的 AttributeError 异常费时费力。

在 Java 中，静态变量（在 Python 中叫类属性）和实例变量（在 Python 中叫数据属性）两者是紧跟在类定义之后定义的（一个有 static 关键字，一个没有）。在 Python 中，只有类属性可以定义在这里，数据属性定义在 __init__ 方法中。
'''