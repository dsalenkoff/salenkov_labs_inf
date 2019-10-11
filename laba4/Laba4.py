from tkinter import*
from random import randrange as rnd, choice
import time
import math


colors = ['red','orange','yellow','green','blue']


class Game:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('800x600')
        self.canv = Canvas(self.root, bg='white')
        self.canv.pack(fill=BOTH, expand=1)
        self.ball = None


    def click(self, event):
        self.ball.click(event)


    def new_ball(self):
        self.canv.delete(ALL)
        self.ball = Ball(rnd(100, 700), rnd(100, 500), choice(colors), rnd(30, 40))
        self.canv.create_oval(self.ball.cordx - self.ball.radius, self.ball.cordy - self.ball.radius,
                         self.ball.cordx + self.ball.radius, self.ball.cordy + self.ball.radius,
                         fill=self.ball.color, width=0)
        self.root.after(2000, self.new_ball)
        return self.ball


class ObjectClick(Game):
    def __init__(self, cordx, cordy, color):
        self.cordx = cordx
        self.cordy = cordy
        self.color = color


class Ball(ObjectClick):
    def __init__(self, cordx, cordy, color, radius):
        self.cordx = cordx
        self.cordy = cordy
        self.color = color
        self.radius = radius


    def click(self, event):
        print(self.cordy, self.cordx)
        print(event.x, event.y)
        if ((self.cordx - event.x) ** 2) + ((self.cordy - event.x) ** 2) < self.radius ** 2 :
            print('Попадание')



game = Game()
game.new_ball()
game.canv.bind('<Button-1>', game.click)
mainloop()
