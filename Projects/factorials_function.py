def fac(n):
    if n==0 or n==1:
        return 1
    else:
        return n * fac(n-1)

num=int(input("Please write a number: "))
if num<0:
    print("Number must be positive integer")
else:
    print(f"{num}! = {fac(num)}")

