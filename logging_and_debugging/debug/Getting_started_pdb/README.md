Using Breakpoints with pdb
==========================

Introduction to Breakpoints
---------------------------

Breaking into the debugger can be achieved with a single line of Python code:

```python
import pdb; pdb.set_trace()   
```

When execution reaches this point in the program, the program stops, and you’re dropped into the pdb debugger. This is effectively the same as inserting a breakpoint on the line below where set\_trace() is called. Execution will stop right before that line of code is executed.

### The breakpoint() Function

If you’re using Python 3.7 or later, there’s an even easier way:

```python  
breakpoint()   
```

This function works in the same way as pdb.set\_trace() but has added flexibility. It automatically imports pdb and calls set\_trace() for you.

#### Advantages of breakpoint():

*   **Customizable Behavior**: You can modify its behavior by changing environment variables.
    
*   **Enable/Disable Breakpoints**: You can enable or disable all breakpoints before your script runs, avoiding the need to comment out breakpoint() calls manually.
    

### Post-Mortem Debugging

pdb also supports post-mortem debugging, which allows you to enter the debugger without modifying the code. No need for breakpoint() or set\_trace() calls.

To start post-mortem debugging:

```python 
python3 -m pdb <script_name>
``` 

#### How It Works

Post-mortem debugging is initiated when your program encounters an unhandled exception. The debugger will pause execution and drop you into the interactive debugging mode, allowing you to investigate the state of the program at the moment the exception occurred.

You can:

*   Inspect the stack trace to identify where the error originated.
    
*   Examine the values of variables to understand the program's state at the time of failure.
    
*   Step through the code to analyze the flow leading to the exception.
    

#### Advantages

*   **No Code Modification Required**: Ideal for debugging third-party scripts or production code you cannot modify.
    
*   **Quick Error Analysis**: Provides immediate insight into the root cause of runtime errors without prior setup.
    
*   **Works with Any Python Script**: Can be used with any Python program, even those not designed for debugging.

#### Example

Consider a script example2.py with the following content:

```python
def divide(a, b):
    return a / b

result = divide(10, 0)
```
Running this script normally would result in a ZeroDivisionError. To debug it with post-mortem debugging:

```python
python3 -m pdb example2.py
```
When the exception occurs, you’ll see output like this:

```python
Traceback (most recent call last):
  File "example2.py", line 4, in <module>
    result = divide(10, 0)
  File "example2.py", line 2, in divide
    return a / b
ZeroDivisionError: division by zero
> example2.py(2)divide()
-> return a / b
```

Now you’re in the interactive debugger and can:

*   Use p to inspect variables (p a, p b).
    
*   Use up and down to navigate the stack trace.
    
*   Use l to view surrounding lines of code.
    

#### Limitations

*   **Post-Mortem Only**: You can only debug after an exception occurs.
    
*   **Read-Only**: While you can inspect variables and navigate the stack, you cannot change the code or program state.
    

Despite these limitations, post-mortem debugging is a powerful tool for diagnosing issues in scripts where you cannot set traditional breakpoints.


Example: Setting a Breakpoint
-----------------------------

Here’s an example using the set\_trace() function:

### Example Code (example1.py):

```python  
filename = __file__  import pdb; pdb.set_trace()  print(f"This script is named: {filename}")   
```

### Running the Script:

Run the script in your terminal:

```python  
./example1.py   
```

### Debugger Output:

When you reach the breakpoint, you’ll see output similar to this:

```python  
> /path/to/example1.py(5)()  -> print(f"This script is named: {filename}")   
```

*   The angled bracket (>) indicates the context of the breakpoint.
    
*   The line number and module name (or function name, if applicable) are displayed.
    
*   The arrow (->) points to the line where the breakpoint is set.
    

### Inspecting Variables:

To inspect a variable, use the p command followed by the variable name:

```python  
p filename   
```

Output:

```python  
'/path/to/example1.py'   
```

### Exiting the Debugger:

To exit the interactive debugger, use the q command. Note that you may see a traceback, which can be ignored.

Key Takeaways
-------------

*   Breakpoints can be set using pdb.set\_trace() or breakpoint().
    
*   Post-mortem debugging allows you to debug scripts without modifying the code.
    
*   The p command lets you inspect variable values within the debugger.
    

Great job following along! Next, we’ll explore more advanced uses of the p command to deepen our debugging skills.