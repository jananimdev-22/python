l=[1,2,3,4,5,6]
max=min=l[0]
for i in l:
    if i>max:
        max=i
    if i<min:
        min=i
print("Max:",max)
print("Min:",min)







print("count occurence")

l=[1,2,3,4,57,5,9,10,4,8,12,4,5]
print("Occurrence of 4:",l.count(4))
print("Occurrence of 12:",l.count(12))






print("Sorting")

l=[1,2,3,4,5]
l.sort()
print("Ascending:",l)
l.sort(reverse="True")
print("Descending:",l)
