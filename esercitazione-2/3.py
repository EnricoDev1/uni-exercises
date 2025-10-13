import g2d 
from typing import Tuple
from random import randrange

ARENA_W,ARENA_H, BALL_W,BALL_H = 480,360, 20,20

class Ball:
    def __init__(self, x0: int, y0: int):
        self._x = x0
        self._y = y0
        self._dx, self._dy = 4, 4
        self.color = (randrange(256), randrange(256), randrange(256))
        
    def move(self):
        if not 0 <= self._x + self._dx <= ARENA_W - BALL_W:
            self._dx = -self._dx
            self.set_color()
        if not 0 <= self._y + self._dy <= ARENA_H - BALL_H:
            self._dy = -self._dy
            self.set_color()
        self._x += self._dx
        self._y += self._dy

    def pos(self) -> Tuple[int, int]:
        return self._x, self._y

    def get_color(self) -> Tuple[int, int, int]:
        return self.color

    def set_color(self):
        self.color = (randrange(256), randrange(256), randrange(256))

b1 = Ball(140, 180)
b2 = Ball(90, 20)
b3 = Ball(200, 100)

def tick():
    g2d.clear_canvas()
    
    g2d.set_color(b1.get_color())
    g2d.draw_rect(b1.pos(), (BALL_W, BALL_H))
    
    g2d.set_color(b2.get_color())
    g2d.draw_rect(b2.pos(), (BALL_W, BALL_H))

    g2d.set_color(b3.get_color())
    g2d.draw_rect(b3.pos(), (BALL_W, BALL_H))
    
    b1.move()
    b2.move()
    b3.move()

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()