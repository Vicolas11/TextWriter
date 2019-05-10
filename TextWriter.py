from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import colorchooser
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
from os import path, listdir
import Pmw

class Notepad:
    def __init__(self):
        self.master = Tk()
        self.master.title("Untitled - Notepad")
        self.icon = PhotoImage(file='editor_icon.png')
        self.master.wm_iconphoto(self.master,self.icon)# ICON PHOTO
        self.master.geometry('600x450+361+150')
        self.master.bind('<Control-o>',self.open_file) # OPENING A DOCUMENT | Ctrl + o
        self.master.bind('<Control-O>', self.open_file) # OPENING A DOCUMENT | Ctrl + Shift + o
        self.master.protocol('WM_DELETE_WINDOW',self.quited) # PROMPT THE CLOSE WINDOW DIALOG WHEN YOU CLICK ON THE CLOSE BUTTON
        self.build_Notepad()
        self.master.mainloop()
        # print(self.master.winfo_screenheight(),self.master.winfo_screenwidth())

    def build_Notepad(self):
        # BUILD FILE MENU
        self.frame = ttk.Frame(self.master)
        self.frame.pack()
        self.menu = Menu(self.frame,takefocus=1,activeborderwidth=14)
        self.master.configure(menu=self.menu)
        self.filemenu = [None] * 6
        for f in range(1,6):
            self.filemenu[f] = Menu(self.menu,tearoff=False)

        imagesdir = listdir('use')  #FILE MENU ICON IMAGES
        self.iconimages = []
        for img in range(len(imagesdir)):
            self.openimage = Image.open(imagesdir[img])
            f, fext = path.splitext(imagesdir[img])
            # print(f)
            self.iconimages.append(ImageTk.PhotoImage(self.openimage))

        # FILE MENU
        self.menu.add_cascade(label='File',menu=self.filemenu[1],underline=3)
        for i,k,l in (('New','Ctrl+N','33'),('Open...','Ctrl+O','28'),('Save','Ctrl+S','33'),
                  ('Save As...','','20'),('Page Setup...','','20'),('Print...','Ctrl+P','30'),('Exit','','20')):
            if i == 'New':
                self.filemenu[1].add_command(label='{} \t{:>{}}'.format(i, k, l), command= self.new_file,image=self.iconimages[8],compound=LEFT)
            elif i == 'Open...':
                self.filemenu[1].add_command(label='{} \t{:>{}}'.format(i, k, l),command =self.open_file,image=self.iconimages[9],compound=LEFT)
            elif i == 'Save':
                self.filemenu[1].add_command(label='{} \t{:>{}}'.format(i, k, l), command=self.save_file,image=self.iconimages[12],compound=LEFT)
            elif i == 'Save As...':
                self.filemenu[1].add_command(label='{} \t{:>{}}'.format(i,k,l),command=self.saveas_file)
                self.filemenu[1].add_separator('')
            elif i == 'Print...':
                self.filemenu[1].add_command(label='{} \t{:>{}}'.format(i, k, l), command=self.save_file,image=self.iconimages[11], compound=LEFT)
            elif i == 'Exit':
                self.filemenu[1].add_separator('')
                self.filemenu[1].add_command(label='{} \t{:>{}}'.format(i,k,l),command=self.quited,image=self.iconimages[7],compound=LEFT)
            else:
                self.filemenu[1].add_command(label='{} \t{:>{}}'.format(i,k,l))

        # EDIT MENU
        self.menu.add_cascade(label='Edit', menu=self.filemenu[2])
        for i, k, l in (('Undo', 'Ctrl+Z', '33'),('Cut...','Ctrl+X', '33'),('Copy','Ctrl+C','33'),
                        ('Paste', 'Ctrl+V', '33'),('Delete','Del','34'),('Find...','Ctrl+F', '32'),
                        ('Find Next', 'F3', '30'),('Replace...','Ctrl+H','26'),('Go to...','Ctrl+G','30'),
                        ('Select All','Ctrl+A','27'),('Time/Date','F5','28')):
            if i == 'Undo':
                self.filemenu[2].add_command(label='{} \t{:>{}}'.format(i, k, l),command=lambda: self.text.event_generate('<<Undo>>'),image=self.iconimages[14],compound=LEFT)
                self.filemenu[2].add_separator('')
            elif i == 'Cut...':
                self.filemenu[2].add_command(label='{} \t{:>{}}'.format(i, k, l),command=lambda: self.text.event_generate('<<Cut>>'),image=self.iconimages[2],compound=LEFT)
            elif i == 'Copy':
                self.filemenu[2].add_command(label='{} \t{:>{}}'.format(i, k, l),command=lambda: self.text.event_generate('<<Copy>>'),image=self.iconimages[1],compound=LEFT)
            elif i == 'Paste':
                self.filemenu[2].add_command(label='{} \t{:>{}}'.format(i, k, l), command=lambda: self.text.event_generate('<<Paste>>'),image=self.iconimages[10],compound=LEFT)
            elif i == 'Delete':
                self.filemenu[2].add_command(label='{} \t{:>{}}'.format(i, k, l),command=lambda: self.text.event_generate('<<Delete>>'),image=self.iconimages[3],compound=LEFT)
                self.filemenu[2].add_separator('')
            elif i == 'Find...':
                self.filemenu[2].add_command(label='{} \t{:>{}}'.format(i, k, l),image=self.iconimages[4],compound=LEFT)
            elif i == 'Go to...':
                self.filemenu[2].add_command(label='{} \t{:>{}}'.format(i, k, l))
                self.filemenu[2].add_separator('')
            elif i == 'Select All':
                self.filemenu[2].add_command(label='{} \t{:>{}}'.format(i, k, l),command=self.select_all_text)
                self.filemenu[2].add_separator('')
            else:
                self.filemenu[2].add_command(label='{} \t{:>{}}'.format(i, k, l))

        # FORMAT MENU
        self.menu.add_cascade(label='Format',menu=self.filemenu[3])
        for i in ('Word Wrap','Font...'):
            self.wrap = BooleanVar()
            if i == 'Word Wrap':
                    self.filemenu[3].add_checkbutton(label=i,offvalue=0,variable=self.wrap,command=self.wrap_text)
            else:
                self.filemenu[3].add_command(label=i,command=self.configure_notepad,image=self.iconimages[13],compound=LEFT)

        # VIEW MENU
        self.menu.add_cascade(label='View',menu=self.filemenu[4])
        self.filemenu[4].add_command(label='Status Bar',state=DISABLED)

        # HELP MENU
        self.menu.add_cascade(label='Help',menu=self.filemenu[5])
        self.filemenu[5].add_command(label='View Help',command=None,image=self.iconimages[5],compound=LEFT)
        self.filemenu[5].add_separator('')
        self.filemenu[5].add_command(label='About Notepad',command=self.about_notepad,image=self.iconimages[6],compound=LEFT)
        # Search MenuBar
        self.frame_1 = Frame(self.master)
        self.stylish = ttk.Style(self.frame_1)
        self.stylish.configure('Search.TEntry',relief=SUNKEN,bd=4,fg='blue')
        self.frame_1.pack(expand=False,fill=Y)
        self.find_label = ttk.Label(self.frame_1,text='Find: ')
        self.find_label.pack(side=LEFT,anchor=CENTER)
        self.pattern = StringVar()
        self.find_entry = ttk.Entry(self.frame_1, style='Search.TEntry', textvariable=self.pattern)
        self.find_entry.bind('<Return>',self.search_for_text) # Hightlights the matched text in the text area
        self.find_entry.pack(side=LEFT,anchor=CENTER,pady=5)

        #BUILD TEXT AREA AND SCROLLED BAR
        self.frame_2 = ttk.Frame(self.master)
        self.frame_2.pack(fill=BOTH, expand=True, padx=5)
        self.scrollbar = ttk.Scrollbar(self.frame_2)
        self.scrollbar.pack(side=RIGHT, fill=Y, expand=False)
        self.scrollbar_2 = ttk.Scrollbar(self.master, orient=HORIZONTAL)
        self.text = Text(self.frame_2,yscrollcommand=self.scrollbar.set,xscrollcommand=self.scrollbar_2.set,wrap=NONE,undo=True)
        self.text.pack(side=LEFT,fill=BOTH,expand=True)
        self.text.bind('<Button-3>',self.popup_menu)
        self.scrollbar.configure(command=self.text.yview)
        self.text.tag_configure('sel', background='red', lmargin1=50)
        self.text.insert(INSERT,'Select every text now','sel')
        self.text.tag_add('sel','1.0', END)
        self.text.bind('<Button-1>', self.deselect_text) #Deselect text after clicking on the text area

        #STATUSBAR - Found Below the Programme
        self.text.bind('<Key>', self.count_text)
        self.status_frame = ttk.Frame(self.master)
        self.counting_char = len(self.text.get(1.0, END))
        self.status_label = ttk.Label(self.status_frame, text=f': {self.counting_char} characters', padding=5)
        self.status_label.pack(anchor=W)
        self.status_frame.pack(fill=BOTH, expand=False)

    def count_text(self, evt=None): #This Function returns the number of each character in the TextArea!
        self.status_label['text'] = f':: {len(self.text.get(1.0, END)) - 1} characters'

    def popup_menu(self,event): # right-clicked menu option
        try:
            self.popup_menu = Menu(self.master, tearoff=False)
            for i,k in [('Undo','separator'),('Cut',''),('Copy',''),('Paste',''),('Delete','separator'),('Select All','separator'),('Right to left Reading order','cb'),
                        ('Show Unicode control characters','cb'),('Insert Unicode control characters','separator/insert'),
                        ('Open IME',''),('Reconversion','')]:
                if  i == 'Undo':
                    self.popup_menu.add_command(label=i, command=lambda: self.text.event_generate('<<Undo>>'))
                    self.popup_menu.add_separator('')
                elif i == 'Cut':
                    self.popup_menu.add_command(label=i,state=ACTIVE,command=self.cut_text)
                elif i == 'Copy':
                    self.popup_menu.add_command(label=i, command=self.copy_text)
                elif i == 'Paste':
                    self.popup_menu.add_command(label=i,command=self.paste_text)
                elif i == 'Delete':
                    self.popup_menu.add_command(label=i,state=ACTIVE,command=lambda evt=None: self.text.delete(SEL_FIRST,SEL_LAST))
                elif i == 'Select All':
                    self.popup_menu.add_separator('')
                    self.popup_menu.add_command(label=i, command=self.select_all_text)
                    self.popup_menu.add_separator('')
                elif k == 'separator':
                    self.popup_menu.add_command(label=i)
                    self.popup_menu.add_separator('')
                elif k ==  'separator/insert':
                    self.submenu = Menu(self.popup_menu,tearoff=False)
                    self.popup_menu.add_cascade(label=i,menu=self.submenu)
                    self.popup_menu.add_separator('')
                    submenuitems = dict(LRM='Left-to-right mark',RLM='Right-to-left mark',ZWJ='Zero width joiner',ZWNJ='Zero width non-joiner',LRE='Right-to-Center',
                                        RLE='Start of right-to-left embedding',LRO='Start of left-to-right override',RLO='Start of right-to-left override',
                                        PDF='Pop directional formatting',NADS='National digit shapes substitution',NODS='Nominal (European) digit shapes')
                    for _ in submenuitems:
                        self.submenu.add_command(label=_,accelerator=submenuitems[_])
                elif k == 'cb':
                    self.popup_menu.add_checkbutton(label=i)
                else:
                    self.popup_menu.add_command(label=i)
            self.popup_menu.tk_popup(event.x_root,event.y_root)
        finally:
            self.popup_menu.grab_release()

    def copy_text(self,evt=None):
        self.text_get = self.text.selection_get()
        self.text.clipboard_clear()
        self.text.clipboard_append(self.text_get)

    def cut_text(self,evt=None):
        self.copy_text()
        self.text.delete(SEL_FIRST,SEL_LAST)

    def paste_text(self,evt=None):
        self.text.insert(INSERT,self.text.clipboard_get())

    def select_all_text(self,event=None):
        self.text.tag_configure('sel',background='#8A2BE2')
        # self.text.tag_add(SEL, '1.0-1c linestart', 'end-1c')
        for self.line in self.text.get('1.0','end-1c').splitlines():
                self.line = self.text
                # self.line.tag_add(SEL,'insert linestart','insert lineend')
                self.line.tag_add(SEL, '1.0', 'end-1c')
                self.line.mark_set(INSERT,'1.0')
                self.line.see(INSERT)
        return 'break'

    def search_for_text(self,evt=None):
        self.text.tag_remove('highlight','1.0',END)
        self.pattern_get = self.pattern.get()  #Gets the text from the entry widget once enter is pressed and then  highlight
        if self.pattern_get:
            idx = 1.0
            while True:
                idx = self.text.search(self.pattern_get, idx, stopindex=END, nocase=True)
                if not idx: break
                lastidx =   '%s+%dc' % (idx,len(self.pattern_get))
                self.text.tag_add('highlight', idx, lastidx)
                idx = lastidx
                self.text.see(idx)
            self.text.tag_config('highlight', background='#000000', foreground='#ffffff')

    def deselect_text(self,evt): #After searching a text once you click on the text area, the found highlighted text gets deselected
        self.text.tag_remove('highlight',1.0,END)

    def new_file(self,evt=None):
        global savefile
        self.master.title('Untitled - Notepad')
        savefile = None
        self.text.delete(1.0,END)

    current_file_open = 'no_file'
    def open_file(self,evt=None): #There's an issue with these function please remind me to fix it. Thanks!
            self.openfile = filedialog.askopenfilename(filetypes=(('Text Files','*.txt'),('All Files','*.*')))
            if self.openfile != None:
                self.text.delete(1.0, END)
                self.insert_file = open(self.openfile,'r').read()
                self.text.insert(END, self.insert_file)
                self.current_file_open = self.openfile.name
                self.master.title(path.basename(self.openfile))
            else:
                print('Caught You')

    def saveas_file(self,evt=None):
        self.file = filedialog.asksaveasfile(mode='w',defaultextension='.txt',initialfile='Untitled',
                                        filetypes=(('Text File (*.txt)','.txt'),('All Files','*.*')))
        if self.file == None:
            return
        text_to_save = self.text.get(1.0,END)
        self.file.write(text_to_save)
        self.file.close()
        self.current_file_open = self.file.name
        self.master.title(self.file.name[25::])
        # self.master.title(path.basename(self.file))

    def save_file(self):
        if self.current_file_open == 'no_file':
            self.saveas_file()
        else:
            file = open(self.current_file_open,'w+')
            file.write(self.text.get(1.0,END))
            file.close()

    def wrap_text(self):
        self.use  = self.wrap.get()
        if self.use:
            self.text.config(wrap=NONE)
            self.scrollbar_2.pack(fill=X, expand=NO)
            self.scrollbar_2.configure(command=self.text.xview)
            self.wrap.set(False)
        else:
            self.text.config(wrap=WORD)
            self.scrollbar_2.pack_forget()
            self.wrap.set(True)

    def configure_notepad(self): # FONTS AND COLOR SETTINGS
        self.fontname = ('Arial','Times','Candara','Broadway','Elephant','Forte','Gabriola','Impact','Jokerman')
        self.fontstyle = ('bold','normal','italic','roman',"underline","noline","overstrike","unstrike")
        self.toplvl = Toplevel(self.master,relief=GROOVE,background='red')
        self.toplvl.attributes('-toolwindow',1)
        self.toplvl.title('Fonts and Colors')
        self.toplvl.geometry('+470+200')

        self.frame_top = ttk.Frame(self.toplvl,relief=RAISED,borderwidth=2)
        self.frame_top.pack(fill=BOTH,expand=True)

        self.groupfont = Pmw.Group(self.frame_top,tag_text='Fonts Format')
        self.groupfont.pack(fill=BOTH,expand=True,padx=5,pady=8)
        self.fontname = Pmw.ComboBox(self.groupfont.interior(),labelpos=NW,label_text='Fonts:',listbox_height=5,
                                           selectioncommand=self.effect_fontfamily,dropdown=False,
                                           scrolledlist_items=sorted(self.fontname))
        self.fontname.pack(side=LEFT,padx=5,pady=5)
        self.fontstyle= Pmw.ComboBox(self.groupfont.interior(), labelpos=NW, label_text='Font style:', listbox_height=5,
                                     selectioncommand=self.effect_fontstyle, dropdown=False,
                                     scrolledlist_items=self.fontstyle)
        self.fontstyle.pack(side=LEFT,padx=5,pady=5)
        self.fontsize = Pmw.ComboBox(self.groupfont.interior(), labelpos=NW, label_text='Fontsize:', listbox_height=5,
                                     selectioncommand=self.effect_fontsize, dropdown=False,listbox_width=1,
                                     scrolledlist_items=list(i for i in range(8,73)))
        self.fontsize.pack(side=LEFT,padx=5,pady=5)
        # COLOR CONFIGURATION
        self.groupcolor = LabelFrame(self.frame_top,text='Color Format')
        self.groupcolor.pack(fill=Y,expand=True,padx=3,pady=5,side=LEFT)
        self.colornames = ('black','white','red','green','blue','orange','pink','purple','light blue','grey')
        self.color = Pmw.ComboBox(self.groupcolor, labelpos=NW, label_text='Color:', listbox_height=5,
                                     selectioncommand=self.effect_color, dropdown=False,label_takefocus=True,
                                     scrolledlist_items=self.colornames)
        self.color.pack(anchor=W,padx=5, pady=5)
        #CLICK THIS LABEL TO GET MORE COLOR TO CHOOSE FROM
        self.more_colors = Label(self.groupcolor,text='Choose More Color',font='times 9 underline',foreground='royalblue',cursor='mouse')
        self.more_colors.bind("<Button-1>",self.choose_color)
        self.more_colors.pack(anchor=W)
        self.canvas = Canvas(self.groupcolor)
        # SETTINGS PREVIEW THAT SHOWS HOW YOUR FONTS AND COLORS WILL APPEAR IN THE TEXT WIDGET
        self.labelframe = LabelFrame(self.frame_top,text='Sample Preview',labelanchor=NW,width=250,height=50)
        self.labelframe.pack_propagate(0)
        self.labelframe.pack(side=LEFT,fill=BOTH,expand=True,pady=5,padx=5)

        self.lbl = ttk.Label(self.labelframe,text='Vicolas',justify=CENTER)
        self.lbl.pack(fill=Y,expand=True)
        # THE EXIT AND EXECUTE BUTTON BELLOW
        self.frame_bottom = ttk.Frame(self.toplvl,relief=RAISED,borderwidth=2)
        self.frame_bottom.pack(fill=BOTH,expand=True)
        self.btn = ttk.Button(self.frame_bottom,text='OK',command=self.toplvl.destroy)
        self.btn.pack(side=RIGHT,padx=5,pady=3)

    def effect_fontfamily(self,evt):
        self.font = font.Font(family=evt)
        self.lbl.configure(font = self.font)
        self.text.config(font=f'{evt} 14 bold')

    def effect_fontstyle(self,evt):
        try:
            for i,k,l,m in (("bold","italic","underline","overstrike"),("normal","roman","noline","unstrike")):
                if evt == i:
                    self.font.configure(weight=evt)
                    self.lbl.configure(font=self.font)
                elif evt == k:
                    self.font.configure(slant=evt)
                    self.lbl.configure(font=self.font)
                elif evt == l:
                    if l == "underline":
                        self.font.configure(underline=1)
                        self.lbl.configure(font=self.font)
                    else:
                        self.font.configure(underline=0)
                        self.lbl.configure(font=self.font)
                elif evt == m:
                    if m == "overstrike":
                        self.font.configure(overstrike=1)
                        self.lbl.configure(font=self.font)
                    else:
                        self.font.configure(overstrike=0)
                        self.lbl.configure(font=self.font)
        except AttributeError as e:
            print(e)
        except Exception as e:
            print(e)

    def effect_fontsize(self,evt):
        try:
            self.font['size'] = evt # THIS METHOD IS ALSO THE SAME
            self.lbl.configure(font=self.font)
            # self.font = font.Font(size=ev)
            # self.font.configure(size=evt) WITH THIS
        except AttributeError as e:
            print(e)
        except Exception as e:
            print(e)

    def effect_color(self,evt):
        self.lbl.configure(foreground=evt)

    def effect_textarea_color(self,evt):
        self.text.configure(background=evt)

    def choose_color(self,evt):
        self.chclr = colorchooser.askcolor(parent=self.toplvl,color='black',title='More Colors')
        self.lbl["foreground"] = self.chclr[1]

    def about_notepad(self):
        # TOP LEVEL MENU
        self.toplvl = Toplevel(self.master)
        self.toplvl.geometry('350x300+510+230')
        self.toplvl.title('About Notepad')
        self.toplvl.resizable(0,0)
        #WINDOW LOGO
        self.photo = PhotoImage(file='Win 10 Logo.gif')
        self.label = ttk.Label(self.toplvl,image=self.photo,compound=RIGHT)
        self.label.pack(padx=0,pady=0,fill=X,expand=True)
        # STYLING
        self.s = ttk.Style(self.toplvl)
        self.s.configure('This.TSeparator')
        # SEPARATOR
        self.separator = ttk.Separator(self.toplvl, style='This.TSeparator')
        self.separator.pack(fill=X, expand=True,padx=5)
        self.msg = Message(self.toplvl, width=300, justify=CENTER,
                           text='Microsoft Windows\nVersion 1607\n(c) 2016 Microsoft Corporation. All Right reserved.\n'
                                'The Windows 10 Pro Operating system and its user interface are protected by trademark'
                                'and other pending or existing intelletual property rights in the United States and'
                                'other countries/regions.')
        self.msg.pack(fill=BOTH, expand=YES, padx=8, pady=5)
        self.button = ttk.Button(self.toplvl, text='OK', command=self.toplvl.destroy)
        self.button.pack(padx=5, pady=5, anchor=E)

    def quited(self):
        try:
            self.root = Tk()
            self.root.eval(f'tk::PlaceWindow {self.master.winfo_toplevel()} center')
            self.root.withdraw()
            if messagebox.askokcancel('Confirm Exit','Do you want to exit', icon = 'question'):
                self.master.quit()
            else:
                self.root.destroy()
            self.root.iconify()
            self.root.bell()
            # self.toplvl = Toplevel(self.master)
            # self.toplvl.withdraw()
            # self.toplvl.title('Close Window')
            # self.toplvl.geometry('250x80+550+300')
            # self.label = ttk.Label(self.toplvl,text='Do you really want to quit?',anchor=CENTER)
            # self.label.pack(fill=BOTH,expand=True)
            # self.btn = ttk.Button(self.toplvl,text='Nope',command=self.toplvl.destroy)
            # self.btn.pack(side=LEFT,anchor=CENTER,padx=5,pady=5)
            # self.bttn = ttk.Button(self.toplvl,text='Yeah',command=quit)
            # self.bttn.pack(side=RIGHT,padx=5,pady=5)
        except  TclError as e:
            print(e)

if __name__== "__main__":
    Notepad()