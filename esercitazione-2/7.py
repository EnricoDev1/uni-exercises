s = input("Inserisci una stringa: ")

cont = [0, 0]

for c in s:
    if c.lower() == c:
        cont[ord(c) % 2] += 1

print(f"Pari: {cont[0]}\nDispari: {cont[1]}")