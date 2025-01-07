The Logging Module
==================

The logging module in Python is a ready-to-use and powerful module that is designed to meet the needs of beginners as well as enterprise teams. It is used by most of the third-party Python libraries, so you can integrate your log messages with the ones from those libraries to produce a homogeneous log for your application.

Adding logging to your Python program is as straightforward as this:

import logging  

With the logging module imported, you can use something called a “logger” to log messages that you want to see. By default, there are 5 standard levels indicating the severity of events. Each has a corresponding method that can be used to log events at that level of severity.

The defined levels, in order of increasing severity, are the following:

*   DEBUG
    
*   INFO
    
*   WARNING
    
*   ERROR
    
*   CRITICAL


You can use the basicConfig(\*\*_kwargs_) method to configure the logging:

> You will notice that the logging module breaks PEP8 styleguide and uses camelCase naming conventions. This is because it was adopted from Log4j, a logging utility in Java. It is a known issue in the package but by the time it was decided to add it to the standard library, it had already been adopted by users and changing it to meet PEP8 requirements would cause backwards compatibility issues. [(Source)](https://wiki.python.org/moin/LoggingPackage)

Some of the commonly used parameters for basicConfig() are the following:

*   level: The root logger will be set to the specified severity level.
    
*   filename: This specifies the file.
    
*   filemode: If filename is given, the file is opened in this mode. The default is a, which means append.
    
*   format: This is the format of the log message.
    

By using the level parameter, you can set what level of log messages you want to record. This can be done by passing one of the constants available in the class, and this would enable all logging calls at or above that level to be logged.

### Summary: Using basicConfig() in Python's Logging Module

The basicConfig() method is used to configure the default logger in Python. Unlike most methods in Python, it uses camel casing due to its Java origins, where the logging module was initially developed. This non-PEP 8 naming convention was retained for backward compatibility with legacy Python code.

#### Key Parameters of basicConfig():

1.  **level**: Sets the minimum severity level to log (e.g., logging.DEBUG logs events at DEBUG level or higher).
    
2.  **filename**: Specifies a file to write log output to.
    
3.  **filemode**: Defines how the file should be opened:
    
    *   'a' (default): Appends new logs to the existing file.
        
    *   'w': Overwrites the file each time the program runs.
        
4.  **format**: Specifies the log message format. Common built-in variables include:
    
    *   name: Logger name.
        
    *   levelname: Event severity level.
        
    *   message: Log message.

#### Important Notes:

*   If basicConfig() is not explicitly called, it is implicitly called by the first severity function (e.g., logging.warning or logging.debug). After this implicit call, basicConfig() cannot be called again on the default logger.
    
*   To ensure proper configuration, always call basicConfig() before logging any events.
    

By understanding and leveraging basicConfig(), you can effectively configure Python's logging output for various use cases.


The format parameter in Python's basicConfig() method allows you to define how log messages are structured. While you can use custom variables, there are several built-in variables from the LogRecord metadata that can be included in the log format. The LogRecord contains information about the logging event, such as process details, severity level, and the message itself.

#### Key Built-In Variables for format:

1.  **process**: Process ID of the event.
    
2.  **levelname**: Severity level (e.g., DEBUG, INFO, WARNING).
    
3.  **message**: The log message.
    
4.  **asctime**: Timestamp of when the log was created.


Logging critical events, such as crashes, is essential for debugging large-scale applications. In Python, you can log stack traces using the exc\_info parameter or the logging.exception() method. Both approaches include detailed exception information in your logs, making it easier to diagnose issues.

#### Using exc\_info Parameter:

The exc\_info parameter (short for "exception info") can be set to True to include the stack trace in the log. If exc\_info is False (default), only the log message will be recorded.


```python
import logging

# Configure the logger
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

try:
    # Code that raises an exception
    result = 5 / 0
except ZeroDivisionError:
    # Log the exception with stack trace
    logging.error("Exception occurred", exc_info=True)
```


output:

```python
2024-12-20 14:00:00 - ERROR - Exception occurred
Traceback (most recent call last):
  File "example.py", line 10, in <module>
    result = 5 / 0
ZeroDivisionError: division by zero
```


#### Using logging.exception():

The logging.exception() method is a shorthand for logging an error message with exc\_info=True. It logs at the ERROR level by default.

**Example with logging.exception():**

```python
try:
    # Code that raises an exception
    result = 5 / 0
except ZeroDivisionError:
    # Log the exception using logging.exception()
    logging.exception("Exception occurred")
```

**Output:**(Same as the previous example)

#### Key Points:

1.  **exc\_info=True**: Use this parameter to include stack traces for any severity level (DEBUG, INFO, WARNING, etc.).

```python
logging.warning("A warning occurred", exc_info=True)
```

1.  **logging.exception()**: Equivalent to logging.error(exc\_info=True), but it always logs at the ERROR level.
    

#### Benefits:

*   Stack traces provide crucial details about where and why an error occurred.
    
*   Simplifies debugging in complex applications with multiple components.
    

Understanding and leveraging exc\_info and logging.exception() helps ensure your logs contain the detailed information needed to troubleshoot issues effectively.

### Custom Loggers in Python

By default, Python's logging module uses the root logger, which is sufficient for basic logging. However, robust applications often require custom loggers for more flexibility and control.

#### Key Classes in the Logging Module:

1. **Logger**: 
   - Represents a custom logger.
   - Allows customization and logging of events.

2. **LogRecord**: 
   - Automatically created by loggers for each logged event.
   - Contains metadata about the event, such as the logger name, function, line number, and message.
   - Populates the log output.

3. **Handler**: 
   - Sends LogRecord objects to specific output destinations.
   - Subclasses define the output type:
     - `StreamHandler`: Sends logs to `stdout`.
     - `FileHandler`: Logs to a file.
     - `SMTPHandler`: Sends logs via email.
     - `HTTPHandler`: Sends logs to a web server using HTTP methods.
   
4. **Formatter**: 
   - Specifies the string format of log output.

#### Example: Creating a Custom Logger

Here’s an example of creating a custom logger with output directed both to `stdout` and a file:

```python
import logging

# Create a custom logger
logger = logging.getLogger('example_logger')

# Set the default log level
logger.setLevel(logging.DEBUG)

# Create handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('example.log')

# Set levels for handlers
console_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.ERROR)

# Create a formatter and set it for the handlers
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Log some messages
logger.warning("This is a warning.")
logger.error("This is an error.")
```


1.  By default, the Python logging module uses the **root logger**, which is implicitly invoked when functions like logging.debug() or logging.error() are called. While this works for simple scripts, more robust applications with multiple modules benefit greatly from custom loggers.
    
2.  Defining your own logger provides better flexibility and modularity, especially when dealing with complex logging configurations.
    
3.  Key Classes in the Logging Module
    
4.  **Logger**:
    

6.  The central class used to create and manage loggers.
    
7.  Provides methods (debug(), info(), warning(), error(), critical()) to log events at different severity levels.
    
8.  Custom loggers can be instantiated using logging.getLogger(name).
    
9.  Calling logging.getLogger(name) multiple times with the same name returns a reference to the same logger, allowing shared usage without explicitly passing the logger object around.
    
10.  **LogRecord**:
    
    *   Automatically created by loggers for every logged event.
        
    *   Contains metadata about the event, such as:
        
        *   Logger name
            
        *   Function name
            
        *   Line number
            
        *   Severity level
            
        *   Log message
            
    *   This metadata populates the log output and helps in debugging.
        
11.  **Handler**:
    
    *   Responsible for sending LogRecord objects to specific output destinations.
        
    *   Acts as a base class for various output destinations, such as:
        
        *   **StreamHandler**: Sends logs to standard streams like stdout or stderr.
            
        *   **FileHandler**: Writes logs to files.
            
        *   **SMTPHandler**: Sends logs via email.
            
        *   **HTTPHandler**: Sends logs to a web server using HTTP.
            
    *   You can attach multiple handlers to a single logger to send logs to different destinations simultaneously.
        
12.  **Formatter**:
    
    *   Defines how log messages should appear by specifying a format string.
        
    *   Allows customization of log attributes, such as:
        
        *   %(name)s: Logger name.
            
        *   %(levelname)s: Severity level (DEBUG, INFO, etc.).
            
        *   %(message)s: Log message.
            
        *   %(asctime)s: Timestamp.
            
    *   Ensures logs are readable and informative.
        
13.  Why Use Custom Loggers?
    
14.  **Modularity**
    
15.  : Each module in your application can have its own logger, which helps isolate and organize logs.
    
16.  **Reusability**: The logging.getLogger(name) method ensures that multiple calls with the same name return the same logger object, avoiding redundancy and simplifying logger usage.
    
17.  **Flexibility**: By combining loggers, handlers, and formatters, you can direct logs to various outputs (console, files, external services) with custom formats.
    
18.  Example: Setting Up a Custom Logger

```python
import logging

# Create a custom logger
logger = logging.getLogger('custom_logger')

# Set the log level for the logger
logger.setLevel(logging.DEBUG)

# Create handlers for different outputs
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('app.log')

# Set levels for handlers
console_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.WARNING)

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Attach the formatter to the handlers
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Log messages
logger.debug("This is a DEBUG message (console won't log this).")
logger.info("This is an INFO message (logged to console).")
logger.warning("This is a WARNING message (logged to console and file).")
logger.error("This is an ERROR message (logged to console and file).")
```

### Comprehensive Guide: Building a Custom Logging System in Python

In complex applications, using custom loggers allows for greater control and flexibility compared to the default root logger. This guide demonstrates how to create a custom logger with multiple handlers, attach formatters to each handler, and log events to both the console and a file with different formatting and severity levels.

#### Steps to Create a Custom Logging System

1.  **Create a Custom Logger**:
    
    *   Use logging.getLogger(name) to create a custom logger.
        
    *   Pass \_\_name\_\_ as the logger name to track the module generating the logs.
        
2.  **Add Handlers**:
    
    *   Handlers determine where the logs are directed (e.g., console, file).
        
    *   Use StreamHandler for console output and FileHandler for file logging.
        
3.  **Set Severity Levels for Handlers**:
    
    *   Define the minimum severity level for each handler using setLevel().
        
    *   This ensures only events of the specified level or higher are logged to that handler.
        
4.  **Attach Formatters**:
    
    *   Formatters control the appearance of log messages.
        
    *   Define unique formats for each handler based on the log destination.
        
5.  **Link Handlers to the Logger**:
    
    *   Attach handlers to the logger using the addHandler() method.
        
6.  **Log Events**:
    
    *   Use the logger's severity level methods (debug(), info(), warning(), etc.) to log events.

```python
import logging

# Step 1: Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Set the minimum severity level for the logger

# Step 2: Create handlers
c_handler = logging.StreamHandler()  # Console handler
f_handler = logging.FileHandler('file.log')  # File handler

# Step 3: Set severity levels for each handler
c_handler.setLevel(logging.WARNING)  # Console: Log warnings and higher
f_handler.setLevel(logging.ERROR)    # File: Log errors and higher

# Step 4: Create formatters
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Attach formatters to handlers
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Step 5: Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

# Step 6: Log events
logger.debug("This is a DEBUG message")       # Not logged anywhere
logger.info("This is an INFO message")       # Not logged anywhere
logger.warning("This is a WARNING message")  # Logged to console
logger.error("This is an ERROR message")     # Logged to both console and file
```

### Key Features of the Example:

1.  **Logger Name**: The logger is named after the current module (\_\_name\_\_), making it easier to identify logs from different modules when the logger is used across a project.
    
2.  **Handler Levels**:
    
    *   Console logs events with severity WARNING and above.
        
    *   File logs events with severity ERROR and above.
        
3.  **Formatter Customization**:
    
    *   Console format: Displays logger name, severity level, and message.
        
    *   File format: Includes timestamp (asctime), logger name, severity level, and message.


### Configuring Loggers with Config Files in Python

Custom loggers are powerful, but managing configurations programmatically can become cumbersome in larger projects. Python's logging module allows you to define logger configurations in external files, making it easier to reuse or share settings. You can use fileConfig() or dictConfig() to load these configurations.

### Example: Using fileConfig() to Configure a Logger

1.  **Create a Configuration File (file.conf)**:This configuration defines loggers, handlers, and formatters.

```python
[loggers]
keys=root,sampleLogger

[handlers]
keys=consoleHandler

[formatters]
keys=sampleFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[logger_sampleLogger]
level=DEBUG
handlers=consoleHandler
qualname=sampleLogger
propagate=0

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=sampleFormatter
args=(sys.stdout,)

[formatter_sampleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
```
    
2.  **Python Code to Use the Config File:**

```python
import logging
import logging.config

# Load the configuration from the file
logging.config.fileConfig('file.conf', disable_existing_loggers=False)

# Create a logger from the configuration
logger = logging.getLogger(__name__)

# Log a debug message
logger.debug('This is a debug message')
```
### Explanation of Configuration File:

1.  **Loggers**:
    
    *   **root**: Configures the built-in root logger with a DEBUG level and the consoleHandler.
        
    *   **sampleLogger**: Configures a custom logger named sampleLogger with:
        
        *   DEBUG level
            
        *   consoleHandler
            
        *   A qualified name (qualname) for identification
            
        *   Propagation disabled (propagate=0)
            
2.  **Handlers**:
    
    *   **consoleHandler**:
        
        *   Class: StreamHandler (logs to stdout)
            
        *   Level: DEBUG
            
        *   Formatter: sampleFormatter
            
        *   Arguments: (sys.stdout,)
            
3.  **Formatters**:
    
    *   **sampleFormatter**: Defines how log messages are formatted.
        
        *   Format: Includes timestamp (asctime), logger name (name), severity level (levelname), and the log message (message).
            

### Output:

When the Python program is executed, the following will be logged to the console:

```python
2024-12-20 14:00:00,123 - __main__ - DEBUG - This is a debug message
```

### Benefits of Using Config Files:

1.  **Reusability**: Configurations can be reused across different projects or modules.
    
2.  **Separation of Concerns**: Keeps logging logic separate from application code.
    
3.  **Ease of Sharing**: Config files can be easily shared with team members.
    

### Key Notes:

*   **fileConfig()**:
    
    *   Reads from an .ini-style configuration file.
        
    *   Use disable\_existing\_loggers=False to prevent disabling other loggers when the configuration is loaded.
        
*   **Use Case**:
    
    *   Ideal for simple configurations or when working with pre-existing .ini files.
        

By externalizing your logger configuration into files, you enhance the maintainability and scalability of your logging setup.

If the **logger** and **handler** have different levels, both levels will influence which log messages are ultimately processed and output. Here’s how the levels interact:

### Key Points:

1.  **Logger Level**:
    
    *   Determines whether a log event should be passed to the handlers.
        
    *   If the logger's level is set to DEBUG, all events of level DEBUG and above (e.g., INFO, WARNING, etc.) will be passed to its handlers.
        
2.  **Handler Level**:
    
    *   Determines whether the handler will actually process the log event it receives from the logger.
        
    *   Even if the logger passes an event to the handler, the handler will only output events that meet or exceed its level.
        

### Example Scenario:

#### Config Details:

*   **Logger Level**: DEBUG (from \[logger\_sampleLogger\]).
    
*   **Handler Level**: WARNING (if you change the level in \[handler\_consoleHandler\] to WARNING).

```python
import logging
import logging.config

# Load the configuration from the file
logging.config.fileConfig('file.conf', disable_existing_loggers=False)

# Create a logger
logger = logging.getLogger('sampleLogger')

# Log events of different levels
logger.debug("This is a DEBUG message")   # Level: DEBUG
logger.info("This is an INFO message")   # Level: INFO
logger.warning("This is a WARNING message")  # Level: WARNING
logger.error("This is an ERROR message")  # Level: ERROR
```
#### Behavior:

*   **Logger**:
    
    *   Since the logger's level is DEBUG, all messages (DEBUG, INFO, WARNING, ERROR) are passed to the consoleHandler.
        
*   **Handler**:
    
    *   If the handler's level is WARNING, only messages at level WARNING and above are processed.
        
    *   As a result, the DEBUG and INFO messages are ignored by the handler.

```python
2024-12-20 14:00:00,123 - sampleLogger - WARNING - This is a WARNING message
2024-12-20 14:00:01,123 - sampleLogger - ERROR - This is an ERROR message
```


### Summary of Logger and Handler Level Interaction:

1.  **Logger Level < Handler Level**:
    
    *   Events below the handler's level are ignored, even if the logger passes them.
        
    *   Example: Logger level = DEBUG, Handler level = WARNING.
        
        *   Only WARNING and higher events are logged.
            
2.  **Logger Level ≥ Handler Level**:
    
    *   All events meeting the handler's level are processed and output.
        
    *   Example: Logger level = WARNING, Handler level = WARNING.
        
        *   All WARNING and higher events are logged.
            
3.  **Logger Level Only**:
    
    *   If the logger's level is stricter (e.g., INFO), no events below INFO are even passed to the handler, regardless of the handler’s level.


### Best Practices:

*   Ensure the **logger level** is less restrictive or equal to the **handler level** for maximum flexibility.
    
*   Use **handler levels** to control what is logged to specific destinations:
    
    *   Example: Debugging info to a file (DEBUG handler), while only warnings appear in the console (WARNING handler).

### Configuring Loggers Using the Dictionary Approach in Python

Using a dictionary configuration to set up loggers in Python is a powerful and flexible alternative to .ini configuration files. This method allows for the definition of complex configurations, often stored in YAML files, which can then be loaded and used by the dictConfig() function from the logging.config module.

### Steps to Configure Logging with a YAML File

#### 1\. **Create the YAML Configuration File (config.yaml)**

This YAML file defines formatters, handlers, and loggers.

```yaml
version: 1
formatters:
  simple:
    format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

handlers:
  console:
    class: logging.StreamHandler
    level: DEBUG
    formatter: simple
    stream: ext://sys.stdout

loggers:
  sampleLogger:
    level: DEBUG
    handlers: [console]
    propagate: no

root:
  level: DEBUG
  handlers: [console]
```
**Explanation:**

*   **formatters**:
    
    *   Defines a formatter named simple with a specific format string.
        
*   **handlers**:
    
    *   Defines a console handler using the StreamHandler class.
        
    *   Outputs logs to stdout at the DEBUG level using the simple formatter.
        
*   **loggers**:
    
    *   Defines a custom logger named sampleLogger:
        
        *   Level: DEBUG
            
        *   Handlers: \[console\]
            
        *   Propagation: Disabled (propagate: no).
            
*   **root**:
    
    *   Configures the root logger to use the same console handler at the DEBUG level.

2\. **Python Code to Load and Use the YAML Configuration**

```python
import logging
import logging.config
import yaml

# Install PyYAML if not already installed: pip install PyYAML

# Load the YAML configuration file
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f.read())

# Configure the logger using the dictionary configuration
logging.config.dictConfig(config)

# Create a custom logger
logger = logging.getLogger('sampleLogger')

# Log a debug message
logger.debug('This is a debug message')
```
### Output:

#### Console Output:
```python
2024-12-20 14:00:00,123 - sampleLogger - DEBUG - This is a debug message
```
### Key Steps and Concepts:

1.  **YAML Configuration**:
    
    *   Use a YAML file to define the entire logging setup, including formatters, handlers, loggers, and root logger.
        
2.  **Loading YAML**:
    
    *   Use the PyYAML library to read and parse the YAML file.
        
    *   Load the file with yaml.safe\_load() to convert the YAML into a Python dictionary.
        
3.  **Dictionary Configuration**:
    
    *   Pass the dictionary to logging.config.dictConfig() to configure the logging system.
        
4.  **Logger Usage**:
    
    *   Retrieve the logger (sampleLogger) using logging.getLogger(name).
        
    *   Use logger methods like debug(), info(), and error() to log events.
        

### Advantages of the Dictionary Approach:

*   **Flexibility**: Easily support dynamic configurations.
    
*   **Modularity**: YAML or JSON files can be updated or replaced without changing the code.
    
*   **Reusability**: Configuration files can be shared across projects or teams.
    
*   **Clarity**: YAML provides a clean, readable structure for complex configurations.


In Python's logging module, the **style** parameter is used to define the type of placeholder for your format string. The style parameter specifies which style of string formatting to use when configuring a Formatter.

### Accepted Values for style:

*   '%' (default): Uses the %-style placeholders (e.g., '%(levelname)s').
    
*   '{': Uses str.format-style placeholders (e.g., '{levelname}').
    
*   '$': Uses string.Template-style placeholders (e.g., '$levelname').

```python
import logging

# Configure the logger
formatter = logging.Formatter(
    fmt='{asctime} - {name} - {levelname} - {message}', 
    style='{'
)

handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger = logging.getLogger('example')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

# Log a message
logger.debug('This is a debug message')
```
Output:
```python
2024-12-20 14:00:00,123 - example - DEBUG - This is a debug message
```
### Notes:

*   By default, the logging module uses the '%' style, so you don’t need to specify style='%' unless you want to make it explicit.
    
*   The style parameter is particularly useful if you prefer the more modern str.format syntax or string.Template style for custom logging formats.

[This is the code of the logging module](https://github.com/python/cpython/blob/d730719b094cb006711b1cd546927b863c173b31/Lib/logging/__init__.py#L804)

[Python Logging Flow Documentation](https://docs.python.org/3.5/howto/logging.html#logging-flow)
