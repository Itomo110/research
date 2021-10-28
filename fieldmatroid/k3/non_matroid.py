import linear_combination as lic
from matroids.Matroid import Matroid
from matroids.DependentMatroid import DependentMatroid
import matroids
import numpy as np
import itertools

def matroid_chaeck(k,n,q):
    """
    input:k:列数,n:行数,q:位数(素数)
    """
    with open("result1.txt","w") as z:
        row0 = np.array([0,0,0,0,0,0])
        col0 = np.array([0,0,0])
        ele = list(range(q))
        vec = list(itertools.product(ele, repeat = k*n))
        for i in range(len(vec)):
            matrix = np.reshape(vec[i],(k,n))
            t_matrix = matrix.T
            flg = False
            for j in range(k):
                if (matrix[j] == row0).all():
                    flg = True
                    break

            for l in range(n):
                if (t_matrix[l] == col0).all():
                    flg = True
                    break
            
            if flg:
                continue

            D = lic.combination_list(q,matrix)
            E = set(range(1,n+1))
            try:
                result = DependentMatroid((E,D))
            except matroids.core.exception.MatroidAxiomError:
                print(matrix,file = z)
                continue
                

#######################################################################################3
matroid_chaeck(3,6,2)


    