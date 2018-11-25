from tkinter import *
import random

SIZE_PIC = 20
X_SIZE, Y_SIZE = 30, 20

w, h = X_SIZE*SIZE_PIC, Y_SIZE*SIZE_PIC

root = Tk()
root.resizable(0, 0)
cnv = Canvas(root, width=w, height=h, bg='white')
cnv.pack()


def sqr(x, y, color, tag = 'unknown'):
    return cnv.create_rectangle(x*SIZE_PIC, y*SIZE_PIC, x*SIZE_PIC+SIZE_PIC, y*SIZE_PIC+SIZE_PIC,
                                fill=color, tag=tag)


class Snake():
    def key_press(self, k):
        if k.keysym in {'Up', 'Down', 'Left', 'Right'}:
            self.dir = k.keysym
        self.step()

    def _add(self, x, y):
        self.list_items.insert(0, (x, y))
        self.dict_items[(x, y)] = sqr(x, y, 'green', 'snake')

    def _del(self):
        x, y = self.list_items.pop()
        p = self.dict_items.pop((x, y))
        cnv.delete(p)

    def __init__(self):
        L0 = 6
        x, y = 10, 9
        self.list_items = []
        self.dict_items = {}
        self.dir = 'Right'
        self.ok = True
        for i in range(L0):
            self._add(x, y)
            x += 1
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
        if 0 <= x < X_SIZE and 0 <= y < Y_SIZE and not (x, y) in self.dict_items:
            self._add(x, y)
            self._del()
        else:
            self.ok = False


class Apple():
    def __init__(self, x, y):
        self.pos = (x, y)
        self.p = sqr(x, y, 'red', 'apple')


class Game():
    def __init__(self):
        self.snake = Snake()
        self.put_apple()

    def put_apple(self):
        while True:
            x1 = random.randint(0, X_SIZE-1)
            y1 = random.randint(0, Y_SIZE-1)
            if not (x1, y1) in self.snake.dict_items:
                break
        self.apple = Apple(x1, y1)

Game()

root.mainloop()