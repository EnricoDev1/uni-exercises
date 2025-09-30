x1, y1 = (int(x.strip()) for x in input("Inserisci il primo punto nel formato: x, y: ").split(","))
x2, y2 = (int(x.strip()) for x in input("Inserisci il secondo punto nel formato: x, y: ").split(","))

if x1 - x2 != 0:
    print(f"Il coefficiente angolare è: {(y1 - y2)/(x1 - x2)}")
else:
    print("retta verticale")