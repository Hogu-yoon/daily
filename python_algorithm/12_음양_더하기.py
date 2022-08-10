"""
 제목 : 음양 더하기
문제 주소 : programmers.co.kr/learn/courses/30/lessons/76501,
작성일 : 2022/04/27
"""

def solution(absolutes, signs):
    c=[]
    for i in range(len(absolutes)):
        if signs[i]:
            c.append(absolutes[i])
        else:
            c.append(-absolutes[i])

    return sum(c)