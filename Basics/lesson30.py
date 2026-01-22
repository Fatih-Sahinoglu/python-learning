#Nested class

class Car:
    def __init__(self,b,m,h,f):
        self.brand=b
        self.model=m
        
        self.obj=Car.Engine(h,f) 
        #Creating an object of Engine with parameters which we get from constructor
    def show(self):
        print(f"Car: {self.brand} {self.model}")
        self.obj.detail() #Spawning engine's function
    class Engine: #inner class
        def __init__(self,h,f):
            self.type="FS10"
            self.hp=h
            self.fuel=f
        def detail(self):
            print(f"Engine: {self.type} {self.hp}hp {self.fuel}")

objc=Car("BMW","I7",100,"Petrol")
objc.show()