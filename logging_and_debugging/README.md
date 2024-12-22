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