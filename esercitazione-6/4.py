from lib import g2d
from math import sqrt
from random import randrange

def make_palette(depth):
    return [(randrange(256), randrange(256), randrange(256)) for _ in range(depth)]

DIRS = [(1,1), (1,-1), (-1,1), (-1,-1)]

def rec_circles(x, y, r, depth, palette, skip_dir=None):
    if depth == 0:
        return
    
    g2d.set_color(palette[depth-1])
    g2d.draw_circle((x, y), r)

    # raggio successivo
    new_r = r * (sqrt(2) - 1)

    for dx, dy in DIRS:
        if skip_dir == (dx, dy):
            # evita di tornare indietro
            continue
        
        rec_circles(
            x + dx * r,
            y + dy * r,
            new_r,
            depth - 1,
            palette,
            skip_dir=(-dx, -dy)
        )

def main():
    g2d.init_canvas((400, 400), scale=2)
    depth = 4
    rec_circles(200, 200, 100, depth, make_palette(depth))
    g2d.main_loop()

if __name__ == "__main__":
    main()
