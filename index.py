from tkinter import *

def add_task():
    task = entry.get()
    if task:
        listbox.insert(END, task)
        entry.delete(0, END)

def delete_task():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        pass

# Create the main window
window = Tk()
window.title("To-Do List")

# Create a Listbox to display tasks
listbox = Listbox(window, width=50)
listbox.pack(pady=10)

# Create a Scrollbar for the Listbox
scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill=Y)

# Connect the Listbox to the Scrollbar
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Create an Entry for new tasks
entry = Entry(window, font=("Arial", 12))
entry.pack(pady=10)

# Create buttons to add and delete tasks
add_button = Button(window, text="Add Task", command=add_task)
add_button.pack(pady=5)
delete_button = Button(window, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# Start the main event loop
window.mainloop()