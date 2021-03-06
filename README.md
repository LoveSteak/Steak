# Steak-XSS
<div align=center>
<img src="https://raw.githubusercontent.com/LoveSteak/Steak/master/logo.jpg"/>
</div>

**Steak ——An advanced XSS exploitation tool**

Steak is an advanced XSS exploitation tool built for skilled professional penetration testers and red teams. With Steak, you can customize and automate every step of exploitation by building your own "project script" to perform several advanced attacks. 

Want to create a fake Flash update to perform a phish attack but don't want victims installed your trojan still see the pop-up window? A piece of cake! We can use Steak to receive external events from Cobalt Strike or Metasploit to stop the attack at the right time!

Doing pentest in a highly adversarial environment and don't want to be caught by analysts? Elementary!  We can use Steak to detect users using proxy or incognito window and replace original malicious javascript into a normal harmless javascript file to evade from them!

More over, our Steak-XSS framework is easy-to-extend to hack in the way you like. The only limit is your imagination.

Having an 0day exploit on a router and would like to triger it via CSRF? Pretty easy! Just build a module and fire to the victim! 

Using your internal-use secret RAT other than MSF or CS but still want Steak to intereact with it? Not a problem! Implement an event handler to receive information from the RAT or any other tools you like!

**This is a new project and it might not be perfect. We welcome your issues or pull requests to imporve Steak together.**

# Why we choose the name "Steak"?

Because we'd like to salute to our predecessor, the Beefproject. And one of our core developers love eating steak

# Install

You can use pip to install Steak easily. Using command below:

```
pip install steak-xss
```

Or you can clone our code and run:

```
python setup.py install
```

If you don't wanna install Steak into your Python `site-packages` folder, you can just download the `steak` folder and put your project file as below:

```
- run.py
- Project.py
- Steak
	- core
	...
```

# How to use

## Basic Usage

Steak needs at least two files to run. There are demo files in `examples` folder. You can read them and you will know how to use Steak easily.

`run.py` contains Handler and Project loading code. You can load more than one project when you are starting a single Steak server. You also needs to load Handers you are about to use in this file.

``DemoProject.py`` contains your own attack ways of a project. We identify clients from JavaScript url it requests. Different JavaScript url will lead to different Projects. In this file, you must inherit class ``Project`` to implement your own project. You just need to overwrite `attack_client` function to do your own job. In this function, you can load modules in Steak or wrriten by yourself. Then send payload to client to get result.

## Moudles

### Alert

Alert Moudle can run `alert` command in client browser.

Demo Usage:

```python
alert=self.load_module('Alert',content='Hello World')
```

> Parameters:
>
> Content: Alert Content

### Consolelog

Consolelog Moudle can run console.log command in client browser.

Demo Usage:

```python
alert=self.load_module('Consolelog',content='Hello World')
```

> Parameters:
>
> Content: Consolelog Content

### How to write your own modules?

Steak will read modules in `steak/modules` folder. Each module has its own subfolder whose name is module name.This module name must be same with class name and python file name in this subfolder.

You must inherit `Modules` class when you are implementing your own module.

You need to return a `Payload` object in your own ``__init__`` function. You can also use  ``__init__`` function implemented by us. This function will use `command.js` in the same subfolder. It will replace Steak tag with information users input. For example, in Alert Module , our `command.js` is below:

```
alert('<steak>content</steak>');
sendDataBack({'status':'done'},'<steak>taskid</steak>')
```

Specially, you must use `sendDataBack` to send your running result in javascript. `sendDataBack` receives `taskid` as another parameter. This will be filled automatically when Steak send payload to client. You just need to use `<steak>taskid</steak>` to symbol it.

## Handlers

Handlers can be used to receive outside information such as online information from MSF.

We implemented two Handlers inside Steak.

### MSF Handler

You can load it in `run.py` using code below:

```python
steak.add_handler("MetasploitHandler",password="demo",port=55552,ssl=False)
```

This handler is a wrap of `pymetasploit3`, you need to start your `msfrpc` service before using.

When a new client is online in MSF, this handler will call `on_metasploithandler` of every project.

### CS Handler

You can load it in `run.py` using code below:

```python
steak.add_handler("CobaltStrikeHandler",listenonpath='/cobaltstrikecallback',password='demo')
```

This handler needs you to run a `cna` script in your CobalStrike teamserver. You can use `agscript` to run it.

We provided a `cobaltstrike.cna` file in `handler` folder. You need to modify callback path and password in it. These settings must be the same with setting you add this handler in Steak.

When a new client is online in CS, `cna` script will request listenonpath opened in Steak server and this Handler will call `on_cobaltstrikehandler` of every project.

### How to write your own handlers?

Steak will read handlers in `steak/handlers` folder. Each handler has its own py file whose name is handler name. 

You must inherit `Handlers` class when you are implementing your own handler.

You just need to overwrite `generate_event` function to implement your own communication functions in standard Python code. Steak will start a new thread to call this function continuously. Importantly, this function should return only when an external event happened. If you have one or more parameters that you need to return to callback function, you can just use it as the return value of `generate_event` function. When you return, Steak will call `on_{your handler name}` function in every project if exists automatically.

Moreover, you can also use Steak server as the source of your message. You need to use code below to register a path in Steak server. When there is a request in this path, Steak server will call callback function you give and pass you a Request object in Flask.

```python
self.steak.server.register_path(self.lisenonpath,self.callback_registedpath)
```

# To Do
1. Add more moudles
2. Optimize javascript script in Steak
3. Add more documents
4. Add graphical interface
