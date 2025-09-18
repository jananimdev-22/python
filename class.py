class stud:
    def __init__(self,a,b,c):
        self.sno=a
        self.sname=b
        self.sage=c
    def disp(self):
        print("student no:",self.sno)
        print("student name:",self.sname)
        print("student age:",self.sage)

x=int(input("Enter roll no:"))
y=input("Enter name:")
z=int(input("Enter age:"))

ob=stud(x,y,z)
ob.disp()
