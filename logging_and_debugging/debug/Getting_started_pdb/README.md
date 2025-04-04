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

### Debugging with pdb: Using n (next) and s (step)

When debugging Python code with the pdb (Python Debugger) tool, there are two essential commands to navigate through the code: n (short for **next**) and s (short for **step**). These commands allow developers to control how they move through the program during execution.

The n command is equivalent to **step over**, meaning it moves to the next line of code, skipping the execution of any function calls on the current line. On the other hand, the s command is equivalent to **step into**, allowing you to dive into the code of a function call and examine its inner workings.

Here’s an example of how these commands work:

#### Example Script: example3

In this demonstration, the script includes a breakpoint set at **line 14**, where the program halts execution. Before the breakpoint, a variable filename\_path is assigned the relative file path returned by the get\_path() function, which is then printed.

1.  **Using n (next):**
    
    *   After hitting the breakpoint at line 14, typing n skips the execution of the get\_path() function call. The program moves directly to the print() line.
        
    *   At this point, the variable filename\_path can be inspected by typing p filename\_path. The output shows '.', representing the current directory, since the script is located there.
        
    *   By skipping the function call, the debugger avoids entering the internal details of the get\_path() function.
        
2.  **Using s (step into):**
    
    *   Restarting the program and typing s at the breakpoint at line 14 results in stepping into the get\_path() function. This action is marked by the --Call-- message in the debugger output, indicating that the program is entering a function call.
        
    *   The debugger shows the function definition on **line 6**. From here, you can use n to proceed line by line within the function or press Enter to repeat the last n command.
        
    *   Upon reaching the return statement in the get\_path() function, the debugger displays a --Return-- message. This output also shows the value being returned by the function (in this case, '.'), represented by the arrow (->) following the function name.
        
    *   Continuing with n, the debugger exits the function and returns to the main program. The print() statement is executed, displaying path = . in the console output.
        
3.  **Exiting the Debugger:**
    
    *   After completing execution at the module level, the debugger shows a --Return-- message, indicating the return from the module, which yields a NoneType. Typing Enter again concludes the debugging session.
        

#### Summary of Key Commands:

*   **n (next):** Moves to the next line of code, skipping any function calls.
    
*   **s (step):** Steps into a function call, allowing you to debug the function’s code line by line.
    
*   **p (print):** Prints the value of a variable or expression.
    
*   **q (quit):** Exits the debugger.
    

By combining these commands, developers can effectively trace program execution, inspect variable values, and debug their code with precision. This approach is especially useful for identifying and fixing issues in complex scripts or functions.

### Advanced Debugging with pdb: Setting and Managing Breakpoints

Debugging often requires flexibility to efficiently navigate through code, especially when you want to skip unnecessary lines or set new breakpoints while already debugging. The Python Debugger (pdb) makes this process straightforward with commands for setting breakpoints, continuing execution, and even creating conditional breakpoints. Here's a detailed explanation of these features:

#### Setting New Breakpoints During Debugging

After hitting an initial breakpoint, you can set additional breakpoints and continue execution up to those points without stepping through every line. This is useful for targeting specific areas in your code.

##### Example Scenario

In the example, there are two files:

1.  example4.py: The main script importing a module.
    
2.  util.py: A separate module containing the get\_path() function from earlier.
    
3.  **Setting a New Breakpoint in a Module:**
    
    *   Run the example4.py script, and execution stops at the breakpoint on **line 7**.
        
    *   To set a new breakpoint at **line 5** of the util module, use the command: 
    ```python
        b util:5
    ```
    *  This tells pdb to create a breakpoint in the util module at line 5. The debugger confirms the breakpoint creation.
    
2.  **Continuing Execution:**
    
    *   Use the c command to continue execution until the newly set breakpoint is hit. In this case, the debugger halts at the return line of get\_path().
        
3.  **Listing and Managing Breakpoints:**
    
    *   Type b to view all active breakpoints. Each breakpoint is assigned a number and shows how many times it has been hit.
        
    *   Manage breakpoints with the following commands:
        
        *   **enable** : Enable a specific breakpoint.
            
        *   **disable** : Disable a specific breakpoint.
            
        *   **cl** : Clear (delete) a specific breakpoint.
            

#### Using Conditional Breakpoints

Conditional breakpoints allow execution to halt only when a specified condition is met. This feature is particularly helpful for debugging specific scenarios.

##### Example Scenario with Conditional Breakpoints

The get\_path() function is expected to return an absolute path, which always starts with a forward slash (/) on Unix-based systems. If the path is not absolute, debugging is triggered.

