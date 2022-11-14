x=[1,2,3,4,5,6]
print(x[2])
x[2]="Nisha"
print(x)
del x[3]
print(x)
y=[7,8,9]
x.extend(y)
print(x)
x.append(y)
print(x)
print(x.count(5))
print(x.index(5))
x.insert(3,"Santosh")
print(x)
x.remove("Nisha")
print(x)
x.pop()
print(x)
x.pop(3)
print(x)
x.reverse()
print(x)
print(len(x))
print(max(y))
print(min(y))
print(sorted(y))

p=[]
a=int(input("enter value"))
n=1
while n<=a:
    x=int(input("enter value"))
    p.append(x)

    n=n+1
print(p)    



