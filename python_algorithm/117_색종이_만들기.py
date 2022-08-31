"""
제목 : 색종이 만들기
문제 주소 : https://www.acmicpc.net/problem/2630
작성일 : 2022/08/25
"""

"""
입력
첫째 줄에는 전체 종이의 한 변의 길이 N이 주어져 있다. N은 2, 4, 8, 16, 32, 64, 128 중 하나이다. 색종이의 각 가로줄의 정사각형칸들의 색이 윗줄부터 차례로 둘째 줄부터 마지막 줄까지 주어진다. 하얀색으로 칠해진 칸은 0, 파란색으로 칠해진 칸은 1로 주어지며, 각 숫자 사이에는 빈칸이 하나씩 있다.

출력
첫째 줄에는 잘라진 햐얀색 색종이의 개수를 출력하고, 둘째 줄에는 파란색 색종이의 개수를 출력한다.

예제 입력 1 
8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1

예제 출력 1 
9
7
"""

n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

# print(*graph, sep="\n")

"""
그래프에 0,0 ~n/2,n/2 , 

"""

result = []


def solution(end, y=0, x=0):
    color_paper = graph[y][x]
    for i in range(y, y + end):
        for j in range(x, x + end):
            if color_paper != graph[i][j]:
                solution(end // 2, y, x)
                solution(end // 2, y + end // 2, x)
                solution(end // 2, y, x + end // 2)
                solution(end // 2, y + end // 2, x + end // 2)
                return
    if color_paper == 1:
        result.append(1)
    else:
        result.append(0)


solution(n)
print(result)
print(result.count(0))
print(result.count(1))
