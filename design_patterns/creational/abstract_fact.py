# Abstract Factory Pattern Example in Python

"""
Abstract Factory Pattern

The Abstract Factory pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes.
It is useful when a system should be independent of how its products are created.

Why use Abstract Factory Pattern:
- When the system needs to be independent of how its objects are created.
- When families of related or dependent objects need to be used together.
- To provide a library of products without exposing implementation details.
"""

# Abstract Factory
class GUIFactory:
    def create_button(self):
        pass

    def create_checkbox(self):
        pass

# Concrete Factory 1
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()

# Concrete Factory 2
class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()

# Abstract Product A
class Button:
    def paint(self):
        pass

# Abstract Product B
class Checkbox:
    def paint(self):
        pass

# Concrete Product A1
class WindowsButton(Button):
    def paint(self):
        print("Render a button in Windows style.")

# Concrete Product B1
class WindowsCheckbox(Checkbox):
    def paint(self):
        print("Render a checkbox in Windows style.")

# Concrete Product A2
class MacButton(Button):
    def paint(self):
        print("Render a button in Mac style.")

# Concrete Product B2
class MacCheckbox(Checkbox):
    def paint(self):
        print("Render a checkbox in Mac style.")

# Client Code
class Application:
    def __init__(self, factory):
        self.factory = factory
        self.button = None
        self.checkbox = None

    def create_ui(self):
        self.button = self.factory.create_button()
        self.checkbox = self.factory.create_checkbox()

    def paint(self):
        self.button.paint()
        self.checkbox.paint()

# Usage
if __name__ == "__main__":
    # Suppose we get the OS type from a configuration or environment
    os_type = 'Windows'  # Or 'Mac'
    if os_type == 'Windows':
        factory = WindowsFactory()
    elif os_type == 'Mac':
        factory = MacFactory()
    else:
        raise Exception("Unknown OS Type")

    app = Application(factory)
    app.create_ui()
    app.paint()
    # Output if os_type is 'Windows':
    # Render a button in Windows style.
    # Render a checkbox in Windows style.
