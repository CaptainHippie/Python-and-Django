#from ast import pattern
import re
str="Python Programming is easy"
a=re.search("Py",str)
print(a)

pattern="Python"
res=re.match(pattern,str)
print(res)

res=re.split("\s",str)
print(res)

res=re.findall("ea",str)
print(res)

res=re.sub("\s","\n",str)
print(res)

res=re.search("Py",str).group()
print(res)

