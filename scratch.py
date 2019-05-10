"""
count = 0
while True:
    count += 1
    print(count)

from tkinter import *

class Panel(Frame):

    def __init__(self,senior):
        Frame.__init__(self,senior)
        self.grid()

        top_left = Label(senior,text="Top Left", bg="black",fg="white",font=("Arial Bold",20))
        top_left.place(x=0,y=0,width=150,height=40)

        top_right = Label(senior,text="Top Right", bg="black",fg="white")
        top_right.place(x=1266,y=0,width=100,height=40)

        bottom_left = Label(senior,text="Bottom Left", bg="black",fg="white")
        bottom_left.place(x=0,y=703,width=100,height=40)

        bottom_right = Label(senior,text="Bottom Right", bg="black",fg="white")
        bottom_right.place(x=1266,y=703,width=100,height=40)

if __name__ == "__main__":
    root = Tk()
    root.title("Title")
    panel = Panel(root)
    panel.mainloop()"""

"""

from random import *
from string import *

alp_upper = ascii_uppercase
alp_lower = ascii_lowercase
symbol = digits + ascii_lowercase + ascii_uppercase

print("".join(SystemRandom().choice(symbol) for _ in range(10)))
print(list(randint(1,20) for _ in range(20)))
print(list(randrange(30) for _ in range(20)))
print(list(choice("Vicolas") for _ in range(6)))

from re import *
from string import *
from sys import exit

password = input("Enter your Password: ")

if not compile(r"[A-Z]").search(password):
    print("Your password must contain uppercase!")
    exit()
elif not compile(r"[0-9]").search(password):
    print("Your password must contain a number!")
    exit()
elif not compile(r"[!#$%]").search(password):
    print("Your password must contain a character!")
    exit()
elif len(password) < 8:
    print("The length of the character must be 8 or more!")
    exit()
else:
    print("Strong Password!")"""

"""
from functools import reduce
from operator import mul

def factorial(num):
    print(reduce(mul,range(1,num+1)))

factorial(3)"""

"""
with open("Work.txt","w") as f:
    f.write("Welcome back to Python Vicolas")

from timeit import timeit
a = print(list(i*i for i in range(11)))
b = print(list(map(lambda x: x*x, range(11))))
c = list(range(11))
d = list(range(11))
for i,k in zip(c,d):
    print(i+k)
    if i+k == 11:
        print("Found")
        break
else:
    print("Can't find it")
    print("Still Looping...")

e = timeit("[x**2 for x in range(10)]")
print(e)
"""

# def square_num (num):
#     for i in num:
#         yield (i*i)
#
# my_num = square_num([1,2,3,4,5])
#
# print(list(_ for _  in my_num))
#
# def out_func(msg):
#     message = msg
#     def inner_func():
#         print(message)
#     return inner_func
#
# say = out_func("Hi")
# bye =  out_func("Bye")
# say()
# bye()

#UNDERSTANDING DECORATOR!

"""
def decorator_function(original_function):
    def wrapper_function(*args,**kwargs):
        print("The function name is {}".format(original_function.__name__))
        return original_function(*args,**kwargs)
    return wrapper_function

class decorator_class(object):

    def __init__(self,original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print("The function name is {}".format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)

def display_function():
    print("Display ran this!")

def display_another_function():
    print("Other things!")

display_this = decorator_function(display_function) #A DECORATOR IS A FUNCTION THAT IS INSIDE ANOTHER FUNCTION LIKE THIS LINE OF CODES
display_this()
@decorator_function
def display_function():
    print("Display ran this!")

@decorator_function #A DECORATOR IS A FUNCTION THAT IS WRAPPED INSIDE ANOTHER FUNCTION
def display_another_function(name,age):
    print("My name is {} and am {} yrs old".format(name,age))

@decorator_class
def display_function():
    print("Display ran this!")

@decorator_class #A DECORATOR IS A FUNCTION THAT IS WRAPPED INSIDE ANOTHER FUNCTION
def display_another_function(name,age):
    print("My name is {} and am {} yrs old".format(name,age))

display_function()
display_another_function("Vicolas",31)
print("\n")
display_function()
display_another_function("Victor",18) """

"""
from tkinter import *
from sys import exit

# def click():
#     En.get()

window = Tk()
window.title("Project")
window.configure(bg="red")

Lbl = Label(window,text="Enter a word:",width=10,height=1,bg="red",fg="white",font="Arial 18 bold italic")
Lbl.grid(row=0,column=0,sticky=W)

En = Entry(window,width=113,bg="white",fg="black")
En.grid(row=1,column=0,sticky=W)

Btn = Button(window,width=10,height=1,command=click,text="SUBMIT",bg="black",fg="white",font=("Tahoma",12))
Btn.grid(row=1,column=2,sticky=W)

Txt = Text(window,width=85,height=10)
Txt.grid(row=3,column=0,columnspan=2,sticky=W)

def out():
    exit()

Btn_2 = Button(window,width=5,height=1,command=out,text="exit",bg="black",fg="white",font=("Tahoma",12))
Btn_2.grid(row=4,column=0,sticky=W)

Photo = PhotoImage(file="nike_hd.gif")
Label(window,image=Photo,fg="yellow",font="Tahoma 30 bold",compound=CENTER,width=600,height=200,text="Nike what a nice product").pack(side="left")
Label(window,fg="yellow",font="Tahoma 30 bold",justify=RIGHT,padx=100,width=600,height=200,text="Nike what a nice product").pack(side="right")
"""

"""
from tkinter import *
from sys import *

window = Tk()
window.title("Project")
window.config(bg="red")

counter = 11
def counter_num(num):
    def countz():
        global counter
        counter -= 1
        if counter == -1:
            exit()
        num.config(text=str(counter))
        num.after(1000,countz)
    countz()

num = Label(window,width=8,height=1, bg="green", fg="white", font="Candara 20 bold")
num.grid(row=0,column=1,sticky=W)
counter_num(num)

Msg = Message(text="This is the first line.\nAnother new line.\nGood day!",fg="red",bg="#e3e3e3", font="candara 16 bold", bd=7, padx=4, pady=4,takefocus=True, relief="raised", anchor=NE)
Msg.grid(row=2,column=2,sticky=W)

Lbl = Label(window, text="This is the first line.\nAnother new line.\nGood day!", width=10, height=1, bg="black", fg="white", font="arial 18 bold", bd=40, justify="left")
Lbl.grid(row=0,column=0,sticky=W)

Ent = Entry(window, width=16, bg="black", fg="white", font="tahoma 14")
Ent.grid(row=1,column=0,sticky=W)

Txt = Text(window, width=16, height=5, bg="black", fg="white", font="tahoma 14")
Txt.grid(row=2,column=0,sticky=W)

def write():
    print("This is awesome!")

Btn = Button(window, width=5, height=1, bg="white", fg="black", text="OK", font="tahoma 12 bold",relief="raised",command=write)
Btn.grid(row=3,column=0,sticky=W)

Btn = Button(window, width=5, height=1, bg="black", fg="white", text="Exit", font="tahoma 12 bold", command=exit)
Btn.grid(row=4,column=0,sticky=W)

Photo = PhotoImage(file="nike_hd.gif")
Label(window, image=Photo, width=900, height=500, compound="center", text="Above and not beneath!", fg="red", font="arial 20 bold").grid(row=5, column=0, sticky=W)

window.mainloop()

"""

from tkinter import *

# window = Tk()
# window.title("Project")
# window.config(bg="white")
# window.geometry("550x400")

"""

# RADIO BUTTON AND CHECKBUTTON

label = Label(window,text="Please chooose your best Programming Language:",font="arial 12 bold", bg="black", fg="white")
label.pack()

v = IntVar()

button = Radiobutton(window,text="Python",font="arial 12 bold",fg="black",bg="white",value=1,variable=v)
button.pack(anchor=W)

button = Radiobutton(window,text="C++",font="arial 12 bold",fg="black",bg="white",value=2,variable=v)
button.pack(anchor=W)

button = Radiobutton(window,text="Ruby",font="arial 12 bold",fg="black",bg="white",value=3,variable=v)
button.pack(anchor=W)

button = Radiobutton(window,text="JavaScript",font="arial 12 bold",fg="black",bg="white",value=4,variable=v)
button.pack(anchor=W)
v = IntVar()
v.set(1+1)
language =  [["Python",1],["JavaScript",2],["Java",3],["Pearl",4],["Ruby",5],["C#",6],["C++",7],["C",8],["R",9],["Delphi",10],["PHP",11]]

def makechoice():
    print(v.get())

for i,k in enumerate(language):
    Radiobutton(window,text=k,padx=20,variable=v,value=i,bg="white",indicatoron=0,command=makechoice,width=20).pack(anchor=W)
button =  Button(text="Quit",command=quit,width=20,relief="raised").pack(anchor=CENTER)"""

