import g2d
from math import pi

g2d.init_canvas((500, 500))

r = int(input("Inserisci raggio cerchio compreso tra 0 e 200: "))

if r < 0 or r > 200:
    g2d.alert("dati sbagliati")
else:
    area = round(pi * r**2, 2)
    circ = round(2 * pi * r, 2)

    g2d.draw_circle((250, 250), r)
    g2d.draw_text(f"Area: {area}", (250, 270 + r), 16)
    g2d.draw_text(f"Circonferenza: {circ}", (250, 230 - r), 16)

g2d.main_loop()