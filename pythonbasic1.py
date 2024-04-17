listofnum=[1,2,3,44,66,78,98,96,87,96,46,68,1000000]
def max(list1):
    n=len(list1)
    res=0
    for i in range(n-1):
        if list1[i]>res:
            res=list1[i]
    return res


result=max(listofnum)
print(result)


