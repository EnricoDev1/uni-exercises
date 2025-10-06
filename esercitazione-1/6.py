import g2d
import random 

x, y, dx, dy = 200, 200, 0, 0
ARENA_W, ARENA_H = 400, 400

def tick():
    global x, y, dy, dx
    g2d.clear_canvas()  
    g2d.draw_circle((x, y), 20)
    
    if x % 20 == 0 and y % 20 == 0:
        dx = random.choice([-2, 0, 2])
        dy = random.choice([-2, 2]) if not dx else 0

    x += dx    
    y += dy
    
g2d.init_canvas((ARENA_W, ARENA_H))
g2d.main_loop(tick) 