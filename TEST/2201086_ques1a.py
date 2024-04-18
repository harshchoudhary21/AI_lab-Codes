number1 = float(input("Enter the first number:"))
number2 = float(input("Enter the second number:"))
op = input("Enter the operation you want to perform i.e. +,-,*,/: ")
if op == '+':
    result = number1 + number2
elif op == '-':
    result = number1 - number2
elif op == '*':
    result = number1 * number2
elif op == '/':
    if number2 != 0:
        result = number1 / number2
    else:
        result = "Invalid, cant divide by zero"
else:
    result = "User has entered Invalid operation"
print("The required result is :", result)