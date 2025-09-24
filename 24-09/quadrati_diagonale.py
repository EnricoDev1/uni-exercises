import g2d 
import random 

g2d.init_canvas((500, 500))

n = int(input("Inserisci numero quadrati: "))

# TODO: controlli input...

for i in range(n):
    color = (random.randint(0, 255) for _ in range(3))
    g2d.set_color(color)
    l = 500 / n
    
    g2d.draw_rect((l * (i), l * (i)), (l, l))

g2d.main_loop()