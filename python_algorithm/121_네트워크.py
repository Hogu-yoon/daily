"""
제목 : 게임 맵 최단거리
문제 주소 : https://school.programmers.co.kr/learn/courses/30/lessons/1844
작성일 : 2022/08/30
"""

"""
문제 설명
네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

제한사항
컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
computer[i][i]는 항상 1입니다.
입출력 예
n	computers	return
3	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	2
3	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	1
"""

n = 3
computers = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]

from collections import deque


def solution_1(n, computers):
    answer = 0
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                computers[i][j] = 2
                answer += 1
                # start_node = [x,y]
                bfs_queue(n, computers, start_node=[j, i])
    return answer


def bfs_queue(n, computers, start_node=None):
    if start_node is None:
        start_node = [0, 0]

    queue = deque([start_node])

    while queue:
        print(*computers, sep="\n")
        print()
        x, y = queue.popleft()
        dir_x = [-1, 1, 0, 0]
        dir_y = [0, 0, -1, 1]
        for i in range(4):
            now_x = x + dir_x[i]
            now_y = y + dir_y[i]
            # 범위 지정(전체 크기)
            if 0 <= now_x < n and 0 <= now_y < n:
                if computers[now_y][now_x] == 1:
                    computers[now_y][now_x] = 2
                    queue.append([now_x, now_y])


# print(*computers, sep="\n")



def bfs_queue(list_a,visited, start_node=0):
    queue = deque()
    queue.append(start_node)
    while queue:
        idx = queue.popleft()
        for t in list_a[idx]:
            if t not in visited:
                visited.append(t)
                queue.append(t)

def solution(n, computers):
    list_a = [[] for _ in range(n)]
    for j in range(n):
        for i in range(len(computers[j])):
            if computers[j][i] == 1:
                list_a[j].append(i)
    # print(solution(n, computers))
    # print(*list_a,sep="\n")
    visited = []
    cnt = 0
    for i in range(n):
        if i not in visited:
            bfs_queue(list_a,visited,start_node = i)
            cnt += 1

    return cnt

print(solution(n, computers))