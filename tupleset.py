t=(1,2,3,5,4,6)
print(t.count(3))
print(t.index(4))
print(len(t))
print(max(t))
print(min(t))
print(sorted(t))

#set
x={1,2,3,4,5}
y={10,20,30,40,50}
#x.update(y)
#print(x)
x.remove(3)
print(x)
y.discard(30)
print(y)
y={4,5,6,7,8}
#x.symmetric_diffrence(y)
print(y.pop())
y.clear()
print(y)
z={4,5,6,7,8,9}
print(x.union(z))
print(x.intersection(z))
print(x.difference(z))
print(z.difference(x))
print(x.symmetric_difference(z))




