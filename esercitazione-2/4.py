import g2d
import random 

ARENA_W, ARENA_H = 400, 400

class RandomWalker():
    def __init__(self, x0: int, y0: int):
        self.x = x0 + (x0 % 2)
        self.y = y0 + (y0 % 2)
        self.dx = 2
        self.dy = 2

    def move(self):
        if self.x % 20 == 0 and self.y % 20 == 0:
            possible_dx = [-2, 0, 2]
            possible_dx.remove(-self.dx)
            possible_dy = [-2, 2]

            if self.dy:
                possible_dy.remove(-self.dy)

            self.dx = random.choice(possible_dx)
            self.dy = random.choice(possible_dy) if not self.dx else 0
        self.x += self.dx
        self.y += self.dy

    def pos(self):
        return self.x, self.y
    
rw = RandomWalker(119, 119)

def tick():
    g2d.clear_canvas()  
    g2d.draw_rect(rw.pos(), (30, 30))
    rw.move()
    

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick) 

if __name__ == "__main__":
    main()