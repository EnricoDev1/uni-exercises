anno = int(input("Inserisci anno di nascita: "))

print("era l'anno del drago" if (anno - 2024) % 12 == 0 else "non era l'anno del drago")