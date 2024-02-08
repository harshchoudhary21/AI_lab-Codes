# Reversing a string in python
reverse = input("Enter the String: ")
required = ""
for i in reverse:
    required = i+required
print("The reversed string is ",required)    