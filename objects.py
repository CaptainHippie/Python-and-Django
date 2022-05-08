class Employee: #employee base class
    empcount = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empcount += 1
    
    def displaycount(self):
        print ("Total employees %d" % Employee.empcount)
        
    def displayEmployee(self):
        print ("Name : ", self.name, ", Salary : ", self.salary)
#adding employees data
emp1 = Employee("Neeraj",5000)
emp2 = Employee("Sachin",6000)
emp3 = Employee("Raju",2000)

#printing data
emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()

#printing employee count
emp3.displaycount()