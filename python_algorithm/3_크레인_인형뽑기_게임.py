"""
 제목 : 크레인 인형뽑기 게임
문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/64061,
작성일 : 2022/04/21
"""


def solution(board, moves):
    y_field = len(board)
    x_field = len(board[0])
    result_list = []
    answer = 0
    for move in moves:
        if len(result_list) > 1 and result_list[-1] == result_list[-2]:
            result_list.pop()
            result_list.pop()
            answer += 2
        for x in range(x_field):
            if x == move - 1:
                for y in range(y_field):
                    num = board[y][x]
                    if num != 0:
                        result_list.append(num)
                        board[y][x] = 0
                        break

    return answer