class MyClass:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    # Mohamed Essawey
    def generate_fibonacci(*,N):
        a, b = 0, 1
        for _ in range(N):
            print(a, end=' ')
            a, b = b, a + b


# Creating an instance of the class
MyClass_Obj = MyClass(value = "Hello, World!")

# Mohamed Essawey - 202000440
MyClass_Obj.generate_fibonacci(N = 10)


# Accessing the class attribute and method
print(MyClass_Obj.get_value())  # Output: Hello, World!
