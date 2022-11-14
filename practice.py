'''
for i in range(0,10,2):
    print(i)

#sum of N:
n=int(input("enter value N"))
sum=0
for i in range(1,n+1):
    sum=sum+i
    print("sum",sum)

#pattern
for i in range(10,0,-1):
    print( " "*(10-i)," *"*i)

n=int(input("enter value N"))
while n>0:
    print("santosh")
    n=n-1

s=("hello santosh gambhava")
p=("welcome to python word")
print(s,end=",")
print(p)

a=10
b=20
c=a+b
print("addition:",c)

a=int(input("enter value A:"))
if a>0:
     print("positive number")
else:
     print("negative number")

a=int(input("enter value A:"))
if a%2==0:
    print("A is even num")
else:
    print("A is odd num")
 
a=int(input("enter value A:"))
b=int(input("enter value B:"))
if a>b:
    print("A is greater number")
else:
    print("B is greater number")

a=int(input("enter value A:"))
b=int(input("enter value B:"))
c=int(input("enter value C:"))
if a>b:
    if a>c:
         print("A is greater number")
    else:
         print("C is greater number")
    elif b>c:
        print("B is greater number")
    else:
         print("C is greater number")        

for i in range(1,10):
    if i==5:
        break
    else:
        print(i)
 
for i in range(1,10):
    if i==4:
        continue
    else:
        print("i:",i)

s="t o p s te chno l o gi es"
sp=0
for i in s:
    if i.isspace():
        sp=sp+1
        print("total space:",sp)

def printline():
    print("*"*40)
printline()
print("welcomme to the python word")
printline()

def printline():
    print("*"*40)
printline()
def add(a,b):
    print("addition:",a+b)
printline()
a=int(input("enter value of A:"))
b=int(input("enter value of B:"))
printline()
add(a,b)
printline()
    

def sub(a,b):
    return a-b
a=int(input("enter value of A:"))
b=int(input("enter value of B:"))
ans=sub(a,b)
print("substraction:",sub(a,b))
 '''
def pattern(n):
    for i in range(1,n+1):
        print("*"*i)
def oddeven(a):
    if a%2==0:
        print("even number",a)
    else:
        print("odd number",a)

def maxoftwo(c,d):

    if c>d:
        print("C is greater number")
    else:
        print("D is greater number")

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

def fibbonacci(n):
    a,b=0,1
    while b<n:
        print(b,end=" ")
        a,b=b,a+b
def prime(n):
    if n%2!=0:
        for i in range(3,int(n/2)+1,2):
            if n%i==0:
                print("not prime")
                break
            else:
                print("prime")
prime(n)
