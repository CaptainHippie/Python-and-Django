from tkinter import *

def factorial(n):
    if n<0:
        return "Enter positive number"
    elif (n==0) or (n==1):
        return 1
    else:
        fact=1
        for i in range(1, n+1):
            fact = fact * i
        return fact
        
def calculate():
    try:
        result=factorial(int(float(entryText.get())))
    except:
        result="Invalid Input"
    canvas.itemconfig(output,text=result)
        
mw = Tk()
mw.title("Factorial")
mw.geometry("330x250")
mw.resizable(1,1)

canvas = Canvas(mw,width=330,height=250)
canvas.pack(fill='both',expand=True)
img = PhotoImage(file="resources\\images\\background5cut.png")
canvas.create_image(0,0,anchor='nw',image=img)

Header = canvas.create_text(170,40,text="FACTORIAL OF A NUMBER",fill='#0066ff',font=('gisha',13,'bold'))
L1 = canvas.create_text(95,95,text="Enter the number  :",fill='green',font=('comic sans ms',10))
L2 = canvas.create_text(94,130,text="Output                  :",fill='green',font=('comic sans ms',10))

entryText=Entry(mw,bg='white')
entryText.place(x=165,y=82,width=130,height=25)

btn = Button(mw,text='calculate',bg='blue',fg='white',command=calculate)
btn.place(x=120,y=180,width=100,height=25)

output = canvas.create_text(190,130,text="",fill='red',font=('gisha',10))

mw.mainloop()