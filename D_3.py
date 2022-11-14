for i in range (1,10):
    print(i)
    if i==5:
        break
    else:("i:",i)
for i in range (1,10):
    if i==5:
        continue
    else:
        print("i:",i)
s="A B C D E F G H I"
print(s[3:13])
print(s[:10])
print(s[1:16:3])
print(s[::5])
print(s[-15:-3])
print(s[:-1])
print(s[-12:])
s="to p s t e chn o log i es"
sp=0
for i in s:
    if i.isspace( ):
        sp=sp+1
    print("totalspace:,sp")

l=(1,2,1.1,2.2,"tops",1000,True,10,"python","false",1,2,100,101,102,103)
print(l[15:])
print(l[1:2])
print(l[10:15:5])
print(l[12::3])
print(l[:3:3])
print(l[::12])
print(l[-1:])
print(l[-16:-15])
print(l[-12:-2:7])
print(l[-13::10])
print(l[:-3:7])
print(l[:-3:7])
print(l[:])
l=[]
l.append(10)
print(l)
l.append(20)
print(l)
l.append(30)
print(l)
l.append(40)
print(l)
l.append(50)
print(i)
l.pop()
print(l)
l.pop()
print(l)
l.pop()
print(l)
l.pop()
print(l)
l.pop()
print(l)