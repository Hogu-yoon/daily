"""
 제목 : 실패율
문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/42889,
작성일 : 2022/04/29
"""


def solution(N, stages):
    bean_list = []
    bean_list_2 = []
    bean_list_3 = []
    bean_list_4 = []
    bean_list_5 = []
    for x in range(1, N + 1 + 1):
        bean_list.append(stages.count(x))

    for i in range(N):
        bean_list_2.append(sum(bean_list[i:]))
        try:
            bean_list_3.append(bean_list[i] / bean_list_2[i])
        except ZeroDivisionError:
            bean_list_3.append(0)

    for i in enumerate(bean_list_3):
        bean_list_4.append(i)

    bean_list_4.sort(key=lambda x: -x[1])

    for i in bean_list_4:
        bean_list_5.append(i[0] + 1)
    return bean_list_5