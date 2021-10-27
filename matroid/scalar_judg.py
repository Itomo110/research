import numpy as np


def scalar(ex_matrix):
    trace_matrix = ex_matrix.T
    print(trace_matrix)
    row_num = len(trace_matrix)
    print(row_num)
    



####################################################################################################################

matrix_a = np.array(
    [1,0,0,1],
    [0,1,1,1]
)

matrix_b = np.array(
    [1,0,1,1],
    [0,1,2,3]
)

scalar(matrix_a)