def texting(n):
    ones=["","one","two","three","four","five","six","seven","eight","nine"]
    tens=["","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
    specials=["","eleven","twelve","thirteen","fourteen","fifteen","seventeen","sixteen","nineteen"]

    one=n%10 
    ten=(n//10) %10
    hund=(n//100) %10
    thou= (n//1000) %10

#Thousand part
    print(f"{ones[thou]} thousand",end="") #100% thousand digit can't 0

#Hundred part
    if hund==0: #if hundred digit 0 do nothing
        pass
    else:
        print(f" {ones[hund]} hundred",end="") #otherwise write

#Tens and ones part
    if ten==0: #if tens digit 0 do nothing
        print(f" {ones[one]}",end="")

    elif ten==1: #if it is ten we have special names
        print(f" {specials[one]}",end="")

    else:
        print(f" {tens[ten]}",end="") 
        print(f" {ones[one]}",end="")
    
#finish of function----------------------------------------------------


number=int(input("Enter a 4 digit number: "))

if not(1000<=number<=9999): # number check
    print("Just 4 digit")
else:
    texting(number) #function