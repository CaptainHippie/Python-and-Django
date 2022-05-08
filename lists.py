list_1 = ["lewandowski","muller","sane","neuer"]
print(list_1)

print(list_1[-1])
list_1 = list_1 + ["kimmich","gnabry"]
print(list_1)
print(len(list_1))


list_1.remove("muller")
print(list_1)

list_1.pop(-1)
print(list_1)

del list_1[0]
print(list_1)

list_1.append("davies")
print(list_1)

list_1.insert(2, "hernandez")
print(list_1)

list_2 = ["pavard","upamecano"] 
list_1.extend(list_2)
print(list_1)

list_1.sort()
print(list_1)

list_1.sort(reverse=True)
print(list_1)

list_1.reverse()
print(list_1)
