import numpy as np
#Generating two random numpy arrays having same shape
shape = (4,5)
arr1 = np.random.randint(1,10,size=shape)
arr2 = np.random.randint(1,10,size=shape)
print(arr1)
print("\n")
print (arr2)
print("\n")
#Concatenation of array horizontally and vertically
arr_h = np.hstack((arr1,arr2))
arr_v = np.vstack((arr1,arr2))
print(arr_h)
print("\n")
print(arr_v)

#Elementary operations on the arrays
arr_add = arr1+arr2
arr_sub = arr1-arr2
arr_mult = arr1*arr2
print("\n Array after addition: ",arr_add)
print("\n Array after subtraction: ",arr_sub)
print("\n Array after multiplication: ",arr_mult)


