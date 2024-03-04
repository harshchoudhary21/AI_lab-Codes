import numpy as np 
#3.i.
file_path = r'/home/harsh/AI_ASSIGNMENTS/ASSIGNMENT3/Question3/data.txt'
data = np.loadtxt(file_path,dtype = int,delimiter=',')
print(data)
#3.ii
print(np.mean(data))
row_mean = np.mean(data,axis=1)
print (row_mean)
mean_array = np.array(row_mean)
row_std = np.std(data,axis =1)
std_array = np.array(row_std)
#3.iii
result = np.array([row_mean,row_std])
print(result)
#3.iv
file = open(r'/home/harsh/AI_ASSIGNMENTS/ASSIGNMENT3/Question3/out.txt','w+')
content = '\n'.join(','.join(map(str, row)) for row in result)
file.write(content)
file.close()


