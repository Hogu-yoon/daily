"""
 제목 : 하샤드 수
문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/12947,
작성일 : 2022/05/03
"""

def solution(x):
    str_x = str(x)
    str_x = list(str_x)
    int_x = map(int,str_x)
    if x % sum(list(int_x)) == 0:
        return True
    else:
        return False