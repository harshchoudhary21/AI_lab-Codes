copy_file = open(r'C:\Users\Harsh Choudhary\Desktop\AI Assignments\Assignment2\Ques4\copy.txt', 'w')
original_file = open(r'C:\Users\Harsh Choudhary\Desktop\AI Assignments\Assignment2\Ques4\demo.txt', 'r')

copy_file.write(original_file.read())
print("File read and written successfully")

copy_file.close()
original_file.close()