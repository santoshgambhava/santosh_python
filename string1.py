s=int(input("enter a santance:"))
w=1
c=0
sp=0
d=0
sc=0
for i in s:
    if i.isalpha():
        c=c+1
    if i.numerical():
            d=d+1
    elif i.ispace():
            sp=sp+1
            w=w+1
    else:
        sc=sc+1
print("total word:",w)
print("total number:",d)
print("total space:",sp)
print("total character:",c)
print("total special symbol",sc)
