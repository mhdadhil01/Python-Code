age=int(input("Enter Your Age:"))
if age >18:
    print("You Are A Voter")
    if age >=21:
        print("You Are Eligible To Marry")
    else:
        print("You Are Not Eligible To Marry")
else:
    print("Your Age Is Less Than 18")