# CHECK BUTTON
"""
label = Label(window,text="Please chooose all your best Programming Language:",font="arial 12 bold", bg="black", fg="white")
label.pack()

v = IntVar()

button = Checkbutton(window,text="Python",font="arial 12 bold",fg="black",bg="white")
button.pack(anchor=W)

button = Checkbutton(window,text="Java",font="arial 12 bold",fg="black",bg="white")
button.pack(anchor=W)

button = Checkbutton(window,text="Pearl",font="arial 12 bold",fg="black",bg="white")
button.pack(anchor=W)

button = Checkbutton(window,text="Delphi",font="arial 12 bold",fg="black",bg="white")
button.pack(anchor=W)

"""
'''
infor = ["First name","Last name", "Sex", "Age", "Major"]

def information():
    print("First name: {}\nLast Name: {}\nSex: {}\nAge: {}\nMajor: {}".format(Ent_1.get(),Ent_2.get(),Ent_3.get(),Ent_4.get(),Ent_5.get()))
    # Ent_1.delete(0,END)

lbl_1 = Label(window,text="First Name",font="arial 18 bold",bg="white").grid(row=0,column=0,sticky=W)
lbl_2 = Label(window,text="Last Name",font="arial 18 bold",bg="white").grid(row=1,column=0,sticky=W)
lbl_3 = Label(window,text="Sex",font="arial 18 bold",bg="white").grid(row=2,column=0,sticky=W)
lbl_4 = Label(window,text="Age",font="arial 18 bold",bg="white").grid(row=3,column=0,sticky=W)
lbl_5 = Label(window,text="Major",font="arial 18 bold",bg="white").grid(row=4,column=0,sticky=W)

Ent_1 = Entry(window,width=30,bg="white",font="candara 14")
Ent_1.grid(row=0,column=1,sticky=W)
Ent_2 = Entry(window,width=30,bg="white",font="candara 14")
Ent_2.grid(row=1,column=1,sticky=W)
Ent_3 = Entry(window,width=30,bg="white",font="candara 14")
Ent_3.grid(row=2,column=1,sticky=W)
Ent_4 = Entry(window,width=30,bg="white",font="candara 14")
Ent_4.grid(row=3,column=1,sticky=W)
Ent_5 = Entry(window,width=30,bg="white",font="candara 14")
Ent_5.grid(row=4,column=1,sticky=W)

Ent_1.insert(0,"Vicolas")
Ent_2.insert(0,"Akoh")
bot = Button(window,text="Get Information",width=12,bg="black",fg="white",command=information,activebackground="red",cursor="circle").grid(row=5,column=0,sticky=W)

if __name__ == '__main__':
    window.mainloop()


infor = ["First name","Last name", "Sex", "Age", "Major"]

def inform():
    # print(map(list(lambda x:x.get(),Ent)))
    print("First name: {}\nLast Name: {}\nSex: {}\nAge: {}\nMajor: {}".format(*Ent.get()))
def clear():
    Ent.delete(0,END)

for i in infor:
    Lbn = Label(window,text=i,font="arial 16 bold",bg="white")
    Lbn.pack(anchor=W)
    Ent = Entry(window,width=20)
    Ent.pack(anchor=E)

Btn = Button(window,text="GRAB",width=15,bg="black",fg="white",activebackground="red",command=inform)
Btn.pack(after=Ent)

window.mainloop()
'''
"""
for n in range(1,20+1):
    def clear():
        Ent.delete(0, END)
    Label(window,text=n,relief="raised",padx=12,width=5,bg="black",fg="white").grid(row=n,column=0)
    Ent=Entry(window,width=40,bg="yellow",fg="red",font="arial 12 bold")
    Ent.grid(row=n,column=1)
    Ent.insert(0,"Vicolas")
    Button(window,width=5,bg="black",fg="white",text="clear",command=clear).grid(row=21,column=1)

window.mainloop()"""

"""
#CANVAS WIDGETS
canvas_width = 800
canvas_height = 400
can = Canvas(window,width=canvas_width,height=canvas_height,bg="white")
can.pack()

#TRIANGLE
can.create_polygon(10,10,400,200,10,400,fill="yellow",outline="blue",width=3)
can.create_polygon(800,10,400,200,800,400,fill="red",outline="blue",width=3)
can.create_polygon(10,400,400,200,1800,900,fill="#00ff00",outline="blue",width=3)
can.create_polygon(400,200,800,10,10,10,fill="#00ffff",outline="blue",width=3)"""

"""
#CREATING A STAR       1      2        3        4        5       6       7       8
# can.create_polygon(0,130, 95,160, 120,300, 160,160, 260,120, 150,100, 115,0, 90,110,fill="gold",width=5,outline="black")

def poly_star(a,b,c,d,e,f,g,h,fill="gold",width=5,outline="black"):
    do = can.create_polygon(a,b,c,d,e,f,g,h,fill="gold",width=5,outline="black")
    return do

for i in range(1,10):
   poly_star([(0*i,130*i)], [95*i,160*i], [120*i,300*i], [160*i,160*i], [260*i,120*i], [150*i,100*i], [115*i,0*i], [90*i,110*i],fill="gold",width=5,outline="black")"""

"""#FIND OUT MORE ON BITMAP
bitmap =  ["error","question","info","warning","hourglass"]
for _  in bitmap:
    can.create_bitmap()

#CREATING AN IMAGE INTO A CANVAS WIDGET
Photo = PhotoImage(file="nike_hd.gif")
can.create_image(1,1,anchor=CENTER,image=Photo)"""

"""
#CREATING LINES INTO A CANVAS WIDGET
can.create_line(0,0,100,100,fill="red",width=4)
can.create_line(800,0,700,100,fill="blue",width=4)
can.create_line(0,400,100,300,fill="black",width=4)
can.create_line(800,400,650,300,fill="green",width=4)
can.create_rectangle(300,200,500,100,fill="orange",width=10,outline="blue")
can.create_text(400,150,text="Python",font="tahoma 18 bold")"""

"""
#PAINT
def paint(event):
    x1,y1 = (event.x - 3),(event.y - 3)
    x2,y2 = (event.x + 3),(event.y + 3)
    can.create_oval(x1,y1,x2,y2,fill="red",width=0)

def clean():
    can.delete(0,END)

can.bind("<B1-Motion>",paint)
but = Button(window,width=12,text="clean",command=clean).pack(side=BOTTOM)
"""

"""
#SCALE WIDGET
#BY DEFAULT THE SCALE WIDGET IS VERTICAL

def show():
    print("The scale is at {}".format(scale.get()))

scale = Scale(window,from_=0,to=50,orient=VERTICAL,relief="raised",bg="red",activebackground="green",cursor="heart",tickinterval=5,length=400)
scale.pack()
scale.set(35)
scale = Scale(window,from_=0,to=50,orient=HORIZONTAL,length=600,relief="raised",bg="purple",fg="white",activebackground="yellow",cursor="heart",tickinterval=10)
scale.pack()
# scale.set(5000)
btn = Button(window,text="Display",width=20,command=show)
btn.pack(after=scale)
msg =  Text(window,width=30,height=15,relief="sunken",bg="grey",fg="black").pack(side=BOTTOM)


#SCROLLING DOWN
txt = Text(window,width=50,height=25)
txt.pack(side=LEFT, fill=Y)
sc = Scrollbar(window,command=txt.yview)
sc.pack(side=RIGHT,fill=Y)
txt.config(yscrollcommand=sc.set)"""


"""
#THE BEGINNING  *****************************************************************************

from tkinter import *
from random import choice,choices

window = Tk()
window.title("Counter")
# window.geometry("100x50")
window.config(bg="grey")

# SECONDS COUNTDOWN -----------------------------------------------------------------------------
count = -1
colors = ["#9400D3","#FF1493","#00DED1","#9932CC","#BDB76B","#1E90FF","#00008B","#0000FF","orange"]
def counter(num):
    def countz():
        global count
        count += 1
        if  count == 60:
            count = -1
            count += 1
        num.config(text=(count),bg=choice(colors))
        num.after(1000,countz)
    countz()

lb = Label(window,text="SECONDS",width=12,font="arial 14 bold",relief="raised")
lb.grid(row=0,column=2,sticky=W)

num = Label(window,bg=choices(colors),fg="white",width=4,height=2,font="candara 50 bold",relief="groove",bd=2)
num.grid(row=1,column=2,sticky=W)
counter(num)
#---------------------------------------------------------------------------------------

# MINUTES COUNTDOWN --------------------------------------------------------------------
count_1 = -1
def counter_1(num1):
    def counts():
        global count_1
        count_1 += 1
        if count_1 == 60:
            count_1 = -1
            count_1 += 1
        num1.config(text=str(count_1),bg=choice(colors))
        num1.after(60000,counts)
    counts()

lb = Label(window,text="MINUTES",width=12,font="arial 14 bold",relief="raised")
lb.grid(row=0,column=1,sticky=W)

num1 = Label(window,bg=choices(colors),fg="white",width=4,height=2,font="candara 50 bold",relief="sunken")
num1.grid(row=1,column=1,sticky=W)
counter_1(num1)#THIS IS THE FUNCTION CALLER!
# ----------------------------------------------------------------------------------------

# HOURS COUNTDOWN ------------------------------------------------------------------------
count_2 = -1
def counter_2(num2):
    def countss():
        global count_2
        count_2 += 1
        if count_2 == 60:
            count_2 = 0
            count_2 += 1
        num2.config(text=str(count_2),bg=choice(colors))
        num2.after(3600000,countss)
    countss()

lb = Label(window,text="HOURS",width=12,font="arial 14 bold",relief="raised")
lb.grid(row=0,column=0,sticky=W)

num2 = Label(window,bg=choices(colors),fg="white",width=4,height=2,font="candara 50 bold",relief="groove")
num2.grid(row=1,column=0,sticky=W)
counter_2(num2)
# ----------------------------------------------------------------------------------------

window.mainloop()


from tkinter import *
window = Tk()
window.title("Set Thresholds")
window.config(bg="white")
"""
do = ["BER","VSWR","RX Level","Tx Level"," AC Supply","DC Supply","","","dB","Watts","Volts","Volts"]
doo = ["1x10-6","1:2",-100,5,110,24,"Alarm Over","Alarm Over","Alarm Under","Alarm Under","Alarm Under","Alarm Under"]

# som = (i for i in do)
# for i in do[0:6]:
#   Lbn = Label(window,text=i,justify=LEFT,width=10,font="arial 14 bold")
#   Lbn.grid(row=0,column=0,sticky=W)
#
# for i in do[6:]:
#   Lbn_2 = Label(window, text=i, justify=LEFT, width=10, font="arial 14 bold")
#   Lbn_2.grid(row=1,column=1,sticky=E)

# w = Frame(window,bg="grey",width=400,height=350,relief="ridge")
# w.pack(side=LEFT)

