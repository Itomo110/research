import numpy as np
import itertools


def make_matrix(k:int,n:int,q:int):
    ele = list(range(q))
    vec = list(itertools.product(ele, repeat = k*n))
    for i in range(len(vec)):
        matrix = np.reshape(vec[i],(k,n))
        print(matrix)


make_matrix(2,4,2)