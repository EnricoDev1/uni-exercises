from random import randint

def main():
    w, h = map(int, input("Insersici w,h: ").split(","))
    occ = []
    mat = [[0 for _ in range(h)] for _ in range(w)]

    buf = ""
    for i in range(w):
        for j in range(h):
            while (num := randint(1, w*h)) in occ:
                pass
            mat[i][j] = num 
            occ.append(num)
            buf += str(mat[i][j]) + ("," if j != h-1 else "\n")

    with open("lib/1.csv", "w") as f:
        f.write(buf)

if __name__ == "__main__":
    main()