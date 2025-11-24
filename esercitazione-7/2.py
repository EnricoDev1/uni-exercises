from random import randint

def main():
    mat = list()
    lines = open("lib/1.csv", "r").readlines()
    for row in lines:
        mat.append([int(val.strip()) for val in row.split(",")])
    maxx = [0 for _ in range(len(mat[0]))]
    minn = [mat[0][i] for i in range(len(mat[0]))]

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] > maxx[j]:
                maxx[j] = mat[i][j]
            if mat[i][j] < minn[j]:
                minn[j] = mat[i][j]

    for i in range(len(mat[0])):
        print(f"Il massimo della colonna {i} è: {maxx[i]}")
        print(f"Il minimo  della colonna {i} è: {minn[i]}")
    
    buf = ""
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j] = round((mat[i][j] - minn[j]) / (maxx[j] - minn[j]), 2)
            buf += str(mat[i][j]) + ("," if j != len(mat[0])-1 else "\n")
    
    open("lib/2.csv", "w").write(buf)

if __name__ == "__main__":
    main()