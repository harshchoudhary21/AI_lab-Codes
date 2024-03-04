import numpy as np
arr = np.random.randint(0,25,20)
print(arr[:len(arr)//2])
print(arr[len(arr)//2:])
#Modifying arrays 
arr[0] = 100
arr[5:10] = 5
print(arr)