# SUM UPTO A NUMBER

num = int(input("Enter the number :"))
if num <= 0:
    print("Please enter a positive number")
else:
    sum1 = 0
    while num > 0:
        sum1 = sum1 + num
        num = num - 1
    print("The sum is", sum1)
