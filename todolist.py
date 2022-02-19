import pickle
from tkinter import *
from tkinter.font import Font
import tkinter.messagebox
from tkinter import filedialog
import pickle


root=Tk()
root.title("Bipaswi_Todo List")
root.geometry("500x500")
root.resizable(False,False)

    #Font
my_font=Font(
    family="Brush Script MT",
    size=30,
    weight="bold",)

    #Created frame
my_frame=Frame(root,)
my_frame.pack(pady=10)

    #Listbox making
my_list= Listbox(my_frame,
                 font=my_font,
                 width=25,
                 height=5,
                 bg="SystemButtonFace",
                 bd=0,
                 fg="#464646",
                 highlightthickness=0,
                 selectbackground="#A6A6A6",
                 activestyle="none")
my_list.pack(side=LEFT,fill=BOTH)

    # Creating ScrollBar
my_scrollbar=Scrollbar(my_frame,)
my_scrollbar.pack(side=RIGHT,fill=BOTH)

    #add scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

    #Creating Entrybox
my_entry=Entry(root,font=("Helvetica",24),width=26,)
my_entry.pack(pady=20)

    #Creating button frame
button_frame=Frame(root)
button_frame.pack(pady=20)

    #FUNCTIONS
def delete_item():
    my_list.delete(ANCHOR)

def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0,END)

def cross_off_item():
    #Cross off Item
    my_list.itemconfig(
        my_list.curselection(),
        fg="#DEDEDE",)

    #Getting rid of selection bar
    my_list.select_clear(0,END)

def uncross_item():
    # Cross off Item
    my_list.itemconfig(
        my_list.curselection(),
        fg="#464646", )

    # Getting rid of selection bar
    my_list.select_clear(0, END)

def delete_crossed_item():
    count=0
    while count < my_list.size():
        if my_list.itemcget(count,"fg")== "#DEDEDE":
            my_list.delete(my_list.index(count))

        else:
            count+=1

    #  At list
def save_list():
   file_name=filedialog.asksaveasfilename()
   initialdir="Desktop",
   title="Save File",
   filetypes=(
       ("Dat Files","*.dat"),
       ("All Files","*.* "))
   if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name=f'{file_name}.dat'

            #Delete crossed off items before saving
        count=0
        while count < my_list.size():
            if my_list.itemcget(count, "fg") == "#DEDEDE":
                my_list.delete(my_list.index(count))

            else:
                count += 1
        #GRABBING ALL FROM LIST
        stuff=my_list.get(0,END)

       #Open the file
        output_file=open(file_name,'wb')
       #Add the stuff to the file
        pickle.dump(stuff,output_file)


def open_list():
   file_name=filedialog.askopenfilename(
       initialdir="Desktop",
       title = "Save File",
       filetypes = (
       ("Dat Files", "*.dat"),
       ("All Files", "*.* "))
   )

   if file_name:
       #Delete currently open list
       my_list.delete(0,END)

       #Open the file
       input_file=open(file_name,'rb')

       #Load data from file
       stuff=pickle.load(input_file)

        #outputing Stuff on screen
       for item in stuff:
          my_list.insert(END, item)

def delete_list():
    my_list.delete(0, END)

    #Create Menu
my_menu=Menu(root)
root.config(menu=my_menu)

    #Add items to Menu
file_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File",menu=file_menu)

    #Add dropdown Items
file_menu.add_command(label="Save List",command=save_list)
file_menu.add_command(label="Open List",command=open_list)
file_menu.add_separator()
file_menu.add_command(label="Clear List",command=delete_list)




    #Adding buttons
delete_button=Button(button_frame,text="Delete ITEM",command=delete_item)
add_button=Button(button_frame,text="Add ITEM",command=add_item)
cross_off_button=Button(button_frame,text="Cross_off ITEM",command=cross_off_item)
uncross_button=Button(button_frame,text="Uncross ITEM",command=uncross_item)
delete_crossed_button=Button(button_frame,text="Delete Crossed",command=delete_crossed_item)

delete_button.grid(row=0,column=0)
add_button.grid(row=0,column=1,padx=20,)
cross_off_button.grid(row=0,column=2)
uncross_button.grid(row=0,column=3,padx=20,)
delete_crossed_button.grid(row=0,column=4)


mainloop()