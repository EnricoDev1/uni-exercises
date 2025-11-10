import g2d 
from random import randrange
dx = 4
x, y = 20, 20

def tick():
    g2d.clear_canvas()
    global dx, y, x
    g2d.draw_rect((x, y), (30, 30))
    x += dx
    
    if g2d.mouse_clicked():
        dx = -dx
        
    if x >= 500 and dx > 0:
        x = -100
    if x <= -30 and dx < 0:
        x = 600
    
def main():
    g2d.init_canvas((500, 500))
    g2d.main_loop(tick)
    
if __name__ == "__main__":
    main()
