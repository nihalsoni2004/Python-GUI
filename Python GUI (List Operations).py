from tkinter import *
from tkinter import simpledialog, messagebox

def insert_at_position():
   
    position = simpledialog.askinteger("Insert at Specific Position","Enter the position of element")
    if(position>0):
        ele = simpledialog.askinteger("Insert at Specific Position", "Enter the Item to Insert at the Given position:")
        numbers.insert(position-1, ele)
    else:
        messagebox.showinfo("Error","Invalid Position")    
   
def remove_from_list():
    position = simpledialog.askinteger("Remove from List", "Enter the  Position to Delete an Item:")
    if(position>0 and position<=len(numbers)):
        numbers.pop(position-1)
    else:
        p="Inavild position"
        messagebox.showinfo("List ",p)
     
       
def add_to_list():
    ele = simpledialog.askinteger("Add to List", "Enter an Element to add:")
    numbers.append(ele)
     
def display_list():
    messagebox.showinfo("List Content", format(numbers))
    print (len(numbers)) 

def exit_program():
    root.destroy()

numbers = []

root =Tk()
root.title("List Manipulation Program")
root.minsize(width=400,height=300)
root.maxsize(width=800,height=600)

button_add = Button(root, text="Add to List", font="Calibri 12 bold",bg="dodgerblue4",fg = "white",command=add_to_list)
button_add.pack()

button_insert = Button(root, text="Insert at Specific Position", font="Calibri 12 bold",bg="dodgerblue4",fg = "white", command=insert_at_position)
button_insert.pack()

button_remove = Button(root, text="Remove from List", font="Calibri 12 bold",bg="dodgerblue4",fg = "white", command=remove_from_list)
button_remove.pack()

button_display = Button(root, text="Display the List", font="Calibri 12 bold",bg="dodgerblue4",fg = "white", command=display_list)
button_display.pack()

button_exit = Button(root, text="Exit", font="Calibri 12 bold",bg="dodgerblue4",fg = "white", command=exit_program)
button_exit.pack()


root.mainloop()
