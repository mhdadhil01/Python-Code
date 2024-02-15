def tri_recurtion(k):
    if(k>0):
        result=k+tri_recurtion(k-1)
        print(result)
    else:
        result=0
    return result

print("Recurtion result") 
tri_recurtion(7)   