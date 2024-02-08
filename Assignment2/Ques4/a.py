words = 0
file_path = r'C:\Users\Harsh Choudhary\Desktop\AI Assignments\Assignment2\Ques4\demo.txt'


with open(file_path, 'r') as file:
        data = file.read()
        lines = data.split()
        words = len(lines)
        print(words)
        print(lines)
