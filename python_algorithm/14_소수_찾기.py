"""
 제목 : 소수 찾기
문제 주소 : programmers.co.kr/learn/courses/30/lessons/42839,
작성일 : 2022/04/28
"""
import itertools


def is_prime_num(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    test_list = list(numbers)
    num_list = is_permutations(test_list)

    for num in set(num_list):
        # print("num = ",num)
        if is_prime_num(num) and num != 0 and num != 1:
            answer += 1

    return answer


def is_permutations(nums):
    num_list = []
    for i in range(1,len(nums)+1):
        result = list(itertools.permutations(nums, i))
        for a in result:
            num_list.append(int(''.join(a)))

    return num_list