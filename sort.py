'''
# selection sort
x=[20,60,70,100,10,5,78,93]
for i in range(0,len(x)-1):
    for j in range(i+1,len(x)):
        if x[i]>x[j]:
            c=x[i]
            x[i]=x[j]
            x[j]=c
print(x)
# bubble sort
x=[2,3,5,6,8,7,9,1]
for i in range(0,len(x)):
    for j in range(0,len(x)-1):
        if x[j]>x[j+1]:
            c=x[j]
            x[j]=x[j+1]
            x[j+1]=c
print(x)
# insertion sort
x=[66,44,88,99,33,22,77,11]
for i in range(1,len(x)):
    c=i
    while c>0 and x[c]<x[c-1]:
        a=x[c]
        x[c]=x[c-1]
        x[c-1]=a
        c=c-1
print(x)
x=[66,44,88,99,33,22,77,11]
for i in range(0,len(x)):
    print(x[i])
for i in x:
    print(i)
######user input in list
n=int(input("enter limit:"))
l=[]
for i in range(1,n+1):
    x=input("enter value:")
    l.append(x)
print(l)
#or
l=eval(input("enter value:"))
print(l)

#linear search
l=[2,4,6,75,9,34,76,98,14,5,7]
n=int(input("enter number:"))
flag=-1
for i in range(0,len(l)):
    if n==l[i]:
        flag=i
        break
if flag==-1:
    print(n,"is not in list")
else:
    print(n,"found",flag+1,"location")
          
'''
#binary search
l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
n=int(input("enter number to search:"))
first=0
last=len(l)-1
while first<=last:
    mid=(first+last)//2
    if l[mid]==n:
        print("number is in",mid+1,"location")
        break
    elif l[mid]>n:
        last=mid-1
    else:
        first=mid+1
if first>last:
    print("number isnot avalible")
    
