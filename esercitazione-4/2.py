def len_common_prefix(str1, str2):
    for i in range(c := min(len(str1), len(str2))):
        if str1[i] != str2[i]:
            return i

    return c

def main():
    print(len_common_prefix(input("Inserisci stringa: "), input("Inserisci stringa: ")))

if __name__ == "__main__":
    main()