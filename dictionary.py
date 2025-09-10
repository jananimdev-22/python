d={"eno":123,"ename":"janani"}
print(d["eno"])
print(d.get("ename"))
print(d)
d["ename"]="abc"
print(d)
d["age"]=19
print(d)
for key in d:
    print(key)
for values in d.values():
    print(values)
for key,value in d.items():
    print(key,":",value)
d.pop("eno")
print(d)
d.popitem()
print(d)
