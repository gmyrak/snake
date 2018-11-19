from tkinter import *

SIZE_PIC = 20
X_SIZE, Y_SIZE = 30, 20

w, h = X_SIZE*SIZE_PIC, Y_SIZE*SIZE_PIC

root = Tk()
root.resizable(0, 0)
cnv = Canvas(root, width=w, height=h, bg='white')
cnv.pack()


def sqr(x, y):
    return cnv.create_rectangle(x*SIZE_PIC, y*SIZE_PIC, x*SIZE_PIC+SIZE_PIC, y*SIZE_PIC+SIZE_PIC,
                                fill='green', tag='snake')


class Snake():
    def __init__(self):
        L0 = 4
        x, y = 10, 9
        self.items = []
        self.dir = 'E'
        for i in range(L0):
            self.items.append((x, y, sqr(x, y)))
            x -= 1

    def step(self):
        head = 1





s = Snake()


root.mainloop()