from tkinter import *
import schooldb


def select(event):
    try:
        global selected
        index = l11.curselection()[0]
        selected = l11.get(index)
        if program.rows.count(selected):
            e1.delete(0, END)
            e1.insert(END, selected[1])
        elif program.rows1.count(selected):
            e2.delete(0, END)
            e2.insert(END, selected[1])
    except IndexError:
        pass

def views():
    l11.delete(0, END)
    for rows in program.view():
        l11.insert(END, rows)
    for rows1 in program.view1():
        l11.insert(END, rows1)

def searchs():
    l11.delete(0, END)
    for rows in program.search(teacher.get()):
        l11.insert(END, rows)

def searchs1():
    l11.delete(0, END)
    for rows1 in program.search1(duration.get()):
        l11.insert(END, rows)

def inserts():
    l11.delete(0, END)
    program.insert(teacher.get())
    l11.delete(0, END)
    l11.insert(END, (teacher.get()))

def inserts1():
    l11.delete(0, END)
    program.insert1(duration.get())
    l11.delete(0, END)
    l11.insert(END, (duration.get()))

def deletes():
    if program.rows.count(selected):
        program.delete(selected[0])

def deletes1():
    if program.rows1.count(selected):
        program.delete1(selected[0])


def updates():
    program.update(selected[0], e1.get())

def updates1():
    program.update1(selected[0], e2.get(),)

window = Tk()

window.wm_title("MY BOOK")

l1 = Label(window, text = "teacher")
l1.grid(row = 0, column = 0)

l2 = Label(window, text = "duration")
l2.grid(row = 0, column = 2)

teacher = StringVar()
e1 = Entry(window, textvariable = teacher )
e1.grid(row = 0, column = 1)

duration = StringVar()
e2 = Entry(window, textvariable = duration )
e2.grid(row = 0, column = 3)

l11 = Listbox(window, height = 10, width  = 35)
l11.grid(row = 3, rowspan = 6, column = 0, columnspan = 2)

sb1 = Scrollbar(window)
sb1.grid(row = 2 ,column = 2, rowspan = 6)

l11.configure(yscrollcommand = sb1.set)
sb1.configure(command = l11.yview)
l11.bind('<<ListboxSelect>>', select)

b1 = Button(window, text = 'View all', width = 12, command = views)
b1.grid(row = 2, column = 3)

b2 = Button(window, text = 'Search entry', width = 12, command = searchs)
b2.grid(row = 1, column = 0 )

b3 = Button(window, text = 'Search entry', width = 12, command = searchs1)
b3.grid(row = 1, column = 2 )

b4 = Button(window, text = 'Add entry', width = 12, command = inserts )
b4.grid(row = 1, column = 1 )

b5 = Button(window, text = 'Add entry', width = 12, command = inserts1 )
b5.grid(row = 1, column = 3 )

b6 = Button(window, text = 'Update', width = 12, command = updates)
b6.grid(row = 2, column = 0)

b7 = Button(window, text = 'Update', width = 12, command = updates1)
b7.grid(row = 2, column = 2 )

b8 = Button(window, text = 'Delete', width = 12, command = deletes)
b8.grid(row = 2, column = 1 )

b9 = Button(window, text = 'Delete', width = 12, command = deletes1)
b9.grid(row = 2, column = 4 )

b10 = Button(window, text = 'Close', width = 12, command = window.destroy)
b10.grid(row = 7, column = 3 )

window.mainloop()
