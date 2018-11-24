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


#def key_press(k):



class Snake():

    def key_press(self, k):
        self.dir = k.keysym
        print(self.dir)
        self.step()

    def add(self, x, y):
        self.list_items.append((x, y))
        self.dict_items[(x, y)] = sqr(x, y)

    def _del(self):
        x, y = self.list_items.pop()
        p = self.dict_items.pop((x, y))
        cnv.delete(p)


    def __init__(self):
        L0 = 4
        x, y = 10, 9
        self.list_items = []
        self.dict_items = {}
        self.dir = 'Right'
        for i in range(L0):
            self.add(x, y)
            x -= 1
        root.bind('<KeyPress>', self.key_press)

    def step(self):
        x, y = self.list_items[0]
        if self.dir == 'Up':
            y -= 1
        elif self.dir == 'Down':
            y += 1
        elif self.dir == 'Left':
            x -= 1
        elif self.dir == 'Right':
            x += 1

        self.add(x, y)
        self._del()

s = Snake()


root.mainloop()