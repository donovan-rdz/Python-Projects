class Dog:
    def bark(self):
        print("Woof!")
        
    def run(self):
        self.bark()

dog = Dog()
dog.run()