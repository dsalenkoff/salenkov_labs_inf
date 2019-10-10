import math

from graph import brushColor, polygon, \
    randColor, rectangle, changeFillColor, windowSize, \
    canvasSize, onTimer, run, penSize, polyline, moveObjectBy

angle = 0

# Number of Marlin Monro`s < 6
n = 3

# Scale
k = 4

# Start points
p = -200
o = 0

lines = 0
rows = 0

# Background
brushColor(randColor())
rectangle(0 * k + p, 0 * k + o, 800 * k, 400 * k + o)

canvasSize(720 + 320 * n, 960)
windowSize(720 + 320 * n, 960)
penSize(2)


def draw_marlin():
    global marlin
    marlin = list()
    global lines, rows, p, o
    while lines <= 1:
        while rows <= n:

            # Face
            marlin.append(polygon([(115 * k + p, 89 * k + o), (108 * k + p, 77 * k + o),
                                   (108 * k + p, 70 * k + o),
                                   (103 * k + p, 58 * k + o), (104 * k + p, 25 * k + o),
                                   (149 * k + p, 20 * k + o),
                                   (150 * k + p, 55 * k + o), (141 * k + p, 69 * k + o),
                                   (143 * k + p, 77 * k + o),
                                   (129 * k + p, 90 * k + o), (115 * k + p, 89 * k + o)]))

            # Lips
            marlin.append(polygon([(113 * k + p, 74 * k + o), (118 * k + p, 71 * k + o),
                                   (128 * k + p, 71 * k + o),
                                   (131 * k + p, 74 * k + o), (124 * k + p, 80 * k + o),
                                   (117 * k + p, 80 * k + o),
                                   (113 * k + p, 74 * k + o)]))

            # Eye
            marlin.append(polyline([(130 * k + p, 52 * k + o), (134 * k + p, 51 * k + o),
                                    (139 * k + p, 53 * k + o)]))
            marlin.append(polyline([(114 * k + p, 52 * k + o), (107 * k + p, 52 * k + o),
                                    (107 * k + p, 55 * k + o)]))
            marlin.append(polyline([(118 * k + p, 64 * k + o), (121 * k + p, 66 * k + o),
                                    (124 * k + p, 65 * k + o),
                                    (128 * k + p, 65 * k + o)]))
            marlin.append(polyline([(130 * k + p, 44 * k + o), (139 * k + p, 42 * k + o),
                                    (146 * k + p, 48 * k + o)]))
            marlin.append(polyline([(114 * k + p, 45 * k + o), (107 * k + p, 43 * k + o),
                                    (103 * k + p, 46 * k + o)]))

            # Brows
            marlin.append(polygon([(126 * k + p, 51 * k + o), (129 * k + p, 48 * k + o),
                                   (133 * k + p, 46 * k + o),
                                   (141 * k + p, 50 * k + o), (134 * k + p, 50 * k + o),
                                   (128 * k + p, 50 * k + o)]))
            marlin.append(polygon(
                [(117 * k + p, 51 * k + o), (115 * k + p, 48 * k + o), (108 * k + p, 49 * k + o),
                 (104 * k + p, 52 * k + o),
                 (109 * k + p, 51 * k + o), (117 * k + p, 51 * k + o)]))

            # Hair
            marlin.append(polygon([(121 * k + p, 27 * k + o), (138 * k + p, 22 * k + o),
                                   (146 * k + p, 25 * k + o),
                                   (150 * k + p, 40 * k + o), (149 * k + p, 55 * k + o),
                                   (142 * k + p, 68 * k + o),
                                   (144 * k + p, 78 * k + o), (159 * k + p, 84 * k + o),
                                   (159 * k + p, 74 * k + o),
                                   (171 * k + p, 61 * k + o), (171 * k + p, 28 * k + o),
                                   (162 * k + p, 16 * k + o),
                                   (149 * k + p, 14 * k + o), (137 * k + p, 4 * k + o),
                                   (112 * k + p, 3 * k + o),
                                   (100 * k + p, 15 * k + o), (92 * k + p, 16 * k + o),
                                   (95 * k + p, 38 * k + o),
                                   (91 * k + p, 44 * k + o), (106 * k + p, 66 * k + o),
                                   (103 * k + p, 41 * k + o),
                                   (110 * k + p, 35 * k + o), (110 * k + p, 24 * k + o),
                                   (121 * k + p, 27 * k + o)]))
            rows += 1
            p += 350
        lines += 1
        rows = 0
        p = -200
        o += 400
    return marlin


def changeColor():
    global angle
    for z in marlin:
        changeFillColor(z, randColor())


def rotateMarlin():
    global angle
    for s in marlin:
        moveObjectBy(s, 0.5 * math.cos(angle), 0.5 * math.sin(angle))
    if angle <= 2 * math.pi:
        angle += 0.005
    else:
        angle = 0


marlin = draw_marlin()
onTimer(rotateMarlin, 1)
onTimer(changeColor, 500)

run()
