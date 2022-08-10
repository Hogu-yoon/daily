"""
 제목 : 시저암호
문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/12926,
작성일 : 2022/05/04
"""

def solution(s, n):
    a_list = list(map(ord, s))
    for i in range(len(a_list)):
        a_num = a_list[i]
        if a_num != 32:
            if 97<= a_num <=122:
                a_list[i] += n
                a_plus_num = a_list[i]
                if a_plus_num > 122:
                    a_list[i] = a_plus_num -26
            elif 65<= a_num <=90:
                a_list[i] += n
                a_plus_num = a_list[i]
                if a_plus_num > 90:
                    a_list[i] = a_plus_num -26
    b_list = list(map(chr, a_list))
    answer = ""
    for b in b_list:
        answer += b
    return answer