import numpy as np


def is_equal(vec1,vec2):
    for i in range(2):
        if vec1[i] != vec2[i]:
            return False
    return True


def linear_combination(g1,g2):
    for m in range(4):
        g_1 = m*g1
        for n in range(4):
            g_2 = n*g2
            linear_combination_g = (g_1 + g_2)%4
            if is_equal(g_0,linear_combination_g) == True:
                party_pattern.append([i+1,j+1])


def change_matrix(row1:list,row2:list):
    matrix = np.array([row1,row2])
    trace_matrix = matrix.T
    g_0 = trace_matrix[0]
    ele_matrix = trace_matrix[1:]
    for i in range(2):                       #二人組判定
        g_i = ele_matrix[i]
        for j in range(i+1,3):
            g_j = ele_matrix[j]
            linear_combination(g_i,g_j)
    return  party_pattern
party_pattern=[]
print(change_matrix([1,1,1,0],[1,2,0,1]))


"""
def judg_one(row3:list,row4:list):
    change_matrix(row3,row4)
    for h in range(3):                      #一人用判定
        single_g = ele_matrix[h]
        if is_equal(g_0,single_g) == True:
            party_pattern.append(h+1) 

judg_one([0,1,2,3,4],[1,2,3,4,5])"""
    

