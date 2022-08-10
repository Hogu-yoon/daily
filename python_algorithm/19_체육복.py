"""
 제목 : 체육복
문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/42862,
작성일 : 2022/05/03
"""

def num_size(n, m):
    if n == m + 1 or n == m - 1 or n == m:
        return True
    else:
        return False


def solution(n, lost, reserve):
    new_lost = list(set(lost)-set(reserve))
    new_reserve = list(set(reserve)-set(lost))
    for re in new_reserve:
        for lo in new_lost:
            if num_size(lo, re):
                new_lost.remove(lo)
                break
    return n - len(new_lost)