from random import randrange as rnd, choice
import tkinter as tk
import math
import time

# print (dir(math))

x_pole = 1020
y_pole = 680

root = tk.Tk()
fr = tk.Frame(root)
root.geometry(str(x_pole) + 'x' + str(y_pole))
canv = tk.Canvas(root, bg='#f0ffff')
canv.pack(fill=tk.BOTH, expand=1)

Numbers_of_targets = 7
Particles = 5
min_radius = 15
max_radius = 30
min_target_velocity = -5
max_target_velocity = 5

colors = ['#47a76a', '#ffb841', '#4285b4']
Number_of_verticles = [0, 4, 5]


class Shapes():
    def draw_oval(self, x, y, r, color):
        self.id = canv.create_oval(
            x - r,
            y - r,
            x + r,
            y + r,
            fill=color,
            outline=color
        )
        return self.id

    def draw_polygon(self, x, y, radius, N, color):
        self.id = canv.create_rectangle(
            x - radius,
            y - radius,
            x + radius,
            y + radius,
            fill=self.color,
            outline=color
        )
        return self.id


class ball(Shapes):
    def __init__(self, x=40, y=450, iteration=0, radius=20, vx=0, vy=0, live=25):
        self.iteration = iteration
        self.x = x
        self.y = y
        self.radius = radius
        self.vx = vx
        self.vy = vy
        self.verticles = choice(Number_of_verticles)
        self.color = choice(colors)
        if self.verticles == 0:
            self.id = self.draw_oval(self.x, self.y, self.radius, self.color)
        else:
            self.id = self.draw_polygon(self.x, self.y, self.radius, self.verticles, self.color)
        self.live = live
        self.move()

    def move(self):
        if self.x + self.radius >= x_pole or self.x - self.radius <= 0:
            self.vx = -0.7 * self.vx
        if self.y + self.radius >= y_pole or self.y - self.radius <= 0:
            self.vy = -0.7 * self.vy
        self.x += 0.5 * self.vx
        self.y -= 0.5 * self.vy
        self.vy -= 2
        canv.coords(
            self.id,
            self.x - self.radius,
            self.y - self.radius,
            self.x + self.radius,
            self.y + self.radius
        )
        root.after(10, self.move)

    def hittest(self, obj):
        if ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) ** 0.5 <= self.radius + obj.radius:
            return True
        else:
            return False

    def spread(self):
        for i in range(Particles):
            balls.append(ball(self.x, self.y, 1, 15, rnd(0, 50), rnd(-50, 50), 50))


class Gun():
    def __init__(self):
        self.points = 0
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.direction = None
        self.x = 20
        self.y = 450
        self.id = None
        self.id_points = None
        self.draw()

    def draw(self):
        self.id = canv.create_line(self.x, self.y, self.x + 30, self.y - 30, width=12)
        self.id_points = canv.create_text(30, 30, text=self.points, font='28')

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        global balls
        new_ball = ball(self.x + 20, self.y)
        new_ball.radius += 5
        self.an = math.atan((event.y - self.y) / (event.x - self.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        if event:
            self.an = math.atan((event.y - self.y) / (event.x - self.x))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, self.x, self.y,
                    self.x + max(self.f2_power, 20) * math.cos(self.an),
                    self.y + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')

    def move_up(self, event=0):
        self.y -= 15
        canv.coords(self.id, self.x, self.y,
                    self.x + max(self.f2_power, 20) * math.cos(self.an),
                    self.y + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def move_down(self, event=0):
        self.y += 15
        canv.coords(self.id, self.x, self.y,
                    self.x + max(self.f2_power, 20) * math.cos(self.an),
                    self.y + max(self.f2_power, 20) * math.sin(self.an)
                    )


class Target(Shapes):
    def __init__(self):
        self.radius = rnd(min_radius, max_radius)
        self.verticles = choice(Number_of_verticles)
        self.color = choice(colors)
        self.points = 0
        self.live = 1
        self.vy = rnd(min_target_velocity, max_target_velocity)
        while self.vy == 0:
            self.vy = rnd(min_target_velocity, max_target_velocity)
        self.new_target()

    def new_target(self):
        self.x = rnd(x_pole - 700, x_pole - 50)
        self.y = rnd(300, y_pole)
        for i in targets:
            while math.fabs(i.x - self.x) <= i.radius + self.radius:
                self.x = rnd(x_pole - 700, x_pole - 50)
                self.y = rnd(300, y_pole)
        if self.verticles == 0:
            self.id = self.draw_oval(self.x, self.y, self.radius, self.color)
        else:
            self.id = self.draw_polygon(self.x, self.y, self.radius, self.verticles, self.color)
        canv.coords(self.id, self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius)
        canv.itemconfig(self.id, fill=self.color)
        self.move()

    def move(self):
        if self.y >= y_pole or self.y <= 0:
            self.vy = -self.vy
        self.y += self.vy
        canv.coords(
            self.id,
            self.x - self.radius,
            self.y - self.radius,
            self.x + self.radius,
            self.y + self.radius
        )
        root.after(10, self.move)

    def hit(self, points=1):
        canv.coords(self.id, -10, -10, -10, -10)
        gun.points += points
        canv.itemconfig(gun.id_points, text=gun.points)


balls = []
targets = []
gun = Gun()
canv.bind('<Button-1>', gun.fire2_start)
canv.bind('<ButtonRelease-1>', gun.fire2_end)
canv.bind('<Motion>', gun.targetting)
root.bind('w', gun.move_up)
root.bind('s', gun.move_down)
z = 0.01


def game(event=''):
    canv.delete('all')
    gun.draw()
    for i in range(Numbers_of_targets):
        targets.append(Target())
    while targets:
        for b in balls:
            b.live -= 1
            if b.live <= 0:
                if b.iteration == 0:
                    b.spread()
                canv.delete(b.id)
                balls.remove(b)
        for k in targets:
            for b in balls:
                if b.hittest(k) and k.live:
                    if b.iteration == 0:
                        b.spread()
                    k.live = 0
                    canv.delete(b.id)
                    balls.remove(b)
                    canv.delete(k.id)
                    targets.remove(k)
                    k.hit()
        canv.update()
        time.sleep(z)
        gun.targetting()
        gun.power_up()
    print('Игра завершилась')
    balls.clear()
    targets.clear()
    canv.create_text(400, 300, text='Вы победили', font='28')
    root.after(2000, game)


game()

tk.mainloop()
