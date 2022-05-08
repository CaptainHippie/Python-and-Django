row=int(input("Width of the Hourglass:"))
row=int(row/2)

for i in range(row,0,-1):
    for j in range((2*row)-(2*i)):
        print(" ",end="")
    for j in range(1,2*i):
        print("* ",end="")
    print()
for i in range(0,row):
    for j in range((2*row)-(2*(i+1))):
        print(" ",end="")
    for j in range((2*i)+1):
        print("* ",end="")
    print()

print("\n")
row2=int(input("Width of the diamond:"))
row2=int(row2/2)

print(((" ")*((2*row2)-1))+"*",end="")  
for i in range(row2,0,-1):
    x=""
    for j in range(i):
        x=x+"  "
    for k in range(2*(row2-i)):
        x=x+"* "
    print(x)
for i in range(0,row2):
    x=""
    for j in range(i):
        x=x+"  "
    for k in range(2*(row2-i)):
        x=x+"* "
    print(x)
print(((" ")*((2*row2)-1))+"*",end="")
        