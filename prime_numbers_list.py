number=int(input("Enter a number to check if it is prime: "))
prime_numbers=[]
prime_numbers.append(2) #2 is the first prime number

if number<2:
    print("Prime number are greater than 1")

else:
    for i in range(3,number+1,2): #check for all numbers from 3 to the given number but only odd numbers
        for j in range(3,int(i**0.5)+1): #check divisibility from 3 to sqrt(j) but range is include last number we add 1
            if i%j==0: #not a prime number
                break

    
        else:
            prime_numbers.append(i) #if loop is not broken then it is a prime number
    print("Prime numbers up to",number,"are:",prime_numbers) #after contorol writing all prime numbers listed
