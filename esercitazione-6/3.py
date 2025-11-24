def find_max(lst):
    max = ""
    for el in lst:
        if isinstance(el, list):
            buf = find_max(el)
        else:
            buf = el
        if buf > max:
            max = buf
    return max

def main():
    print(find_max(["a","b",["av", "Cindy","Ann"],"caiawdijiajwi","aaaaaaaaaaaaaaaaaaa"]))
if __name__ == "__main__":
    main()