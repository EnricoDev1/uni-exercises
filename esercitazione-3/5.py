from string import ascii_lowercase
from random import choice

def add_letter():
    return choice(list(ascii_lowercase))

def main():
    n = int(input("Inserisci un intero: "))
    final = ""

    for _ in range(n):
        final += add_letter()

    print(final)
if __name__ == "__main__":
    main()