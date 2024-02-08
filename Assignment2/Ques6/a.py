keys = ['Ten','Twenty','Thirty']
values = [10,20,30]
ans ={}
for k in keys:
    for v in values:
        ans[k] = v
        values.remove(v)
        break
       
print("Required dictionary is ",ans)