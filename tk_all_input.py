from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("Registration Form")
root.resizable(1,1)

font=('comic sans ms',10)
bgcolor = "#CCCCCC"
dist_list = ["Alappuzha","Ernakulam","Idukki","Kannur","Kasergod","Kollam","Kottayam",
             "Kozhikode","Malappuram","Palakkad","Pathanamthitta","Trivandrum","Thrissur","Wayanad"]
dist_list=sorted(dist_list)
gen=StringVar()
gen.set("Male")
lg=["","","",""]
lg[0] = StringVar()
lg[1] = StringVar()
lg[2] = StringVar()
lg[3] = StringVar()
district = StringVar()
district.set("Select district")

def reset():
    name.delete(0,END)
    age_select.set(18)
    gen.set("Male")
    district.set("Select district")
    for x in range(0,4):
        lg[x].set(0)
            
def submit(): 
    confirm = tkinter.messagebox.askyesno("Confirm", "Do you want submit data?")
    if confirm>0: 
        #print_all()
        file_write()
        reset()
        return

def file_write():
    filename = "file_outputs//"+name.get()+".txt"
    file = open(filename, 'w+')
    file.write("NAME : "+name.get()+"\n")
    file.write("AGE : "+str(age_select.get())+"\n")
    file.write("GENDER : "+gen.get()+"\n")
    file.write("DISTRICT : "+district.get()+"\n")
    file.write("LANGUAGES : "+calc_languages()+"\n")
    file.close()

def calc_languages():
    lang=[]
    for x in range(0,4):
        y = lg[x].get()
        if y!="":
            lang.append(y)
    #print(lang)
    z = ""
    for x in range(0,len(lang)):
        if x == (len(lang)-1):
            z = z+lang[x]
        else:
            z = z+lang[x]+", "
    #print(z)
    return z

def print_all():
    print("NAME :", name.get())
    print("AGE :", age_select.get())
    print("GENDER :", gen.get())
    print("DISTRICT :", district.get())
    lang=[]
    for x in range(0,4):
        y = lg[x].get()
        if y!="":
            lang.append(y)
    print(lang)
    z = "LANGUAGE : "
    for x in range(0,len(lang)):
        if x == (len(lang)-1):
            z = z+lang[x]
        else:
            z = z+lang[x]+", "
    print(z)
    #file_write()
    
frame = Frame(root, bd=2, bg=bgcolor, relief=SOLID, padx=35, pady=10)
Label(frame, text="    REGISTRATION FORM", bg=bgcolor, font=('gisha',20,'bold')).grid(row=0, column=0, sticky=W, columnspan=3, pady=26)
Label(frame, text="NAME            :", font=font, bg=bgcolor, width=14).grid(row=1, column=0, sticky=W)
Label(frame, text="AGE               :", font=font, bg=bgcolor, width=14).grid(row=2, column=0, sticky=W)
Label(frame, text="GENDER         :", font=font, bg=bgcolor, width=14).grid(row=3, column=0, sticky=W)
Label(frame, text="DISTRICT      :", font=font, bg=bgcolor, width=14).grid(row=4, column=0, sticky=W)
Label(frame, text="LANGUAGES   :", font=font, bg=bgcolor, width=14).grid(row=5, column=0, sticky=W)

name = Entry(frame, font=font)
age_select = Scale(frame, from_=14, to_=60, orient=HORIZONTAL, font=font, bg=bgcolor,length=150)
age_select.set(18)
email = Entry(frame, font=font)

male_rb = Radiobutton(frame, text="Male", bg=bgcolor, variable=gen, value="Male")
female_rb = Radiobutton(frame, text="Female", bg=bgcolor, variable=gen, value="Female")

name.grid(row=1, column=1, sticky=W, pady=10, columnspan=2)
age_select.grid(row=2, column=1, sticky=W, pady=6, columnspan=2)
male_rb.grid(row=3, column=1, pady=10)
female_rb.grid(row=3, column=2, pady=10)

Checkbutton(frame, text="English", onvalue="English",offvalue="",bg=bgcolor, variable=lg[0]).grid(row=5, column=1, sticky=W)
Checkbutton(frame, text="Malayalam", onvalue="Malayalam",offvalue="", bg=bgcolor, variable=lg[1],width=10).grid(row=5, column=2, sticky=W)
Checkbutton(frame, text="Hindi", onvalue="Hindi",offvalue="", bg=bgcolor, variable=lg[2]).grid(row=6, column=1, sticky=W)
Checkbutton(frame, text="Others", onvalue="Others",offvalue="", bg=bgcolor, variable=lg[3],width=7).grid(row=6, column=2, sticky=W)

OptionMenu(frame,district, *dist_list).grid(row=4, column=1, columnspan=2, sticky=W)
register = Button(frame, width=15, text='REGISTER', font=font, relief=SOLID, cursor='hand2',command=submit)
register.grid(row=7, column=1, pady=20)
frame.pack()
root.mainloop()
