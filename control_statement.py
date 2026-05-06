n=0
if n == 0:
    print("n is zero")
elif n%2 == 0:
    print(n,"is an Even number")
else:
    print(n,"is an Odd number")


n1 = 36
n2 = 26
n3 = 46
if n1>n2:
    if n1>n3:
        print("n1 is the largest number!")
    else:
        print("n3 is the largest number!")
elif n2>n3:
        print("n2 is the largest number!")


        
# switch

day = "sunday"
match day:
        case "monday":
            print("starting the weekend")
        case "wednesday":
            print("middle of the weekend")
        case "sunday":
            print("weekend")
        case _:
            print("Just another day")