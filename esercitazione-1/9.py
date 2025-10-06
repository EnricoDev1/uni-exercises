def count_groups(text: str) -> tuple:
    text = text.lower()
    c1 = c2 = 0
    for c in text:
        if "a" <= c <= "m":   
            c1 += 1
        elif "n" <= c <= "z":
            c2 += 1

    return (c1, c2)

while True:
    text = input("Inserisci un testo: ")
    if len(text) > 0:
        counts = count_groups(text)
        print(f"Gruppo [A-M]: {counts[0]}\nGruppo [N-Z]: {counts[1]}")
    else:
        break