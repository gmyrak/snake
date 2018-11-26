from tkinter import *
import random
from time import time

SIZE_PIC = 30
X_SIZE, Y_SIZE = 20, 20

w, h = X_SIZE*SIZE_PIC, Y_SIZE*SIZE_PIC

root = Tk()
root.resizable(0, 0)
cnv = Canvas(root, width=w, height=h, bg='white')
cnv.pack()

panel = Frame(root, height= 30)
panel.pack(fill=X)

but_ng = Button(panel, text='New Game', command=lambda : Game())
but_ng.pack(side=LEFT)

inf = Label(panel, text='')
inf.pack(side=LEFT)


def sqr(x, y, color, tag = 'unknown'):
    return cnv.create_rectangle(x*SIZE_PIC, y*SIZE_PIC, x*SIZE_PIC+SIZE_PIC, y*SIZE_PIC+SIZE_PIC,
                                fill=color, tag=tag)


def circl(x, y, color, tag = 'unknown'):
    return cnv.create_oval(x*SIZE_PIC, y*SIZE_PIC, x*SIZE_PIC+SIZE_PIC, y*SIZE_PIC+SIZE_PIC,
                                fill=color, tag=tag)

class Snake():
        #self.step()

    def _add(self, x, y):
        self.list_items.insert(0, (x, y))
        self.dict_items[(x, y)] = sqr(x, y, 'green', 'snake')

    def _del(self):
        x, y = self.list_items.pop()
        p = self.dict_items.pop((x, y))
        cnv.delete(p)

    def __init__(self):
        self.length = 6
        self.dir = 'Right'
        x, y = 0, Y_SIZE//2
        self.list_items = []
        self.dict_items = {}
        self.ok = True
        self.eating = False
        for i in range(self.length):
            self._add(x, y)
            x += 1
        #root.bind('<KeyPress>', self.key_press)

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
        if 0 <= x < X_SIZE and 0 <= y < Y_SIZE and not (x, y) in self.dict_items:
            self._add(x, y)
            if not self.eating:
                self._del()
            else:
                self.eating = False
        else:
            self.ok = False


class Apple():
    def __init__(self, x, y):
        self.pos = (x, y)
        self.p = circl(x, y, 'red', 'apple')


class Game():
    def __init__(self):
        cnv.delete('all')
        cnv['bg'] = 'sky blue'
        self.timeout = 200
        self.snake = Snake()
        self.apple = self.get_apple()
        inf['text'] = self.snake.length
        self.start_time = time()
        self.go = True
        root.bind('<KeyPress>', self.key_press)

        self.run()

    def key_press(self, k):
        if k.keysym in {'Up', 'Down', 'Left', 'Right'}:
            self.snake.dir = k.keysym

    def get_apple(self):
        while True:
            x1 = random.randint(1, X_SIZE-2)
            y1 = random.randint(1, Y_SIZE-2)
            if not (x1, y1) in self.snake.dict_items:
                break
        return Apple(x1, y1)

    def run(self):
        #self.timeout -= int((time() - self.start_time)/10)
        self.snake.step()
        inf['text'] = len(self.snake.list_items)
        if self.snake.ok:
            if self.snake.list_items[0] == self.apple.pos:
                self.snake.eating = True
                cnv.delete(self.apple.p)
                self.apple = self.get_apple()
            cnv.after(self.timeout, self.run)
        else:
            inf['text'] = 'Game Over!'
            cnv['bg'] = 'orange2'



Game()

root.mainloop()