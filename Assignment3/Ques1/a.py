def read_data():
    file_path = r'C:\Users\Harsh Choudhary\Desktop\AI Assignments\Assignment3\Ques1\text.txt'
    record = []
    with open(file_path,'r') as file:
        line = file.readlines()
        for lines in line:
            lines = lines.strip()
            store = lines.split(',')
            records = {
                'ID': int(store[0]),
                'Name': store[1],
                'Age': int(store[2])

            }
            record.append(records)

    return record

def write(path,record):
    with open(path,'w') as file:
        for records in record:
            line = f"{records['ID']}, {records['Name']}, {records['Age']}\n"
            file.write(line)

def update_age(file_path, record_id, new_age):
    records = read_data()
    
    for record in records:
        if record['ID'] == record_id:
            record['Age'] = new_age
    
    write(file_path, records)



record = read_data()
for i in record:
    print(i)
write(r'C:\Users\Harsh Choudhary\Desktop\AI Assignments\Assignment3\Ques1\write.txt',record)
update_age(r'C:\Users\Harsh Choudhary\Desktop\AI Assignments\Assignment3\Ques1\text.txt',2,11)



