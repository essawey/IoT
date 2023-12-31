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

    def check_prime(self):
        if self.value <= 1:
            return False
        elif self.value == 2:
            return True
        else:
            for i in range(2, int(self.value ** 0.5) + 1):
                if self.value % i == 0:
                    return False
            return True

    def prime_factors(self):
        factors = []
        num = self.value
        divisor = 2
        while divisor <= num:
            if num % divisor == 0:
                factors.append(divisor)
                num = num // divisor
            else:
                divisor += 1
        return factors
    
    def squareRoot(self):
        return self.value ** 0.5


    def Power(self):
        return self.value ** 2

    

        


MyClass_Obj = MyClass(value=10)

# Mohamed Essawey
print(MyClass_Obj.generate_fibonacci())

# Amira Ahmed
print(MyClass_Obj.check_prime())

# Esraa Negm
print(MyClass_Obj.prime_factors())

# Rawan Elframawy
print(MyClass_Obj.squareRoot())

# Samaa Maged 
print(MyClass_Obj.Power())
