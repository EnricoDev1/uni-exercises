from lib import g2d
from math import sqrt

def rec_circles(x, y, r):
    if r <= 5:
        return

    g2d.draw_circle((x, y), r)

    delta = [(r, -r), (-r, -r), (r, r), (-r, r)]

    for dx, dy in delta:
        rec_circles(x + dx, y + dy, r * (sqrt(2) - 1))

def main():
    g2d.init_canvas((400, 400))
    g2d.set_color((0,0,0))
    rec_circles(200, 200, 100)
    g2d.main_loop()

if __name__ == "__main__":
    main()
