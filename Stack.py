from tkinter import *
from tkinter import ttk

class Stack:
    def __init__(self):
        self.root = Tk()
        self.root.title('Add And Remove')
        self.build_stack()
        self.root.mainloop()

    def build_stack(self):
        #Entries
        self.frame_top =  ttk.Frame(self.root)
        self.lbl = ttk.Label(self.frame_top, text='Cities: ')
        self.entry_var = StringVar()
        self.entry = ttk.Entry(self.frame_top, textvariable=self.entry_var)
        self.frame_top.pack(pady=5)
        self.lbl.pack(side=LEFT, fill=BOTH, expand=True)
        self.entry.pack(side=RIGHT, fill=BOTH, expand=True)

        #Buttons
        self.frame_2 = ttk.Frame(self.root)
        self.frame_2.pack()
        self.btnames = ['push','pop','exit']
        self.btn = [None] * 3
        for i in range(len(self.btnames)):
            self.btn[i] = ttk.Button(self.frame_2, text=self.btnames[i], padding=5)
            self.btn[i].pack(side=LEFT, fill=BOTH, expand=True)
        self.btn[0].config(command=self.insert)
        self.btn[1].config(command=self.remove)
        self.btn[2].config(command=quit)

        #Array
        self.frame_3 = ttk.Frame(self.root)
        self.frame_3.pack(side=BOTTOM)
        self.cities = ['London','Rome','Berlin','Paris']
        self.count = 1
        self.entre = [None] * 10
        for k in range(len(self.cities)):
            self.entre[k] = ttk.Entry(self.root)
            self.entre[k].insert(END, self.cities[k])
            self.entre[k].pack(fill=BOTH, expand=False, pady=5, padx=5)

    def insert(self):
        self.count += 1
        self.entre[self.count] = ttk.Entry(self.root)
        self.entre[self.count].pack(fill=BOTH, expand=False, pady=5, padx=5)
        self.entre[self.count].insert(END, self.entry_var.get())
        self.entry.delete(0, END)

    def remove(self):
        self.count -= 1
        self.entre[self.count].pack_forget()

if __name__ == "__main__":
    Stack()

stack = ['London','Berlin','Rome','Paris']
stack.append('Athens')
stack.pop()
stack.append('Madrid')
stack.append('Moscow')
stack.pop()
print(stack)