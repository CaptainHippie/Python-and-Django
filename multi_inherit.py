class Primary:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def print_base(self):
        print("BASIC INFO :")
        print("Name :",self.name)
        print("Age :",self.age)
        print("Gender :",self.gender)

class Secondary:
    def __init__(self,place,email,mobile):
        self.place = place
        self.email = email
        self.mobile = mobile
    def print_secondary(self):
        print("SECONDARY INFO :")
        print("Place :",self.place)
        print("Email :",self.email)
        print("Mobile No: :",self.mobile)

class Person(Primary,Secondary):
    def __init__(self,name,age,gender,place,email,mobile):
        Primary.__init__(self,name,age,gender)
        Secondary.__init__(self,place,email,mobile)

p1=Person("Neeraj V B",23,"Male","Valapad","neerajvb3@gmail.com",7558882214)


p1.print_base()
p1.print_secondary()
