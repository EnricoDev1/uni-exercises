def clamp(vals, max):
    for i, v in enumerate(vals):
        if v > max:
            vals[i] = max

    return vals 

def main():
    vals = []
    max = float(input("Inserisci il numero massimo: "))
    while True:
        if (val := float(input("Inserisci elemento: "))) > 0:
            vals.append(val)
        else:
            break
    
    print(clamp(vals, max))

if __name__ == "__main__":
    main()