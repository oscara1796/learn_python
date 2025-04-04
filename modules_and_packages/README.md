# Python Modules and Packages

Modular programming is the process of breaking a large, unwieldy programming task into separate, smaller, more manageable subtasks or modules. Individual modules can then be put together like building blocks to create a larger application.

## What are advantages of modularizing code in a large application?

* **Simplicity**: Rather than focusing on the entire problem at hand, a module typically focuses on one relatively small portion of the problem. If you’re working on a single module, then you’ll have a smaller problem domain to wrap your head around. This makes development easier and less error-prone.

* **Maintainability**: Modules are typically designed so that they enforce logical boundaries between different problem domains. If modules are written in a way that minimizes interdependency, then there is decreased likelihood that modifications to a single module will have an impact on other parts of the program. (You may even be able to make changes to a module without having any knowledge of the application outside that module.) This makes it more viable for a team of many programmers to work collaboratively on a large application.

* **Reusability**: Functionality defined in a single module can be easily reused (through an appropriately defined interface) by other parts of the application. This eliminates the need to recreate duplicate code.

* **Scoping**: Modules typically define a separate namespace, which helps avoid collisions between identifiers in different areas of a program. (One of the tenets in the Zen of Python is *Namespaces are one honking great idea—let’s do more of those!*)

Functions, modules, and packages are all constructs in Python that promote code modularization.

---

## The Module Search Path

In this lesson, you’ll learn about the module search path. Continuing with the example from the previous lesson, take a look at what happens when Python executes the following statement:

```python
>>> import mod
>>> mod.a
[100, 200, 300]
>>> mod.s
'Computers are useless. They can only give you answers.'
```

When the interpreter executes the above import statement, it searches for mod.py in a list of directories assembled from the following sources:

1.  The directory from which the input script was run, or the current directory if the interpreter is being run interactively
    
2.  The list of directories contained in the PYTHONPATH environment variable, if it is set. (The format for PYTHONPATH is OS-dependent but should mimic the PATH environment variable.)
    
3.  An installation-dependent list of directories configured at the time Python is installed
    

The resulting search path is accessible in the Python variable sys.path, which is obtained from a module named sys:

```python
>>> import sys
>>> sys.path
['', '/Library/Frameworks/Python.framework/Versions/3.7/bin', 
'/Library/Frameworks/Python.framework/Versions/3.7/lib/python37.zip', 
'/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7', 
'/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload', 
'/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages']

```

**Note**: The exact contents of sys.path are installation-dependent. The above code block will almost certainly look slightly different on your computer. The operating system used in this lesson is macOS. If you would like to see what the path structure looks like in a Windows environment, check out the original article that this course is based on.

So, to ensure that your module is found, you need to do one of the following:

*   Put mod.py in the directory where the input script is located, or the current directory if interactive
    
*   Modify the PYTHONPATH environment variable to contain the directory where mod.py is located before starting the interpreter. Or put mod.py in one of the directories already contained in the PYTHONPATH variable.
    
*   Put mod.py in one of the installation-dependent directories, which you may or may not have write-access to, depending on the OS.
    

There is also one additional option: You can put the module file in any directory of your choice and then modify sys.path at run-time so that it contains that directory. For example, in this case, you could put mod.py in directory /Users/chris/ModulesAndPackages and then issue the following statements:

```python
>>> import sys
>>> sys.path
['', '/Library/Frameworks/Python.framework/Versions/3.7/bin', 
'/Library/Frameworks/Python.framework/Versions/3.7/lib/python37.zip', 
'/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7', 
'/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload', 
'/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages']

```

Once you’ve imported a module, you can determine the location where it was found with the module’s \_\_file\_\_ attribute:


```python
>>> sys.path.append(r'/Users/chris/ModulesAndPackages')
>>> sys.path
['', '/Library/Frameworks/Python.framework/Versions/3.7/bin', 
'/Library/Frameworks/Python.framework/Versions/3.7/lib/python37.zip', 
'/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7', 
'/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload', 
'/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages', 
'/Users/chris/ModulesAndPackages']
>>> import mod
>>> mod.s
'Computers are useless. They can only give you answers.'
```

The directory portion of \_\_file\_\_  should be one of the directories in sys.path.

### import

The simplest form is the one you already saw:

```python
import <module_name>
```

