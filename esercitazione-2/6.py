import g2d
from random import randrange

def main():
    g2d.init_canvas((500, 500))

    n = int(input("Inserisci il numero di quadrati da disegnare: "))
    inc = 480 / n

    for i, j in zip(reversed(range(n + 1)), range(n)):
        g2d.set_color((randrange(256), randrange(256), randrange(256)))

        inc_color = 256 / n

        g2d.set_color((0, j * inc_color, 0))
        g2d.draw_rect((j * inc + 10, 10), (inc * i, inc * i))

    g2d.main_loop()

if __name__ == "__main__":
    main()