def pattern(n):
    for i in range(1,n+1):
        print("*"*i)

def maxoftwo(a,b):
    if a>b:
        print("A is greater")
    else:
        print("B is greater")
        
def maxofthree(a,b,c):
    if a>b:
        if a>c:
            print("A is greater number")
        else:
            print("C is greater number")
    elif b>c:
        print("B is greater number")
    else:
        print("C is greater number")
def oddeven(a):
    if a%2==0:
        print("a is even number")
    else:
        print("a is odd number")
def fibonacci(n):
    a,b=0,1
    while b<n:
        print(b,end=" ")
        a,b=b,a+b
def prime(n):
    if n%2!=0:
        for i in range(3,int(n/2)+1,2):
            if n%i==0:
                print(n," is not prime")
                break
        else:
            print(n," is prime")
    else:
        print(n,"is not prime")

        
