#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

from random import choice, randrange, uniform
from lib.actor import Actor, Arena, Point
import math
view_x, view_y = 0,0
ARENA_W, ARENA_H = 600,600
VIEW_W, VIEW_H = 200, 200

class Ball(Actor):
    def __init__(self, pos):
        self._x, self._y = pos
        self._w, self._h = 20, 20
        self._dx, self._dy = 4, 4

    def move(self, arena: Arena):
        global view_x, view_y

        for other in arena.collisions():
            if not isinstance(other, Ghost):
                x, y = other.pos()
                if x < self._x:
                    self._dx = abs(self._dx)
                else:
                    self._dx = -abs(self._dx)
                if y < self._y:
                    self._dy = abs(self._dy)
                else:
                    self._dy = -abs(self._dy)

        self._y = (VIEW_W / 2) + view_y
        self._x = (VIEW_H / 2) + view_x 

    def pos(self) -> Point:
        return self._x, self._y

    def size(self) -> Point:
        return self._w, self._h

    def sprite(self) -> Point:
        return 0, 0


class Ghost(Actor):
    def __init__(self, pos):
        theta = uniform(0, 2 * math.pi)  # angolo casuale
        self._startX=self._x = pos[0] + 100 * math.cos(theta)
        self._startY=self._y = pos[1] + 100 * math.sin(theta)
        self._w, self._h = 20, 20
        self._visible = True

    def move(self, arena: Arena):
        aw, ah = arena.size()
        dx = choice([-4, 0, 4])
        dy = choice([-4, 0, 4])
        self._x = (self._x + dx) % aw
        self._y = (self._y + dy) % ah
        keys = arena.current_keys()
        if "h" in keys:
            self._x = self._startX
            self._y = self._startY

        if randrange(100) == 0:
            self._visible = not self._visible
        if randrange(1000) == 0:
            arena.spawn(Ball(self.pos()))

    def pos(self) -> Point:
        return self._x, self._y

    def size(self) -> Point:
        return self._w, self._h

    def sprite(self) -> Point:
        if self._visible:
            return 20, 0
        return 20, 20


class Turtle(Actor):
    def __init__(self, pos):
        self._x, self._y = pos
        self._w, self._h = 20, 20
        self._speed = 2

    def move(self, arena: Arena):
        for other in arena.collisions():
            if isinstance(other, Ball):
                self.hit(arena)

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

    global view_x, view_y

    keys = g2d.current_keys()
    if "ArrowUp" in keys:
        view_y = max(view_y - 10, 0)
    elif "ArrowRight" in keys:
        view_x = min(view_x + 10, ARENA_W - VIEW_W)
    elif "ArrowDown" in keys:
        view_y = min(view_y + 10, ARENA_H - VIEW_H)
    elif "ArrowLeft" in keys:
        view_x = max(view_x - 10, 0)

    g2d.draw_image("background.png", (0,0), (view_x, view_y), (VIEW_W, VIEW_H))
    
    for a in arena.actors():
        if a.sprite() != None:
            x,y = a.pos()
            g2d.draw_image("sprites.png", (x-view_x,y-view_y), a.sprite(), a.size())
        else:
            pass  # g2d.draw_rect(a.pos(), a.size())
    
    arena.tick(g2d.current_keys())  # Game logic


def main():
    global g2d, arena
    import lib.g2d as g2d  # game classes do not depend on g2d

    arena = Arena((ARENA_W, ARENA_H))
    arena.spawn(Ball((80, 40)))
    arena.spawn(Ghost((ARENA_W/2, ARENA_H/2)))

    g2d.init_canvas((VIEW_W, VIEW_H))
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()
