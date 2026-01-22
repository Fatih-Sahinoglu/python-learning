#Polymorphism

class Shape:
    def area(self): #raise NotImplementError() means if a child don't have this method show an error
        raise NotImplementedError("Child class must have this method")
    
class Circle(Shape):
    def __init__(self,r):
        self.radius=r
        
    def area(self):
        return self.radius*self.radius*3.14

class Square(Shape):
    def __init__(self,l):
        self.length=l

    def area(self):
        return self.length*self.length
    
obj=[Circle(5),Square(10)] #object of all this

for i in obj: # Polymorphism: same method name, different behavior
    print(f"Area = {i.area()} cm²") #for ² alt 0178