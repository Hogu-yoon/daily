"""
제목 : 참외밭
문제 주소 : https://www.acmicpc.net/problem/2477
작성일 : 2022/08/11
"""

"""
시골에 있는 태양이의 삼촌 댁에는 커다란 참외밭이 있다. 문득 태양이는 이 밭에서 자라는 참외가 도대체 몇 개나 되는지 궁금해졌다. 어떻게 알아낼 수 있는지 골똘히 생각하다가 드디어 좋은 아이디어가 떠올랐다. 유레카! 1m2의 넓이에 자라는 참외 개수를 헤아린 다음, 참외밭의 넓이를 구하면 비례식을 이용하여 참외의 총개수를 구할 수 있다.

1m2의 넓이에 자라는 참외의 개수는 헤아렸고, 이제 참외밭의 넓이만 구하면 된다. 참외밭은 ㄱ-자 모양이거나 ㄱ-자를 90도, 180도, 270도 회전한 모양(┏, ┗, ┛ 모양)의 육각형이다. 다행히도 밭의 경계(육각형의 변)는 모두 동서 방향이거나 남북 방향이었다. 밭의 한 모퉁이에서 출발하여 밭의 둘레를 돌면서 밭경계 길이를 모두 측정하였다.



예를 들어 참외밭이 위 그림과 같은 모양이라고 하자. 그림에서 오른쪽은 동쪽, 왼쪽은 서쪽, 아래쪽은 남쪽, 위쪽은 북쪽이다. 이 그림의 왼쪽위 꼭짓점에서 출발하여, 반시계방향으로 남쪽으로 30m, 동쪽으로 60m, 남쪽으로 20m, 동쪽으로 100m, 북쪽으로 50m, 서쪽으로 160m 이동하면 다시 출발점으로 되돌아가게 된다.

위 그림의 참외밭  면적은 6800m2이다. 만약 1m2의 넓이에 자라는 참외의 개수가 7이라면, 이 밭에서 자라는 참외의 개수는 47600으로 계산된다.

1m2의 넓이에 자라는 참외의 개수와, 참외밭을 이루는 육각형의 임의의 한 꼭짓점에서 출발하여 반시계방향으로 둘레를 돌면서 지나는 변의 방향과 길이가 순서대로 주어진다. 이 참외밭에서 자라는 참외의 수를 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 1m2의 넓이에 자라는 참외의 개수를 나타내는 양의 정수 K (1 ≤ K ≤ 20)가 주어진다. 참외밭을 나타내는 육각형의 임의의 한 꼭짓점에서 출발하여 반시계방향으로 둘레를 돌면서 지나는 변의 방향과 길이 (1 이상 500 이하의 정수) 가 둘째 줄부터 일곱 번째 줄까지 한 줄에 하나씩 순서대로 주어진다. 변의 방향에서 동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4로 나타낸다.

출력
첫째 줄에 입력으로 주어진 밭에서 자라는 참외의 수를 출력한다.
7
4 50
2 160
3 30
1 60
3 20
1 100
"""

k = int(input())
queue = []
max_width_idx = [0, 0]
max_height_idx = [0, 0]
width = [1, 2]
height = [3, 4]
for i in range(6):
    a, b = map(int, input().split())
    queue.append([a, b])
    if a in width and b >= max_width_idx[0]:
        max_width_idx = [b, i]
    elif a in height and b >= max_height_idx[0]:
        max_height_idx = [b, i]

max_rec_area = max_width_idx[0] * max_height_idx[0]

if max_width_idx[1] > max_height_idx[1]:
    try:
        min_height = max_height_idx[0] - queue[max_width_idx[1] + 1][1]
    except :
        min_height = max_height_idx[0] - queue[0][1]
    min_width = max_width_idx[0] - queue[max_height_idx[1] - 1][1]
else:
    try:
        min_width = max_width_idx[0] - queue[max_height_idx[1] + 1][1]
    except :
        min_width = max_width_idx[0] - queue[0][1]
    min_height = max_height_idx[0] - queue[max_width_idx[1] - 1][1]

small_rec_area = min_width * min_height
print(max_width_idx, max_height_idx)
print("m_w", min_width, "m_h", min_height)
print((max_rec_area - small_rec_area) * k)


# 1
# 4 10
# 2 10
# 3 2
# 1 1
# 3 8
# 1 9
