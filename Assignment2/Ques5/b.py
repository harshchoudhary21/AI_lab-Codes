def fibonacci(x):
    a =0
    b =1
    list = [0,1]
    for i in range (x-2):
        c= a+b
        list.append(c)
        a = b
        b = c
    print(list)

number = int(input("Enter the number "))
if(number ==1):
    print("0")
elif(number ==2):
    print("[0,1]")
else:
    print(fibonacci(number))

     