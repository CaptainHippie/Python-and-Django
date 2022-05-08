import re
strg="Python programming is easy to learn"
st = "the sum of 12 and 11 is 23"
s="start every day ofd with a smile and get it over with"

x=re.findall("[a-o]",strg)
print(x)

x=re.findall("\d",st)
print(x)

x=re.findall("l...n",strg)
print(x)

x=re.findall("^Python",strg)

if x:
    print("Yes, the string starts with 'Python'")
else:
    print("No match")

