replies = {"england": "Hello",
           "india": "Namaste",
           "spain": "Hola",
           "france": "Bonjour"}

def greeting(loc):
    return replies[loc]

name = input("Enter your name:\n")

location = input("Where are you from:")
greet = greeting(location)
print(greet, name)
print(len(replies))