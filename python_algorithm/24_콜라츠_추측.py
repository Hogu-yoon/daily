"""
 제목 : 콜라츠 추측
문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/12943,
작성일 : 2022/05/09
"""
cnt = 1
def solution(num):
    global cnt
    if num == 1:
        return 0
    if not num % 2:
        num = num / 2
    else:
        num = num * 3 + 1
    if num == 1:
        return cnt
    else:
        cnt += 1
        if cnt == 490:
            return -1
        return solution(num)