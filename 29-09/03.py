import g2d 
import random 

g2d.init_canvas((500, 500))

n = int(input("Inserisci numero di cerchi da disegnare: "))

for _ in range(n):
    c = (random.randint(0, 500), random.randint(0, 500))
    color = (random.randint(0, 255) for _ in range(3))
    g2d.set_color(color)
    g2d.draw_circle(c, 50)

g2d.main_loop()