def recursive_pow(x, n):
    if n == 0:
        return 1
    else:
        return x * recursive_pow(x, n-1)

def main():
    print(f"Il risultato è: {recursive_pow(int(input("Inserisci base: ")), int(input("Inserisci esponente: ")))}")

if __name__ == "__main__":
    main()