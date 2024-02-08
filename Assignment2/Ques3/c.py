list = [1,1,2,2,3,3,4,5,8,8]
ans =[]
for i in list:
    if i not in ans:
        ans.append(i)
print("Unique elements in list: ", ans)