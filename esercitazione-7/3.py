from random import randint, seed
seed(1)
def main():
    w,h = map(int,input("inserisci w e h").split(","))
    mat = [[0 for _ in range(h)] for _ in range(w)]
    for i in range(w):
        for j in range(h):
            mat[i][j] = randint(0,3)
            print(f"{mat[i][j]} ", end="")
        print()
    buff = [i for i in range(10)]
    flag = False
    for val in buff:
        for i in range(h):
            flag = False
            for j in range(w):
                 if mat[j][i] == val:
                    flag = True
                    break
            if not flag:
                break
        if flag:
            print(f"{val} valore presente in ogni colonna")
            
if __name__ == "__main__":
    main()