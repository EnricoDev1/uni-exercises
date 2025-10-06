import g2d 
from math import sqrt

g2d.init_canvas((400, 400))

n = int(input("Inserisci numero di punti: "))

x1, y1 = map(int, input("Inserisci coordinate PRIMO punto separate da uno spazio: ").split(" "))
x2, y2 = map(int, input("Inserisci coordinate SECONDO punto separate da uno spazio: ").split(" "))

r1, g1, b1 = map(int, input("Insersci colore PRIMO punto nel formato r g b: ").split(" "))
r2, g2, b2 = map(int, input("Insersci colore SECONDO punto nel formato r g b: ").split(" "))

inc = sqrt((x2 - x1)**2 + (y2 - y1)**2) / n 

incR = (r2 - r1) / n
incG = (g2 - g1) / n
incB = (b2 - b1) / n

for i in range(n):
    g2d.set_color((r1 + incR*i, g1 + incG*i, b1 + incB*i))
    g2d.draw_circle((x1 + (inc*i), y1 + (inc*i)), 5)  

g2d.main_loop()

