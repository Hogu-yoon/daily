"""
 제목 : 완주하지 못한 선수
문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/42576,
작성일 : 2022/04/22
"""

def solution(participant, completion):
    participant.sort()
    completion.sort()


    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[-1]