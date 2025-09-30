import g2d 
import random 

g2d.init_canvas((500, 500))

n = int(input("Inserisci numero di quadrati da disegnare: "))

for _ in range(n):
    p = (random.randint(0, 445), random.randint(0, 445))
    color = (random.randint(0, 255) for _ in range(3))
    
    # ombra 
    g2d.set_color((59, 59, 59))
    g2d.draw_rect((p[0] + 5, p[1] + 5), (50, 50))

    # quadrato 
    g2d.set_color(color)
    g2d.draw_rect(p, (50, 50))

g2d.main_loop()