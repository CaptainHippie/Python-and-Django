# ROOT OF A QUADRATIC FUNCTION
import cmath

a = float(input("Enter a :"))
b = float(input("Enter b :"))
c = float(input("Enter c :"))

d = (b**2) - (4*a*c)
root1 = (-b - cmath.sqrt(d))/(2*a)
root2 = (-b + cmath.sqrt(d))/(2*a)

print("The roots are :", root1, "and", root2)
