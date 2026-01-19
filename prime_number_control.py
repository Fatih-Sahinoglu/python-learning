number=int(input("Enter a number to check if it is prime: "))
prime=True
if number<2:
    print("Prime number are greater than 1")

else:
    for i in range(2,int(number**0.5)+1): #check divisibility from 2 to sqrt(number) but range is include last number we add 1
        if number%i==0:
            prime=False
            break

    
    if prime==False:
        print(number,"is not a prime number")
    else:
        print(number,"is a prime number")

