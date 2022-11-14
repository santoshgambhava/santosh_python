from _collections import deque

l=deque([])
l.append(10)
print(list(l))
l.append(20)
print(list(l))
l.append(30)
print(list(l))
l.append(40)
print(list(l))
l.popleft()
print(list(l))
l.popleft()
print(list(l))
l.popleft()
print(list(l))
l.popleft()
print(list(l))

t=(1,2,1.1,1.2,True,"tops",[10,20,30],False,10,11,"python")
print(t)
print(t.count(1))
print(t.index(10))
for i in t:
    print(i)
print(t[6])
t[6].append(40)
print(t)


