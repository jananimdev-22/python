class mark:
    def __init__ (self,a,b,c):
        self.mark1=a
        self.mark2=b
        self.mark3=c
    def disp(self):
        print(self.mark1)
        print(self.mark2)
        print(self.mark3)

x=int(input("Enter mark1:"))
y=int(input("Enter mark2:"))
z=int(input("Enter mark3:"))

obj=mark(x,y,z)
obj.disp()
