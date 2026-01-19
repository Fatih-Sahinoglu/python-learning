number=int(input("Enter a number to write Fibonacci series up to: "))
list_fib=[0,1,1] #fibonacci series starting with 0,1,1

if number<=0:
    print("Please enter a positive integer.")
elif number==1 or number==2 or number==3:
    print("Fibonacci series up to",number,":")
    print(list_fib[:number])
else:
    for i in range(2,number-1):
        f=list_fib[i]
        s=list_fib[i-1]
        t=f+s
        list_fib.append(t)
    print("Fibonacci series up to",number,":")
    print(list_fib)