from lib import g2d
from math import sin, cos, pi 

def regular_poly(n, p, r, a):
    points = list()
    ang = 2*pi / n
    x, y = 0, 0
    for i in range(n):
        x = p[0] + r*cos(ang * i)
        y = p[1] + r*sin(ang * i)
        points.append((x, y))

    print(points)
    
    return points

def tick():
    g2d.clear_canvas()
    g2d.set_stroke(1)
    vals = regular_poly(5, (200, 200), 100, 0)
    g2d.draw_circle((200, 200), 100)
    g2d.draw_polygon(vals)

def main():
    g2d.init_canvas((400, 400))
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()
