# DISPLAY MULTIPLICATION TABLE

num = int(input("Display multiplication table of :"))
range1 = int(input("Till range :"))
count = 1
print("USING WHILE LOOP")
while count < (range1 + 1):
    print(num, "x", count, "=", num*count)
    count = count+1

print("USING FOR LOOP")
for count in range(1, range1 + 1):
    print(num, "x", count, "=", num*count)
