"""
제목 : 분수찾기
문제 주소 : https://www.acmicpc.net/problem/1193
작성일 : 2022/08/18
"""

"""
무한히 큰 배열에 다음과 같이 분수들이 적혀있다.

1/1	1/2	1/3	1/4	1/5	…
2/1	2/2	2/3	2/4	…	…
3/1	3/2	3/3	…	…	…
4/1	4/2	…	…	…	…
5/1	…	…	…	…	…
…	…	…	…	…	…
이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.

X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.
"""

x = int(input())
# 해당라인까지의 분수의 개수
zig_num = 0
# 해당라인의 번호
zag_cnt = 1
while x > zig_num:
    zig_num = zig_num + zag_cnt
    zag_cnt += 1
    # print(zag_cnt)
    line_number = x - (zig_num - (zag_cnt - 1))
    print(line_number,"num:",zig_num,"cnt",zag_cnt-1)


if zag_cnt % 2 == 0:
    print(str(zag_cnt - line_number) + '/' + str(line_number))
else:
    print(str(line_number) + '/' + str(zag_cnt - line_number))
