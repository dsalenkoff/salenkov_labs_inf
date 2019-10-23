from random import randrange as rnd

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)


    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)


    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            return Vector(self.x * other, self.y * other, self.z * other)


    def __abs__(self):
        return ((self.x ** 2) + (self.y ** 2) + (self.z ** 2)) ** 0.5



    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        elif item == 2:
            return self.z


def len(self):
        return ((self.x ** 2) + (self.y ** 2) + (self.z ** 2)) ** 0.5


v1 = Vector(rnd(1, 10), rnd(1, 10), rnd(1, 10))
print('Вектор 1: ', v1.x, v1.y, v1.z)
v2 = Vector(rnd(1, 10), rnd(1, 10), rnd(1, 10))
print('Вектор 2: ', v2.x, v2.y, v2.z)
v3 = v1 + v2
print('Вектор суммы: ', v3.x, v3.y, v3.z)
v4 = v1 - v2
print('Вектор разности: ', v4.x, v4.y, v4.z)
scalar = v1 * v2
print('Скалярное произведение векторов: ', scalar)
k = rnd(1, 10)
print('Коэффициент: ', k)
v5 = v1 * k
print('Вектор 1, умноженный на коэффициент: ', v5.x, v5.y, v5.z)
print('Длина вектора 1: ', abs(v1))
print('Длина вектора 1: ', len(v1))