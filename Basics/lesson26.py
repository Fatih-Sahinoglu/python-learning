#Encapsulation

# Public do nothing and you can accesses everywhere
# Protected _x and you can accesses just child class(actually everywhere but you shouldn't)
# Private __x and just that class (_classname_privateone then we can use)

class Animal: # base - parent class
    def __init__(self,n,s):
        self.name=n # public attribute property
        self._species=s #protected attribute property

    def _makeSound(self): # protected method
        return "Animal sound"
    
    def __name(self): #private so we can use like obj.__name() can used in this class
        print("Hello",self.name)


class Dog (Animal): #child-derived class
    def __init__(self, n, b):
        super().__init__(n, "Dog") #species is "Dog"
        self.breed=b

    def display_info(self): # public method
        return f"Dog name: {self.name}, Breed: {self.breed}, Species: {self._species}"

    def make_sound(self): # public method

        return self._makeSound() # protected method

dog=Dog("Kurt", "Golden Retriever")
print(dog._makeSound())
