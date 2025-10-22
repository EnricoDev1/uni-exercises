import lib.g2d as g2d 
from random import uniform
from math import pi, cos, sin

def randline(p1):
    x, y = p1 
    angolo = uniform(0, 2*pi)

    x2 = x + 100 * cos(angolo)
    y2 = y + 100 * sin(angolo)
    
    g2d.draw_line((p1), (x2, y2))

    return (x2, y2)

def main():
    n = int(input("Inserisci il numero di figure: "))
    g2d.init_canvas((400, 400))
    p = (200, 200)
    
    for i in range(n):
        p = randline(p)
        
    g2d.main_loop()

if __name__ == "__main__":
    main()