"""


# ------------------------------ CALCULATOR -------------------------------------------------

from tkinter import *
from sys import exit

def frame(root,SIDE):
    w = Frame(root, borderwidth=6, bg="powder blue")
    w.pack(side=SIDE,fill=BOTH,expand=YES)
    return w

def button(root,text,SIDE,command=None):
    w = Button(root,text=text,command=command,bg="#6495ED",fg="black")
    w.pack(side=SIDE,fill=BOTH,expand=YES)
    return w

class Calculator(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.option_add("*font","candara 20 bold")
        self.master.title("Simple Calculator")
        self.pack(fill=BOTH,expand=YES)

        display = StringVar()
        framee = frame(self, TOP)
        Ent = Entry(framee,bg="navy",fg="snow",font="tahoma 20 bold",justify=RIGHT,textvariable=display,bd=4)
        Ent.pack(side=TOP,fill=BOTH,expand=YES)

        numbers = ["123*","456-","789/",".0+="]
        for numbuttons in numbers:
            global Fram
            Fram = frame(self,TOP)
            for numbut in numbuttons:
                if numbut == "=":
                    but = button(Fram,numbut,LEFT)
                    but.bind("<ButtonRelease-1>",lambda f, s=self,w=display: s.calc(w))
                else:
                    but = button(Fram,numbut,LEFT,lambda w=display,s=numbut: w.set(w.get() + s))

        Framy = frame(self,TOP)
        button(Framy,"CE",BOTTOM,lambda w=display: w.set(""))

        Fram = frame(self,TOP)
        button(Fram,"exit",BOTTOM, exit)


    def calc(self,disp):
        try:
            disp.set(eval(disp.get()))
        except:
            disp.set("MATH ERROR")

# if __name__ == "__main__":
#     Calculator().mainloop()
# ---------------------------------THE END ----------------------------------------------------------
"""

