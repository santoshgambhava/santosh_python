'''
n=int(input("enter N:"))
while n>0:
    print("asdf")
    n=n-1
for i in range(1,10):
    if i==5:
        break
    print(i)

for i in range(1,10):
    if i==5:
        pass
    print(i)
for i in range(1,10):
    if i%3==0:
        continue
    else:
        print(i)
 
for i in range(4):
    for j in range(4):
        print("# ",end="")
    print()
n=4
while n>0:
    print(4*"# ",end="")
    print()
    n=n-1

for i in range(10,0,-1):
    print("#"+(10-i-1)*" "+"#")
for i in range(1,10):
    print("#"+(10-i-1)*" "+"#")
for i in range(1,10):
    print(" "*(10-i-1)+"#"+" "*(10-i-1)+"# ")
   
n=int(input("enter N:"))
if n%2==0:
    for j in range(3,int(int(i)/2)+1,2):
        if int(i)%j==0:
            print("not prime")
        else:
            print("prime")
else:
    print("prime")
 
from array import*
arr=array('i',[])
n=int(input("enter length of array:"))

for i in range(n):
    x=int(input("enter next value:"))
    arr.append(x)
print(arr)

val=int(input("enter the value for search:"))
k=0
for e in arr:
    if e==val:
        print(k)
        break
    k+=1

l=[]
for i in range(10):
    if i%2:
        l.append(i)
print(l)

d={}
for i in range(1,10):
   
    d[i]=i*i
print(d)
   
l=[i for i in range(10)if i%2]
print(l)
d={n:n*n for n in range(1,10)}
print(d)
    
l=[1,2,3,5,3,2,7,8,9,6]
myset=set(l)
print(myset)
newlist=list(myset)
print(newlist)

n=int(input("enter value:"))
if n>0:
    print("positive value")
else:
    print("negative")

n=int(input("enter value:"))
fact=1
while n>0:
    fact=fact*n
    n=n-1
print("fectorial:",fact)

n=int(input("enter value:"))
a,b=0,1
while n>b:
    print(b,end=" ")
    a,b=b,a+b

a=5
b=6
a,b=b,a
print(a)
print(b)
a=4
b=5
temp=b
b=a
a=temp
print(a)
print(b)

n=int(input("enter value:"))
if n%2==0:
    print("even")
else:
    print("odd")

n=input("enter value:")
if (n=="a"or"i"or"e"or"o" or"u"or"A"or"E"or"I"or"O"or"U"):
    print("vowel")
else:
    print("not vowel")


def testcode(a,b):
    if a==b or (a+b==5) or (a-b==5):
        return True
    else:
        return False
print(testcode(9,4))

s=("santoshgambhavasantosh")
print(s.count("santosh"))

a="santosh"
b="gambhava"
new_a=b[:2]+a[2:]
new_b=a[:2]+b[2:]
print(new_a)
print(new_b)
print(new_a+" "+new_b)
'''
l=[1,2,3,4]
print(l.pop())
list1=[2, 33, 222, 14,25]
print(list1[-1])
list1.append(36)
print(list1)
list1.extend([10,20,30])
print(list1)
list1.max()
print(list1)





