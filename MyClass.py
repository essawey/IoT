class MyClass:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

    def generate_fibonacci(self):
        a, b = 0, 1
        fibonacci_list = []
        for _ in range(self.value):
            fibonacci_list.append(a)
            a, b = b, a + b
        return fibonacci_list



MyClass_Obj = MyClass(value=10)

print(MyClass_Obj.generate_fibonacci())