#---------------------------------------SCIENTIFIC CALCULATOR-----------------------------------------
# from tkinter import *
# from math import *
#
# def frame(stem,SIDE):
#     w = Frame(stem,borderwidth=1,bg="#2F4F4F")
#     w.pack(side=SIDE,fill=BOTH,expand=YES)
#     return w
#
# def button(stem,SIDE,text,command=None):
#     w = Button(stem,text=text,command=command,width=5,height=1,relief=RAISED,bd=5)
#     w.pack(side=SIDE,fill=BOTH,expand=YES)
#     return w
#
# def label(stem,SIDE,text):
#     w = Label(stem,text=text,bg="#2F4F4F",font="arial 7 bold",fg="powder blue")
#     w.pack(side=SIDE,fill=BOTH,expand=YES)
#     return w
#
# class Calculation(Frame):
#
#     def __init__(self):
#         Frame.__init__(self)
#         self.option_add("*font","candara 13 bold")
#         self.master.title("Scientific Calculator")
#         self.pack(fill=BOTH,expand=YES)
#
#         display = StringVar()
#         dis = IntVar()
#         F = frame(self,TOP)
#         Entry(F,bg="tomato",fg="snow",textvariable=display,justify=RIGHT,font="tahoma 14 bold").pack(fill=BOTH,expand=YES)
#         # Txt = Text(F,bg="tomato",fg="snow",font="tahoma 14 bold",width=12,height=4).pack(fill=BOTH,expand=YES)
#         # label(self, TOP, "Calculate").pack(fill=BOTH, expand=YES)
#
#         ky = [
#               {"2nd":"second","Mode":"Quit","STO":"Ins","Alpha":"Lock","Start":"List"},
#               {"Math":"Test  A","Mtrx":"Angle  B","Prgm":"Draw  C","Vars":"YVars","^":""},
#               {"x2":"square","sin":"sin-1","cos":"cos-1","tan":"tan-1","Ln":""},
#               {"sqrt":"Root 1Root 1",",":"EE J","(":"{  k",")":"} L","/":" M"},
#               {"Log":"","7":"G","8":"H","9":"I","*":""},
#               {"Clr":"Clear","4":"D","5":"E","6":"F","-":""},
#               {"Del":"","1":"A","2":"B","3":"C","+":""},
#               {"OFF":"END","0":"",".":"","π":"","ENTER":"="}
#               ]
#
#         special = [i for i in ["+","-","*","/"]]
#
#         for i in ky:
#             H = frame(self, TOP)
#             G = frame(self,TOP)
#             for k,l in i.items():
#                 if k == "Clr":
#                     button(G,LEFT,k,lambda w=display: w.set("")).config(bg="gold")
#                 elif k == "Del":
#                     button(G,LEFT,k,lambda w=display: w.set(display.get()[:-1])).config(bg="gold")
#                 elif k == "OFF":
#                     button(G,LEFT,k,lambda w=display: quit()).config(bg="red",fg="white")
#                 elif k == "sqrt":
#                     button(G,LEFT,k,lambda w=display,s=k:w.set(sqrt(float(display.get())))).config(bg="powder blue")
#                 elif k == "ENTER":
#                     button(G,LEFT,k).bind("<ButtonRelease-1>",lambda v,s=self,w=display:s.calc(w))
#                 elif k == "sin":
#                     button(G,LEFT,k,lambda w=display,s=k: w.set(sin(float(display.get())))).config(bg="powder blue")
#                 elif k == "cos":
#                     button(G,LEFT,k,lambda w=display,s=k: w.set(cos(float(display.get())))).config(bg="powder blue")
#                 elif k == "tan":
#                     button(G,LEFT,k,lambda w=display,s=k: w.set(tan(float(display.get())))).config(bg="powder blue")
#                 elif k == "x2":
#                     button(G,LEFT,k,lambda w=display,s=k: w.set(float(display.get())**2)).config(bg="powder blue")
#                 elif k == "π":
#                     button(G,LEFT,k,lambda w=display, s=k: w.set(pi)).config(bg="powder blue")
#                 elif k == ["1","2"]:
#                     button(G,LEFT,k).config(bg="powder blue")
#                 else:
#                     label(H, LEFT, l)
#                     button(G,LEFT,k,lambda w=display, s=k: w.set(w.get()+s))
#
#
#     def calc(self,display):
#         try:
#             display.set(eval(display.get()))
#         except:
#             display.set("MATH ERROR")
#
#
# if __name__ == "__main__":
#     Calculation().mainloop()
#----------------------------------------------END--------------------------------------------------------------
"""
from tkinter import *
root =  Tk()
root.title("Wonders")

h = Frame(root, borderwidth=4,bd=10,bg="silver")
h.pack(side=TOP, fill=BOTH, expand=YES,padx=20,pady=10)
b = Frame(root, borderwidth=4,bd=10,bg="gold")
b.pack(side=BOTTOM, fill=BOTH, expand=YES,padx=20,pady=10)

for o in [RAISED,SUNKEN,RAISED,FLAT,GROOVE]:
    Button(h, text=o, relief=o, width=20).pack(side=LEFT)
    Label(b, text=o, relief=o, width=20).pack(side=LEFT)

root.mainloop()

from tkinter import *
root = Tk()
root.title("Let me see")
of = [None]*6
for bdw in range(1,6):
    of[bdw] = Frame(root, borderwidth=0)
    Label(of[bdw], text=f'borderwidth = {bdw}').pack(side=LEFT)
    ifx = 0
    iff = []
    for relief in [RAISED, SUNKEN, FLAT, RIDGE, GROOVE, SOLID]:
        iff.append(Frame(of[bdw], borderwidth=bdw, relief=relief))
        Label(iff[ifx], text=relief, width=10).pack(side=LEFT)
        iff[ifx].pack(side=LEFT, padx=10 - bdw, pady=5 - bdw)
        ifx = ifx + 1
    of[bdw].pack()

root.mainloop()
"""
"""
from tkinter import *
root = Tk()
root.title("Taste | See")

def out():
    print("HE IS ALIVE")
f = Frame(root,width=450,height=200,bg="grey")
f.pack()

xf = Frame(f,relief=GROOVE,borderwidth=4,bd=4,bg="white")
Label(xf,text="You got it!",font="tahoma 14 bold").pack(pady=20)
Button(xf,text="HE IS DEAD!",font="arial 8 bold",state="disable").pack(side=LEFT,padx=20,pady=10)
Button(xf,text="HE IS NOT DEAD",font="arial 8 bold",command=quit).pack(side=RIGHT,padx=20,pady=10)
Button(xf,text="HE IS ALIVE",font="arial 8 bold",command=out).pack(side=RIGHT,padx=20,pady=10)
xf.place(relx=0.05,rely=0.08)
Label(f,text="AM ABOVE ALL!",height=1,font="arial 10 bold").place(relx=0.09,rely=0.05,anchor=NW)
"""
"""
from tkinter import *
leave = Tk()
off = [None]*5
for i in range(5):
    off[i] = Frame(leave,borderwidth=0)
    Label(off[i],text=f"Borderwidth = {i}").pack(side=LEFT)
    j = 0
    k = []
    for l in sorted([FLAT,RIDGE,RAISED,SUNKEN,SOLID,GROOVE]):
        k.append(Frame(off[i],borderwidth=i,relief=l))
        Button(k[j],text=l.capitalize(),width=10).pack(side=LEFT)
        k[j].pack(side=LEFT,padx=9 - i,pady=9 + i)
        j += 1
    off[i].pack(fill=BOTH,expand=YES)


from tkinter import *
root = Tk()
v = IntVar()
f = Frame(root)

for i in ["Passion fruit","Loganberries","Mangoes in syrup","Oranges","Apples","Grapefruit"]:
    Rd = Radiobutton(root,variable=v,text=i,value=i,indicatoron=0,width=20)
    Rd.pack(side=TOP,anchor=W)
    v.set("Apples")
    f.pack(padx=50,side=TOP)
root.mainloop()

from tkinter import *
root = Tk()
# root.geometry("500x250")
for i, row, column in [("John Clease",0,0),("Eric Idle",1,0),("Graham Chapman",2,0),("Terry Jones",0,1),("Michael Palin",1,1),("Terry Gilliam",2,1)]:
    Checkbutton(root,text=i,font="tahoma 14 bold").grid(row=row,column=column,sticky=W)
    if "Eric Idle" in i:
        Checkbutton(root,text=i,font="tahoma 14 bold",state=DISABLED).grid(row=row,column=column,sticky=W)
root.mainloop()
"""
"""
# ----------------------------------------------------- MENUBAR WIDGET -------------------------------------------------
from tkinter import *
root = Tk()
root.title("MenuBar")
root.geometry("500x300")
root.config(bg="powder blue")

f = Frame(root)
MenuBar = Menu(f)

filename = Menu(MenuBar,tearoff=0,background="grey")
MenuBar.add_cascade(label="File",menu=filename)
filename.add_command(label = "New")
filename.add_command(label = "Save")
filename.add_command(label = "Save as")
filename.add_command(label = "Open")
filename.add_separator()
filename.add_command(label = "Exit",command=quit)

filename = Menu(MenuBar,tearoff=0)
MenuBar.add_cascade(label="View",menu=filename)
filename.add_checkbutton(label = "New")
filename.add_checkbutton(label = "Save")

filename = Menu(MenuBar,tearoff=0)
MenuBar.add_cascade(label="Edit",menu=filename)
filename.add_cascade(label = "New")
filename.add_command(label="New Folder")
filename.add_radiobutton(label = "Save")

f.grid()
root.config(menu=MenuBar)
root.mainloop()
# ---------------------------------------------------- END -------------------------------------------------------------
"""
"""
#------------------------------------------------- POSITIONING ---------------------------------------------------------
from tkinter import *
stem = Tk()
stem.title("Positioning")

frame = Frame(stem,width=500,height=250,bg="white")
lb = Label(frame,text="Please move me!",font="tahoma 16 bold")
# lb.grid(row=10,column=10,sticky=E)
lb.place(relx=.5,rely=.5,anchor=CENTER)

def top_left():
    lb.place(relx=.18, rely=.15, anchor=CENTER)
    lb.config(bg="red",fg="white")
def top_right():
    lb.place(relx=.82, rely=.15, anchor=CENTER)
    lb.config(bg="blue",fg="white")
def bottom_left():
    lb.place(relx=.18, rely=.83, anchor=CENTER)
    lb.config(bg="orange",fg="white")
def bottom_right():
    lb.place(relx=.82, rely=.84, anchor=CENTER)
    lb.config(bg="purple",fg="white")

use = [("TopLeft",0,0),("TopRight",0,200),("BottomLeft",200,0),("BottomRight",200,200)]
use_2 = [("TopLeft",0,0,top_left),("TopRight",420,0,top_right),("BottomLeft",0,225,bottom_left),("BottomRight",420,225,bottom_right)]

for i,j,k,l in use_2:
    Btn = Button(frame,text=i,relief=RAISED,bd=3,bg="black",fg="white",command=l)
    # Btn.grid(row=j,column=k,sticky=W)
    Btn.place(x=j,y=k,width=80,height=25)
# frame.place(x=5,y=5,width=500,height=250)
frame.pack()

# --------------------------------------------- END -------------------------------------------------------------------
"""
"""
from tkinter import *
window = Tk()
window.title("Writer")
window.config(bg="royal blue")
f = Frame(window)
text = Text(f,width=80,height=30)
scrollbar = Scrollbar(f,command=text.yview)
text.config(yscrollcommand=scrollbar.set)

text.tag_config("fonts", font=("candara", 20, "bold", "italic", "underline"))
text.tag_config("color", foreground="white", background="red")

text.tag_bind("click","<1>",lambda vicolas, t=text: t.insert(END,"Hello am a the best programmer!\n"))

text.insert(END,"Am really enjoying this dude!\n")
text.insert(END,"The sky is your starting point\n","fonts")
text.insert(END,"Are are a psycho?\n","color")
text.insert(END,"PYTHON IS ONE OF THE BEST PROGRAMMING LANGUAGE\n","color")

Photo = PhotoImage(file="nike_hd.gif")
text.image_create(END,image=Photo)

but = Button(text,text="Click this Button",width=12,command=quit)
text.window_create(END,window=but)
text.insert(END,"\n")
text.insert(END,"Touch me and see something\n","click")

scrollbar.pack(side=RIGHT,fill=Y,expand=YES)
text.pack(side=LEFT)
f.pack(padx=10,pady=10)
"""
"""-------------------  CANVAS  -----------------------------------------------
from tkinter import *
window = Tk()
window.title("Canvas")
window.config(bg="grey")

f = Frame(window)
f.pack(pady=10,padx=10)
canvas = Canvas(f,bg="white",width=600,height=350)
scrollbar = Scrollbar(f,command=canvas.yview)
scrollbar.pack(side=RIGHT,fill=Y)
canvas.create_line(300,0,300,400,fill="blue",width=5)
canvas.create_line(0,175,600,175,fill="green",width=5)
# canvas.create_oval(200,100,400,300,fill="red",width=0)
canvas.create_oval(200,120,400,250, fill="pink", width=0)
canvas.create_rectangle(10,400,110,500,fill="grey",width=2,outline="blue")

def move():
    canvas.create_oval(10, 30, 110, 130, fill="pink", width=0)
    canvas.create_rectangle(10,250,110,350,fill="grey",width=2,outline="blue")

canvas.create_rectangle(200,120,400,250,fill="orange",width=0)
xy = 150,250,300,80,450,250
# canvas.create_polygon(xy,fill="green",width=0)
canvas.create_bitmap(500, 170, bitmap='questhead')
xy = 400, 100, 500, 200
canvas.create_arc(xy, start=90, extent=270, fill='gold',width=0)

# img = PhotoImage(file='nike_hd.gif')
# canvas.create_image(320,110, image=img, anchor=CENTER)

frm = Frame(canvas,relief=RAISED,borderwidth=2)
use=Label(canvas,text="Embedded Button",relief=RAISED,bd=1,borderwidth=2)
use.pack()
canvas.create_window(50,10,window=use,anchor=CENTER)

but = Button(canvas,text="Circle Appear Now",command=move)
but.pack()
canvas.create_window(53,14,window=but,anchor=CENTER)

canvas.create_text(200,100,text="Dominion is my Heritage!")

canvas.config(yscrollcommand=scrollbar.set)

canvas.pack(side=LEFT,padx=0,pady=0)

"""
"""
from tkinter import *
root = Tk()
root.config(bg="pink")
# F = Frame(root,bg="pink")
# listed = Listbox(F,width=4,height=15,font="tahoma 20 bold",justify=CENTER,bg="lightblue")
# listed.pack(side=LEFT)
# scroll = Scrollbar(F,command=listed.yview)
# scroll.pack(side=RIGHT,fill=Y)
# listed.config(yscrollcommand=scroll.set)
# for i in range(1,101):
#     listed.insert(END,i)
#
# F.pack(padx=10,pady=10)

F = Frame(root)
canvas =  Canvas(F,width=150,height=360, highlightthickness=0)
canvas.create_line(80,18,80,300,fill="black",width=25)
canvas.create_polygon(40,250,78,350,120,250,fill="black",width=5,outline="black")
canvas.create_line(80,20,80,300,fill="blue",width=20)
canvas.create_polygon(40,250,78,350,120,250,fill="blue",width=0)

canvas.pack(side=RIGHT)

scale = Scale(F,from_=1,to=50,length=380,tickinterval=6,font=('Verdana', 8, 'italic'))
scale.pack(side=LEFT)

F.pack()
"""
"""""

"""
'''
from tkinter import *
root = Tk()
root.title("About About Dialog")

f1 = Frame(root,bg="grey80",relief=FLAT,bd=2,borderwidth=3)
f2 = Frame(f1,relief=RAISED,bd=7,borderwidth=2,width=470,height=225,bg="grey80")

msg = Message(f2,font="arial 12 bold",justify=CENTER,width=483,bg="grey80",
              # text="About Dialog\n\nVersion 1.5\nCopyright Company Name 1999"
              #      "\nAll rights reserved\n\nFor information about this application contact:\n"
              #      "Sales at Company Name\nPhone:(401)555-1212\nemail:info@company.com")
msg.place(relx=.5,rely=.5,anchor=CENTER)

f3 = Frame(f1,relief=RAISED,bd=4,borderwidth=2,bg="grey80",width=470,height=50)
but = Button(f3,text="close",bd=2,borderwidth=2,font="arial 13 bold",bg="grey80",command=quit)
but.place(relx=.5,rely=.5,anchor=CENTER)
f3.pack(side=BOTTOM)
f2.pack()
#f1.pack(padx=1,pady=1)
'''
'''
from tkinter import *
import _tkinter
root = Tk()
root.geometry('320x250')
# root.config(bg="grey80")
frame = Frame(root)
f2 = Frame(root)
f3 =  Frame(root)
def obtain():
    global en
    en = vat.get()
    enn = var.get()
    if enn == 1 and en:
        txt.insert(END,"Hello Mr {}!\nHow are you Sir?\n".format(en.capitalize()))
    elif enn == 2 and en:
        txt.insert(END, "Hello Miss {}!\nHow are you Ma'am?\n".format(en.capitalize()))
    else:
        txt.insert(END, "Please input your detials!\n".format(en))
def clean():
    txt.delete(0.0,END)
    ent.delete(0,END)
def hover(event):
    print("Entered Button: x={} y={}".format(event.x,event.y))
def pressed(avt=None):
    txt.insert(END,"About To Type something! {}\n".format(avt.x))
    # print("Button is pressed")
Lb1 = Label(f3,text="Name")
Lb1.pack(side=LEFT,padx=5,pady=5)
vat = StringVar()
ent = Entry(f3,font="times 11",textvariable=vat)
ent.pack(side=LEFT,ipadx=10)
ent.bind('<KeyPress-space>',pressed)
Lb = Label(f2,text="Gender")
Lb.pack(side=LEFT,padx=5,pady=5)
var = IntVar()
r1 = Radiobutton(f2,text="Male",value=1,variable=var)
r1.pack(side=LEFT,padx=5,pady=5)
r2 = Radiobutton(f2,text="Female",value=2,variable=var)
r2.pack(side=LEFT,padx=5,pady=5)
btn = Button(frame,text="Register",bg="purple",fg="white",width=20,command=obtain)
btn.pack(side=TOP,expand=YES)
btn = Button(frame,text="clear",bg="purple",fg="white",width=20,command=clean)
btn.pack(side=TOP,expand=YES,pady=5)
btn.bind("<Any-Enter>",hover)
txt = Text(frame,width=100,height=100)
txt.pack(side=TOP,pady=5)

f3.pack(side=TOP)
f2.pack(side=TOP)
frame.pack(side=TOP,pady=5,padx=5)
'''
"""
#--------------------------- CHECKING ---------------------------------------------------------------------
from tkinter import *
root = Tk()
root.title("Checking")
root.geometry("310x300")
root.resizable(0,0)

frame = Frame(root,relief=RAISED)

def command():
    blank = ""
    word = var.get()
    for i in word:
        if i in "AEIOUaeiou":
            blank += "*"
        else:
            blank += i
    # global lb
    # lb = Label(root, text=blank + "\n", font="tahoma 12 bold")
    # lb.grid(row=2, column=0, pady=2)
    tx.tag_config('just',font=("arial",12),foreground="red")
    tx.insert(END,blank)

def clear():
    ent.delete(0,END)
    tx.delete(0.0,END)

Label(frame,text="Enter A Word").grid(row=0,column=0,padx=5,pady=5,sticky=W)
var = StringVar()
ent = Entry(frame,textvariable=var,width=30)
ent.grid(row=0,column=1,sticky=W)
f = Frame(root)
but = Button(f,text="check",bg="purple",fg="white",width=10,command=command)
but.grid(row=1,column=0,sticky=W,padx=15)
butt = Button(f,text="clear",bg="purple",fg="white",width=10,command=clear)
butt.grid(row=1,column=1,sticky=W,padx=15)

tx = Text(root,width=32,height=12)
tx.grid(row=3,column=1,pady=5,padx=18,sticky=W)
scr = Scrollbar(root,command=tx.yview)
scr.grid(row=3,column=1,ipady=78,sticky=E)
tx.config(yscrollcommand=scr.set)
f.grid(row=1,column=1,pady=5)
frame.grid(row=0,column=1,pady=5)
root.mainloop()
#-------------------------------    END     ----------------------------------------------------
"""
"""
from tkinter import *
window = Tk()
window.title("Entry Field Validation")
window.geometry('450x220')
window.option_add("*background","light blue")
# window.option_add("*font","arial 16 bold")
window.config(bg="light blue")
# window.resizable(0,0)

frame = Frame(window)
f2 = Frame(window)
for j,_ in enumerate([("Date (mm/dd/yy):"),("Time (24hr clock):"),("Real (50.0 to 1099.0):"),("Social Security #:")]):
    Lb = Label(frame,text=_,font="times 16 bold")
    Lb.pack(side=TOP,anchor=W,pady=5,padx=5)
    var = StringVar()
    ent = Entry(f2,width=39,bg="yellow",textvariable=var)
    ent.pack(side=TOP, anchor=W, pady=7,ipady=3,padx=5,expand=NO,fill=X)
    def clean():
        ent.delete(0,END)
f3 = Frame(window)
bt = Button(f3,text="QUIT",width=10,command=quit)
bt.pack(side=LEFT,pady=5,padx=5)
btt = Button(f3,text="CLEAN",width=10,command=clean)
btt.pack(side=LEFT,pady=5,padx=5)
f3.pack(side=BOTTOM)
f2.pack(side=RIGHT)
frame.pack(side=LEFT)
window.mainloop()
"""
"""
from tkinter import *
from time import sleep
window = Tk()
window.title("Automated Teller Machine (ATM)")
window.option_add("*background","orange")
window.option_add("*font","times 14 bold")
window.geometry("350x250")
window.config(bg="orange")
def passcode():
    psw = "1234"
    start = 0
    limit = 3
    get = var.get()
    out_of_guess = True
    text.tag_config("bg",foreground="red")
    text.tag_config("bgg",foreground="blue")
    start_out1 = str(limit - 1)
    start_out2 = str(limit - 2)
    start_out3 = str(limit - 3)
    while get != psw and out_of_guess:
     if start < limit:
         start += 1
         if start <= 1:
            text.insert(END,f"Incorrect PIN\nPlease try again!\nYou have {start_out1} out of 3\n")
         elif start <= 2:
            text.insert(END, f"Incorrect PIN\nPlease try again!\nYou have {start_out2} out of 3\n")
         elif start <= 3:
            text.insert(END, f"Incorrect PIN\nPlease try again!\nYou have {start_out3} out of 3\n","bg")
         else:
            pass
     else:
        out_of_guess = False
    if out_of_guess:
        text.insert(END,"Successful","bg")
    else:
        text.insert(END,"Terminating\nCalling FBI...","bgg")

def clear():
    entry.delete(0, END)
    text.delete(1.0,END)
frame = Frame(window)
f2 = Frame(window)
f3 = Frame(window,relief=GROOVE,bg="white",borderwidth=2,bd=3)
label = Label(f3,text="GTBank",fg="white",font="arial 20 bold")
label.pack(side=TOP)
label = Label(f2,text="Enter Your ATM PIN:")
label.pack(side=LEFT)
var = StringVar()
entry = Entry(f2,textvariable=var,show="x",bg="white")
entry.pack(side=LEFT,padx=5,pady=10)
button = Button(frame,text="GO",bg="black",fg="white",width=5,command=passcode)
button.pack(side=LEFT,padx=5)
button = Button(frame,text="CLEAR",bg="black",fg="white",width=6,command=clear)
button.pack(side=LEFT,padx=5)
button = Button(frame,text="QUIT",bg="black",fg="white",width=6,command=window.destroy)
button.pack(side=LEFT,padx=5)
f4 = Frame(window)
text = Text(f4,width=50,height=4,bg="white")
text.pack(side=TOP,padx=5,pady=5)
f4.pack(side=BOTTOM)
f3.pack(side=TOP,pady=10)
f2.pack(side=TOP)
frame.pack(side=TOP)
window.mainloop()
"""
"""
from tkinter import *
import Pmw

root = Tk()
root.title('Register')
def status():
    word = varr.get()
    gender = var.get()
    if gender == 1:
        text.insert(END,f'Hi Mr {word.capitalize()}\nHow are you doing today?\n','Color')
        text.tag_config('Color', foreground='blue')
    elif gender == 2:
        text.insert(END, f'Hi Miss {word}\nHow are you doing today?\n','Color')
        text.tag_config('Color',foreground='red')
        text.insert(END,'Please enter your name')
    else:
        text.insert(END, 'Please input something!\n')
balloon =  Pmw.Balloon(root)
varr = StringVar()
entryfield = Pmw.EntryField(root,labelpos=W,label_text='Name:',entry_width=22,entry_textvariable=varr)
entryfield.grid(row=0,column=0,sticky=W,padx=5,pady=5)
button = Button(root,text='Status',command=status)
button.grid(row=0,column=0,sticky=E,padx=5,pady=5,ipadx=10)
balloon.bind(entryfield,'Enter Your Name')
balloon.bind(button,'Check Your Status')
var = IntVar()
f = Frame(root)
f.grid()
radiobutton = Radiobutton(f,text='Male',variable=var,value=1,indicatoron=0,activebackground='grey').grid(row=1,column=0,sticky=W,padx=5,pady=5,ipadx=30)
radiobutton_2 = Radiobutton(f,text='Female',variable=var,value=2,indicatoron=0).grid(row=1,column=1,sticky=W,padx=5,pady=5,ipadx=30)
frame = Frame(root)
frame.grid()
text = Text(frame,width=30,height=5)
text.grid(row=2,column=0,sticky=W,padx=5,pady=5)
scrollbar = Scrollbar(frame,command=text.yview)
scrollbar.grid(row=2,column=0,sticky=E,ipady=17)
text.config(yscrollcommand=scrollbar.set)
balloon.bind(text,'Your Status Display Here')
btn = Button(frame,text='Clear',command=lambda: text.delete(0.0,END))
btn.grid(row=3,column=0,sticky=W,pady=5,padx=90,ipadx=15)
root.mainloop()
"""
"""
from tkinter import *
import Pmw

class Bind:
    def __init__(self):
        self.root = Tk()
        self.root.title('ButtonBox')
        self.build_Event()
        self.root.mainloop()

    def build_Event(self):
        self.label = Label(self.root,text='What Event?',width=30)
        self.label.pack(fill=X,expand=YES)
        self.label.bind('<B3-Motion>', self.motion)

        self.entryfield = Pmw.EntryField(self.root, label_text='What Event?', labelpos=W)
        self.entryfield.pack(fill=X, expand=YES,padx=5,pady=5)
        self.entryfield.bind('<Return>', self.key)

        self.buttonbox = Button(self.root,text='click')
        self.buttonbox.pack(side=LEFT,padx=2,pady=5,fill=X,expand=YES)
        self.buttonbox.bind('<ButtonRelease-3>', self.click)

        self.buttonbox_1 = Button(self.root, text='double')
        self.buttonbox_1.pack(side=LEFT,padx=2, pady=5, fill=X, expand=YES)
        self.buttonbox_1.bind('<Double-Button-1>',self.double)

        self.buttonbox_2 = Button(self.root, text='Enter')
        self.buttonbox_2.pack(side=LEFT, padx=2, pady=5, fill=X, expand=YES)
        self.buttonbox_2.bind('<Enter>',self.leave_enter)
        self.buttonbox_2.bind('<Leave>', self.leave_enter)

        self.buttonbox_3 = Button(self.root, text='Focus')
        self.buttonbox_3.pack(side=LEFT, padx=2, pady=5, fill=X, expand=YES)
        self.buttonbox_3.bind('<FocusIn>', self.focusin)

    # EVENTS FUNCTIONS DEFINED BELLOW:
    def motion(self,event):
        print(f'({event.x},{event.y})')
        if event.x == 10 and event.y == 10:
            self.root.destroy()
            print('Yeah Dude you got the point. Congratulations!!!')

    def click(self,event):
        print('You just released left clicked button')
        self.label.configure(text='You click!')

    def key(self,event):
        print('You pressed down a key')

    def double(self,event):
        print('You double-clicked and single clicked')
        self.label.configure(text='You double Clicked!')

    def leave_enter(self,event):
        print('You just left')
        self.label.configure(text='You just left the button widget!')

    def focusin(self,event):
        print('You just focusin')
        self.label.configure(text='You focusin!')

if __name__ == '__main__':
     Bind()

"""
"""
from tkinter import *
from time import *
import Pmw

class Counter:
    def __init__(self):
        self.root = Tk()
        self.root.title('Counter')
        self.build_Count()
        self.build_CountDialog()
        self.root.mainloop()

    def build_Count(self):
        self.date = Pmw.Counter(self.root,labelpos=W,
                    label_text = 'Date (4-Years):',
                    entryfield_value = strftime('%d/%m/%Y',localtime(time())),
                    datatype = dict(counter='date',format='dmy',yyyy=1),
                    entryfield_command = self.execute)
        self.integer = Pmw.Counter(self.root,labelpos=W,
                    label_text = 'Integer:',
                    entry_width = 2,
                    entryfield_value = 50,
                    entry_justify = CENTER,
                    orient = VERTICAL,
                    entryfield_validate = dict(validator='integer',min=0,max=80))
        self.real = Pmw.Counter(self.root,labelpos=W,
                    label_text = 'Real (with comma):',
                    entryfield_value = 4,
                    entryfield_validate = dict(validator='numeric',min=0,max=10),
                    increment = 1)
        counters = (self.date,self.integer,self.real)
        Pmw.alignlabels(counters)
        for _ in counters:
            _.pack(expand=1,fill=BOTH,padx=5,pady=5)

    def build_CountDialog(self):
        self.counterdialog = Pmw.CounterDialog(self.root,counter_labelpos=N,
            label_text = 'Enter the number of twits (2 to 8)',
            buttons = ('Ok','Cancel'),
            defaultbutton = 'Ok',
            command = lambda event: print('You just click',event),
            counter_datatype = 'numeric',
            entryfield_value = 4,
            entryfield_validate = dict(validator='numeric',min=2,max=8),
            title='CounterDialog')
        self.counterdialog.tkraise()
        print(f'You click',self.counterdialog.activate())

    def execute(self,event):
        print('You clicked',event)

if __name__ == '__main__':
    Counter()
"""
"""
from tkinter import *
import Pmw

class Entryfield:
    def __init__(self):
        self.window = Tk()
        self.window.title('EntryField')
        self.build_EntryField()
        self.window.mainloop()

    def build_EntryField(self):
        for i in ('No Validation:','Real (96.0 to 107.0):','Integer (5 to 42):','Date (in 2000):'):
            if i == 'Real (96.0 to 107.0):':
                self.entryfield = Pmw.EntryField(self.window, labelpos=W,label_text=i,label_width=15,entry_width=30,label_anchor=W,value=94.5,validate = dict(validator='real',min=96.0,max=107.0))
            elif i == 'Integer (5 to 42):':
                self.entryfield = Pmw.EntryField(self.window, labelpos=W, label_text=i, label_width=15, entry_width=30,label_anchor=W,value=30,validate=dict(validator='integer',min=5,max=42))
            elif i == 'Date (in 2000):':
                self.entryfield = Pmw.EntryField(self.window, labelpos=W, label_text=i, label_width=15, entry_width=30,label_anchor=W, value='2000/1/1',validate=dict(validator='date', min='2000/2/2', max='2000/3/3'))
            else:
                self.entryfield = Pmw.EntryField(self.window, labelpos=W, label_text=i, label_width=15, entry_width=30,label_anchor=W, validate=dict(validator=None))
            self.entryfield.pack(fill=X,expand=1,padx=5,pady=8)

if __name__ == '__main__':
    Entryfield()
"""
"""
from tkinter import *
from tkinter import ttk
import Pmw

class New_Register:

    def __init__(self):
        self.root = Tk()
        self.root.title('New Register')
        self.style = ttk.Style()
        self.style.configure('danger.TButton',relief=RAISED,background='blue')
        self.gender = [('Male',1),('Female',2),('item',3)]
        self.build_Register()
        self.root.mainloop()

    def build_Register(self):
        f = Frame(self.root)
        self.string = StringVar()
        self.entry = Pmw.EntryField(f,labelpos=N,label_text='Name:',entry_textvariable=self.string)
        self.entry.pack(side=LEFT,padx=5,pady=5)
        self.button = ttk.Button(f,text='check',style='danger.TButton',command=self.execute)
        self.button.pack(side=TOP,padx=5,pady=5)
        self.button_2 = ttk.Button(f, text='clear', style='danger.TButton', command=self.clear)
        self.button_2.pack(side=TOP, padx=5, pady=5)
        f.pack()
        F = Frame(self.root)
        self.var = IntVar()
        for i,k in (self.gender):
            self.radiobutton = ttk.Radiobutton(F,text=i,variable=self.var,value=k)
            self.radiobutton.pack(side=LEFT,padx=5,pady=5)
        F.pack()
        frame = Frame(self.root)
        self.msg = Text(frame,width=30,height=5)
        self.msg.pack(side=LEFT,padx=0,pady=5)
        self.scroll =  ttk.Scrollbar(self.root,command=self.msg.yview)
        self.scroll.pack(side=RIGHT,fill=Y,expand=1)
        self.msg.config(yscrollcommand=self.scroll.set)
        frame.pack()

    def execute(self):
        self.get_int = self.var.get()
        self.get_string = self.string.get()
        if self.get_string == '':
            self.msg.insert(END, 'Please input something\n')
        elif self.get_int == 1:
            self.msg.insert(END,f'Hello Mr. {self.get_string}\nHow are you today Sir?\n')
        elif self.get_int == 2:
            self.msg.insert(END, f'Hello Miss {self.get_string}\nHow are you today Ma?\n')
        elif self.get_int == 3:
            self.msg.insert(END, f'Hello {self.get_string}\nHow are you today Ma?\n')
        else:
            self.msg.insert(END,'Please click either male, female or item\n')

    def clear(self):
        self.msg.delete(0.0,END)
        self.entry.delete(0,END)

if __name__=='__main__':
    New_Register()
"""
"""
from tkinter import *
import Pmw

class MenuWidget:
    def __init__(self):
        self.root = Tk()
        self.root.title('Menu Widget')
        self.root.wm_geometry('500x250+9+9')
        self.root.option_add("*background","orange")
        self.build_Menu_Widget()
        self.root.mainloop()

    def build_Menu_Widget(self):
        frame = Frame(self.root,bg='blue')
        frame.pack()
        self.balloon = Pmw.Balloon(self.root)
        menu = Menu(frame,tearoff=False,activebackground='red')
        self.root.config(menu=menu)
        g = [None]*6
        for filemenu in range(1,6):
            g[filemenu] = Menu(menu,tearoff=False,selectcolor='red',activeborderwidth=2,activebackground='black',relief=SOLID,bd=5)

        # FILE MENU
        menu.add_cascade(label='File',menu=g[1],underline=1)

        for i in ['New', 'Open', 'Save', 'Print', 'Exit']:
            if i == 'Exit':
                g[1].add_separator()
                g[1].add_command(label=i,command=quit)
            else:
                g[1].add_command(label=i)

        # EDIT MENU
        dropdown = Menu(menu,tearoff=False)
        for x in ['Update','View','Review','Home','Page']:
            dropdown.add_command(label=x)

        menu.add_cascade(label='Edit',menu=g[2])
        for k,l in [('Copy','Ctrl+C'),('Cut','Ctrl+X'),('Paste','Ctrl+V'),('Find','Ctrl+F'),('Delete','Delete')]:
            if k == 'Paste':
                g[2].add_separator('')
                g[2].add_command(label=(f'{k} \t \t {l:>12}'))
            elif k == 'Delete':
                g[2].add_separator('')
                g[2].add_cascade(label=(f'{k} \t \t {l:>12}'),menu=dropdown)
            else:
                g[2].add_command(label=(f'{k} \t \t {l:>15}'))

        # VIEW MENU
        menu.add_cascade(label='View',menu=g[3])
        for i in ['ToolBar','Tool Button','Status Bar','Navigation Bar']:
            g[3].add_radiobutton(label=i)

        # WINDOW MENU
        menu.add_cascade(label='Window',menu=g[4])
        for i in ['ToolBar','Tool Button','Status Bar','Navigation Bar']:
            g[4].add_checkbutton(label=i)

        # HELP MENU
        menu.add_cascade(label='Help',menu=g[5])
        g[5].add_command(label='Press F1',command=self.do_Something)

    def do_Something(self):
        self.toplevel = Toplevel(self.root)
        self.toplevel.geometry('200x100+10+10')
        self.button =  Button(self.toplevel,text='Do Nothing Yet!',command=self.toplevel.destroy)
        self.button.pack(pady=24)
        self.balloon.bind(self.button, 'Click and See!')
        # Pmw.initialise()
        Pmw.aboutversion('1.5')
        Pmw.aboutcopyright('Copyright SoftTouch International \nA subsidiry of Vicolas Cooperation')
        Pmw.aboutcontact('No. 21 Garki, Abuja Nigeria\nvicolas@softouch.io\n(+234)9099693940')
        self.about = Pmw.AboutDialog(self.toplevel)

if __name__ == '__main__':
    MenuWidget()
"""
"""
from tkinter import *
import Pmw

class Message:
    def __init__(self):
        self.root = Tk()
        self.build_Message()
        self.root.mainloop()

    def build_Message(self):
        self.entry = self.combobox =  None
        self.messages = {'Help': 'Save current file',
                         'Userevent': 'Saving file "foo"',
                         'Busy': 'Busy deleting all files from file system ...',
                         'Systemevent': 'File "foo" saved',
                         'Usererror': 'Invalid file name "foo/bar"',
                         'Systemerror': 'Failed to save file: file system full',
                         }
        self.combobox = Pmw.ComboBox(self.root, labelpos=N, label_text='Message Type',
                                dropdown=False,
                                listbox_relief=SUNKEN,
                                listbox_font = 'tahoma 10 bold',
                                scrolledlist_items = self.messages.keys(),
                                selectioncommand = self.enter,
                                listbox_background='grey')
        self.combobox.pack(fill=X,padx=5,pady=5)
        self.entry = Pmw.MessageBar(self.root,labelpos=W,label_text='Status:',entry_width=30)
        self.entry.pack(fill=X,padx=5,pady=5)

    def enter(self,event):
        self.combobox.configure(label_text=event)
        self.entry.helpmessage(self.messages[event])

if __name__=="__main__":
    Message()
"""
"""
from tkinter import *
from tkinter import ttk

class Notebook:
    def __init__(self):
        self.root = Tk()
        self.root.title('Note Book')
        self.build_Menu()
        self.build_NoteBook()
        self.build_page_1()
        self.count = 1
        self.root.mainloop()

    def build_Menu(self):
        # MENU WIDGET CONFIGURATION
        self.menu = Menu(self.root)
        self.root.configure(menu=self.menu)
        self.filemenu = [None] * 3
        for f in range(1,3):
            self.filemenu[f] = Menu(self.menu,tearoff=False)
        #FILE MENU
        self.menu.add_cascade(label='File', menu=self.filemenu[1])
        for i in ['New','Open','Save','Print','Exit']:
            if i == 'New':
                self.filemenu[1].add_command(label=i,command=self.Add_New_Tab)
            elif i == 'Print':
                self.filemenu[1].add_command(label=i)
                self.filemenu[1].add_separator('')
            elif i == 'Exit':
                self.filemenu[1].add_command(label=i,command=quit)
            else:
                self.filemenu[1].add_command(label=i)
        #EDIT MENU
        self.menu.add_cascade(label='Edit',menu=self.filemenu[2])
        for i,k,l in [('Copy','Ctrl+C',''),('Cut','Ctrl+X','s'),('Paste','Ctrl+P',''),('Select All','Ctrl+A','s'),('Delete','Delete','')]:
            if i == 'Delete':
                self.filemenu[2].add_command(label=(f'{i} {k:>20}'),command=lambda:self.canvas.delete(ALL))
            elif l == 's':
                self.filemenu[2].add_command(label=(f'{i} {k:>20}'))
                self.filemenu[2].add_separator('')
            else:
                self.filemenu[2].add_command(label=(f'{i} {k:>20}'))
    # ADD NEW TAG CODE
    def Add_New_Tab(self):
        self.count += 1
        self.notebook.add(self.tab[self.count],text=f'Page {self.count}')

    def build_NoteBook(self):
        # NOTEBOOK WIDGET CONFIGURATION
        self.notebook = ttk.Notebook(self.root,height=400,width=800)
        self.tab = [None] * 10
        for t in range(1,10):
            self.tab[t] = ttk.Frame(self.notebook)
        self.notebook.add(self.tab[1],text='Page 1',underline=0)
        self.notebook.pack(fill=BOTH, expand=YES, padx=5, pady=5)

        #PAGE ONE CONTENTS
    def build_page_1(self):
        self.canvas = Canvas(self.tab[1],width=100,height=50,bg='#ffffff',cursor='heart')
        self.canvas.pack(fill=BOTH,expand=True,padx=5,pady=5)
        self.canvas.bind('<B1-Motion>',self.bind_paint)
        ttk.Button(self.tab[1], text='clean', command=lambda: self.canvas.delete(ALL)).pack(side=LEFT,anchor=CENTER,padx=90,pady=5,fill=X,expand=1)
        ttk.Button(self.tab[1], text='close', command=quit).pack(side=LEFT, padx=90, fill=X, anchor=CENTER,expand=1)

    #BINDING MOTION THAT SKETCHED THE CIRCLES RED COLORS
    def bind_paint(self,event):
        x1,y1 = (event.x - 5),(event.y - 5)
        x2,y2 = (event.x + 5),(event.y + 5)
        i = self.canvas.create_oval(x1,y1,x2,y2,fill='#ff0000',outline='#000000')
        return i

if __name__ == '__main__':
    Notebook()
"""
"""
from tkinter import *
import Pmw
class Radioselect:

    def __init__(self):
        self.master = Tk()
        self.master.title("Option Menu")
        self.build_RadioSelect()
        self.master.mainloop()

    def build_RadioSelect(self):
        self.master.configure(padx=5,pady=10)
        self.frame = Frame(self.master,relief=RIDGE,bd=2)
        self.frame.pack(ipadx=5,pady=6)
        self.dic = {('Passion Fruit',1):('Doug',1),
                    ('Loganberries',2):('Dinsdale',2),
                    ('Mangoes in Syrup',3):("Stig O'Tracy",3),
                    ('Vince',4):('Oranges',4),
                    ('Gloria Pules',5):('Apples',5),
                    ('PineApple',6):('Grapefruit',6)}
        #UPPER CHAMBERS
        self.var = IntVar()
        self.label = Label(self.frame, text='Horizonal:').pack(side=LEFT)
        for i,k in self.dic.keys():
            self.radio = Radiobutton(self.frame,text=i,value=k,variable=self.var,indicatoron=False,width=15)
            self.radio.pack(side=LEFT,padx=0,pady=12)
            self.radio.bind('<Button-1>',self.selected)

        # LOWER CHAMBERS
        self.f = Frame(self.master,relief=RIDGE,bd=2)
        self.f.pack(ipadx=5,ipady=5,pady=5)
        self.label = Label(self.f, text='Multiple\nSelection:').pack(side=LEFT)

        for i,k in self.dic.values():
            self.radio_2 = Radiobutton(self.f,text=None,value=k,variable=self.var,indicatoron=False,width=15)
            self.radio_2.pack(side=LEFT,padx=0,pady=12)

    def selected(self,event):
        for event,k in self.dic.values():
            self.radio_2.configure(text=f'{event}')
            self.radio_2.pack()

if __name__ == "__main__":
    Radioselect()
"""
"""

#-------------------------------------------- RECORDING DIALOG WINDOW -------------------------------------------------
from tkinter import *
root = Tk()
root.title("New Waveform")
root.geometry("370x272")

frame = Frame(root, width=370, height=270)
f2 = Frame(frame,relief=GROOVE,borderwidth=3,width=103,height=259)

label = Label(frame,text="Sample Rate")
label.place(relx=.03,rely=.001)
f2.place(relx=.01,rely=.03)
var = StringVar()
entry = Entry(f2,text="",bg="white",relief=SUNKEN,width=14,textvariable=var)
entry.place(relx=.04,rely=.05)

mvarr = StringVar()
listbox = Listbox(f2,width=14,height=13,bd=2,listvariable=mvarr,takefocus=True)
listbox.place(rely=.15,relx=.03)
lis = ("192000","96000","88200","64000","48000","44100","32000","22050","16000","11025","8000","6000")
for z in lis:
    listbox.insert(END,str(z))

def CurSelect(evt):
    cur = listbox.curselection()[0]
    if listbox.get(cur) == '6000':
        entry.delete(0, END)
        entry.insert(INSERT,'Last Number Sir!')
    else:
        entry.delete(0,END)
        entry.insert(INSERT,listbox.get(cur))

listbox.bind('<<ListboxSelect>>',CurSelect)
scr = Scrollbar(listbox,command=listbox.yview)
scr.place(relx=.991,rely=.5,anchor=E,height=208)
listbox['yscrollcommand'] = scr.set

f3 = Frame(frame,width=120,height=90,relief=GROOVE,borderwidth=3)
label2 = Label(frame,text="Channels")
label2.place(relx=.33,rely=.001)
ivar = IntVar()
for i,j,k,l in [("Mono",.1,.13,1),("Stereo",.1,.40,2)]:
    Radiobutton(f3,text=i,variable=ivar,value=l).place(relx=j,rely=k)
    ivar.set(2)
f3.place(relx=.3,rely=.03)

f4 = Frame(frame,width=120,height=90,relief=SUNKEN,borderwidth=1,bd=2)
label3 = Label(frame,text="Resolution")
label3.place(relx=.68,rely=.001)
v = IntVar()
for o,j,k,l in [("8-bit",.1,.13,1),("16-bit",.1,.40,2),("32-bit(float)",.1,.68,3)]:
    Radiobutton(f4,text=o,variable=v,value=l).place(relx=j,rely=k)
    v.set(2)
f4.place(relx=.65,rely=.03)

def do_something():
    add_to_list = var.get()
    entry.delete(0,END)
    listbox.insert(END,add_to_list)

for _,x,y in [("OK",.8,.6),("Cancel",.8,.73),("Help",.8,.87)]:
    if _ == "Cancel":
        Button(root, text=_, width=7, relief=RAISED, bd=3,command=lambda:listbox.delete(END,END)).place(relx=x, rely=y)
    elif _ == "OK":
        Button(root, text=_, width=7, relief=RAISED, bd=3,command=do_something).place(relx=x, rely=y)
    else:
        Button(root, text=_, width=7, relief=RAISED, bd=3,command=quit).place(relx=x, rely=y)

frame.pack()
root.mainloop()
"""
"""
stem = Tk()
cars = ['BMW','Toyota','Honda','AUDI','ACURA']
mvar = StringVar()
mvar.set(mvar[0])
OptionMenu(stem,mvar,*cars).pack(fill=BOTH,expand=True)
stem.mainloop()
"""
"""
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from os import listdir, path

root = Tk()
root.title('PlaneWindow')
style = ttk.Style()
style.configure('TProgressbar',troughcolor='red',background='light green')
style.theme_use('classic')
plane_window = PanedWindow(root,width=500,height=250,
                           handlepad=2,handlesize=8,
                           bd=2,sashpad=0,orient=VERTICAL,
                           sashrelief=SUNKEN,sashwidth=0,
                           showhandle=True)
frame = Frame(plane_window,bg='blue',height=125)
frame_2 = Frame(plane_window,bg='red')
frame_3 = Frame(plane_window,bg='green')

def toggle():
    # bvar_get = bvar.get()
    # if bvar_get:
    #     msg.insert(END,'Check one, two\n')
    #     bvar.set(True)
    # else:
    #     msg.insert(END,'Check Three Four\n')
    #     bvar.set(False)
    scalevar_get = scalevar.get()
    msg.insert(END,scalevar_get)

spinbox_get = StringVar()
scalevar = IntVar()
bvar = BooleanVar()
comvar = StringVar()
provar = IntVar()
#Entry Widget Validation
validate_entry = ttk.Entry(frame,validate='',validatecommand=)
validate_entry.pack()
#_______________________________________
spinbox = Spinbox(frame,from_=0,to=10,increment=1,activebackground='red',buttonuprelief=FLAT,format='%5.2f',textvariable=spinbox_get)
spinbox.pack(pady=10)
but=ttk.Button(frame_2,text='Click',command=toggle)
but.pack()
scale = ttk.Scale(frame, from_=0.0, to=10.0, length=500, orient=HORIZONTAL, variable=scalevar, value=0.0)
scale.pack(padx=5)
checkbutton = ttk.Checkbutton(frame_2,text='Click And See',variable=bvar)
checkbutton.pack()
msg = Text(frame_3)
msg.pack()

sizegrip = ttk.Sizegrip(frame_3)
sizegrip.pack(padx=5,pady=5,fill=BOTH,expand=True)
# but.configure(command=lambda:msg.insert(END, '\n'+spinbox_get.get()))
combobox = ttk.Combobox(frame,values=('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'),textvariable=comvar,
                        postcommand=lambda: msg.insert(END,'\n'+comvar.get()))
combobox.pack(pady=5)
progressbar = ttk.Progressbar(frame_2,length=500,mode='determinate',variable=provar,style='TProgressbar')
progressbar.start(50)
progressbar.step()
# progressbar.stop()
progressbar.pack(pady=5,padx=5)


openimg = listdir('use')
img = []
for i in range(len(openimg)):
    imgfile = Image.open(openimg[i])
    img.append(ImageTk.PhotoImage(imgfile))

label = ttk.Label(root,image=(img[1],'selected', img[2],('!disabled', 'alternate'), img[3]))
label.pack()

plane_window.add(frame)
plane_window.add(frame_2)
plane_window.add(frame_3)
plane_window.pack(fill=BOTH,expand=True)
root.mainloop()
"""
from tkinter import *
from tkinter import ttk

