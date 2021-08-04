import itertools
import numpy as np



def judg_combinaiton(g0,g1):
    """
    input:g0,g1線形結合した結果
    output: True or False
    """
    if (g0 == g1).all == True:
        return True
    else:
        return False

def linear_combination(ele:int,matrix):
    """
    input: ele位数,matrix行列
    output: 
    """
    trace_matrix = matrix.T
    repeat_time = len(trace_matrix)
    g_0 = trace_matrix[0]
    for i in range(1,repeat_time):
        g1 = trace_matrix[i]
        for j in range(1,repeat_time):
            g2 = trace_matrix[j]
            for k in range(ele):
                g_1 = k*g1
                for l in range(ele):
                    g_2 = l*g2
                    result = (g_1 + g_2) % 4
                    print(result)
                    """
                    if judg_combinaiton(g_0,result) == True:
                        return [i,j]
                    else:
                        pass
                    """

        


#以下挙動確認用
mat = np.array([
    [1,1,1,0],
    [1,2,0,1]
])
trace_mat = mat.T 
print(linear_combination(4,mat)) 


