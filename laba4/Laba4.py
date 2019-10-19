from tkinter import*
from random import randrange as rnd, choice
import time
import math


colors = ['#212638','#072776','#ba5a1a','#fdb766','#4b6700']

N = 10

x_pole = 1360 # cm
y_pole = 780 # cm

min_velocity = 30 # cm/s
max_velocity = 60 # cm/s

max_radius = 70 # cm
min_radius = 50 # cm

density =  0.00093 # kg/cm^3

global g
g = 100 # cm/s^2
dt = 10 # ms

class Game:
    def __init__(self):
        self.root = Tk()
        self.root.geometry(str(x_pole) + 'x' + str(y_pole))
        self.canv = Canvas(self.root, bg = '#e9e9c6')
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
        self.ball = Ball()
        return self.ball


class Object(Game):
    def __init__(self):
        self.image = None
        self.velocity_x = (rnd(min_velocity, max_velocity) - (min_velocity + max_velocity) / 2) / 4
        self.velocity_y = (rnd(min_velocity, max_velocity) - (min_velocity + max_velocity) / 2) / 4
        self.color = choice(colors)


class Ball(Object):
    def __init__(self):
        Object.__init__(self)
        self.radius = rnd(min_radius, max_radius)
        self.cord_x = rnd(max_radius, x_pole - max_radius)
        self.cord_y = rnd(max_radius, y_pole - max_radius)
        for i in balls:
            while (i.radius + self.radius) ** 2 >= (i.cord_x - self.cord_x) ** 2 + (i.cord_y - self.cord_y) ** 2:
                self.cord_x = rnd(max_radius, x_pole - max_radius)
                self.cord_y = rnd(max_radius, y_pole - max_radius)
        self.vector = None
        self.mass = math.ceil(4.2 * (self.radius ** 3) * density)


    def click(self, event):
        #print(self.cord_x, self.cord_y, self.radius)
        #print(event.x, event.y)
        if ((self.cord_x - event.x) ** 2) + ((self.cord_y - event.y) ** 2) <= self.radius ** 2 :
            #print('Попадание')
            return 1
        else:
            return 0


    def movement(self):
        global g
        game.canv.delete(self.image)
        game.canv.delete(self.vector)
        self.image = game.canv.create_oval(self.cord_x - self.radius, self.cord_y - self.radius,
                        self.cord_x + self.radius, self.cord_y + self.radius, fill = self.color,
                        width = 0)
        self.vector = game.canv.create_line(self.cord_x, self.cord_y, self.cord_x + 20 * self.velocity_x,
                                            self.cord_y + 20 * self.velocity_y, arrow = LAST, width = 5)
        self.cord_x += self.velocity_x
        self.cord_y += self.velocity_y
        self.collision()
        game.root.after(dt, self.movement)


    def collision(self):
        if self.cord_x + self.radius >= x_pole or self.cord_x - self.radius <= 0:
            self.velocity_x = -self.velocity_x
        elif self.cord_y + self.radius >= y_pole or self.cord_y - self.radius <= 0:
            self.velocity_y = -self.velocity_y
        for i in balls:
            if self != i and ((i.radius + self.radius) ** 2 >= (i.cord_x - self.cord_x) ** 2 + (i.cord_y - self.cord_y) ** 2):
                self.velocity_x = -self.velocity_x
                self.velocity_y = -self.velocity_y

game = Game()

balls = []

for i in range(N):
    balls.append(game.new_ball())


for i in balls:
    i.movement()
    print(i.mass, 'kg')


game.canv.bind('<Button-1>', game.click)
mainloop()
