from math import sqrt

c = True

while c:
    a, b, c = map(int, input("Inserisci i 3 coefficienti dell'equazione separati da uno spazio: ").split(" "))

    delta = b ** 2 - 4*a*c

    if delta > 0:
        print(f"x1 = {round((-b + sqrt(delta)) / 2*a, 2) }\nx2 = {round((-b - sqrt(delta)) / 2*a, 2)}")
    elif delta < 0:
        print("Nessuna soluzione reale")
    else:
        print(f"x1 = x2 = {round((-b + sqrt(delta)) / 2*a, 2) }")

    c = input("Inserire C per continuare, altro per stoppare: ") == "C"
