import numpy as np
import time



def make_matrix(ele:int): #(ele:int,rows:int,lines:int)
    """
    input ele:元の数,(rows:k(行数),lines:n(列数))
    output matrix
    """
    matrix_ele_list = []
    for i in range(2*4): # range(rows*lines)
        matrix_ele_list.append(0)
    t1 = time.time()
    for a in range(ele):
        matrix_ele_list[0] = a
        for b in range(ele):
            matrix_ele_list[1] = b
            for c in range(ele):
                matrix_ele_list[2] = c
                for d in range(ele):
                    matrix_ele_list[3] = d
                    for e in range(ele):
                        matrix_ele_list[4] = e
                        for f in range(ele):
                            matrix_ele_list[5] = f
                            for g in range(ele):
                                matrix_ele_list[6] = g
                                for h in range(ele):
                                    matrix_ele_list[7] = h
                                    matrix = np.array(np.array_split(matrix_ele_list,2))
                                    print(matrix)
    t2 = time.time()
    times = t2 - t1
    print(times)

def main():
    """
    print("Z_m上のk×ｎ行列のmとkとnに代入したい値を半角区切りで打ち込んでください")
    m,k,n = [int(i) for i in input().split()]
    print(f"Z_{m}上の{k} × {n}行列を表示します",)
    """
    make_matrix(4)
if __name__ == "__main__":
    main()

