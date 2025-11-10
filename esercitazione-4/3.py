from random import randint

def main():
    n = int(input("Inserisci quante volte vuoi lanciare il dado: "))
    count = [0] * 11

    for _ in range(n):
        count[randint(1, 6) + randint(1, 6) - 2] += 1        

    for i, res in enumerate(count):
        print(f"Il numero {i + 2} è uscito {res} volte")

if __name__ == "__main__":  
    main()