# PRINTING FIBONACCI SEQUENCE FOR A GIVEN NUMBER

n_terms = int(input("Enter the number of terms :"))
n1 = 0
n2 = 1
count = 0

if n_terms <= 0:
    print("Please enter a positive integer")
elif n_terms == 1:
    print("Fibonacci sequence upto", n_terms, ":")
    print(n1)
else:
    print("Fibonacci sequence upto", n_terms, ":")
    while count < n_terms:
        print(n1, end=", ")
        n = n1 + n2
        n1 = n2
        n2 = n
        count = count + 1
