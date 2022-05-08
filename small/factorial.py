# FACTORIAL OF A NUMBER

factorial = 1
num = int(input("Enter the number :"))

if num < 0:
    print("Factorial does not exist for a negative number")
elif num == 0:
    print("Factorial of zero is 1")
else:
    for i in range(1, num+1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)
