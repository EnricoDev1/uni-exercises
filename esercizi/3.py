import g2d 
from random import randrange, uniform
dx, dy = 4, 20
from math import sin, cos, pi
from time import sleep

class Circle:
    def __init__(self, n):
        self._n = n
        self._color = (255, 0, 0)
        self._radius = 0
        self._x = 270
        self._y = 270
        self._angle = 0
        self._i = 0
        
    def pos(self):
        return self._x, self._y
    
    def color(self):
        return self._color
    
    def radius(self):
        return self._radius
    
    def move(self):       
        if self._i >= self._n:
            self._i = 0
        
        self._radius = 5 + ((self._i+1) * 5)
        self._x = 250 + (self._radius * 2) * sin(self._angle)
        self._y = 250 + (self._radius * 2) * cos(self._angle)
        self._angle -= (2*pi / 6)
        self._color = (randrange(256) for _ in range (3))                
        
        self._i += 1
        
circle = Circle(10)    

def tick():
    g2d.clear_canvas()
    g2d.set_color(circle.color())
    g2d.draw_circle(circle.pos(), circle.radius())
    circle.move()
    sleep(0.2)
    
def main():
    g2d.init_canvas((500, 500))
    g2d.main_loop(tick)
    
if __name__ == "__main__":
    main()
