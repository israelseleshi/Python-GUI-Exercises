"""

Exercise 1: To-Do List Application

Create a simple to-do list application using Tkinter with the following features:

An entry box to enter tasks.
A button to add tasks to a list.
Display the list of tasks using labels.
Checkboxes next to each task to mark them as completed.

"""

# ==============================================
# Solution to Exercise 1: To-Do List Application 
# ==============================================

from tkinter import *

def add_task():

  task = task_entrybox.get()
  tasks.append(task)

  numberofTasks = task_listbox.size()
  task_listbox.insert(numberofTasks, task)
  numberofTasks += 1



window = Tk()
window.title("To-Do List Application")
window.geometry("600x600")

# Task Entry Frame
entry_frame = Frame(window)
entry_frame.pack(pady = 20, padx = 20)

# Enter Task Label
enter_task_label = Label(entry_frame, text = "Enter Task: ", font = ("Consolas", 16), fg = 'black')
enter_task_label.pack(side = LEFT)

# Add Task Button
add_task_button = Button(entry_frame, 
                         text = "Add Task", 
                         font = ("Consolas", 12),
                         bg = 'black',  
                         fg = 'white', 
                         activebackground='black', 
                         activeforeground='white',
                         command= add_task)
add_task_button.pack(side = RIGHT)

# Enter Task Entry Box
task_entrybox = Entry(entry_frame, font = ("Consolas", 16), fg = 'blue')
task_entrybox.pack(side = RIGHT, padx = 15)

# ListBox Frame
listbox_frame = Frame(window)
listbox_frame.pack()

# Tasks ListBox
tasks = []
task_listbox = Listbox(listbox_frame, 
                       height = 600, 
                       width = 500, 
                       bg= 'light blue',
                       font = ("Consolas", 16), fg = 'black'
                      )
task_listbox.pack(side = RIGHT)

# CheckBoxes
x = IntVar()
checkbox = Checkbutton(listbox_frame,
                       variable = x,
                       onvalue=1,
                       offvalue=0
                      )
checkbox.pack(side = LEFT)

# Mark_As_Completed Button

mark_as_completed_button = Button(window, text = 'Mark As Completed', font = ("Consolas", 16), fg = 'black')
mark_as_completed_button.pack(pady = 20)

window.mainloop()



