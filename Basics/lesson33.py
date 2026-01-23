#Getter , Setter , Deleter Methods

class Person:
    def __init__(self,name):
        self._name=name

    @property #getter method so we can use this method like property
    def namef(self):
        return self._name
    
    @namef.setter #when we change this method will start
    def namef(self,new):
        if not new: #if new empty
            raise ValueError("Name cannot be empty") #raise ValueError() show an error
        self._name=new

    @namef.deleter #when we want del method this method will start
    def namef(self):
        print("Deleting...")
        self._name = None

obj=Person("F")
print(obj.namef) #not obj.method() because of @property

obj.namef="S" #using like property and setter start oto
print(obj.namef)

del obj.namef #using like property and deleter start oto
print(obj.namef)


#Metaprogramming

class Empty:
    ... #There is no method

def amethod(self): #Create a method for empty class
    print("Here")

Empty.new=amethod #add with name (new) this method
obj1=Empty()
obj1.new() #now we can use with name