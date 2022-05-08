# FINDING THE LARGEST OF THREE NUMBERS
num = [0, 0, 0]
num[0] = float(input("Enter first number :"))
num[1] = float(input("Enter second number :"))
num[2] = float(input("Enter third number :"))

largest = num[0]

for x in num:
    if x > largest:
        largest = x

print("Largest number is :", largest)
