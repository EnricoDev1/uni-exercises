from lib import g2d 
from random import randrange

def main():
    g2d.init_canvas((400, 400))
    coords = []

    cond = True

    while cond:
        pos = (randrange(400), randrange(400))
        for coord in coords:
            if (abs(pos[0] - coord[0]) < 20 and abs(pos[1] - coord[1]) < 20):
                cond = False

        g2d.draw_rect(pos, (20, 20))
        coords.append(pos)
        
    g2d.main_loop()
if __name__ == "__main__":
    main()