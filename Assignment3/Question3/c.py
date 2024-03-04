import numpy as np
def multiply_matrix(matrix1,matrix2):
    output_arr  =np.multiply(matrix1,matrix2)
    return output_arr
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[7,8,9],[10,11,12]])
ans_matrix = multiply_matrix(arr1,arr2)
print(ans_matrix)

    