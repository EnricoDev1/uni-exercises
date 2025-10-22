import lib.g2d as g2d 

def draw_figure(centro, raggio, n):
    inc = raggio / n
    inc_color = 255 / n 
    
    for i, j in zip(reversed(range(1, n + 1)), range(n)):    
        print(i)
        g2d.set_color((inc_color * j, inc_color * j, inc_color * j))
        g2d.draw_circle(centro, inc * i)

def main():
    n = int(input("Inserisci il numero di figure: "))
    g2d.init_canvas((500, 500))

    for i in range(n):
        raggio = 500 / 2 / n
        centro = ((500 / n) * i + raggio, 250)
        draw_figure(centro, raggio, n)
    
    g2d.main_loop()

if __name__ == "__main__":
    main()