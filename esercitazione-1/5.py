import g2d

x, y, dx = 200, 200, 2  
ARENA_W, ARENA_H = 400, 400
countdown = 30

def tick():
    global x, dx, countdown
    g2d.clear_canvas()  

    g2d.draw_circle((x, y), 20)
    
    if g2d.mouse_clicked() or 0 < countdown < 30:
        countdown -= 1
    else:
        x += dx  
        countdown = 30

g2d.init_canvas((ARENA_W, ARENA_H))
g2d.main_loop(tick) 