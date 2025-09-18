try:
    n=int(input("Enter a value"))
    res+60/n
except zerodivisionerror:
    if n==0:
        print("You have given as the value ,It is division zero error")
else:
    print(res)
finally:
    print("Bye")
