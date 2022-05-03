import tkinter.messagebox
from tkinter import *
from pysondb import db


# add to to-do
def add_todo(root):
    frame = Frame(root)
    # show possible day tasks
    label = Label(frame, text="Enter todo", font=('Aerial 12'))
    label.pack()
    label1 = Label(frame, text="Task", font=('Aerial 12'))
    label1.pack()
    ent1 = Entry(frame)
    ent1.pack()
    label2 = Label(frame, text="Quadrant", font=('Aerial 12'))
    label2.pack()
    ent2 = Entry(frame)
    ent2.pack()
    enter = Button(frame, text='Enter', width=25, command=lambda:save_task(ent1.get(), ent2.get()))
    enter.pack()
    frame.pack()


# fetch to-do
def update_todo(root):
    frame = Frame(root)
    frame.grid()

    # show possible tasks with ids
    # enter id, updated task, updated quad
    Label(frame, text="Enter id, task, and quadrant", font=('Aerial 12')).grid(row=1)
    ent1 = Entry(frame)
    ent1.grid(column=0, row=2)
    ent2 = Entry(frame)
    ent2.grid(column=1, row=2)
    ent3 = Entry(frame)
    ent3.grid(column=2, row=2)
    Button(frame, text='Enter', width=25, command=lambda: update_task(ent1.get(), ent2.get(), ent3.get())).grid(row=3)

    # add suggestions here
    Label(frame, text="List of todos", font=('Aerial 12')).grid(row=4)
    # fetch to-do list
    todo = db.getDb("../ToDo/todo.json")
    todo_list = todo.getAll()
    for i, item in enumerate(todo_list):
        w = Text(frame, width=15, height=2)
        w.grid(row=(i+5))
        value = f'{item["task"]} {item["quad"]} {item["id"]}'
        w.insert(END, value)


# create day workplan
def day_plan(root):
    frame = Frame(root)
    frame.grid()
    # show possible day tasks
    Label(frame, text="Enter 4 todos", font=('Aerial 12')).grid(row=1)
    Label(frame, text="1. High Work and High quality: ", font=('Aerial 12')).grid(row=2, column=0)
    ent1 = Entry(frame)
    ent1.grid(row=2, column =1)
    Label(frame, text="2. High Work and Low quality", font=('Aerial 12')).grid(row=3, column=0)
    ent2 = Entry(frame)
    ent2.grid(row=3, column=1)
    Label(frame, text="3. Low Work and Low quality", font=('Aerial 12')).grid(row=4, column=0)
    ent3 = Entry(frame)
    ent3.grid(row=4, column=1)
    Label(frame, text="4. Low Work and High quality", font=('Aerial 12')).grid(row=5, column=0)
    ent4 = Entry(frame)
    ent4.grid(row=5, column=1)
    Button(frame, text='Enter', width=25, command=lambda: save_plan(ent1.get(), ent2.get(), ent3.get(), ent4.get())).grid(row=6)

    # add suggestions here
    Label(frame, text="List of to-dos", font=('Aerial 12')).grid(column=2, row=2)
    # fetch to-do list
    todo = db.getDb("ToDo/todo.json")
    todo_list = todo.getAll()
    for i, item in enumerate(todo_list):
        w = Text(frame, width=20, height=4)
        w.grid(column=2, row=(i+3))
        w.insert(END, item["task"]+" "+item["quad"])


def update_task(id, task, quad):
    update = {"task": task, "quad": quad}
    todo = db.getDb("ToDo/todo.json")
    todo.updateById(pk=id, new_data=update)
    tkinter.messagebox.showinfo("Update Task",  "SUCCESS")


def save_task(task, quad):
    todo = db.getDb("ToDo/todo.json")
    todo.add({"task": task, "quad": quad})
    tkinter.messagebox.showinfo("Save Task",  "SUCCESS")


def save_plan(ent1, ent2, ent3, ent4):
    # save to db
    todo = db.getDb("ToDo/daily.json")
    new_items = [
        {"task": ent1, "quad": 1},
        {"task": ent2, "quad": 2},
        {"task": ent3, "quad": 3},
        {"task": ent4, "quad": 4},
    ]

    todo.addMany(new_items)
    tkinter.messagebox.showinfo("Save Plan",  "SUCCESS")


def delete_plan():
    todo = db.getDb("ToDo/daily.json")
    todo.deleteAll()


if __name__ == "__main__":
    root = Tk()
    day_plan(root)
    root.mainloop()
