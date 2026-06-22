import tkinter as toolkit
from tkinter import messagebox
window=toolkit.Tk()

def list_boxitems():
    item=text_input.get()
    if item !="":
        list_box.insert(toolkit.END,f"{item} ---- Pending ")
        text_input.delete(0,toolkit.END)
        text_input.focus()

def mark_buttonuse():
    if not list_box.curselection():
        messagebox.showinfo("Info","Select a task first!")
        return
    index=list_box.curselection()[0]
    item2=list_box.get(index)
    new_item=item2.replace("Pending","Completed")
    list_box.delete(index)
    list_box.insert(index,new_item)

def delete_buttonuse():
    if list_box.size() >0:
       list_box.delete(0,toolkit.END)
       messagebox.showinfo(" Info "," Deleted Succesfully! ")
    else:
        messagebox.showinfo(" Info "," No Task Exists ")

def delete_itembuttonuse():
    if not list_box.curselection():
        messagebox.showinfo("Info","Select Task First")
        return
    index = list_box.curselection()[0]
    list_box.delete(index)

window.title("ToDoList-Application")
window.geometry("500x600")
text_label=toolkit.Label(window,text=" Basic ToDoList Application ",font=("Georgia",16))
text_label.pack(padx=20,pady=5)
text_input=toolkit.Entry(window,width=40)
text_input.pack(padx=20,pady=5)
add_button=toolkit.Button(window,text="  Add Task  ",command=list_boxitems)
add_button.pack(padx=20,pady=5)
list_box=toolkit.Listbox(window,width=60,height=15,font=("Arial",12),activestyle="none")
list_box.pack(pady=15,padx=5)

button_frame=toolkit.Frame(window)
button_frame.pack()

mark_button=toolkit.Button(button_frame,text=" Mark Complete ",command=mark_buttonuse)
mark_button.grid(row=0,column=0,padx=15)

delete_button=toolkit.Button(button_frame,text=" Delete All ",command=delete_buttonuse)
delete_button.grid(row=0,column=1,padx=15)

delete_itembutton=toolkit.Button(button_frame,text=" Delete ",command=delete_itembuttonuse)
delete_itembutton.grid(row=0,column=2,padx=15)

exit_button=toolkit.Button(button_frame,text=" Exit ",command=window.destroy)
exit_button.grid(row=0,column=3,padx=15)



window.mainloop()
