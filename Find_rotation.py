def findrotation(a,n):
    min=a[0]
    for i in range(0,n):
        if min>a[i]:
            min=a[i]
            rot=i
    return rot

a=[4,5,6,1,2,3]
n=len(a)
print(findrotation(a,n))
       
            
