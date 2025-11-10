from lib import g2d 
from random import randrange

def main():
    g2d.init_canvas((500, 500))
    g2d.set_color((0, 0, 255))
    vals = []
    while True:
        if (val := int(input("Inserisci valore: "))) > 0:
            vals.append(val)
        else:
            break

    stepY = 500 / len(vals)
    stepX = 500 / max(vals)

    for i, val in enumerate(vals):
        g2d.draw_rect((0, i * stepY), (val * stepX, stepY))

    g2d.main_loop()

if __name__ == "__main__":
    main()