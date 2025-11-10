from random import choice, seed
from string import ascii_lowercase

seed(1)

def main():
    w, h = map(int, input("Inserisci w e h separati da uno spazio: ").split(" "))
    lista = [[choice(ascii_lowercase) for _ in range(h)] for _ in range(w)]

    for i in range(w):
        for j in range(h):
            print(f"{lista[i][j]}", end="," if j < h-1 else "\n")

    while True:
        char = input("Inserisci un carattere, linea vuota per stoppare: ").strip()
        if not char:
            break
    
        count = 0
        count_bordo = 0

        for i in range(w):
            for j in range(h):
                if lista[i][j] == char:
                    count += 1
                    if (i == 0 or i == w-1) or (j == 0 or j == h-1):
                        count_bordo += 1
        
        print(f"Il carattere è presente {count} volte")
        print(f"Il carattere è ai bordi {count_bordo} volte")

if __name__ == "__main__":
    main()