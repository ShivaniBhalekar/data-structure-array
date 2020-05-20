import array
arr=array.array('i',[1,2,3])
print('The new created array is: ')
for i in range(0,3):
	print(arr[i])
arr.append(4)
print("the append array is: ")
for i in range(0,4):
	print(arr[i])
arr.insert(2,5)
for i in range(0,5):
	print(arr[i])
print("the pop array is: ")
print(arr.pop(2))
for i in range(0,4):
	print(arr[i])
arr.reverse()
for i in range(0,4):
	print(arr[i])

