# PRODUCT OF ALL NUMBERS IN A LIST

def multiply(list):
    result=1
    for x in list:
        result = result * x
    return result

num = int(input("Enter number of elements : "))
lst1 = []
for i in range(0,num):
    value = int(input("Enter next element : "))
    lst1.append(value)

print("The product of is :", multiply(lst1))
