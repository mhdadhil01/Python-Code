def recurtion(x):
    if(x>0):
        y=x+recurtion(x-1)
        print(y)
    else:
        y=0
        return y
print("Recurtion result")
recurtion(10)