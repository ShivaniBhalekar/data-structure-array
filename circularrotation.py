def rotate():
        
	for i in range(n-1,0,-1):
                arr[i]=arr[i-1]
       

def printarray():
        for i in range(n):
                 print(arr[i])

arr=[1,2,3,4,5,6,7]
n=len(arr)
temp=arr[n-1] 
rotate()
arr[0]=temp
printarray()
                
		
