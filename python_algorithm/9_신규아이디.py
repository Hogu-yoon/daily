"""
 제목 : 신규아이디
문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/72410,
작성일 : 2022/04/26
"""

import re

def solution(id):
    id = id.lower()
    id = re.sub('[^a-z0-9_.-]', '', id)
    id = id.replace('......', '.').replace('.....', '.').replace('....', '.').replace('...', '.').replace('..', '.')
    id = id.strip('.')
    if not id:
        id = 'a'
    elif len(id) >= 16:
        id = id[:15]
        id = id.strip('.')
    if len(id) == 2:
        id = id + id[-1]
    elif len(id) == 1:
        id = id + (id[-1]*2)

    return(id)