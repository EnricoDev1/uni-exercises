import re

def main():
    content = open("lib/g2d.py", "r").read()
    content = re.split(r"\s+", content)
    occ = {word: 0 for word in content}

    for word in content:
        occ[word] += 1

    for word in occ:
        print(f"\"{word}\" appare {occ[word]} volte")
    print("--------------------------------------------------------")    
    vals = sorted(occ.items(), key=lambda x: x[1], reverse=True)[:10]
    for val in vals:
        print(f"{val[0]} - {val[1]}")

if __name__ == "__main__":
    main()