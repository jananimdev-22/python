name=input("Enter your name :")
rollno=input("Enter your roll no :")
m1=int(input("Enter mark1"))
m2=int(input("Enter mark2"))
m3=int(input("Enter mark3"))
m4=int(input("Enter mark4"))
m5=int(input("Enter mark5"))
total=m1+m2+m3+m4+m5
avg=total/5
print("Total=",total)
if m1>=35 and m2>=35 and m3>=35 and m4>=35 and m5>=35:
    result="Pass"
    print("The student is Passed")
else:
    result="Fail"
    print("The student is Failed")
if result=="Pass":
    if avg>=90:
        print("Grade: A")
    elif avg>80:
        print("Grade: B")
    elif avg>70:
        print("Grade: C")
    elif avg>60:
        print("Grade: D")
    else:
        print("Grade: F")
            
