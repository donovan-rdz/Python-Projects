class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.") 
        
p1 = Person("Alonso", 30)
p2 = Person("Maria", 25)

p1.greet()  # Output: Hello, my name is Alonso and I am 30 years old.
p2.greet()  # Output: Hello, my name is Maria and I am 25 years old.