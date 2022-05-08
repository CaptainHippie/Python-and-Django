file = open('file_outputs//data.txt', 'a')
file.write("Hello\n")
count = 0
file = open('file_outputs//data.txt', 'r')

for line in file:
    count += 1

print("Number of lines in the file :", count)
file.close()
