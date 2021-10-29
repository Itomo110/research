from itertools import combinations, product
from matroids.Matroid import Matroid
from matroids.DependentMatroid import DependentMatroid
import matroids

import numpy as np


def PG(r: int) -> list[list[int]]:
    '''
    PG(r, 2) の点集合を持ってくる
    '''
    arrays = list(product(range(2), repeat=r+1))[1:] 
    return list(map(lambda arr: np.array(arr), arrays))


def is_accessible(key_point: list[int], points: list[list[int]]) -> bool:
    '''
    点集合(points)が key_point にアクセス可能かどうか判定する
    '''
    n = len(points)
    k = len(points[0])

    for num_of_points in range(1, n+1): # 1 ~ n
        for ps in combinations(points, r=num_of_points):
            point = sum(ps) % 2
            if (point == key_point).all():
                return True

    return False


def find_inaccessible_labels(key_point: list[int], points: list[list[int]]) -> list[set[int]]:
    '''
    点集合(points)からキーの点(key_point)にアクセス不可能なラベルを取得する
    '''
    n = len(points)
    k = len(points[0])
    result = [set()]

    for num_of_points in range(1, n+1): # 1 ~ n
        for pis in combinations(range(n), r=num_of_points):
            ps = list(map(lambda i: points[i], pis))
            if not is_accessible(key_point, ps):
                result.append({i+1 for i in pis})
    
    return result


def find_non_matroids(n: int, k: int, out = None):
    '''
    長さ n、次数 k のアクセス構造がマトロイドにならない点集合を求める
    out はファイル出力であればそいつを入れる。
    '''
    all_points = PG(k-1)
    key_point, other_points = all_points[0], all_points[1:]

    for points in combinations(other_points, r=n-1):
        ground_set = {i for i in range(1, n)}
        independent_set = find_inaccessible_labels(key_point, points)
        try:
            result = matroids.IndependentMatroid((ground_set, independent_set))
        except matroids.core.exception.MatroidAxiomError:
            print(np.array([key_point] + list(points)).T, file = out)
            print(independent_set, file = out)
            continue



if __name__ == '__main__':
    k = 5
    for n in range(k, 2**k - 1):
        with open(f"k{k}/n{n}.txt", "w") as f:
            find_non_matroids(n, k, f)

    # find_non_matroids(6, 4)
    # key_point = np.array([1, 0, 0])
    # points = [np.array([0, 1, 0]), np.array([0, 0, 1]), np.array([0, 1, 1]), np.array([1, 0, 1])]
    # print(find_accessible_labels(key_point, points))