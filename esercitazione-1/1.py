from math import pi 

def circumference(r: float) -> float:
    if r > 0:
        return 2 * pi * r
    else:
        raise ValueError("Hai inserito un numero negativo")
    
r = int(input("Inserisci misura del raggio: "))
print(f"La circonferenza del cerchio è: {round(circumference(r), 2)}")
