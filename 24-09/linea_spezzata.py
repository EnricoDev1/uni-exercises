import g2d 
import random 

g2d.init_canvas((500, 500))

start = (random.randint(50, 450), random.randint(50, 450)) 
n = int(input("Inserisci numero segmenti: "))
for i in range(n):
    g2d.set_color((255, 0, 0))
    
    stop = (random.randint(50, 450), random.randint(50, 450))
    
    g2d.draw_line(start, stop)
    start = stop
    