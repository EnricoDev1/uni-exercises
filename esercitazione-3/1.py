values = []

while True:
    n = int(input("Inserisci intero: "))
    if n == 0:
        break

    values.append(n)

avg = round(sum(values) / len(values), 2)

minori = []
maggiori = []

for val in values:
    if val < avg:
        minori.append(val)
    else:
        maggiori.append(val)

print(f"La media è: {avg}")
print(f"I valori sopra o uguali alla media sono: {maggiori}")
print(f"I valori sotto alla media sono: {minori}")
