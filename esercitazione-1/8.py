import g2d
from math import sin, pi 
import random 

x, y, dx, dy = 200, 200, 2, 0
ARENA_W, ARENA_H = 400, 400

sprites_pos = [(21, 1), (0, 0), (0, 21)]
curr_sprite = (21, 1)

def tick():
    global x, y, dy, dx, curr_sprite
    g2d.clear_canvas()  
    g2d.draw_image("sprites.png", (x, y), curr_sprite, (17, 18))

    if x % 20 == 0:
        new_sprite = random.choice(sprites_pos)
        if new_sprite == (21, 1) and curr_sprite == (21, 1):
            curr_sprite = (21, 21)
        elif new_sprite == (21, 21) and curr_sprite (21, 21):
            curr_sprite = (21, 1)
        else: 
            curr_sprite = new_sprite  

    a = 10 
    t = 80

    y = y + a * sin(x * (2*pi/t))
    x += dx    

    if x >= ARENA_W + 10:
        x = -10
    
g2d.init_canvas((ARENA_W, ARENA_H))
g2d.main_loop(tick) 