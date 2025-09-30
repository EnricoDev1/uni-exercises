n = int(input("Insersci un numero intero: "))

for i in range(1, n+1):
    if n % i == 0:
        print(i)