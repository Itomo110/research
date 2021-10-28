import itertools
from matroids.Matroid import Matroid
import numpy as np
from matroids.DependentMatroid import DependentMatroid



def judg_combinaiton(g0,g1):
    """
    input:g0,g1線形結合した結果
    output: True or False
    """
    if (g0 == g1).all:
        return True
    else:
        return False

def single(ele,matrix):
    t_matrix = matrix.T
    decoding_single_list =[]
    g0 = t_matrix[0]
    repeat = len(t_matrix)
    for i in range(1,repeat):
        g1 = t_matrix[i]
        for j in range(ele):
            g1 = (j*t_matrix[i]) % ele
            if (g0 == g1).all():
                decoding_single_list.append({i}) 
                break
    return decoding_single_list

def linear_combination(ele:int,matrix):
    """
    input: ele位数,matrix行列
    output: 
    """
    trace_matrix = matrix.T
    decoding_pair_list = []
    repeat_time = len(trace_matrix)
    g_0 = trace_matrix[0]
    for i in range(1,repeat_time):
        g1 = trace_matrix[i]
        for j in range(1,repeat_time):
            g2 = trace_matrix[j]
            for k in range(ele):
                g_1 = (k*g1) % ele
                for l in range(ele):
                    g_2 = (l*g2) % ele
                    result = (g_1 + g_2) % ele
                    if (g_0 == result).all():
                        decoding_pair_list.append({i,j})
    return decoding_pair_list

def trio_combination(ele,matrix):
    trace_matrix = matrix.T
    g0 = trace_matrix[0]
    decoding_trio_list = []
    repeat_time = len(trace_matrix)
    for i in range(1,repeat_time):
        g_1 = trace_matrix[i]
        for j in range(1,repeat_time):
            g_2 = trace_matrix[j]
            for k in range(1,repeat_time):
                g_3 = trace_matrix[k]
                for m in range(ele):
                        g1 = (m*g_1) % ele
                        for n in range(ele):
                            g2 = (n*g_2) % ele
                            for o in range(ele):
                                g3 = (o*g_3) % ele
                                result = (g1 + g2 +g3) % ele
                                if (g0 == result).all():
                                    if len({i,j,k}) == 3:
                                        decoding_trio_list.append({i,j,k})
                                    else:
                                        continue
    return decoding_trio_list

def quartet_combination(ele,matrix):
    trace_matrix = matrix.T
    g0 = trace_matrix[0]
    decoding_quartet_list = []
    repeat_time = len(trace_matrix)
    for i in range(1,repeat_time):
        g_1 = trace_matrix[i]
        for j in range(1,repeat_time):
            g_2 = trace_matrix[j]
            for k in range(1,repeat_time):
                g_3 = trace_matrix[k]
                for l in range(1,repeat_time):
                    g_4 = trace_matrix[l] 
                    for m in range(ele):
                        g1 = (m*g_1) % ele
                        for n in range(ele):
                            g2 = (n*g_2) % ele
                            for o in range(ele):
                                g3 = (o*g_3) % ele
                                for p in range(ele):
                                    g4 = (p*g_4) % ele
                                    result = (g_1 + g_2 + g_3 + g_4) % ele
                                    if (g0 == result).all():
                                        decoding_quartet_list.append([i,j,k,l])
                                    else: 
                                        continue
    return decoding_quartet_list


def quintet_combination(ele,matrix):
    trace_matrix = matrix.T
    g0 = trace_matrix[0]
    decoding_quintet_list = []
    for i in range(ele):
        g_1 = (i*trace_matrix[1]) % ele
        for j in range(ele):
            g_2 = (j*trace_matrix[2]) % ele
            for k in range(ele):
                g_3 = (k*trace_matrix[3]) % ele
                for l in range(ele):
                    g_4 = (l*trace_matrix[4]) % ele
                    for m in range(ele):
                        g_5 = (m*trace_matrix[5]) % ele
                        result = (g_1 + g_2 + g_3 + g_4 + g_5) % ele
                    if (g0 == result).all():
                        decoding_quintet_list.append({1,2,3,4,5})
                        return decoding_quintet_list
                    else:
                        continue
    

def combination_list(ele,matrix):
    sin = single(ele,matrix)
    #print("sin=",sin)
    pair = linear_combination(ele,matrix)
    #print("pair=",pair)
    trio = trio_combination(ele,matrix)
    #print("trio=",trio)
    result = sin + pair + trio
    result_list = []
    for i in range(len(result)):
        if result[i] in result_list:
            continue
        else:
            result_list.append(result[i])
    return result_list

"""
def matroido_judg1(decoding_list:list):
    max_length = 0
    index =  []
    for i in decoding_list:
        length = len(i)
        if length > max_length:
            max_length = length
    for j in decoding_list:
        if len(j) == max_length:
            index.append(j)
    print(max_length)
    set_all_pattern = []
    for k in range(1,max_length):
        for l in range(len(index)):
            pattern = list(itertools.combinations(index[l],k))
            set_all_pattern = pattern + set_all_pattern
    list_all_patern = []
    for  l in range(len(set_all_pattern)):
        list_all_patern.append(list(set_all_pattern[l]))
    print(list_all_patern)
"""
    


        

#________________________________________________________________________________________________________________________
#以下挙動確認用
mat = np.array([
    [1,1,1,0,0,0],
    [1,0,0,1,1,0],
    [0,1,1,1,0,1]
])
ma = np.array([
    [1,1,1,0],
    [1,2,1,1]
])

print(quartet_combination(2,mat))