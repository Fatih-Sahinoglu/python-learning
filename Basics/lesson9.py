#while loop

words=["hello","world","python","cake","awesome","fun"]
i=0
while i<len(words): #Condition

    if i==3:
        print("Cake is lie")
        i+=1
        continue #skip the current iteration
    elif i==5:
        print("Okey this is enough")
        break #exit the loop

    print(words[i])
    i+=1
else: #else block if while loop is finished normally
    print("Loop is ended")

#Creating list-------------------
numbers=[]
j=1
while j<=5:
    number=int(input("Enter a number: "))
    numbers.append(number)
    j+=1
print(numbers)
