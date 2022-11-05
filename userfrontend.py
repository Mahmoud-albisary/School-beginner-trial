from tkinter import *
import userinfo


def select(event):
    try:
        global selected
        index = l11.curselection()[0]
        selected = l11.get(index)
        e1.delete(0, END)
        e1.insert(END, selected[1])
        e2.delete(0, END)
        e2.insert(END, selected[2])
    except IndexError:
        e1.delete(0, END)
        e1.insert(END, selected[0])
        e2.delete(0, END)
        e2.insert(END, selected[1])

def views():
    l11.delete(0, END)
    for rows in userinfo.view():
        l11.insert(END, rows)


def searchs():
    l11.delete(0, END)
    for rows in userinfo.search(username.get(), password.get()):
        l11.insert(END, rows)

def inserts():
    l11.delete(0, END)
    userinfo.insert(username.get(), password.get())
    l11.delete(0, END)
    l11.insert(END, (username.get(), password.get()))

def deletes():
    userinfo.delete(selected[0])

def updates():
    userinfo.update(selected[0], e1.get(), e2.get(),)

window = Tk()

window.wm_title("MY BOOK")

l1 = Label(window, text = "username")
l1.grid(row = 0, column = 0)

l2 = Label(window, text = "password")
l2.grid(row = 0, column = 2)

username = StringVar()
e1 = Entry(window, textvariable = username )
e1.grid(row = 0, column = 1)

password = StringVar()
e2 = Entry(window, textvariable = password )
e2.grid(row = 0, column = 3)

l11 = Listbox(window, height = 6, width  = 35)
l11.grid(row = 2, rowspan = 6, column = 0, columnspan = 2)

sb1 = Scrollbar(window)
sb1.grid(row = 2 ,column = 2, rowspan = 6)

l11.configure(yscrollcommand = sb1.set)
sb1.configure(command = l11.yview)
l11.bind('<<ListboxSelect>>', select)

b1 = Button(window, text = 'View all', width = 12, command = views)
b1.grid(row = 2, column = 3)

b2 = Button(window, text = 'Search entry', width = 12, command = searchs)
b2.grid(row = 3, column = 3 )

b3 = Button(window, text = 'Add entry', width = 12, command = inserts )
b3.grid(row = 4, column = 3 )

b4 = Button(window, text = 'Update', width = 12, command = updates)
b4.grid(row = 5, column = 3 )

b5 = Button(window, text = 'Delete', width = 12, command = deletes)
b5.grid(row = 6, column = 3 )

b6 = Button(window, text = 'Close', width = 12, command = window.destroy)
b6.grid(row = 7, column = 3 )

window.mainloop()
