# TO FIND THE SUM OF CUBE OF EACH DIGIT

lower = int(input("Enter lower range :"))
upper = int(input("Enter upper range :"))

for num in range(lower, upper + 1):
    order = len(str(num))
    sum1 = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum1 += digit ** order
        temp //= 10
    if num == sum1:
        print(num)
