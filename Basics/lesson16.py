#Functions


def hello(): #def name(parameters):
    print("Hello from 16.py lesson!")

hello() #function call


def hello2(parameter1,parameter2,parameter3):
    print(parameter1,parameter2,parameter3,"Thats myy name!")

hello2("Spamton","G","Spamton") #same parameters also okey


def name(name="Fatih"):
    print(name)

name() #Write default one


def hello3(*args): #*args for multiple parameters
    print("Hello",end=" ")

    for name in args: #for loop to using all args (parameters)
        print(name,end=" ")
    
    print("  BUT Hello specially",args[0],end=" ") #using first parameter
    print("!")

hello3("F","at","ih")


def hello4(name2,name1):
    print(name1,name2)

hello4(name1="F",name2="S") #Even though its not same order we can write like this


def hello5(**kwargs): #**kwargs for multiple named parameters
    print("Hello mr",kwargs["lastname"]) #we can use key value

hello5(lastname="Sahinoglu",firstname="Fatih") #key=value

def math(x):
    return x*x

print(math(5)) #funcitons just return not print

print(math(math(3))) #first 3*3 second 9*9 third print 81

