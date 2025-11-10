def select_chars(text: list):
    buf = ""
    for i in range(0, len(text)):
        if not (text[i] < text[i-1] or text[i] < text[i+1]):
            buf += text[i]
    return buf

def main():
    print(select_chars(list("testo di prova")))

if __name__ == "__main__":
    main()