# AREA OF A TRIANGLE

a = float(input("Enter length of first side :"))
b = float(input("Enter length of second side :"))
c = float(input("Enter length of third side :"))

s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("Area of the triangle is :", area)
