class car: #parent1
    def move(self):
        return "earth"
    
class ship: #parent2
    def move(self):
        return "water"
    
class skeleton(car): #child
    pass

class plane(car,ship): #child of both

    def move(self): #method overriding dont use others even though same name
        return "Both"
    

obj=plane()
print(obj.move()) #"Both"

isinstance(obj,plane) #True because plane's object
isinstance(obj,car) #True becuse car parent of plane

issubclass(skeleton,car) #True because skeleton is child of car