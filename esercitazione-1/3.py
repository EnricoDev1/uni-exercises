import g2d 
from math import sqrt

g2d.init_canvas((400, 400))

n = int(input("Inserisci numero di punti: "))

x1, y1 = map(int, input("Inserisci coordinate PRIMO punto separate da uno spazio: ").split(" "))
x2, y2 = map(int, input("Inserisci coordinate SECONDO punto separate da uno spazio: ").split(" "))

inc = sqrt((x2 - x1)**2 + (y2 - y1)**2) / n 

for i in range(n):
    g2d.set_color((255, 0, 0))
    g2d.draw_circle((x1 + (inc * i), y1 + (inc* i)), 5)

g2d.main_loop()