class TreeView:
    def __init__(self):
        self.window = Tk()
        self.window.title('Treeview Widget')
        self.build_treeview()
        self.tv.bind('<Control-a>', self.select_all)  #Select every item on the tree widget
        self.window.mainloop() #NOTE: Make sure .mainloop() comes last on this function

    def build_treeview(self):
        # FRAME WIDGET CREATED
        self.frame = Frame(self.window)
        self.frame.pack(anchor = W)

        # LABELFRAME WIDGET
        self.labelframe = ttk.Labelframe(self.frame, text='Personal Details', padding=10, borderwidth=2, relief=SUNKEN)
        self.labelframe.pack(expand=True, fill=X, pady=5, padx=5)
        self.frame_button = ttk.Frame(self.labelframe)
        self.frame_button.pack(side=BOTTOM)
        self.frame_tree = ttk.Frame(self.window)
        self.frame_tree.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)

        # LABEL AND ENTRY WIDGET RUNNING SIDE BY SIDE EACH OTHER
        self.entry_idx = [None] * 4  # Entry Widget
        self.entry_var = [None] * 4  # String Variable
        self.entry = []
        label_item = ('Name:','Email:','Password:','Comments:')
        for i in range(len(label_item)):
            self.entry_var[i] = StringVar()
            frame_label_entry = ttk.Frame(self.labelframe)
            frame_label_entry.pack(anchor=W, fill=BOTH)
            label = ttk.Label(frame_label_entry, text=label_item[i])
            label.pack(side=LEFT, padx=5, pady=5, anchor=W)
            self.entry_idx[i] = ttk.Entry(frame_label_entry, textvariable=self.entry_var[i])
            self.entry_idx[i].pack(side=RIGHT, pady=5, anchor=E)
            use = self.entry.append(self.entry_var[i].get())
        self.entry_idx[2].configure(show='*')

        # ScrollBar Widget
        scrollbar = ttk.Scrollbar(self.frame_tree)
        scrollbar.pack(side=RIGHT, fill=BOTH, expand=False)

        # Style Configuration
        style = ttk.Style(self.window)
        style.theme_use('xpnative')
        layout = style.layout('Treeview')
        style.configure('That.Treeview', borderwidth=0)
        style.configure('This.Treeview', borderwidth=0)
        style.configure('TButton', foreground='#ff0000', background='#0000ff')
        style.map('TButton',
                  foreground = [('pressed', '#000000'), ('active',  '#ffffff')],
                  background = [('pressed', '#ffffff'), ('active',  '#000000')],
                  highlightcolor = [('focus','#00ff00'), ('!focus', '#ff0000')],
                  relief = [('pressed', 'sunken'), ('!pressed', 'ridge')],
                  borderwidth = [('pressed', 20), ('!pressed', 20)]
                  )

        # TREEVIEW WIDGET on the LHS -------------------------
        self.tvt = ttk.Treeview(self.frame_tree, style='This.Treeview', selectmode=BROWSE, show='tree')
        self.tvt.pack(side=LEFT, fill=BOTH, expand=False)
        self.quick_items = ('Desktop', 'Downloads', 'Documents', 'Pictures', 'Music', 'Videos')
        self.tvt.insert('', END, 'item1', text='Quick access')
        self.tvt.item('item1', open=True)
        self.picture = []
        for i in range(len(self.quick_items)):
            self.pic = PhotoImage(file=f'C:\\Users\\Vicolas\\Pictures\\TreeIcon\\{self.quick_items[i]}.png').subsample(2, 2)
            self.picture.append(self.pic)
            self.tvt.insert('item1', END, text=f' {self.quick_items[i]}', image=self.picture[i])

        # TREEVIEW WIDGET on the RHS --------------------------------------
        self.tv = ttk.Treeview(self.frame_tree, columns=('Email', 'Password', 'Comments'), style='That.Treeview', yscrollcommand=scrollbar.set, takefocus=True)
        scrollbar.configure(command=self.tv.yview)
        heading = ['Names','Email','Password','Comments']
        for idx,name in enumerate(heading):
            self.tv.heading(f'#{idx}', text=name, anchor=W)
        # tv.tag_configure('color', foreground='#0000ff')
        self.tv.pack(side=LEFT, expand=True, fill=BOTH, anchor=W)

        # INSERT BUTTON WIDGET CREATED
        button = ttk.Button(self.frame_button, text='insert', style='TButton', command=self.insert_items)
        button.pack(side=LEFT, pady=5, padx=5, fill=BOTH, expand=True)
        button_2 = ttk.Button(self.frame_button, text='clear all', style='TButton',command=self.clear_all)
        button_2.pack(side=LEFT, pady=5, padx=5, fill=BOTH, expand=True)

    # Inserting text into the Treeview Widget
        self.img = PhotoImage(file='Information.png')
    def insert_items(self,evt=None):
        self.tv.insert('', END, text=f' {self.entry_var[0].get()}',
                      values=(self.entry_var[1].get(),self.entry_var[2].get(),self.entry_var[3].get()),
                      image = self.img,
                      tags='color')

    def clear_all(self):
            # itemez = tv.get_children()
            # for child in itemez:
            #     tv.delete(child) #Clear All items in the Treeview Widget
            # itemz = tv.item(tv.selection())['values'][1]
            # print(itemz)
            for k in range(len(self.entry_var)): #Loop through every entry widget variable and delete every thing
                self.entry_var[k].set('')

    def select_all(self, evt=None):
        selected = self.tv.item(self.tv.selection())
        print(selected)