Note that this _does not_ make the module contents _directly_ accessible to the caller. Each module has its own **private symbol table**, which serves as the global symbol table for all objects defined _in the module_. So, a module creates a separate [**namespace**](https://realpython.com/python-namespaces-scope/).

The statement import only places in the caller’s symbol table. The **objects** that are defined in the module remain in the module’s private symbol table.

From the caller, objects in the module are only accessible when prefixed with via **dot notation**, as you’ll see below.

After the following import statement, **mod** is placed into the local symbol table. So, mod has meaning in the caller’s local context:

```python

>>> import mod
>>> mod
<module 'mod' from '/Users/chris/ModulesAndPackages/mod.py'>

```

But a, s, and printy() remain in the module’s private symbol table and are not meaningful in the local context:
```python
>>> a
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> s
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> printy
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    printy
NameError: name 'printy' is not defined


```

To be accessed in the local context, names of objects defined in the module must be prefixed by mod:

```python
>>> mod.a
[100, 200, 300]
>>> mod.s
'Computers are useless. They can only give you answers.'
>>> mod.printy('Hello')
arg = Hello

```

Several comma-separated modules may be specified in a single import statement:

```python
import <module_name>[, <module_name> ...]

```

### from import

An alternate form of the import statement allows individual objects from the module to be imported directly into the caller’s symbol table:

```python
from <module_name> import <name(s)>

```

Following execution of the above statement, <name(s)>  can be referenced in the caller’s environment without the <module_name> prefix:

```python
>>> from mod import s, printy
>>> s
'Computers are useless. They can only give you answers.'
>>> printy('Hello')
arg = Hello
```

Because this form of import places the object names directly into the caller’s symbol table, any objects that already exist with the same name will be **overwritten**:


```python
>>> a = ['abc', 'def', 'ghi']
>>> a
['abc', 'def', 'ghi']
>>> from mod import a
>>> a
[100, 200, 300]

```

It is even possible to indiscriminately import everything from a module in one fell swoop:

```python
from <module_name> import *

```

This will place the names of all objects from <module_name> into the local symbol table, with the exception of any that begin with the underscore (_) character:
```python
>>> from mod import *
>>> s
'Computers are useless. They can only give you answers.'
>>> a
[100, 200, 300]
>>> printy
<function printy at 0x03B449C0>
>>> Classy
<class 'mod.Classy'>

```

This isn’t necessarily recommended in large-scale production code. It’s a bit dangerous because you’re entering names into the local symbol table _en masse_. Unless you know them all well and can be confident there won’t be a conflict, you have a decent chance of overwriting an existing name inadvertently.

However, this syntax is quite handy when you’re just mucking around with the interactive interpreter, for testing or discovery purposes, because it quickly gives you access to everything a module has to offer without a lot of typing.

### from import as

It’s also possible to import individual objects but put them into the local symbol table with alternate names:
```python
from <module_name> import <name> as <alt_name>[, <name> as <alt_name> …]


```

This makes it possible to place names directly into the local symbol table but avoid conflicts with previously existing names:

```python
>>> a = ['abc', 'def', 'ghi']
>>> s = 'Hello There!'
>>> from mod import s as string, a as alist
>>> a
['abc', 'def', 'ghi']
>>> s
'Hello There!'
>>> string
'Computers are useless. They can only give you answers.'
>>> alist
[100, 200, 300]

```

### import as

You can also import an entire module under an alternate name:

```python
import <module_name> as <alt_name>

```
Here’s what that looks like in practice:

```python
>>> import mod as my_module
>>> my_module.a
[100, 200, 300]
>>> my_module.s
'Computers are useless. They can only give you answers.'

```

Module contents can be imported from within a function definition. In that case, the import does not occur until the function is **called**:

```python
>>> def importer():
...     from mod import printy
...     printy('Hello Everyone')
...

>>> mod
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    mod
NameError: name 'mod' is not defined
>>> printy
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    printy
NameError: name 'printy' is not defined
>>> importer()
arg = Hello Everyone

```

However, **Python 3** does not allow the indiscriminate **import \*** syntax from within a function:

```python
>>> def importer2():
...     from mod import *
  File "<bpython-input-11>", line 1
SyntaxError: import * only allowed at module level

```
Lastly, you can use a [try statement with an except ImportError](https://realpython.com/python-exceptions/) to guard against unsuccessful import attempts:

```python
>>> try:
...     # Non-existent module
...     import foo
... except ImportError:
...     print('Module not found')
...

Module not found

>>> try:
...     # Existing module, but non-existent object
...     from mod import bar
... except ImportError:
...     print('Object not found in module')
...

Object not found in module

```




