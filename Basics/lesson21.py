sum=lambda a,b: a+b
#name = lambda parameters: code
#name(parameters)
print(sum(5,6))

#always return something and can use with short hanf if
sign=lambda x: "Positive" if x>0 else "0 or negative"
print(sign(0))

#map(function,parameters)-------------------------------------------------------
num=[1,2,3]
square=lambda x: x*x
results=map(square,num) #with map() we can use any list parameter of functions
print(list(results)) #results are list

same=map(lambda x: x,num) #creating lambda function like this also allowed
print(list(same))

num2=[4,5,6]
summ=map(lambda x,y: x+y ,num,num2) #giving more parameters
print(tuple(summ)) 

#------------------------------------------------------------------------------

#filter(lambda,parameters)-----------------------------------------------------
small=filter(lambda x: x<=2, num) #lambda for checking conditions
print(list(small))

#------------------------------------------------------------------------------

#sorted(iterable,key=None,reverse=False)---------------------------------------
num3=[-1,2,-10,5]
absort=sorted(num3,key=lambda x: abs(x)) #first get list second (key=) like changed before sort
print(list(absort))

absort=sorted(num3,reverse=True) #sorting small to big but reverse
print(list(absort))

#------------------------------------------------------------------------------
