from math import sqrt

class Parallelepipedo:
    def __init__(self, l, w, h):
        self.l = l
        self.w = w
        self.h = h

    def volume(self):
        return self.l * self.w * self.h

    def diagonale(self):
        return round(sqrt(self.l ** 2 + self.w ** 2 + self.h ** 2), 2)

def main():
    l, w, h = map(int, input("Inserisci lunghezza, larghezza e altezza separati da una virgola: ").split(","))
    p = Parallelepipedo(l, w, h)
    print(f"Il volume del parallelepipedo è: {p.volume()}")
    print(f"La diagonale del parallelepipedo è: {p.diagonale()}")

if __name__ == "__main__":
    main()