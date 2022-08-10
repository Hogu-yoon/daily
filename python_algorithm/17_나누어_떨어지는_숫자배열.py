"""
 제목 : 나누어 떨어지는 숫자배열
문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/12910,
작성일 : 2022/05/02
"""

def solution(arr, divisor):
    answer = []
    for x in arr:
        if not x % divisor:
            answer.append(x)

    if not len(answer):
        return [-1]
    answer.sort()
    return answer