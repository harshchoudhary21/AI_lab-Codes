import sys
list = [1,2,-310,9,6,100]
ans = -(sys.maxsize)
for i in list:
    if(i>ans):
        ans = i
print("the maximum element in list is ",ans)