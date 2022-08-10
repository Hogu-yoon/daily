"""
 제목 : 없는 숫자 더하기
문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/86051,
작성일 : 2022/04/25
"""


def solution(n):
    if n % 2 == 0:
        num = n/2
        result = "수박" * int(num)
    else:
        num = n / 2
        result = "수박" * int(num) + '수'
    return result