import g2d 
from random import randrange

def tick():
    if g2d.mouse_clicked():
        pos = g2d.mouse_pos()
        color = (randrange(256) for _ in range(3))
        if (pos[0]-50 < 250 < pos[0]+50) and (pos[1]-50 < 250 < pos[1]+50):
            
            if not g2d.confirm("Confermi? (chiude il programma)"):
                g2d.set_color(color)
                g2d.draw_circle((pos), 40)

def main():
    g2d.init_canvas((500, 500))
    g2d.main_loop(tick)
    
if __name__ == "__main__":
    main()
