class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
       
    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, value):
        if value < 0:
            self._speed = 0
        else:
            self._speed = value
                
    def accelerate(self, increase):
        self.speed += increase
        print(f"{self.brand} accelerated to {self.speed} km/h.")
        
    def brake(self, decrease):
        self.speed -= decrease
        print(f"{self.brand} slowed down to {self.speed} km/h.")

    def __str__(self):
        return f"{self.brand} going at {self.speed} km/h"
        
c1 = Car("Toyota", 0)
c1.accelerate(80)  # Output: Toyota accelerated to 80 km/h.
c1.brake(100)       # Output: Toyota slowed down to 0 km/h.
print(c1)  # Output: Toyota going at 0 km/h