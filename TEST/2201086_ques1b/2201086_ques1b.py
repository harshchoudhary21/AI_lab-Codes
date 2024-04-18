def analyze_text_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        word_count = len(content.split())
        line_count = content.count('\n') 
        space_count = content.count(' ')
        
    return word_count, line_count, space_count
def unique_words(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        unique_words = set(words)
    return unique_words

def frequency_of_words(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        frequency = {}
        for word in words:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1
    return frequency
def longest_word(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        longest_word = max(words, key=len)
    return longest_word
def average_word_length(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        total_length = sum(len(word) for word in words)
        average_length = total_length / len(words)
    return average_length
def text_similiar(file1,file2):
    with open(file1, 'r') as file:
        content1 = file.read()
    with open(file2, 'r') as file:
        content2 = file.read()
    return int(content1 == content2)
     
file_path = 'input.txt'
word_count, line_count, space_count = analyze_text_file(file_path)
print(f"Word count in the given text file: {word_count}")
print(f"Line count in the given text file: {line_count}")
print(f"Space count in the given text file: {space_count}")

unique_words = unique_words(file_path)
print(f"Number of unique words in the text file are: {len(unique_words)}")

frequency = frequency_of_words(file_path)
print(f"Frequency of words in the text file: {frequency}")

longestWord = longest_word(file_path)
print("The Longest word in the text file is: ", longestWord)

averageLength = average_word_length(file_path)
print("The average length of words in the text file is: ", averageLength)

file_path2 = 'text2.txt'
similiar = text_similiar(file_path, file_path2)
if similiar==1:
    print("The content of the two files is same")
else:
    print("The content of the two files is different")


    