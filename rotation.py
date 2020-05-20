def leftrotate(arr,d,n):
        for i in range(d):
                leftrotatebyone(arr,n)
def leftrotatebyone(arr,n):
        temp=arr[0]
        for i in range(n-1):
                arr[i]=arr[i+1]
        arr[n-1]=temp
def printarray(arr,size):
        for i in range(size):
                print(arr[i])

arr=[1,2,3,4,5,6,7,8,9]
leftrotate(arr,3,9)
printarray(arr,9)
                
                
        
        
