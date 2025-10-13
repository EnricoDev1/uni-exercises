from math import sin, pi
from random import choice
import g2d 

ARENA_W, ARENA_H = 400, 400
sprites = ((21, 21), (21, 0))

class OscillatingGhost:
    def __init__(self, x0, y0, a, t, size):
        self._x = x0
        self._y = y0
        self._dx = 2
        self._a = a 
        self._t = t        
        self._sprite = sprites[1]
        self._size = size 

    def move(self):
        self._y = self._y + self._a*sin(self._x * (2*pi/self._t))
        self._x += self._dx

        if self._x >= ARENA_W + 10:
            self._x = -10
        
        if self._x % 20 == 0:
            self._sprite = choice(sprites)

    def pos(self):
        return self._x, self._y

    def get_size(self):
        return self._size
    
    def get_sprite(self):
        return self._sprite

og = OscillatingGhost(100, 200, 10, 80, (17, 18))

def tick():
    g2d.clear_canvas()  
    g2d.draw_image("sprites.png", og.pos(), og.get_sprite(), og.get_size())
    og.move()    

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick) 

if __name__ == "__main__":
    main()