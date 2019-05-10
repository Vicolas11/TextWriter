from tkinter import *
from tkinter import ttk
from math import *

root = Tk()
root.title('Quadratic')
entry = [None] * 3
entry_var = [None] * 3
frame_label = ttk.Frame(root)
frame_label.pack(side=LEFT)
frame_entry = ttk.Frame(root)
frame_entry.pack(side=LEFT)
label_items = ('a','b','c')

def quadratic(a,b,c):
    num1 = pow(b,2)
    num2 = 4 * a * c
    num3 = 2 * a
    num4 = num1 - num2
    num5 = num4**(0.5)
    num6 = (-b + num5)/num3
    num7 = (-b - num5)/num3
    txt.delete(1.0, END)
    txt.insert(END, f'x is {num6} or {num7}')
    return a, b, c
# a = float(input("enter a number: "))
# b = float(input("enter another number: "))
# c = float(input("enter another number: "))
def answer(evt=None):
    a = float(entry_var[0].get())
    b = float(entry_var[1].get())
    c = float(entry_var[2].get())
    quadratic(a,b,c)

for i in range(len(label_items)):
    entry_var[i] = StringVar()
    label = ttk.Label(frame_label, text=label_items[i])
    label.pack(padx=5, pady=6)
    entry[i] = ttk.Entry(frame_entry, width=12, textvariable=entry_var[i])
    entry[i].pack(pady=6, padx=6)
btn = ttk.Button(root, text='Answer', command=answer)
btn.pack(pady=5)
txt = Text(root, height=5, width=20)
txt.pack(pady=5)
if __name__ == '__main__':
    root.mainloop()



btn.configure(command=answer)