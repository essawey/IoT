class MyClass:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

    def generate_fibonacci(self):
        a, b = 0, 1
        for _ in range(self.value):
            print(a, end=' ')
            a, b = b, a + b
        else:
          print()

# Creating an instance of the class
MyClass_Obj = MyClass(value=10)

# Calling the instance method
MyClass_Obj.generate_fibonacci()

# Accessing the class attribute
print("Current Value:", MyClass_Obj.get_value())

# Setting a new value
MyClass_Obj.set_value(20)

# Accessing the updated value
print("Updated Value:", MyClass_Obj.get_value())
