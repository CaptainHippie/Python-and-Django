mark = 35
grade_index = { 95 : "O",
                90 : "A+",
                80 : "A",
                70 : "B",
                60 : "C",
                50 : "D",
                40 : "E"
            }

for x in grade_index:
    if mark < 40:
        print("FAIL")
        break
    elif mark >= x:
        print("GRADE : " + grade_index[x])
        break
