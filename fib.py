while(True):
    n=int(input("enter a number (n) so that the series ends at nth number"))   #input
    if n<1:   #validation
        print("enter a valid number")
        continue
    else:
        fib=[0,1]
        i=0
        while len(fib)<n:
            fib.append(fib[i]+fib[i+1])
            i+=1
        if n==1:
            print("the series is [",fib[0],"]")
            break
        else:
            print("the series is ",fib)
            break
