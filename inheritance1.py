class stud:
    def __init__(self,a,b,c):
        self.sno=a
        self.sname=b
        self.sage=c

    def disp(self):
        print("Roll No:",self.sno)
        print("Name:",self.sname)
        print("Age:",self.sage)


class marks(stud):
    def __init__(self,a,b,c,m1,m2,m3):
        super().__init__(a,b,c)
        self.mark1=m1
        self.mark2=m2
        self.mark3=m3

    def disp(self):
        super().disp()
        print("Enter mark1:",self.mark1)
        print("Enter mark2:",self.mark2)
        print("Enter mark3:",self.mark3)


ob=marks(4,'janani',18,98,84,89)
ob.disp()
