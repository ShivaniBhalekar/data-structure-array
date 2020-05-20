def searched(arr,low,high,key):
    mid=int(low+((high-low)/2))
    if arr[mid]==key:
        return mid

    if arr[low]<=arr[mid]:
        if arr[low]<=key and arr[mid]>=key :
            searched(arr,low , mid-1, key)
        else:
            searched(arr, mid+1,high, key)
    '''else:
        if arr[mid]<=key and arr[high]>=key :
            searched(arr, mid+1,high, key)
        else:
            searched(arr,low , mid-1, key)'''


arr=[1, 2, 3, 4, 5, 6,7]
n=len(arr)
key=2
position=searched(arr, 0, n-1,key)
print(position)

