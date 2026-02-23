class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
        
    def accelerate(self, increase):
        self.speed += increase
        print(f"{self.brand} accelerated to {self.speed} km/h.")
        
    def brake(self, decrease):
        self.speed -= decrease
        if self.speed < 0:
            self.speed = 0
        print(f"{self.brand} slowed down to {self.speed} km/h.")

    def info(self):
        print(f"Car Brand: {self.brand}, Going at: {self.speed} km/h")
        
c1 = Car("Toyota", 0)
c1.accelerate(80)  # Output: Toyota accelerated to 80 km/h.
c1.brake(100)       # Output: Toyota slowed down to 0 km/h.
c1.info()  # Output: Car Brand: Toyota, Going at: 0 km/h