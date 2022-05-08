from tkinter import *
import math
import unicodedata

root = Tk() 

root.title("Scientific Calculator")  
root.configure(background = 'white')  
root.resizable(width=False, height=False) 
root.geometry("302x409+0+0")  

# holds the buttons in the calculator, act as a container for numbers and operators 
calc = Frame(root) 
calc.grid()

class Calc(): 
    def __init__(self): 
        self.total = 0
        self.current = '' 
        self.input_value = True
        self.check_sum = False
        self.op = '' 
        self.result = False
        
    def numberEnter(self, num): 
        self.result = False
        firstnum = txtDisplay.get() 
        secondnum = str(num) 
        if self.input_value: 
            self.current = secondnum 
            self.input_value = False
        else: 
            if secondnum == '.': 
                if secondnum in firstnum: 
                    return
            self.current = firstnum+secondnum 
        self.display(self.current)
        
    def sum_of_total(self): 
        self.result = True
        self.current = float(self.current) 
        if self.check_sum == True: 
            self.valid_function() 
        else: 
            self.total = float(txtDisplay.get())
    def display(self, value):
        if (type(value) == float):
            if ((value*10)%10)==0:
                value=int(value)
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)
        
    def valid_function(self): 
        if self.op == "add": 
            self.total += self.current 
        if self.op == "sub": 
            self.total -= self.current 
        if self.op == "multi": 
            self.total *= self.current 
        if self.op == "divide": 
            self.total /= self.current 
        if self.op == "mod": 
            self.total %= self.current 
        self.input_value = True
        self.check_sum = False
        self.display(self.total)
        
    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op 
        self.result = False

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def All_Clear_Entry(self): 
        self.Clear_Entry() 
        self.total = 0

    def pi(self): 
        self.result = False
        self.current = math.pi 
        self.display(self.current)
        
    def e(self): 
        self.result = False
        self.current = math.e 
        self.display(self.current)
        
    def mathPM(self): 
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current) 

    def squared(self): 
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get())) 
        self.display(self.current)
    
    def cos(self): 
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get()))) 
        self.display(self.current) 

    def tan(self): 
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get()))) 
        self.display(self.current) 

    def sin(self): 
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get()))) 
        self.display(self.current) 

    def log(self): 
        self.result = False
        self.current = math.log(float(txtDisplay.get())) 
        self.display(self.current) 

    def exp(self): 
        self.result = False
        self.current = math.exp(float(txtDisplay.get())) 
        self.display(self.current) 

    def log10(self): 
        self.result = False
        self.current = math.log10(float(txtDisplay.get())) 
        self.display(self.current) 

added_value = Calc() 

txtDisplay = Entry(calc, font=('Helvetica', 13, 'bold'), bg='black', fg='white', bd=4, width=32, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=6)
txtDisplay.insert(0, "0")

numberpad = "789456123"

i = 0
btn = [] 
for j in range(4, 7):
        # k is in this range to place the button in that particular column 
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, bg='black', fg='white', font=('Helvetica', 13, 'bold'), bd=3, text=numberpad[i])) 
        # set buttons in row & column and separate them with a padding of 1 unit 
        btn[i].grid(row=j, column=k, pady=2,padx=2)
        # put that number as a symbol on that button 
        btn[i]["command"] = lambda x=numberpad[i]: added_value.numberEnter(x)
        i += 1

btnAllClear = Button(calc, text="AC", width=6, height=2, bg='#cc0000', fg='white', font=('Helvetica', 13, 'bold'), bd=2, 
                command=added_value.All_Clear_Entry).grid(row=3, column=0, pady=2) 

btnClear = Button(calc, text="C", width=6, height=2, bg='#cc0000', fg='white', font=('Helvetica', 13, 'bold'), bd=2, 
                command=added_value.Clear_Entry).grid(row=3, column=1, pady=2) 

