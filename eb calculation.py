class eb:
    def __init__(self,a,b,c,d,e,f):
        self.consumer_no=a
        self.name=b
        self.address=c
        self.current_unit=d
        self.previous_unit=e
        self.u_rate=f


    def calculate(self):
        self.unit=self.current_unit-self.previous_unit
        self.amt=self.unit*self.u_rate


    def disp(self):
        print("Consumer no:",self.consumer_no)
        print("Name:",self.name)
        print("Address:",self.address)
        print("Current Unit:",self.current_unit)
        print("Previous Unit:",self.previous_unit)
        print("1 Unit Rate:",self.u_rate)
        print("Amount:",self.amt)


h=input("Enter consumer no:")
i=input("Enter name:")
j=input("Enter address:")
x=int(input("Enter current unit:"))
y=int(input("Enter previous unit:"))
z=int(input("Enter 1 unit rate:"))



ob=eb(h,i,j,x,y,z)
ob.calculate()
ob.disp()

