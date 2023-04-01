list=[1,2,3,4,5]
print("The original lis is:"+str(list))
res=reduce(lamda i,j:i+j,[list[:1][0]**2]+list[1:])
print("The sum of square of list is:"+str(res))