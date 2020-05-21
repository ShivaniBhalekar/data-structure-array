def pairsum(arr,key,n):
    
        for i in range(0,n):
            for j in range(1,n):
                if i==j:
                    return 0
                else:
                    if arr[i]+arr[j]==key:
                        return True
                        break
            return False

arr=[1,2,3,4,5,6]
n=len(arr)
pairsum(arr,5,n)
if (pairsum(arr,5,n)):
    print(" yes it has a pair")
else:
    print("NO PAIR")        
