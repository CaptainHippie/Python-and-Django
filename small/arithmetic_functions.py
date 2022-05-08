# ARITHMETIC OPERATIONS USING FUNCTIONS

def add(x, y):
    return float(x) + float(y)


def subtract(x, y):
    return float(x) - float(y)


def multiply(x, y):
    return float(x) * float(y)


def divide(x, y):
    return float(x) / float(y)


print("Select Operation :")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = int(input("Enter your choice (1/2/3/4):"))
if choice > 4 or choice <= 0:
    print("Invalid choice")
    exit()
n1 = input("Enter first number :")
n2 = input("Enter second number :")

if choice == 1:
    print(n1, "+", n2, "=", add(n1, n2))
elif choice == 2:
    print(n1, "-", n2, "=", subtract(n1, n2))
elif choice == 3:
    print(n1, "x", n2, "=", multiply(n1, n2))
else:
    print(n1, "/", n2, "=", divide(n1, n2))
