#Inheritance

class Person: #Parent/Base class
    def __init__(self,n,s): #constructor of base
        self.name=n
        self.surname=s

    def cout(self): #method of parent
        print(f"Hello {self.name} {self.surname}")


class Student(Person): #Child/derived class
    #Inheriting parent class

    def __init__(self,n,s,y): #Dont take constructor use this one
        super().__init__(n,s) #super(). means take this one

        self.grad=y #a new property
    
    def consolw(self): #a new method
        print(f"Graduation year: {self.grad}")


obj=Student("Fatih","Sahino","2026") #although this parent's constructor we can use like student's own
obj.cout() #thanks to intherance we can use this even if student has not this method
obj.consolw()