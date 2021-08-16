import matroid_judge as mj
from matroids.Matroid import Matroid
from matroids.DependentMatroid import DependentMatroid
import numpy as np
import itertools



def check_matroid(ele:int): #(ele:int,rows:int,lines:int)
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
                                    D = mj.combination_list(ele,matrix)
                                    E = {1,2,3}
                                    try:
                                        result = DependentMatroid((E,D))
                                        print(result)
                                    except DependentMatroid.MatroidAxiomError:
                                        print(matrix)
                                        continue                           
                                        

#######################################################################################################################################
check_matroid(4)