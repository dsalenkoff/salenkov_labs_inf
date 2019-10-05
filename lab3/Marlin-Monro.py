from graph import *

# Number of Marlin Monros < 6
n = 5

# Scale
k = 3

# Start points
p = -250
o = 0

i = 0

# Background
brushColor(randColor())
rectangle(0 * k + p, 0 * k + o, 800 * k, 400 * k + o)

canvasSize(720 + 250 * n, 720)
windowSize(720 + 250 * n, 720)
penSize(2)


def draw_face(p, o):
    brushColor(randColor())
    face = polygon([(115 * k + p, 89 * k + o), (108 * k + p, 77 * k + o), (108 * k + p, 70 * k + o),
                    (103 * k + p, 58 * k + o), (104 * k + p, 25 * k + o), (149 * k + p, 20 * k + o),
                    (150 * k + p, 55 * k + o), (141 * k + p, 69 * k + o), (143 * k + p, 77 * k + o),
                    (129 * k + p, 90 * k + o), (115 * k + p, 89 * k + o)])
    return face


def draw_lips(p, o):
    brushColor(randColor())
    lips = polygon([(113 * k + p, 74 * k + o), (118 * k + p, 71 * k + o), (128 * k + p, 71 * k + o),
                    (131 * k + p, 74 * k + o), (124 * k + p, 80 * k + o), (117 * k + p, 80 * k + o),
                    (113 * k + p, 74 * k + o)])
    return lips


def draw_eye(p, o):
    penSize(5)
    brushColor(randColor())
    eyelist = list()
    eyelist.append(polyline([(130 * k + p, 52 * k + o), (134 * k + p, 51 * k + o), (139 * k + p, 53 * k + o)]))
    eyelist.append(polyline([(114 * k + p, 52 * k + o), (107 * k + p, 52 * k + o), (107 * k + p, 55 * k + o)]))
    eyelist.append(polyline([(118 * k + p, 64 * k + o), (121 * k + p, 66 * k + o), (124 * k + p, 65 * k + o),
                             (128 * k + p, 65 * k + o)]))
    eyelist.append(polyline([(130 * k + p, 44 * k + o), (139 * k + p, 42 * k + o), (146 * k + p, 48 * k + o)]))
    eyelist.append(polyline([(114 * k + p, 45 * k + o), (107 * k + p, 43 * k + o), (103 * k + p, 46 * k + o)]))
    return eyelist


def draw_brows(p, o):
    brushColor(randColor())
    penSize(2)
    browslist = list()
    browslist.append(polygon(
        [(126 * k + p, 51 * k + o), (129 * k + p, 48 * k + o), (133 * k + p, 46 * k + o), (141 * k + p, 50 * k + o),
         (134 * k + p, 50 * k + o), (128 * k + p, 50 * k + o)]))
    browslist.append(polygon(
        [(117 * k + p, 51 * k + o), (115 * k + p, 48 * k + o), (108 * k + p, 49 * k + o), (104 * k + p, 52 * k + o),
         (109 * k + p, 51 * k + o), (117 * k + p, 51 * k + o)]))
    return browslist


def draw_hair(p, o):
    brushColor(randColor())
    penSize(2)
    hair = polygon([(121 * k + p, 27 * k + o), (138 * k + p, 22 * k + o), (146 * k + p, 25 * k + o),
                    (150 * k + p, 40 * k + o), (149 * k + p, 55 * k + o), (142 * k + p, 68 * k + o),
                    (144 * k + p, 78 * k + o), (159 * k + p, 84 * k + o), (159 * k + p, 74 * k + o),
                    (171 * k + p, 61 * k + o), (171 * k + p, 28 * k + o), (162 * k + p, 16 * k + o),
                    (149 * k + p, 14 * k + o), (137 * k + p, 4 * k + o), (112 * k + p, 3 * k + o),
                    (100 * k + p, 15 * k + o), (92 * k + p, 16 * k + o), (95 * k + p, 38 * k + o),
                    (91 * k + p, 44 * k + o), (106 * k + p, 66 * k + o), (103 * k + p, 41 * k + o),
                    (110 * k + p, 35 * k + o), (110 * k + p, 24 * k + o), (121 * k + p, 27 * k + o)])
    return hair


def draw_marlin():
    global i
    global p, o
    marlin = list()
    while i <= n:
        i += 1
        marlin.append(draw_face(p, o))
        marlin.append(draw_lips(p, o))
        marlin.append(draw_eye(p, o))
        marlin.append(draw_brows(p, o))
        marlin.append(draw_hair(p, o))
        p += 300
    return marlin


marlin = draw_marlin()


def update():
    for i in marlin:
        changeFillColor(i, randColor())


onTimer(update, 1000)

run()
