import numpy as np
import itertools
import logging


def make_matrix(ele:int): #(ele:int,rows:int,lines:int)
    """
    input ele:元の数,(rows:k(行数),lines:n(列数))
    output matrix
    """
    matrix_ele_list = []
    for i in range(2*4): # range(rows*lines)
        matrix_ele_list.append(0)
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

def main():
    list1 = [1,2,3,4,"愛",6,7,8,9,10]
    for i in list1:
        try:
            practice = int(i)
            print(practice)
        except ValueError:
            continue
            print(f"{i}は数字ではありません")
            

    """
    print("Z_m上のk×ｎ行列のmとkとnに代入したい値を半角区切りで打ち込んでください")
    m,k,n = [int(i) for i in input().split()]
    print(f"Z_{m}上の{k} × {n}行列を表示します",)
    for perms in itertools.permutations(range(m),n):
        mat = []
        for rows in itertools.combinations(perms,k):
            mat.append(rows)
        print(mat)
    """
if __name__ == "__main__":
    main()

