#Circumference and area of a circle

name_of_circle=input("Enter the name of the circle: ")
#input() function takes input from the user as a string

pi=3.14 #value of pi (float)
radius=float(input("Enter the radius of the circle: ")) 
#when we write something inside input() function, it shows that as a prompt to the user

#we convert that string input to float using float() function


#we get all the required values from the user

circumference=2*pi*radius #formula for circumference of a circle
area=pi*radius*radius #formula for area of a circle

print("The circumference of the circle",name_of_circle,"is:",circumference)
print("The area of the circle",name_of_circle,"is:",area)