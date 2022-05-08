from tkinter import *
 
root = Tk()
root.title("Calculator")
root.geometry("435x410")
root.resizable(1,1)

canvas = Canvas(root,width=435,height=430)
canvas.pack(fill='both',expand=True)
img = PhotoImage(file="C:\\Users\\neeraj\\Desktop\\Class\\Python\\programs\\resources\\images\\background4cut.png")
canvas.create_image(0,0,anchor='nw',image=img)
                    
def get_num():
    n1,n2=0,0
    try:
        n1 = float(num1.get())
        n2 = float(num2.get())
    except:
        output.config(text="Invalid Input")
        return
    return n1,n2
    
def add():
    x,y=get_num()
    display((x+y))

def subtract():
    x,y=get_num()
    display((x-y))
    
def multiply():
    x,y=get_num()
    display((x*y))
    
def divide():
    x,y=get_num()
    display((x/y))
    
def display(result):
    if ((result*10)%10)==0:
        result=int(result)
    output.config(text=result)
    
H = canvas.create_text(220,58,text="SIMPLE CALCULATOR :",fill='#0066ff',font=('gisha',20,'bold'))
L1 = canvas.create_text(146,125,text="Enter first number    :",fill='green',font=('comic sans ms',14))
L2 = canvas.create_text(145,165,text="Enter second number :",fill='green',font=('comic sans ms',14))
LO = canvas.create_text(145,215,text="Output                      :",fill='red',font=('comic sans ms',14))

num1=Entry(root,fg='#0066ff',relief='flat',font=('kalinga',10),justify='center')
num1.place(x=262,y=109,width=130,height=30)
num2=Entry(root,fg='#0066ff',relief='flat',font=('kalinga',10),justify='center')
num2.place(x=262,y=149,width=130,height=30)

add = Button(root,text='ADD',bg='blue',fg='white',font=('gisha',10),command=add)
add.place(x=47,y=280,width=70,height=25)
subtract = Button(root,text='SUBTRACT',bg='blue',fg='white',font=('gisha',10),command=subtract)
subtract.place(x=135,y=280,width=75,height=25)
multiply = Button(root,text='MULTIPLY',bg='blue',fg='white',font=('gisha',10),command=multiply)
multiply.place(x=228,y=280,width=75,height=25)
divide = Button(root,text='DIVIDE',bg='blue',fg='white',font=('gisha',10),command=divide)
divide.place(x=321,y=280,width=70,height=25)
exit = Button(root,text='EXIT',bg='red',fg='white',font=('gisha',10),command=root.destroy)
exit.place(x=170,y=330,width=100,height=25)

output = Label(root,text='',bg='white',fg='black')
output.place(x=262,y=200,width=130,height=30)

root.mainloop()