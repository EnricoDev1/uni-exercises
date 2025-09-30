a, b, c = map(int, input("Inserisci i 3 coefficienti dell'equazione separati da uno spazio: ").split(" "))

delta = b ** 2 - 4*a*c

if delta > 0:
    print("Due soluzione reali")
elif delta < 0:
    print("Nessuna soluzione reale")
else:
    print("Un'unica soluzione reale")