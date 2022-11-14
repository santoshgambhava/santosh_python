'''
for i in range(1,10):
    print("santosh")
for i in range(1,10):
    print("santosh",end=" ")
for i in range(1,10):
    print(i)
for i in range(1,10,2):
    print(i)
n=1
while n<=5:
    print("santosh")
    n=n+1
for i in range(10):
    if i==5:
        break
    else:
        print(i)
       
for i in range(10):
    if i==5:
        continue
    else:
        print(i)
for i in range(10):
    if i==5:
        pass
    else:
        print(i)
n=1
while (n<=10):
    if n==5:
        break
    print(n)
    n=n+1

s=0
for i in range(1,10):
    s=s+i
print("sum:",s)
n=int(input("enter number:"))
for i in range(1,11):
    print(n,"*",i,"=",n*i)

n=int(input("enter number:"))
fact=1
while n>0:
    fact=fact*n
    print("factorial:",fact)
    n=n-1
n=int(input("enter number:"))
f=1
for i in range(1,n+1):
    f=f*i
print("factorial:",f)
#reverse to number
n=int(input("enter number:"))
s=0
while n!=0:
    x=n%10
    s=s*10+x
    n=n//10
print("reverse is:",s)

#number is perfect or not
n=int(input("enter number:"))
s=0
for i in range(1,n//2+1):
    if n%i==0:
        s=s+i
if s==n:
    print("perfect")
else:
    print("not perfect")

#palindrome a number 12321
n=int(input("enter number:"))
z=n
s=0
while n!=0:
    x=n%10
    s=s*10+x
    n=n//10
if s==z:
    print("number is palindrom")
else:
    print("number is not palindrom")

#armstrong no.45=4*4+5*5   125=1*1*1+2*2*2+5*5*5
n=int(input("enter number:"))
s=0
z=n
while n!=0:
    x=n%10
    s=s+x*x*x
    n=n//10
if s==z:
    print("number is armstrong")
else:
    print("number is not armstrong")

for i in range(100,1000):
    s=0
    z=i
    while z!=0:
        x=z%10
        s=s+x*x*x
        z=z//10
    if i==s:
        print(i)

#fibonacci
n=int(input("enter number:"))
a,b=0,1
while n>b:
    print(b,end=" ")
    a,b=b,a+b
    
# table of 2 t0 10
for i in range(2,10+1):
    for j in range(1,10+1):
        print(i*j,end=" ")
    print("\n")
    

#prime no.
for i in range(1,100):
    if i%2!=0:
        for j in range(3,int(i/2)+1,2):
            if i%j==0:
                print(i,"is not prime")
                break
        else:
            print(i,"is prime")
    else:
        print(i,"not prime")

#HFC
a=int(input("enter number A:"))
b= int(input("enter number B:"))
small=0
if a>b:
    small=b
else:
    small=a
for i in range(small,0,-1):
    if a%i==0 and b%i==0:
        print("HFC no:",i)
        break

#LCM
a=int(input("enter number A:"))
b= int(input("enter number B:"))
big=0
if a>b:
    big=a
else:
    big=b
for i in range(big,a*b+1):
    if i%a==0 and i%b==0:
        print("LCM no:",i)
        break

#LCM &HFC
a=int(input("enter number A:"))
b= int(input("enter number B:"))
big=0
if a>b:
    big=a
else:
    big=b
for i in range(big,a*b+1):
    if i%a==0 and i%b==0:
        print("LCM no:",i)
        print("HFC no:",(a*b)/i)
        break

 '''
#pattern
for i in range(1,6):
    print("*"*i)
for i in range(1,6):
    print(" "*(5-i),"*"*i)
for i in range(5,0,-1):
    print("*"*i)
for i in range(5,0,-1):
    print(" "*(5-i),"*"*i)
for i in range(1,6):
    print(" "*(5-i)," *"*i)
for i in range(5,0,-1):
    print(" "*(5-i)," *"*i)
    
