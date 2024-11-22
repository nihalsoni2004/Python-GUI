from tkinter import *

def G_ratio():
    fib_seq=[0,1]
    n=int(entry.get())
   
    for i in range(2, n):
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
    gratio=[]
    for i in range(2,len(fib_seq)):
        gratio.append(fib_seq[i] / fib_seq[i-1])   
    result_label.config(text=format(gratio))
    
   
def fiblist():
     fib_seq=[0,1]
     n=int(entry.get())
     for i in range(2, n):
       fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
   
     label2.config(text=format(fib_seq))    

window = Tk()
window.title("Golden Ratio Calculator")
window.minsize(width=300,height=250)

label1 = Label(window, text="Enter the number of elements:",bg="grey",font=" Calibri 16 bold")
label1.place(x=10,y=5)
entry=Entry(window,font=18)
entry.place(x=20,y=40)

button_fiblist=Button(window,text="Get Fibonacci list",bg="grey",font=" Calibri 16 bold",command=fiblist)
button_fiblist.place(x=20,y=70)
label2=Label(window,text="Fiblist :",bg="yellow",fg="blue",font=14)
label2.place(x=20,y=120)
ratio_button = Button(window,text="Calculate Golden ratio",bg="grey",font=" Calibri 16 bold",command=G_ratio)
ratio_button.place(x=20,y=160)

result_label=Label(window,text="Golden Ratio:",bg="yellow",fg="blue",font=16)
result_label.place(x=20,y=210)
window.mainloop()
