import re
pattern = input("Enter the pattern ")
file = open(r'C:\Users\Harsh Choudhary\Desktop\AI Assignments\Assignment2\Ques4\demo.txt', 'r')
match = re.search(pattern,file.read())
if(match):
    print("Pattern is present in the file")
else:
    print("Pattern not found")
