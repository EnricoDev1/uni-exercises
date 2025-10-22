from random import choice, randrange, uniform
from lib.actor import Actor, Arena, Point

view_x, view_y = 0,0
ARENA_W, ARENA_H = 600, 187

class Arthur(Actor):
    def __init__(self, pos):
        self._x, self._y = pos
        self._w, self._h = 20, 20
        self._speed = 2

    def move(self, arena: Arena):

        keys = arena.current_keys()
        if "ArrowUp" in keys:
            self._y -= self._speed
        elif "ArrowDown" in keys:
            self._y += self._speed
        if "ArrowLeft" in keys:
            self._x -= self._speed
        elif "ArrowRight" in keys:
            self._x += self._speed

        aw, ah = arena.size()
        self._x = min(max(self._x, 0), aw - self._w)  # clamp
        self._y = min(max(self._y, 0), ah - self._h)  # clamp

    def hit(self, arena: Arena):
        arena.kill(self)

    def pos(self) -> Point:
        return self._x, self._y

    def size(self) -> Point:
        return self._w, self._h

    def sprite(self) -> Point:
        return 0, 20
    

def tick():
    g2d.clear_canvas()
    g2d.draw_image("lib/bg.png", (0,0), (2, 10), (2868, 187))
    for a in arena.actors():
        if a.sprite() != None:
            g2d.draw_image("lib/sprites.png", a.pos(), a.sprite(), a.size())
        else:
            pass  # g2d.draw_rect(a.pos(), a.size())

    arena.tick(g2d.current_keys())  # Game logic

def main():
    global g2d, arena
    import lib.g2d as g2d  # game classes do not depend on g2d

    arena = Arena((ARENA_W, ARENA_H))
    arena.spawn(Arthur((200, 200)))

    g2d.init_canvas(arena.size())
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()
