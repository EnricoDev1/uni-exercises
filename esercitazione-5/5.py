def digits(n):
    dig = []
    while True:
        dig.append(n % 10)
        n //= 10

        if n <= 0:
            break
    return dig 

def main():
    while True:
        n = input("Inserisci il numero: ")
        if not n:
            break

        print(digits(int(n)))

if __name__ == "__main__":
    main()