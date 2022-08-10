"""
 제목 : 최대공약수와 최소공배수
문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/12940,
작성일 : 2022/05/02
"""

import math


def solution(n, m):
    answer = []
    max_num = math.gcd(n, m)
    answer.append(max_num)
    # answer.append(math.lcm(n, m))
    answer.append(n*m//max_num)


    return answer