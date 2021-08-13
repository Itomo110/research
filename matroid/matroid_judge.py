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
                g_1 = k*g1
                for l in range(ele):
                    g_2 = l*g2
                    result = (g_1 + g_2) % 4
                    if (g_0 == result).all():
                        decoding_pair_list.append({i,j})
    return decoding_pair_list

def trio_combination(ele,matrix):
    trace_matrix = matrix.T
    g0 = trace_matrix[0]   
    for i in range(ele):
        g_1 = i*trace_matrix[1]
        for j in range(ele):
            g_2 = j*trace_matrix[2]
            for k in range(ele):
                g_3 = k*trace_matrix[3]
                result = g_1 + g_2 + g_3
                if (g0 == result).all():
                    return[{1,2,3}]

def combination_list(ele,matrix):
    sin = single(ele,matrix)
    pair = linear_combination(ele,matrix)
    trio = trio_combination(ele,matrix)
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
    [1,1,1,0],
    [1,2,0,1]
])
ma = np.array([
    [1,1,1,0],
    [1,2,1,1]
])
trace_mat = mat.T 
list1 =  [[1, 3], [2, 3], [1, 2, 3]] 
E = {1,2,3}
D = combination_list(4,mat)
matroid = DependentMatroid((E,D))
print(matroid)
"""
print(combination_list(4,mat))
E = {1,2,3}
D = [{1,3},{2,3},{1,2,3}]
matroid = DependentMatroid((E,D))
print(Matroid)
#matroido_judg1(list1)

E = {1,2,3}
I = [set(),{1},{2},{3},{1,2},{2,3}]
matroid = IndependentMatroid((E,I))
print(Matroid)
print(linear_combination(4,mat))
print(single(4,mat))
print(trio_combination(4,mat))
result = single(4,mat)+linear_combination(4,mat)+trio_combination(4,mat)
print(result)
result_list = []
for i in range(len(result)):
    if set(result[i]) in result_list:
        continue
    else:
        result_list.append(set(result[i]))
print(result_list)

list1 =  [[1, 3], [2, 3], [1, 2, 3]]      
n_list1 = [str(i) for i in list1]
list2 = [[0],[1],[2],[3],[1,2],[1, 3], [2, 3],[1, 2, 3]] 
#list2 = [[1, 3], [2, 3], [3, 1], [3, 2]]
n_list2 = [str(i) for i in list2]
n_list3 = list(set(n_list2) -set(n_list1))
list3 = []
for i in range(len(n_list3)):
    list3.append(n_list3[i])
print(list3)
"""