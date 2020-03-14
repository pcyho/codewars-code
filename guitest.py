import time
from random import *
from tkinter import *
from tkinter.scrolledtext import ScrolledText

from PIL import Image, ImageTk

file = "E:\\file\\IMG_2473.JPG"
getanswer = []
quechioice = 0

questionlist = [
    "1,",
    "2,",
    "3,",
    "4,",
    "5,",
]
###########################################################################
answerlist = [
    "A",
    "A",
    "A",
    "A",
    "A",
]


root = Tk()
root.wm_state('zoomed')  # 默认窗口最大化


def answerA():
    getanswer.append("A")
    nextquestion()


def answerB():
    getanswer.append("A")
    nextquestion()


def answerC():
    getanswer.append("A")
    nextquestion()


def answerD():
    getanswer.append("A")
    nextquestion()


def checkanswer():
    right = 0
    for a, b in answerlist, getanswer:
        if a == b:
            right += 1
    test.delete('1.0', END)
    test.insert(INSERT, "you get " + right + " right")


def nextquestion():
    quechioice = quechioice + 1
    if quechioice > 10:
        checkanswer()
    else:
        test.delete('1.0', END)
        test.insert(INSERT, questionlist[quechioice])


def start():
    b1.pack_forget()

    test = ScrolledText(root, width=30, height=20, font=(20))
    test.pack(side=BOTTOM, expand=True, fill=X)

    bd = Button(text='A', command=answerA)
    bd.place(x=570, y=610, width=140, height=50)
    bd = Button(text='B', command=answerB)
    bd.place(x=730, y=610, width=140, height=50)
    bd = Button(text='C', command=answerC)
    bd.place(x=890, y=610, width=140, height=50)
    bd = Button(text='D', command=answerD)
    bd.place(x=1050, y=610, width=140, height=50)


load = Image.open(file)
render = ImageTk.PhotoImage(load)
img = Label(image=render, compound=CENTER)
img.image = render
img.place(x=200, y=25)

b1 = Button(text='here to start a qustion game', command=start, fg='green')
b1.place(x=700, y=400, width=200, height=60)

root.title('guitest')
mainloop()
