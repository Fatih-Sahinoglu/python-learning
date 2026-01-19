import random #random number module

print(random.randrange(1,10)) #get random number between 1 and 10 (10 not included) 
print(random.randrange(1,10,3)) #it will give numbers with step of 3 (1,4,7)

#I think most useful one
print(random.randint(1,10)) #get random number between 1 and 10 (10 included)

print(random.uniform(30,70)) #get random float number between 30 and 70
print(random.triangular(30,70,33)) #get random float number between 30 and 70 with mode of 33

mylist=["banana","strawberry","apple"] #for example not impotant list

print(random.choice(mylist)) #gets random element from the list
text="word"
print(random.choice(text)) #gets random character from the string

print(random.choices(mylist,weights=[10,1,1],k=8))
#gets k number of elements from the list with given weights

print(random.shuffle(mylist)) #shuffles the list randomly

print(random.sample(mylist,k=2)) #gets k number of unique elements from the list