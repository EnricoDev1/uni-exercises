import g2d 
import random 
from math import sqrt

g2d.init_canvas((500, 500))

cond = True

def diff(p):
    return sqrt(pow(p[0] - 250, 2) + pow(p[1] - 250, 2)) > 20

while cond:
    c = (random.randint(0, 500), random.randint(0, 500))
    color = (random.randint(0, 255) for _ in range(3))

    g2d.set_color(color)
    g2d.draw_circle(c, 20)

    cond = diff(c)

g2d.main_loop()