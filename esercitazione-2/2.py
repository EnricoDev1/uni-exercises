from math import e, exp

class esponenziale:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def estimate(self, x):
        return self.a * exp(self.b * x) + self.c

def main():
    a, b, c = map(int, input("Inserisci i coefficienti a,b,c separati da una virgola: ").split(","))
    e = esponenziale(a, b, c)
    while True:
        x = input("Inserisci la x in cui valutare la funzione (linea vuota stop): ")
        if not x:
            break

        x = int(x)
        print(f"La funzione in {x} assume valore {round(e.estimate(x), 2)}")

if __name__ == "__main__":
    main()