1.  **Setting a Conditional Breakpoint:**
    
    *   Restart the program and set a conditional breakpoint using: 
    ```python
        b util.get_path, not filename.startswith('/')
    ```
    * This sets a breakpoint at the start of the get\_path() function, but only when the filename argument does not begin with /.
    
    *  **Continuing Execution:**
        
        *   Run the script again. Execution stops at the conditional breakpoint because the filename starts with a . (relative path) instead of /.
            
    *  **Inspecting Function Arguments:**
        
        *   Use the a command to view arguments passed to the function. This confirms that the filename provided does not meet the condition for an absolute path.
            

#### Important Notes on Conditional Breakpoints

*   When setting breakpoints by function name (e.g., b util.get\_path), the conditional expression should reference only variables or arguments available at the start of the function. Using undefined variables will cause the debugger to halt unconditionally.
    
*   Conditional breakpoints are a powerful tool for targeting specific behaviors without cluttering the debugging process with unnecessary stops.
    

#### Summary of Key Commands

*   **b :**: Sets a breakpoint at a specific line in a file.
    
*   **b ,** : Sets a conditional breakpoint that triggers only if the condition evaluates to True.
    
*   **c (continue):** Resumes execution until the next breakpoint.
    
*   **a (args):** Displays the arguments passed to the current function.
    
*   **b (list breakpoints):** Lists all active breakpoints.
    
*   **enable/disable** : Enables or disables the specified breakpoint.
    
*   **cl** : Clears a specific breakpoint.
    

By combining these commands, you can efficiently debug complex scripts, focus on specific code sections, and handle conditional scenarios with ease. For more information on breakpoints and advanced pdb features, refer to the video notes or the official Python documentation.

### Understanding the unt Command in pdb

The unt (short for **until**) command in the Python Debugger (pdb) allows you to continue program execution up to a specific point in your code. Its behavior depends on whether or not a line number is supplied, offering flexible ways to navigate through loops or skip sections of code without stepping through every single line.

#### Overview of unt

1.  **With a Line Number**:
    
    *   When you supply a line number to the unt command, execution will continue until a line with a number **greater than or equal to the specified line** is reached.
        
    *   This is similar to the c (continue) command, but with unt, you explicitly define where to stop.
        
2.  **Without a Line Number**:
    
    *   If no line number is supplied, unt will behave like the n (next) command, stopping at the **next line with a number greater than the current one**.
        
    *   The key difference between n and unt is that n stops at the next logically executed line, while unt strictly moves forward to a line with a higher number.
        

#### Example Usage with a For Loop

To demonstrate the unt command, consider a file named example4unt.py. This script contains the familiar get\_path() function, but with an added **for loop** that iterates through each character in a string called tail.

1.  **Starting the Debugger**:
    
    *   Run the program with ./example4unt.py, and execution halts at a breakpoint.
        
    *   To view the function's contents, use the ll (long list) command. This highlights the current line of execution with an arrow (->).
        
2.  **Using unt Without a Line Number**:
    
    *   Typing unt at this point behaves like n, advancing execution to the next line. This takes you to the start of the for loop.
        
    *   Pressing Enter implicitly runs unt again, advancing to the next iteration of the loop. Continue pressing Enter until you exit the loop entirely.
        
3.  **Skipping the Entire Loop**:
    
    *   Using n in a loop iterates one step at a time, requiring repeated commands to go through each iteration. In contrast, unt automatically completes the loop, advancing execution to the next line after the loop.
        
    *   This can save significant time and effort when debugging code with multiple iterations.
        
4.  **Validating Execution**:
    
    *   After exiting the loop, use p char, tail to inspect the values of char and tail. The char variable will now hold the last character in the tail string, confirming that the loop executed completely.
        

#### Key Points

*   **unt with a Line Number**: Acts as a targeted c command, continuing execution until a specific line.
    
*   **unt Without a Line Number**: Functions like n, but strictly moves forward to a higher line number, skipping over loops or repetitive blocks of code.
    
*   **Efficiency in Loops**: By skipping over entire loops or repetitive sections, unt streamlines the debugging process and eliminates the need for multiple n commands.
    

#### Commands Summary

*   **unt \[line\_number\]**: Continue execution until the specified line number (or the next higher line if no number is provided).
    
*   **n**: Moves to the next logical line of execution.
    
*   **ll**: Displays the function or module's code, showing the current execution line with an arrow.
    
*   **p** : Prints the value of a variable for inspection.
    
*   **Enter**: Repeats the last executed command, such as unt.
    

By leveraging the unt command effectively, you can streamline your debugging sessions and focus on areas of interest without unnecessary stops. This flexibility is particularly valuable in loops or when working through iterative code structures.