btnsq = Button(calc, text="\u221A", width=6, height=2, bg='#94b8b8', font=('Helvetica', 13, 'bold'), bd=2, 
               command=added_value.squared).grid(row=3, column=2, pady=2) 

btnAdd = Button(calc, text="+", width=6, height=2, bg='#94b8b8', font=('Helvetica', 13, 'bold'), bd=2,
                command=lambda: added_value.operation("add")).grid(row=3, column=3, pady=2)

btnSub = Button(calc, text="-", width=6, height=2, bg='#94b8b8', font=('Helvetica', 13, 'bold'), bd=2, 
                command=lambda: added_value.operation("sub")).grid(row=4, column=3, pady=2) 

btnMul = Button(calc, text="x", width=6, height=2, bg='#94b8b8', font=('Helvetica', 13, 'bold'), bd=2,
                command=lambda: added_value.operation("multi")).grid(row=5, column=3, pady=2) 

btnDiv = Button(calc, text="/", width=6, height=2, bg='#94b8b8', font=('Helvetica', 13, 'bold'), bd=2,
                command=lambda: added_value.operation("divide")).grid(row=6, column=3, pady=2) 

btnZero = Button(calc, text="0", width=6, height=2, bg='black', fg='white', font=('Helvetica', 13, 'bold'), bd=2,
                 command=lambda: added_value.numberEnter(0)).grid(row=7, column=0, pady=2) 

btnDot = Button(calc, text=".", width=6, height=2, bg='#94b8b8', font=('Helvetica', 13, 'bold'), bd=2, 
                command=lambda: added_value.numberEnter(".")).grid(row=7, column=1, pady=2) 

btnPM = Button(calc, text=chr(177), width=6, height=2, bg='#94b8b8', font=('Helvetica', 13, 'bold'), bd=2,
               command=added_value.mathPM ).grid(row=7, column=2, pady=2) 

btnEquals = Button(calc, text="=", width=6, height=2, bg='#94b8b8', font=('Helvetica', 13, 'bold'), bd=2,
                command=added_value.sum_of_total).grid(row=7, column=3, pady=2)

btnPi = Button(calc, text="pi", width=6, height=1, bg='#24478f', fg='white', font=('Helvetica', 13, 'bold'), bd=2,
               command=added_value.pi).grid(row=1, column=0, pady=2)

btnCos = Button(calc, text="Cos", width=6, height=1, bg='#24478f', fg='white', font=('Helvetica', 13, 'bold'), bd=2, 
                command=added_value.cos).grid(row=1, column=1, pady=2,padx=1) 

btntan = Button(calc, text="tan", width=6, height=1, bg='#24478f', fg='white', font=('Helvetica', 13, 'bold'), bd=2, 
                command=added_value.tan).grid(row=1, column=2, pady=2,padx=1) 

btnsin = Button(calc, text="sin", width=6, height=1, bg='#24478f', fg='white', font=('Helvetica', 13, 'bold'), bd=2, 
                command=added_value.sin).grid(row=1, column=3, pady=2, padx=1) 

btnlog = Button(calc, text="log", width=6, height=1, bg='#24478f', fg='white', font=('Helvetica', 13, 'bold'), bd=2, 
                command=added_value.log).grid(row=2, column=0, pady=3, padx=1) 

btnExp = Button(calc, text="exp", width=6, height=1, bg='#24478f', fg='white', font=('Helvetica', 13, 'bold'), bd=2, 
                command=added_value.exp).grid(row=2, column=1, pady=2) 

btnE = Button(calc, text="e", width=6, height=1, bg='#24478f', fg='white', font=('Helvetica', 13, 'bold'), bd=2, 
              command=added_value.e).grid(row=2, column=2, pady=2) 

btnlog10 = Button(calc, text="log10", width=6, height=1, bg='#24478f', fg='white', font=('Helvetica', 13, 'bold'), 
                bd=2, command=added_value.log10).grid(row=2, column=3, pady=2) 

root.mainloop()