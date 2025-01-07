Object-Oriented Programming (OOP) in Python: Classes and Objects
================================================================

Welcome Back
------------

In the previous discussion, we explored the fundamentals of Object-Oriented Programming (OOP) and the problems it solves. Now, let’s dive into how we can define and use our own objects in Python programs using classes.

Understanding Classes and Objects
---------------------------------

To create objects in Python, we use **classes**. A class is a blueprint for creating objects. It defines the structure and behavior that the objects will have. For example:

```python
# Creating a class
class Door:
    def __init__(self, height, color, is_locked):
        self.height = height
        self.color = color
        self.is_locked = is_locked

    def open(self):
        print("The door is open.")

    def close(self):
        print("The door is closed.")

    def toggle_lock(self):
        self.is_locked = not self.is_locked
        print(f"The door is now {'locked' if self.is_locked else 'unlocked'}.")

# Instantiating a Door object
front_door = Door(85, "red", False)
print(front_door.color)  # Output: red
front_door.toggle_lock()  # Output: The door is now locked.
```
### Instantiation

The process of creating an object from a class is called **instantiation**. Here, front\_door is an instance of the Door class, and it has its own unique properties and behaviors.

### Objects Are Independent

Each object created from a class is independent. For instance:

```python
back_door = Door(80, "blue", True)
print(back_door.color)  # Output: blue
back_door.toggle_lock()  # Output: The door is now unlocked.
```

The properties of back\_door are distinct from those of front\_door. Changing one object does not affect the other.

Everything in Python is an Object
---------------------------------

In Python, **everything is an object**. Variables like integers, strings, lists, and even functions are objects under the hood. Let’s take a closer look:

### Example: int and max

*   The int class is a blueprint for creating integer objects.

```python
num = int(5)  # Instantiates an integer object of type 'int'
print(type(num))  # Output: <class 'int'>
```
The max function is a callable object. Built-in functions in Python are instances of the builtin\_function\_or\_method class.

```python
print(type(max))  # Output: <class 'builtin_function_or_method'>
```

### Under the Hood

When you use a built-in function like int() or max(), Python performs several steps internally:

1.  It looks up the class definition in its namespace.
    
2.  It calls the \_\_call\_\_ method of the class (for callable objects).
    
3.  The \_\_new\_\_ method allocates memory for the object.
    
4.  The \_\_init\_\_ method initializes the object’s attributes.
    

This process ensures that even built-in types and functions adhere to Python’s object-oriented principles.

Real-World Use Cases of Classes
-------------------------------

Classes and objects are incredibly useful for modeling real-world entities and managing complex systems. Here are some examples:

*   **E-Commerce**: Classes for User, Product, Cart, etc.
    
*   **Gaming**: Classes for Character, Weapon, Level, etc.
    
*   **Data Analysis**: Classes for Dataset, Model, Visualization, etc.

