#Aggregation--------------------------------------------------------------------------
class Employee:
    def __init__(self,n,id):
        self.name=n
        self.id=id

class Department:
    def __init__(self,n):
        self.depname=n
        self.emplo=[] #Aggregation

    def add_employee(self,emp):
        self.emplo.append(emp)
    
    def show(self):
        for i in self.emplo:
            print(f"{i.name} / {i.id}")

e1=Employee("F",132)
e2=Employee("S",235)

obj=Department("Software")

obj.add_employee(e1)
obj.add_employee(e2)

obj.show()

#Connection between them is weak

#Aggregation--------------------------------------------------------------------------
print()
#Composition--------------------------------------------------------------------------

class Employee:
    def __init__(self,n,id):
        self.name=n
        self.id=id

class Department:
    def __init__(self,n,employee):
        self.depname=n
        self.emplo=[Employee(e[0],e[1]) for e in employee] #Composition

    def add_employee(self,emp):
        self.emplo.append(emp)
    
    def show(self):
        for i in self.emplo:
            print(f"{i.name} / {i.id}")

obj=Department("Software",[("F",132),("S",235)])

obj.show()


#Connection between them is strong

#Composition--------------------------------------------------------------------------