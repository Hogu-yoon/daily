"""
 제목 : 폰켓몬
문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/1845,
작성일 : 2022/05/10
"""

def solution(nums):
    max = int(len(nums)/2)
    min = len(set(nums))
    if max <= min:
        return max

    answer = min
    return answer