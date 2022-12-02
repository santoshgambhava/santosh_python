import pickle
'''
file=open("bcd.dat","wb")
n=int(input("enter limit:"))
dic={}
for i in range(1,n+1):
    key=input("enter key:")
    value=input("enter value:")
    dic[key]=value
pickle.dump(dic,file)
#pickle.dump({"name":"santosh","age":23,"study":"python"},file)
file.close()
'''
file=open("bcd.dat","rb")
dic=pickle.load(file)
print(dic)
file.close()

