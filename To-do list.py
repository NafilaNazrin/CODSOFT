from tkinter import*

root = Tk()
root.title("To-Do List")
root.geometry("500x500")

item_list=[]

def add_btn():
    global task_list
    task = item_entry.get()
    item_entry.delete(0, END)

    if task:
        
        item_list.append(task)
        listbox.insert(END, task)

def del_btn():
    global task_list
    task = listbox.curselection()[0]
    listbox.delete(task)

def edit_btn():
    task = listbox.curselection()[0]
    if task:
        new_task = item_entry.get()
        if new_task:
            listbox.delete(task)
            listbox.insert(task, new_task)
            item_entry.delete(0, END)

#header
header = Label(root, text = "To-Do List",font=("century", 20),
               fg='yellow', bg='black', width=30, height=2)
header.pack()

frame = Frame(root, width=400, height=100)
frame.pack()

item_disp = StringVar()

#task entry
item_entry= Entry(frame, width=32, font=('century',20), bd=1)
item_entry.pack()

#add button
addbutton = Button(frame,command=add_btn, text="ADD TASK", font=("century", 15),
                   width=10, bg='blue', fg='white')
addbutton.place(x=350, y=0)

#list
frame1 = Frame(root, width= 700, height=100)
frame1.pack()

listbox = Listbox(frame1, font=("century", 25), width= 30,
                    height=8, fg='cyan',bg='black', cursor="hand2",
                    selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx= 2)

#scroll bar
scrollbar=Scrollbar(frame1,)
scrollbar.pack(side = RIGHT, fill = BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command= listbox.yview)

#edit button
editbutton=Button(root, command= edit_btn, text="EDIT TASK", font=("century", 15),
                   width=18, bg='blue', fg='white' )
editbutton.place(x=10,y=440 )

#delete button
deletebtn = Button(root,command=del_btn,  text="DELETE TASK", font=("century", 15),
                   width=18, bg='blue', fg='white')
deletebtn.place(x=250,y=440)



root.mainloop()


    
