class Mark:
    def __init__(self,a,b,c, mark1, mark2, mark3):
        self.sno=a
        self.sname=b
        self.sage=c
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3


    def calculate(self):
        self.total=self.mark1+self.mark2+self.mark3
        self.avg=self.total/3
        if self.mark1 >= 40 and self.mark2 >= 40 and self.mark3 >= 40:
            self.res = "Pass"
        else:
            self.res = "Fail"

    def disp(self):
        print("Student no:",self.sno)
        print("Student name:",self.sname)
        print("Student age:",self.sage)
        print("Enter mark1:",self.mark1)
        print("Enter mark2:",self.mark2)
        print("Enter mark3:",self.mark3)
        print("Total:", self.total)
        print("Average:", self.avg)
        print("Result:",self.res)

h=int(input("Enter roll no:"))
i=input("Enter name:")
j=int(input("Enter age:"))
x = int(input("Enter mark1: "))
y = int(input("Enter mark2: "))
z = int(input("Enter mark3: "))



obj = Mark(h,i,j,x,y,z)
obj.calculate()
obj.disp()
