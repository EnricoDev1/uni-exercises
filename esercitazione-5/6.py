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

        res = digits(int(n))
        num = 0

        for a, b in enumerate(res):
            num += b * (10**a)

        print(num)
if __name__ == "__main__":
    main()