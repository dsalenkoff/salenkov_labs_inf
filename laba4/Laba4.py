from tkinter import *
from random import randrange as rnd, choice
import time
import math

colors = ['#212638', '#072776', '#ba5a1a', '#fdb766', '#4b6700']

N = 10

x_pole = 1080
y_pole = 720

min_velocity = 5
max_velocity = 10

min_radius = 20
max_radius = 40

red = 1

g = 30
dt = 5


class Game:
    def __init__(self):
        self.root = Tk()
        self.root.geometry(str(x_pole) + 'x' + str(y_pole))
        self.canvas = Canvas(self.root, bg='#e9e9c6')
        self.canvas.pack(fill=BOTH, expand=1)
        self.ball = None
        self.score = 0
        self.direction = 0

    def change(self, event):
        self.direction += 1
        self.direction = self.direction % 4

    def new_ball(self):
        self.ball = Ball()
        return self.ball


class Object:
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
        for k in balls:
            while (k.radius + self.radius) ** 2 >= (k.cord_x - self.cord_x) ** 2 + (k.cord_y - self.cord_y) ** 2:
                self.cord_x = rnd(max_radius, x_pole - max_radius)
                self.cord_y = rnd(max_radius, y_pole - max_radius)
        self.vector = None

    def movement(self):
        game.canvas.delete(self.image)
        game.canvas.delete(self.vector)
        self.image = game.canvas.create_oval(self.cord_x - self.radius, self.cord_y - self.radius,
                                             self.cord_x + self.radius, self.cord_y + self.radius, fill=self.color,
                                             width=0)
        self.vector = game.canvas.create_line(self.cord_x, self.cord_y, self.cord_x + 15 * self.velocity_x,
                                              self.cord_y + 15 * self.velocity_y, arrow=LAST, width=5)
        # self.collision()
        self.cord_x += self.velocity_x
        self.cord_y += self.velocity_y
        if game.direction == 0:
            self.velocity_x += 0
            self.velocity_y += g / 1000
        elif game.direction == 1:
            self.velocity_x += g / 1000
            self.velocity_y += 0
        elif game.direction == 2:
            self.velocity_x += 0
            self.velocity_y -= g / 1000
        elif game.direction == 3:
            self.velocity_x -= g / 1000
            self.velocity_y += 0
        self.collision()
        game.root.after(dt, self.movement)

    def collision(self):
        if self.cord_x + self.radius >= x_pole:
            self.velocity_x = -red * self.velocity_x
            self.velocity_y = red * self.velocity_y
        elif self.cord_x - self.radius <= 0:
            self.velocity_x = -red * self.velocity_x
            self.velocity_y = red * self.velocity_y
        elif self.cord_y + self.radius >= y_pole:
            self.velocity_y = -red * self.velocity_y
            self.velocity_x = red * self.velocity_x
        elif self.cord_y - self.radius <= 0:
            self.velocity_y = -red * self.velocity_y
            self.velocity_x = red * self.velocity_x
        for k in balls:
            if self != k and (k.radius + self.radius) ** 2 >= (k.cord_x - self.cord_x) ** 2 + (
                    k.cord_y - self.cord_y) ** 2:
                velocity = (self.velocity_x ** 2 + self.velocity_y ** 2) ** 0.5
                distance = ((k.cord_x - self.cord_x) ** 2 + (k.cord_y - self.cord_y) ** 2) ** 0.5
                self.velocity_x = - red * velocity * ((k.cord_x - self.cord_x) / distance)
                self.velocity_y = - red * velocity * ((k.cord_y - self.cord_y) / distance)


game = Game()
balls = []
for i in range(N):
    balls.append(game.new_ball())
for i in balls:
    i.movement()
game.canvas.bind('<Button-1>', game.change)
mainloop()
