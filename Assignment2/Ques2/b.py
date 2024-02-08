str = input("Enter the string: ")
count = 0
vowel = "aeiouAEIOU"
for i in str:
    if i in vowel:
        count = count+1
print("Number of vowels are  ",count)