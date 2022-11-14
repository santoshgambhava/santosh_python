
def pattern(n):
    for i in range(1,n+1):
        print("*"*i)
pattern(5)

def oddeven(a):
    if a%2==0:
        print(a,"is even number")
    else:
        print(a,"is odd number")
oddeven(4)

def maxoftwo(a,b):
    if a>b:
        print(a,"is greater")
    else:
        print(b,"is greater")
x=int(input("enter value:"))
y=int(input("enter value:"))
maxoftwo(x,y)


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
a=int(input("enter value A:"))
b=int(input("enter value B:"))
c=int(input("enter value C:"))
maxofthree(a,b,c)


print("1.pattern")
print("2.oddeven")
print("3.maxoftwo")
print("4.maxofthree")
z=int(input("enter choice:"))
if z==1:
    n=int(input("enter n:"))
    pattern(n)
elif z==2:
    n=int(input("enter e:"))
    oddeven(n)
elif z==3:
    s=int(input("enter f:"))
    v=int(input("enter g:"))
    maxoftwo(s,v)
elif z==4:
    x=int(input("enter h:"))
    y=int(input("enter i:"))
    z=int(input("enter j:"))
    maxofthree(x,y,z)
else:
      print("exit")


    


