from lib import g2d

def main():
    g2d.init_canvas((400, 400), scale=1.2)
    with open("lib/file.txt") as f:
        colors = [tuple(map(int, line.split(","))) for line in f if line.strip()]
    
    n = int(input("Inserisci un numero intero: "))

    for i in range(n):
        g2d.set_color(colors[i % len(colors)])
        g2d.draw_circle((200, 200), 200 - (200 / n) * i)
    g2d.main_loop()

if __name__ == "__main__":
    main()