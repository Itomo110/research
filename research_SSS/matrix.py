import numpy as np
n,k = [int(i) for i in input("n×ｋ行列のn,kを一つ空白を開けて入力してください").split()]
t = int(0)
matrix = []
f = open("log.txt","w")

def print_matrix(l, file=None):
    for li in l:
        print(",".join(map(str, li)), file=file)
    print("", file=file)

for i in range(4**8):

    for i in range(k):
        if t < k:
            row = [np.random.randint(0,4)  for s in range(n)]
            matrix.append(row)
            t += 1

        else:
            pass
    print_matrix(matrix,file = f)
    t = int(0)
    matrix =[]


    