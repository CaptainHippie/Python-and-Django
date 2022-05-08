# COMPUTING HCF USING FUNCTIONS

def get_hcf(a, b):
    smaller = a
    hcf = 1
    if b > a:
        smaller = b
    for i in range(1, smaller + 1):
        if (a % i == 0) and (b % i == 0):
            hcf = i
    return hcf


def get_hcf_euclid(a, b):
    while b:
        a, b = b, a % b
    return a


n1 = int(input("Enter first number :"))
n2 = int(input("Enter second number :"))

print("The HCF of", n1, "and", n2, "is")
print("Using normal method :", get_hcf(n1, n2))
print("Using euclidean method :", get_hcf_euclid(n1, n2))
