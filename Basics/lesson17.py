y=5 #global variable
def glo():
    global y #use global one not new one
    y+=5 #chaging global y



def outer():
    x=7 # local variable
    def inner():
        nonlocal x # use local variable at outer function
        x+=12
        print("inner:",x)
    inner()
    print("outer:",x)

outer()

