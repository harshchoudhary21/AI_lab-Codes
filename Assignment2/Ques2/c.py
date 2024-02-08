reverse = input("Enter the String: ")
required = ""
for i in reverse:
    required = i+required
if(reverse ==required):
    print("It is a palindrome")   
else:
    print("Not a palindrome") 