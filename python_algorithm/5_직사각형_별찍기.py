"""
 제목 : 직사각형 별찍기
문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/77884,
작성일 : 2022/04/22
"""

a, b = map(int, input().strip().split(' '))
for _ in range(b):
    for _ in range(a):
        print("*", end="")
    print()