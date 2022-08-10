"""
 제목 : 윤년
문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/12901,
작성일 : 2022/05/09
"""
def solution(a, b):
#마술넘버 ㅇㅇ
    secrets_num = [4,0,1,4,6,2,4,0,3,5,1,3]
    mon = a - 1
    day = (secrets_num[mon]+b) % 7
    answer = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    return answer[day]