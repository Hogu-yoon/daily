"""
 제목 : k번째 수
문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/42748,
작성일 : 2022/04/20
"""

def solution_2(array_2 , commands_2):
    i = commands_2[0]
    j = commands_2[1]
    k = commands_2[2]
    array_2 = array_2[i - 1:j]
    array_2.sort()
    return array_2[k-1]

def solution(array, commands):
    ori = []
    for x in range(len(commands)):
        ori.append(solution_2(array,commands[x]))
    return ori