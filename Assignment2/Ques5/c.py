def isPrime(x):
    for i in range(2,x-1):
        if(x%i == 0):
            return False
        else:
            return True

number = int(input("Enter the number "))
print(isPrime(number))