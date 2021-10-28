import matroid_judge as mj
from matroids.Matroid import Matroid
from matroids.DependentMatroid import DependentMatroid
import matroids
import numpy as np
import itertools

def field_check_matroid(ele:int): #(ele:int,rows:int,lines:int)
    """
    input ele:元の数,(rows:k(行数),lines:n(列数))
    output matrix
    """
    with open("result.txt","w") as z:
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
                                        for j in range(ele):
                                            matrix_ele_list[8] = j
                                            for k in range(ele):
                                                matrix_ele_list[9] = k
                                                for l in range(ele):
                                                    matrix_ele_list[10] = l
                                                    for m in range(ele):
                                                        matrix_ele_list[11] = m
                                                        for n in range(ele):
                                                            matrix_ele_list[12] = n
                                                            for o in range(ele):
                                                                matrix_ele_list[13] = o
                                                                for p in range(ele):
                                                                    matrix_ele_list[13] = p
                                                                    for q in range(ele):
                                                                        matrix_ele_list[14] = q
                                                                        for r in range(ele):
                                                                            matrix_ele_list[15] = r
                                                                            for s in range(ele):
                                                                                matrix_ele_list[16] = s
                                                                                for t in range(ele):
                                                                                    matrix_ele_list[17] = t
                                                                                    matrix = np.array(np.array_split(matrix_ele_list,3))    
                                                                                    D = mj.combination_list(ele,matrix)
                                                                                    E = {1,2,3,4,5}
                                                                                    try:
                                                                                        result = DependentMatroid((E,D))
                                                                                    except matroids.core.exception.MatroidAxiomError:
                                                                                        print(matrix,file = z)
                                                                                    continue                           
#######################################################################################################################################
field_check_matroid(4)
