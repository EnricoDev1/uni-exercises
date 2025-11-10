from random import randint

def randchar(a, b):
    return _chr(randint(ord(a), ord(b)))

def main():
    a = input("Inserisci lettera iniziale: ")
    b = input("Inserisci lettera finale: ")
    print(randchar(a, b))

if __name__ == "__main__":
    main()