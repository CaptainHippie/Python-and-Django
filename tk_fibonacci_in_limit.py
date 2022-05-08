from tkinter import *

def fibonacci_in_limit(l,u):
    in_limit=[]
    fib=[]
    if (u<=0) or (u<=l):
        info.config(text="Please enter a valid limit")
    else:
        first,second=0,1
        fib=[0,1]
        Next=0
        while Next <= u:
            Next = first + second
            fib.append(Next)
            first = second
            second = Next
        for x in fib:
            if x >= l and x <=u:
                in_limit.append(x)
        if len(in_limit)==0:
            info.config(text="no numbers in limit")
        else:
            info.config(text=in_limit)

def fibonacci():
    try:
        lower=int(float(entry1.get()))
        upper=int(float(entry2.get()))
    except:
        info.config(text="Invalid Input")
        return
    fibonacci_in_limit(lower,upper)
    
mw = Tk()
mw.title("Factorial")
mw.geometry("640x480")
mw.resizable(1,1)

canvas = Canvas(mw,width=640,height=480)
canvas.pack(fill='both',expand=True)
img = PhotoImage(file="resources\\images\\background5cut.png")
canvas.create_image(0,0,anchor='nw',image=img)

H1 = canvas.create_text(310,60,text="FIBONACCI IN LIMIT",fill='#0066ff',font=('gisha',18,'bold'))
L1 = canvas.create_text(185,125,text="Lower limit:",fill='green',font=('comic sans ms',14))
L2 = canvas.create_text(185,165,text="Upper limit:",fill='green',font=('comic sans ms',14))
L2 = canvas.create_text(202,235,text="Output:",fill='red',font=('comic sans ms',14))

entry1=Entry(mw,bg='white',fg='#0066ff',relief='flat',font='kalinga',justify='center')
entry1.place(x=300,y=112,width=130,height=25)

entry2=Entry(mw,bg='white',fg='#0066ff',relief='flat',font='andalus',justify='center')
entry2.place(x=300,y=152,width=130,height=25)

btn = Button(mw,text='calculate',bg='red',fg='white',font=('gisha',12,'bold'),command=fibonacci)
btn.place(x=240,y=350,width=125,height=40)

info = Label(mw,text='',bg='white',fg='#0066ff',relief='flat',font='kalinga')
info.place(x=300,y=221,width=300,height=80)

mw.mainloop()
