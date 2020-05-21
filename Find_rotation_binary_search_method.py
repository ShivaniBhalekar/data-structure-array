def findrotation(arr,high,low):
    mid=low+(high-low)/2
    mid=int(mid)

    if arr[mid]<arr[mid-1]:
        return mid-1
    else:
        if arr[mid]>arr[mid+1]:
            return mid
        if arr[mid]<arr[n-1]:
            return findrotation(arr,0,mid-1)
        else:
            return findrotation(arr,mid+1,n-1)
arr=[6,7,8,9,10,11,5]
n=len(arr)
position=findrotation(arr,0,n-1)
print(position)
#time complexity is O(logn)
