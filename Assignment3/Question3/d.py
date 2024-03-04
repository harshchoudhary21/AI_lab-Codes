import numpy as np
def filter_odd_number(arr):
    ans =[]
    for i in arr:
        if(i%2!=0):
            ans.append(i)
    return ans
arr = np.random.randint(1,101,size=10)
ans = []
ans = filter_odd_number(arr)
print(ans)