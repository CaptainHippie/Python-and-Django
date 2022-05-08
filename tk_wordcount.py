from tkinter import *

def count():
    phrase = entry1.get()
    words = phrase.split()
    total = "The words:\n"
    
    for x in words:
        total = total+str(words.index(x) + 1)+". "+x+"\n"
    wordcount= "Word count: "+ str(len(words))
    canvas.itemconfig(out1,text=total)
    canvas.itemconfig(out2,text=wordcount)
     
root = Tk()
root.title("Wordcount")
root.geometry("500x500")
root.resizable(1,1)

canvas = Canvas(root,width=500,height=500)
canvas.pack(fill='both',expand=True)
img = PhotoImage(file="resources\\images\\background4cut.png")
canvas.create_image(0,0,anchor='nw',image=img)

H1 = canvas.create_text(265,50,text="ENTER THE SENTENCE :",fill='#0066ff',font=('gisha',13,'bold'))
#L1 = canvas.create_text(230,95,text="Python has a simple syntax similar to the English language",fill='green',font=('comic sans ms',12))

entry1=Entry(root,fg='#0066ff',relief='flat',font=('kalinga',10),justify='center')
entry1.place(x=35,y=85,width=430,height=50)
#entry1=Entry(canvas)
#canvas.create_window(250,103,window=entry1,width=430,height=35)

btn = Button(root,text='calculate',bg='red',fg='white',font=('comic sans ms',10),command=count)
btn.place(x=350,y=260,width=100,height=25)
exit = Button(root,text='exit',bg='red',fg='white',font=('comic sans ms',10),command=root.destroy)
exit.place(x=350,y=330,width=100,height=25)

out1 = canvas.create_text(105,325,text="",fill='green',font=('comic sans ms',10,'bold'))
out2 = canvas.create_text(240,305,text="",fill='green',font=('comic sans ms',10,'bold'))

root.mainloop()