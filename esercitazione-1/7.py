import g2d
from math import sin, pi 

x, y, dx, dy = 200, 200, 2, 0
ARENA_W, ARENA_H = 400, 400

def tick():
    global x, y, dy, dx
    g2d.clear_canvas()  
    
    g2d.draw_circle((x, y), 20)

    a = 10 
    t = 80

    y = y + a * sin(x * (2*pi/t))
    x += dx    

    if x >= ARENA_W + 10:
        x = -10
    
g2d.init_canvas((ARENA_W, ARENA_H))
g2d.main_loop(tick) 