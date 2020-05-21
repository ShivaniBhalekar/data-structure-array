#only by using right rotation

def maxsum(arr):
    arrsum=0
    current=0
    
    for i in range(0,n):
        arrsum=arrsum+arr[i]
        current=current+(i*arr[i])
    maxval=current
    for i in range(1,n):
        current=current+arrsum-(n*arr[n-i])
        if maxval<current:
            maxval=current
    return maxval

arr=[10,1,2,3,4,5,6,7,8,9]
n=len(arr)

print(maxsum(arr))
#print(maxval)
