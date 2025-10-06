from string import ascii_lowercase, ascii_uppercase

alphabet = ascii_lowercase + ascii_uppercase

def all_apha(predicato: str) -> bool:
    for c in predicato:
        if c not in alphabet:
            return False  
    return True  

text = input("Inserisci una riga di testo: ")
print("Il testo contiene solo caratteri dell'alfabeto" if all_apha(text) else "Il testo non contiene solo caratteri dell'alfabeto")