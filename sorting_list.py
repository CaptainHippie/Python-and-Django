list1 = []
num = int(input("Enter the number of elements:"))
for i in range(num):
    data = int(input("Enter element :"))
    list1.append(data)
    print("List before sorting:", list1)
print("The length of the list is", len(list1))
list1.sort()
print("List after sorting is:", list1)
print("Third largest number is:",list1[2])

def multiply(list_x):
    product = 1
    for x in list_x:
        product = product * x
    return product

print("Product of all elements of the list is:", multiply(list1))
