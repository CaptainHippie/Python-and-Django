dict1 = {                       # creating dictionary
    'Name':'Unknown name',
    'Age':23,
    'Place':'valapad' }

print(dict1)
print(dict1['Name'])            # accessing value using key
print(dict1.get('Age'))         # accessing value using .get

dict1['Name'] = 'Neeraj'        # updating values
print(dict1['Name'])

dict1['Course'] = 'MVoc'        # inserting new element
print(all(dict1))               # using all()
print(any(dict1))               # using any()
print(len(dict1))               # finding length
print(sorted(dict1))            # sorting

print(dict1.fromkeys(dict1))    # getting keys 
print(dict1.items())            # getting every item

print(dict1.pop('Course'))      # deleting an element
print(dict1.popitem())

d3 = dict1.setdefault('Age')
print(d3)
dict1.update({'Phone':7558882214})
print(dict1)