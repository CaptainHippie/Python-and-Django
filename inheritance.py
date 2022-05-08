class Base:
    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height
    def print_base(self):
        print("BASIC INFO :")
        print("Name :",self.name)
        print("Age :",self.age)
        print("Height :",self.height)

class Attributes:
    def __init__(self,position,goals,assists):
        self.pos = position
        self.goals = goals
        self.assists = assists
    def print_attributes(self):
        print("ATTRIBUTES :")
        print("Position :",self.pos)
        print("Goals :",self.goals)
        print("Assists :",self.assists)

class Player(Base,Attributes):
    def __init__(self,name,age,height,position,goals,assists):
        Base.__init__(self,name,age,height)
        Attributes.__init__(self,position,goals,assists)
    def print_all(self):
        print("BASIC INFO :")
        print("Name :",self.name)
        print("Age :",self.age)
        print("Height :",self.height)
        print("ATTRIBUTES :")
        print("Position :",self.pos)
        print("Goals :",self.goals)
        print("Assists :",self.assists)

p1=Player("Joshua Kimmich",27,"178 cm","DMF",5,13)
p2=Player("Alphonso Davies",20,"180 cm","LB",2,9)

p1.print_base()
p1.print_attributes()
#p1.print_all()
p2.print_base()
p2.print_attributes()
