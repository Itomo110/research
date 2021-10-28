import numpy as np
import itertools

def single_combination(ele,matrix) -> list:
    """
    input: ele->位数, matrix->行列
    output: list(set)
    """
    single_result_list = []
    trace_matrix = matrix.T
    g0 = trace_matrix[0]
    for i in range(1,len(trace_matrix)):
        for j in range(ele): 
            g1 = j*trace_matrix[i] % ele
            if (g0 == g1).all():
                single_result_list.append({i})
            else:
                continue
    return single_result_list


def pair_combination(ele,matrix) -> list:
    """
    input: ele->位数, matrix->行列
    output: list(set)
    """
    pair_result_list = []
    trace_matrix = matrix.T
    g0 = trace_matrix[0]
    for i in range(1, len(trace_matrix)):
        for j in range(ele):
            for k in range(1,len(trace_matrix)):
                for l in range(ele):
                    g1 = j*trace_matrix[i]
                    g2 = l*trace_matrix[k]
                    result = (g1 + g2) % ele
                    if (g0 == result).all():
                        if len({i,k}) == int(2):
                            pair_result_list.append({i,k})
                    else: 
                        continue
    return pair_result_list


def trio_combination(ele,matrix) -> list:
    """
    input: ele->位数, matrix->行列
    output: list(set)
    """
    trio_result_list = []
    trace_matrix = matrix.T
    g0 = trace_matrix[0]
    for i in range(1, len(trace_matrix)):
        for j in range(ele):
            for k in range(1,len(trace_matrix)):
                for l in range(ele):
                    for m in range(1, len(trace_matrix)):
                        for n in range(ele):
                            g1 = j*trace_matrix[i]
                            g2 = l*trace_matrix[k]
                            g3 = n*trace_matrix[m]
                            result = (g1 + g2 + g3) % ele
                            if (g0 == result).all():
                                if len({i,k,m}) == int(3):
                                    trio_result_list.append({i,k,m})
                            else:
                                continue
    return trio_result_list


def quartet_combination(ele,matrix)-> list:
    """
    input: ele->位数, matrix->行列
    output: list(set)
    """
    quartet_result_list = []
    trace_matrix = matrix.T
    g0 = trace_matrix[0]
    for i in range(1, len(trace_matrix)):
        for j in range(ele):
            for k in range(1,len(trace_matrix)):
                for l in range(ele):
                    for m in range(1, len(trace_matrix)):
                        for n in range(ele):
                            for o in range(1,len(trace_matrix)):
                                for p in range(ele):
                                    g1 = j*trace_matrix[i]
                                    g2 = l*trace_matrix[k]
                                    g3 = n*trace_matrix[m]
                                    g4 = p*trace_matrix[o]
                                    result = (g1 + g2 + g3 + g4)% ele
                                    if (g0 == result).all():
                                        if len({i,k,m,o}) == int(4):
                                            quartet_result_list.append({i,k,m,o})
    return quartet_result_list

def quintet_combination(ele,matrix) -> list:
    quintet_result_list = []
    trace_matrix = matrix.T
    g0 = trace_matrix[0]
    for i in range(1, len(trace_matrix)):
        for j in range(ele):
            for k in range(1,len(trace_matrix)):
                for l in range(ele):
                    for m in range(1, len(trace_matrix)):
                        for n in range(ele):
                            for o in range(1,len(trace_matrix)):
                                for p in range(ele):
                                    for q in range(1,len(trace_matrix)):
                                        for r in range(ele):
                                            g1 = j*trace_matrix[i]
                                            g2 = l*trace_matrix[k]
                                            g3 = n*trace_matrix[m]
                                            g4 = p*trace_matrix[o]
                                            g5 = r*trace_matrix[q]
                                            result = (g1 + g2 + g3 + g4 + g5) % ele
                                            if (g0 == result).all():
                                                if len({i,k,m,o,q}) == int(5):
                                                    quintet_result_list.append({i,k,m,o,q})
    return quintet_result_list


def sextet_combinaiton(ele,matrix) -> list:
    sextet_result_list =[]
    trace_matrix = matrix.T
    g0 = trace_matrix[0]
    for i in range(1, len(trace_matrix)):
        for j in range(ele):
            for k in range(1,len(trace_matrix)):
                for l in range(ele):
                    for m in range(1, len(trace_matrix)):
                        for n in range(ele):
                            for o in range(1,len(trace_matrix)):
                                for p in range(ele):
                                    for q in range(1,len(trace_matrix)):
                                        for r in range(ele):
                                            for s in range(1, len(trace_matrix)):
                                                for t in range(ele):
                                                    g1 = j*trace_matrix[i]
                                                    g2 = l*trace_matrix[k]
                                                    g3 = n*trace_matrix[m]
                                                    g4 = p*trace_matrix[o]
                                                    g5 = r*trace_matrix[q]
                                                    g6 = t*trace_matrix[s]
                                                    result = (g1 + g2 + g3 + g4 + g5 + g6) % ele
                                                    if (g0 == result).all():
                                                        sextet_result_list.append({i,k,m,o,q,s})
    return sextet_result_list

def combination_list(ele,matrix)->list:
    sin = single_combination(ele,matrix)
    pair = pair_combination(ele,matrix)
    trio = trio_combination(ele,matrix)
    quartet = quartet_combination(ele,matrix)
    quintet = quintet_combination(ele,matrix)
    total = sin + pair + trio + quartet + quintet
    total_list = []
    for i in range(len(total)):
        if total[i] in total_list:
            continue
        else: 
            total_list.append(total[i])
    return total_list
                                                        

                                            





#########################################################################################
#動作確認用テスト
matrix1= np.array([
    [1,0,0,1,0,1],
    [1,1,1,0,1,0],
    [0,1,1,0,1,1]
])

matrix2= np.array([
    [1,0,0,1,0,1],
    [1,1,1,0,1,0],
    [0,1,1,0,1,1]
])

