"""
 제목 : 같은 숫자는 싫어
문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/12906,
작성일 : 2022/04/29
"""


def solution(arr):
    bean_list = []
    checknum = -1

    for i in arr:

        if checknum != i:
            checknum = i
            bean_list.append(i)
    return bean_list