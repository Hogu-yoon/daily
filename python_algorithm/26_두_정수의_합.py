"""
 제목 : 두 정수의 합
문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/12912,
작성일 : 2022/05/10
"""

def solution(a, b):
    x = 0
    if a == b:
        return a
    elif a > b:
        min = b
        max = a
    else:
        min = a
        max = b
    for i in range(min,max+1):
        x += i
    answer = x
    return answer