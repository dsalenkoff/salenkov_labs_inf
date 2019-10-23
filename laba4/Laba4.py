from tkinter import*
from random import randrange as rnd, choice
import time
import math

colors = ['#212638', '#072776', '#ba5a1a', '#fdb766', '#4b6700']

N = 10 # Количество шариков

x_pole = 1080 # cm
y_pole = 720 # cm

min_velocity = 20 # cm/s
max_velocity = 40 # cm/s

max_radius = 40 # cm
min_radius = 30 # cm

density = 0.00093 # kg/cm^3

red = 1.001

global g

g = 10 # cm/s^2
dt = 5 # ms

class Game:
    def __init__(self):
        self.root = Tk()
        self.root.geometry(str(x_pole) + 'x' + str(y_pole))
        self.canv = Canvas(self.root, bg = '#e9e9c6')
        self.canv.pack(fill = BOTH, expand = 1)
        self.ball = None
        self.score = 0
        self.direction = 0


    def click(self, event):
        for i in balls:
            if i.click(event, i) == 1:
                self.score += i.click(event, i)
                balls.append(Ball())
                print('Вы набрали ', self.score)
            else:
                print('Вы промахнулись')


    def change(self, event):
        self.direction += 1
        self.direction = self.direction % 4
        print(self.direction)


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


    def click(self, event, i):
        #print(self.cord_x, self.cord_y, self.radius)
        #print(event.x, event.y)
        if ((i.cord_x - event.x) ** 2) + ((i.cord_y - event.y) ** 2) <= i.radius ** 2:
            print(i.cord_x)
            balls.remove(i)
            return 1
        else:
            return 0


    def movement(self):
        game.canv.delete(self.image)
        game.canv.delete(self.vector)
        self.image = game.canv.create_oval(self.cord_x - self.radius, self.cord_y - self.radius,
                        self.cord_x + self.radius, self.cord_y + self.radius, fill = self.color,
                        width = 0)
        self.vector = game.canv.create_line(self.cord_x, self.cord_y, self.cord_x + 20 * self.velocity_x,
                                            self.cord_y + 20 * self.velocity_y, arrow = LAST, width = 5)
        self.cord_x += self.velocity_x
        self.cord_y += self.velocity_y
        if game.direction == 0:
            self.velocity_x += 0
            self.velocity_y += g * dt / 1000
        elif game.direction == 1:
            self.velocity_x += g * dt / 1000
            self.velocity_y += 0
        elif game.direction == 2:
            self.velocity_x += 0
            self.velocity_y -= g * dt / 1000
        elif game.direction == 3:
            self.velocity_x -= g * dt / 1000
            self.velocity_y += 0
        self.collision()
        game.root.after(dt, self.movement)


    def collision(self):
        if self.cord_x + self.radius >= x_pole:
            self.velocity_x = -red*self.velocity_x
            self.velocity_y = red * self.velocity_y
        elif self.cord_x + self.radius >= x_pole + 2:
            self.cord_x -= self.radius - 2
        elif self.cord_x - self.radius <= 0:
            self.velocity_x = -red * self.velocity_x
            self.velocity_y = red * self.velocity_y
        elif self.cord_x - self.radius <= -2:
            self.cord_x += self.radius + 2
        elif self.cord_y + self.radius >= y_pole:
            self.velocity_y = -red*self.velocity_y
            self.velocity_x = red * self.velocity_x
        elif self.cord_y + self.radius >= y_pole + 2:
            self.cord_y -= self.radius - 2
        elif self.cord_y - self.radius <= 0:
            self.velocity_y = -red * self.velocity_y
            self.velocity_x = red * self.velocity_x
        elif self.cord_y - self.radius <= - 2:
            self.cord_y += self.radius + 2

        for i in balls:
            #if self != i and (i.radius + self.radius) ** 2 + 10 >= (i.cord_x - self.cord_x) ** 2 + (i.cord_y - self.cord_y) ** 2:
             #self.cord_x -= self.radius * ((((i.cord_x - self.cord_x) ** 2)/ ((i.radius + self.radius) ** 2)) ** 0.5)
              #self.cord_y -= self.radius * ((((i.cord_y - self.cord_y) ** 2) / ((i.radius + self.radius) ** 2)) ** 0.5)
            if self != i and (i.radius + self.radius) ** 2 >= (i.cord_x - self.cord_x) ** 2 + (i.cord_y - self.cord_y) ** 2:
                self.velocity_x = -red * self.velocity_x
                self.velocity_y = -red * self.velocity_y
                #self.velocity_x = (self.mass * self.velocity_x - i.mass * (self.velocity_x - 2 * i.velocity_x)) / (self.mass + i.mass)
                #self.velocity_y = (self.mass * self.velocity_y - i.mass * (self.velocity_y - 2 * i.velocity_y)) / (self.mass + i.mass)

game = Game()

balls = []

for i in range(N):
    balls.append(game.new_ball())

for i in balls:
    i.movement()
    print(i.mass, 'kg')

game.canv.bind('<Button-1>', game.change)
#game.canv.bind('<Button-1>', game.click)
mainloop()
