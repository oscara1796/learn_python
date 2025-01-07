Using Breakpoints with pdb
==========================

Introduction to Breakpoints
---------------------------

Breaking into the debugger can be achieved with a single line of Python code:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   import pdb; pdb.set_trace()   `

When execution reaches this point in the program, the program stops, and you’re dropped into the pdb debugger. This is effectively the same as inserting a breakpoint on the line below where set\_trace() is called. Execution will stop right before that line of code is executed.

### The breakpoint() Function

If you’re using Python 3.7 or later, there’s an even easier way:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   breakpoint()   `

This function works in the same way as pdb.set\_trace() but has added flexibility. It automatically imports pdb and calls set\_trace() for you.

#### Advantages of breakpoint():

*   **Customizable Behavior**: You can modify its behavior by changing environment variables.
    
*   **Enable/Disable Breakpoints**: You can enable or disable all breakpoints before your script runs, avoiding the need to comment out breakpoint() calls manually.
    

### Post-Mortem Debugging

pdb also supports post-mortem debugging, which allows you to enter the debugger without modifying the code. No need for breakpoint() or set\_trace() calls.

To start post-mortem debugging:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`python3 -m pdb` 

This is particularly useful for debugging scripts you don’t have write access to.

Example: Setting a Breakpoint
-----------------------------

Here’s an example using the set\_trace() function:

### Example Code (example1.py):

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   filename = __file__  import pdb; pdb.set_trace()  print(f"This script is named: {filename}")   `

### Running the Script:

Run the script in your terminal:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   ./example1.py   `

### Debugger Output:

When you reach the breakpoint, you’ll see output similar to this:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   > /path/to/example1.py(5)()  -> print(f"This script is named: {filename}")   `

*   The angled bracket (>) indicates the context of the breakpoint.
    
*   The line number and module name (or function name, if applicable) are displayed.
    
*   The arrow (->) points to the line where the breakpoint is set.
    

### Inspecting Variables:

To inspect a variable, use the p command followed by the variable name:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   p filename   `

Output:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   '/path/to/example1.py'   `

### Exiting the Debugger:

To exit the interactive debugger, use the q command. Note that you may see a traceback, which can be ignored.

Key Takeaways
-------------

*   Breakpoints can be set using pdb.set\_trace() or breakpoint().
    
*   Post-mortem debugging allows you to debug scripts without modifying the code.
    
*   The p command lets you inspect variable values within the debugger.
    

Great job following along! Next, we’ll explore more advanced uses of the p command to deepen our debugging skills.