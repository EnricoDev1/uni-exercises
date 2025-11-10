def shout(text: str):

    s = text.split("*")

    for i in range(len(s)):
        if i % 2 == 1:
            s[i] = s[i].upper()

    return ''.join(s)

def main():
    print(shout(input("Inserisci stringa: ")))

if __name__ == "__main__":
    main()