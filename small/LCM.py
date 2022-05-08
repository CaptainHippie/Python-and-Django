# FINDING LCM OF A NUMBER

def get_lcm(x, y):
    greater = x
    if y > x:
        greater = y
    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1
    return lcm


def get_gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def get_lcm_euclid(x, y):
    lcm = (x*y)//get_gcd(x, y)
    return lcm


n1 = int(input("Enter first number :"))
n2 = int(input("Enter second number :"))

print("The LCM of", n1, "and", n2, "is")
print("Using normal method :", get_lcm(n1, n2))
print("Using euclidean method :", get_lcm_euclid(n1, n2))
