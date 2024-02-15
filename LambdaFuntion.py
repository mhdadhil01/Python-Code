#lambda Funtion Is a small Anonymous Funtion
#A lambda Funtion Can Take Any Number Of Arguments, But can Only One Expression.
x= lambda a: a + 10
print(x(5))

x= lambda a, b: a*b
print(x(5,6))

x= lambda a, b, c: a + b + c
print(x(5, 6, 2))

#The Power Of Lambda is Better shown when You Use Them As An anonymous Funtion Inside Another Funtion.
#Say YOu have A FUntion Definition That Take One Arguments, And That Argument Will Be Multiplied With An Unknown Number
def twice(n):
    return lambda a: a*n
x= twice(2)
print(x(10))

def twice(n):
    return lambda a: a*n
x= twice(3)
print(x(10))

def myfun(n):
    print("Both Doubling And Thrippling")
    return lambda a: a*n
doubler = myfun(2)
tripler = myfun(3)
print(doubler(10))
print(tripler(10))