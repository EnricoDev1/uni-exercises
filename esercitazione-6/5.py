import random

def init_mat(w, h, n):
    mat = [[0 for _ in range(h)] for _ in range(w)] 
    pos = set()

    while len(pos) < n:
        r = random.randint(0, w -1)
        c = random.randint(0, h - 1)
        pos.add((r, c))

    for r,c in pos:
        mat[r][c] = 1 

    return mat

def save_mat(mat, w, h):
    buf = ""
    for i in range(w):
        for j in range(h):
            buf += str(mat[i][j]) + ("," if j != h - 1 else "")
        buf += '\n'
    open("output.csv", "w").write(buf)

def main():
    w,h,n = map(int, input("Inserisci w,h,n: ").split(","))
    mat = init_mat(w, h, n)
    
    for riga in mat:
        print(riga)
    save_mat(mat, w, h)
    
    while True:
        x,y = map(int, input("Inserire x,y: ").split(","))
        count = 0

        if mat[x][y] == 1:
            print("1 presente")
        else:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < w and 0 <= ny < h:
                        if mat[nx][ny] == 1 and (nx == x and ny == y):
                            count += 1
            print(f"Ci sono {count} 1 attorno")
if __name__ == "__main__":
    main()

