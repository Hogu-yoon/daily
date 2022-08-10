"""
 제목 : 신고결과받기
문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/92334,
작성일 : 2022/04/21
"""

from collections import defaultdict


def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = set(report)
    cnt = defaultdict(int)
    user = defaultdict(set)
    i = 0
    for r in report:
        x, y = r.split()
        user[x].add(y)
        cnt[y] += 1

    for id in id_list:
        result = 0

        for u in user[id]:
            if cnt[u] >= k:
                result += 1
        answer[i] = result
        i += 1

    return answer