"""
 제목 : 3진법 뒤집기
문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/68935,
작성일 : 2022/05/06
"""


def solution(n):
    answer = ''
    while n > 0:
        # 10진법을 n진법으로
        n, b = divmod(n, 3)
        answer += str(b)
    # n진법을 10진법으로 (앞에 0있어도 처리해줌)
    return int(answer, 3)
