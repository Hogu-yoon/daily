"""
제목 : 나이순 정렬
문제 주소 : https://www.acmicpc.net/problem/10814
작성일 : 2022/08/19
"""

array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]

import sys

sys.setrecursionlimit(10 ** 6)

# 퀵솔트로 접근...
# 쪼개고 합치는 리스트
def merge_sort(array):
    # 탈출 조건
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    return merge(merge_sort(left), merge_sort(right))


def merge(array1, array2):
    # 합치는 리스트 정리
    result = []
    array_1_index = 0
    array_2_index = 0
    while array_1_index < len(array1) and array_2_index < len(array2):
        if array1[array_1_index][0] < array2[array_2_index][0]:
            result.append(array1[array_1_index])
            array_1_index += 1
        elif array1[array_1_index][0] == array2[array_2_index][0]:
            # array1[array_1_index][2] 일종의 PK
            if array1[array_1_index][1] < array2[array_2_index][1]:
                result.append(array1[array_1_index])
                array_1_index += 1
            else:
                result.append(array2[array_2_index])
                array_2_index += 1

        else:
            result.append(array2[array_2_index])
            array_2_index += 1
    if array_1_index == len(array1):
        while array_2_index < len(array2):
            result.append(array2[array_2_index])
            array_2_index += 1
    if array_2_index == len(array2):
        while array_1_index < len(array1):
            result.append(array1[array_1_index])
            array_1_index += 1

    return result


# print(merge_sort([["3", "2"],["1", "0"]]))

n = int(input())
join_list = []
join_list_2 = []

for i in range(n):
    age, name = input().split()
    join_list.append([age, name])
    join_list_2.append([age, i])

for x in merge_sort(join_list_2):
    print(int(join_list[x[1]][0]), join_list[x[1]][1], sep=" ")

"""
12
1 Junkyu
21 Dohyun
20 Sunyoung3
21 Junkyu1
21 Dohyun2
20 Sunyoung2
21 Junkyu3
21 Dohyun4
20 Sunyoung1
21 Junkyu5
21 Dohyun6
1 Sunyoung0
"""
