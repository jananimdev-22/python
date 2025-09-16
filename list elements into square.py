l=[1,2,3,4,5]
l1=[]
for i in l:
    square=i**2
    l1.append(square)
print(l1)








print("Another method to turn list into square")

l=[1,2,3,4,5,6]
for i in range(0,len(l)):
    l[i]=l[i]**2
print(l)
