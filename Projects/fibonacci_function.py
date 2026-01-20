def fibo(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)


num=int(input("Enter a number to write Fibonacci series up to: "))

if num<=0:
    print("Enter only positive integers")
    
else:
    for i in range(num):
        if i==num-1:
            print(fibo(i))
        else:
            print(fibo(i),end=" , ")
