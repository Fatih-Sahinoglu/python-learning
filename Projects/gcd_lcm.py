number1=int(input("Enter first number: "))
number2=int(input("Enter second number: "))
small=min(number1,number2)

for i in range(small,0,-1):
    if number1%i==0 and number2%i==0:
        gcd=i

lcm=(number1*number2)//gcd #because there is formula number1*number2=gcd*lcm

print("GCD is:",gcd,"\nLCM is:",lcm)