if __name__ == "__main__":
    TreeView()

"""
from tkinter import *
from tkinter import ttk
from time import sleep
from tkinter.messagebox import showinfo

root = Tk()
root.title('Progress Bar')

def percentage_calculator(a,b):
    result = (a/b) * 100
    return result

def run_action():
    log = open('log.txt', 'a')
    try:
        for i in range(1,21):
            unit = int(percentage_calculator(i, 20))
            sleep(1)
            if i < 10: #Give a small space once the number is less than ten
                log.write(f'{i}    Done\n')
            else:
                log.write(f'{i}  Done\n')
            label['text'] = f'{unit}%'
            progress['value'] = unit
            progress.update()
            label_2['text'] = f'Working on {i}'
        showinfo('Info','Progress Complete!')
        root.quit()
    except Exception as e:
        showinfo('Info',f'Error {e}')
    log.close()

button = ttk.Button(root, text='Start Downloading', command=run_action)
button.grid(row = 0, column = 0, pady=5)

label = ttk.Label(root, text='')
label.grid(row = 1, column = 0)

progress = ttk.Progressbar(root, mode='determinate', length=500)
progress.grid(row = 2, column = 0,  sticky = W, pady = 5, padx = 5)

frame = Frame(root)
frame.grid(row = 3, column = 0, columnspan =  2, ipadx = 20,  pady = 5, padx = 5, sticky = E+W+S+N)

label_2 = ttk.Label(frame, text='Click the button above to start downloading', relief = SUNKEN)
label_2.grid()

if __name__ == '__main__':
    root.mainloop()
"""