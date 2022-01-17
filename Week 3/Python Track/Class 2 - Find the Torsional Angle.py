import math

class Points(object):
    def __init__(self, x, y, z):
        self.list = [x, y, z]
    def __sub__(self, no):
        return Points(*[self.list[i] - no.list[i] for i in range(len(no.list))])

    def dot(self, no):
        return sum([self.list[i] * no.list[i] for i in range(len(no.list))])

    def cross(self, no):
        a, b = self.list, no.list
        return Points(
            *[
                a[1] * b[2] - a[2] * b[1],
                a[2] * b[0] - a[0] * b[2],
                a[0] * b[1] - a[1] * b[0],
            ]
        )

    def absolute(self):
        return pow((self.list[0] ** 2 + self.list[1] ** 2 + self.list[2] ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))