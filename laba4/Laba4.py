from tkinter import*
from random import randrange as rnd, choice
import time
import math


colors = ['red','orange','yellow','green','blue']


class Game:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('800x600')
        self.canv = Canvas(self.root, bg = 'white')
        self.canv.pack(fill = BOTH, expand = 1)
        self.ball = None
        self.score = 0


    def click(self, event):
        if self.ball.click(event) == 1:
            self.score += self.ball.click(event)
            print('Вы набрали ', self.score)
        else:
            print('Вы промахнулись')



    def new_ball(self):
        self.canv.delete(ALL)
        self.ball = Ball(rnd(100, 700), rnd(100, 500), choice(colors), rnd(30, 50))
        self.canv.create_oval(self.ball.cordx - self.ball.radius, self.ball.cordy - self.ball.radius,
                         self.ball.cordx + self.ball.radius, self.ball.cordy + self.ball.radius,
                         fill = self.ball.color, width = 0)
        self.root.after(1000, self.new_ball)
        return self.ball


class Object(Game):
    def __init__(self, cordx, cordy, color):
        self.cordx = cordx
        self.cordy = cordy
        self.color = color


class Ball(Object):
    def __init__(self, cordx, cordy, color, radius):
        Object.__init__(self, cordx, cordy, color)
        self.radius = radius


    def click(self, event):
        #print(self.cordx, self.cordy, self.radius)
        #print(event.x, event.y)
        if ((self.cordx - event.x) ** 2) + ((self.cordy - event.y) ** 2) <= self.radius ** 2 :
            #print('Попадание')
            return 1
        else:
            return 0



game = Game()
game.new_ball()
game.canv.bind('<Button-1>', game.click)
mainloop()
