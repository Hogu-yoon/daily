"""
 제목 : 약수의 개수와 덧셈
문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/77884,
작성일 : 2022/04/27
"""

def test(x):
    cnt = 1
    d = 1
    while d <= x:
        d += 1
        if x % d == 0:
            cnt += 1
    if cnt % 2 == 0:
        return True
    else:
        return False


def solution(left, right):
    bean_list = []
    for x in range(left, right + 1):
        if test(x):
            bean_list.append(x)
        else:
            bean_list.append(-x)
    return sum(bean_list)