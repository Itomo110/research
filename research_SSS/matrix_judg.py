import numpy as np
import itertools as it



"""
def change_matrix(row1:list,row2:list):
    matrix = np.array([row1,row2])
    trace_matrix = matrix.T
    g_0 = trace_matrix[0]
    return g_0
    

def share(t_matrix):
    ele_matrix = t_matrix[1:]
    return ele_matrix
"""


def full_party_pattern(n:int):
    index = list(range(1,n))
    full_party = []



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


def trio_linear_combination(g3,g4,g5):
    for o in range(4):
        g_3 = o*g3
        for p in range(4):
            g_4 = p*g4
            for q in range(4):
                g_5 = q*g5
                trio_linear_combination_g = (g_3 + g_4 + g_5) % 4
                if is_equal(g_0, trio_linear_combination_g) == True:
                    break
    party_pattern.append([1,2,3])
                    



matrix = np.array([
[1,1,1,0],
[1,2,0,1]
])



party_pattern = []
trace_matrix = matrix.T
g_0 = trace_matrix[0]
ele_matrix = trace_matrix[1:]
"""change_matrix([1,1,1,0],[1,2,0,1])
share(trace_matrix)
party_pattern = []"""

#print(ele_matrix[0]+ ele_matrix[1])
#print(ele_matrix[1])
#linear_combination(ele_matrix[0],ele_matrix[1])


for h in range(3):                      #一人用判定
    single_g = ele_matrix[h]
    if is_equal(g_0,single_g) == True:
        party_pattern.append(h+1) 
    
    



for i in range(2):                       #二人組判定
    g_i = ele_matrix[i]
    for j in range(i+1,3):
        g_j = ele_matrix[j]
        linear_combination(g_i,g_j)
        

trio_linear_combination(ele_matrix[0],ele_matrix[1],ele_matrix[2])  #三人組判定
print(party_pattern)

