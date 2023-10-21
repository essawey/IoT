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


MyClass_Obj = MyClass(value=10)

MyClass_Obj.generate_fibonacci()

print("Current Value:", MyClass_Obj.get_value())

MyClass_Obj.set_value(20)

print("Updated Value:", MyClass_Obj.get_value())
