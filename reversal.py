def reversalarray(arr,start,end):
	while(start < end):
		temp=arr[start]
		arr[start]=arr[end]
		arr[end]=temp
		start+=1
		end-=1
def leftrotate(arr, d):
	if d==0 :
		return
	else:
		n=len(arr)
		reversalarray(arr, 0,d-1)
		reversalarray(arr,d ,n-1)
		reversalarray(arr, 0 , n-1)
def printarray():
	for i in range(0,n):
		print(arr[i])

arr=[1, 2, 3, 4, 5, 6, 7]
n=len(arr)

d=4
leftrotate(arr,d)
printarray()











