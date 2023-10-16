class MyClass:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

# Creating an instance of the class
obj = MyClass("Hello, World!")

# Accessing the class attribute and method
print(obj.get_value())  # Output: Hello, World!
