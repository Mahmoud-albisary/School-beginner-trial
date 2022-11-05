from tkinter import *
import programparents
from functools import partial
window = Tk()

window.wm_title("MY BOOK")
row = []
row1 = []
for items in programparents.rows:
    items = list(items)
    row.append(items)

labels =[]

for i in range(len(row)):
    labels.append(Label(window, text = row[i]))
    labels[i].grid(row = i + 1, column = 0)

for items in programparents.rows1:
    items = list(items)
    row1.append(items)

labels1 =[]

for i in range(len(row1)):
    labels1.append(Label(window, text = row1[i], width = 15))
    labels1[i].grid(row = 0, column = i + 1)

multiple = len(row1)
boxes = []
inboxes = []
numbers = len(row)*len(row1)
i = 0
for z in range(numbers):
    var = IntVar()
    inboxes.append(var)

def check(i, x):
    z = x
    for items in range(len(boxes)):
        if i != items and int(i/multiple) == int(items / multiple):
            inboxes[items].set(0)
    while i + 1 > len(row1) :
        i = i - len(row1)
    for item in range(len(labels1)):
        if (i + 1) / (item + 1) == 1:
            x = labels1[item].cget("text")
            print(x)
    while z + 1 > len(row) :
        z = z - len(row)
    for ite in range(len(row)):
        if (z + 1) / (ite + 1) == 1:
            print(ite)
            y = labels[ite].cget("text")
            print(y)
print(len(row))
print(len(labels))
for x in range(len(row)):
    for y in range(len(row1)):
        boxes.append(Checkbutton(window, variable=inboxes[i], command = lambda i = i, x = x:check(i, x)).grid(row = x + 1, column = y + 1))
        i = i + 1
i = i - 1



window.mainloop()
