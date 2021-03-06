# Steak-XSS
<div align=center>
<img src="https://raw.githubusercontent.com/LoveSteak/Steak/master/logo.jpg"/>
</div>

**Steak ——一款高级的XSS利用工具**

Steak是一款面向红队和高级渗透测试人员的XSS利用工具. 你可以通过编写project脚本来控制并自动化渗透攻击的每一步，以此执行一些高级的攻击

想通过假的Flash升级来执行钓鱼攻击，但是不希望上线的的目标依然会看到弹窗提示？小菜一碟！我们可以利用Steak接收由Cobalt Strike和Metasploit产生的外部事件，然后在恰当的时间停止攻击！

在高度对抗的环境下做渗透测试，不想被分析师逮个正着？容易极了！我们可以用Steak来检测到使用代理或者隐身窗口的用户，然后把恶意的JS脚本替换为正常无害的脚本来逃逸检测！

更激动人心的是，Steak-XSS利用框架可以很轻松地扩展，辅助你按照你喜欢的方式进行渗透攻击。唯一的限制就是你的想象力。

有一个路由器的0day并且想用CSRF触发它？非常简单！只需要建立一个module然后朝被攻击者开炮！

用一个内部使用的机密特马而不是MSF或者CS？完全不是问题！你可以实现一个event handler来接收它产生的信息以及配合任何你喜欢的工具！

**这是一个新的项目，它可能不够完善. 我们很欢迎你来提交issue或者pull requests来一起将Steak完善。**



# 为什么这个项目叫做 “Steak”？

因为我们想向我们的前辈Beefproject致敬. 同时我们其中一位核心开发者很喜欢吃牛排


# 安装使用

你可以直接使用下面的命令来使用pip安装Steak

```
pip install steak-xss
```

或者你也可以通过克隆我们的代码并运行setup.py进行安装

```
python setup.py install
```

如果你不想把Steak安装到你的 `site-packages` 文件夹里, 你也可以只下载我们项目里的 `steak` 文件夹，然后将你的项目文件和该文件夹按照下面的方式来放置：

```
- run.py
- Project.py
- Steak
	- core
	...
```

# 使用教程

## 基本使用

使用Steak至少需要2个文件。我们在`examples`文件夹中准备了两个例子，你可以通过研究这些例子学习使用Steak

其中，`run.py`包含了加载项目和Handler的代码，并启动了Steak Server。在这个文件中，你可以加载一个或者多个Steak项目，并可以加载你需要使用到的多个Handler

``DemoProject.py``是一个自定义的示例项目，你可以通过实现自己的项目来完成你的攻击方案。我们通过客户端请求的URL来辨认客户端属于的项目，不同的URL会被分配到不同的项目中，实施攻击。在这个文件的具体编写中，你必须继承``Project`` 来实现你自己的项目。你只需要覆盖其中的`attack_client`方法，并利用这个方法来实现你自己的攻击即可。在这个函数中，你可以加载Steak中内置的模块或者你自己编写的模块，并向客户端发送Payload并取得结果

## Moudles

### Alert模块

Alert模块在客户端上运行`alert`

使用方法：

```python
alert=self.load_module('Alert',content='Hello World')
```

参数：

Content：Alert的内容

### Consolelog模块

Consolelog模块在客户端上运行``console.log``

使用方法：

```python
alert=self.load_module('Consolelog',content='Hello World')
```

参数：

Content：Consolelog的内容

### 更多模块介绍详见英文文档

### 怎么构建自己的模块?

Steak会从`steak/modules`目录读取模块。每个自定义的模块都在这个目录里有自己的一个文件夹，这个文件夹的名字就是模块名。这个模块名同时也是这个文件夹里面的Python文件夹名和对应的类名

在实现自己的模块时，你必须继承我们内置的 `Modules`类

在构造方法中，你必须返回一个`Payload`对象，你也可以直接使用我们在父类中编写好的构造方法，这应该能适用于绝大多数情况。我们预置的构造方法会利用在同一个目录下的 `command.js` ，将其中的steak标签修改为用户输入的内容，例如在Alert模块中，我们的`command.js`如下所示：

```
alert('<steak>content</steak>');
sendDataBack({'status':'done'},'<steak>taskid</steak>')
```

需要注意的是，你必须在自定义的JS脚本中使用 `sendDataBack`函数来回传信息。 `sendDataBack`函数需要接收一个`taskid`参数。这个参数会在Payload发出时由Steak自动分配。所以你只需要在这里填充 `<steak>taskid</steak>` 作为占位符

## Handlers

Handler可以用于接收外部产生的信息，比方说一台机器被MSF上线了。

当前Steak中我们已经实现了两个Handler

### MSF Handler

你可以在 `run.py` 通过以下的方式使用它：

```python
steak.add_handler("MetasploitHandler",password="demo",port=55552,ssl=False)
```

这个Handler是对 `pymetasploit3`的一个封装, 在使用之前你需要首先启用 `msfrpc` 。

当一台新的机器在MSF中上线的时候，该handler会调用每个正在运行的project中的`on_metasploithandler` 函数。

### CS Handler

你可以在 `run.py` 通过以下的方式使用它：

```python
steak.add_handler("CobaltStrikeHandler",listenonpath='/cobaltstrikecallback',password='demo')
```

想要使用这个handler，你需要在CobaltStrike团队服务器中运行一个 `cna`脚本。你可以通过`agscript`来运行它。

我们在 `handler`目录中提供了一个`cobaltstrike.cna` 文件。你需要手动更改其中的回调地址和密码，并且要和你在Steak运行时添加Handler时设置的一致。

当一台新的机器在CS中上线， `cna` 回请求Steak服务器中开着的回调地址来产生事件，然后该handler会调用每个正在运行的project中的`on_cobaltstrikehandler` 函数。

### 如何编写一个你自己的Handler?

Steak会读取 `steak/handlers` 目录下的handler。每个handler都需要有一个自己的py文件，且文件名就是handler的名字。

在py文件中，你需要继承`Handlers`类来实现Handler。

必须通过重写`generate_event` 函数来实现这个Handler所需的和外界通信的方式。Steak会启动一个新的线程来不断执行这个函数。值得注意的是，这个函数应该仅在一个外部事件发生的时候返回。如果你有一个或者多个参数需要返回给回调函数，你可以将其作为`generate_event` 函数的返回值。当函数返回的时候，Steak会调用每个正在运行的project中的 名为`on_{your handler name}` 的回调函数（如果有的话）

除此之外，你可以把Steak的服务器作为Handler的一个信息源。你可以通过以下代码监听Steak服务器的指定路径。当有请求发送到这个路径的时候，Steak服务器会调用你设定的回调函数，然后把Flask的Request对象交由这个函数来处理

```python
self.steak.server.register_path(self.lisenonpath,self.callback_registedpath)
```

# To Do
1. 增加更多模块<del>把介绍吹的牛实现</del>
2. 优化Steak中的Javascript模块
3. 完善文档
4. 编写图形界面
