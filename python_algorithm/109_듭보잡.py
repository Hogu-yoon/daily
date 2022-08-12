"""
제목 : 듣보잡
문제 주소 : https://www.acmicpc.net/problem/1764
작성일 : 2022/08/12
"""
"""
문제
김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다. 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다. 이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.

듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.

출력
듣보잡의 수와 그 명단을 사전순으로 출력한다.

예제 입력 1 
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton
예제 출력 1 
2
baesangwook
ohhenrie
"""

n, m = map(int, input().split())
# 어차피 듣보잡이라는게 듣도못한사람과 보도못한사람의 중복리스트를 찾는 내용.
듣보잡 = {}

for i in range(1, n + m + 1):
    name = input()
    if i < n + 1:
        듣보잡[name] = False
    #     none 과 false를 구분해야함.
    elif 듣보잡.get(name) is False:
        듣보잡[name] = True
result = []
len_list = 0
for key, val in 듣보잡.items():
    if val:
        len_list += 1
        result.append(key)
result.sort()
answer = '\n'.join(result)
print(len_list)
print(answer)
# print(*result, sep='\n')
"""
47599225	redeyes1234	 1764	맞았습니다!!	40900	3708	Python 3 / 수정	566	1분 전
47598282	redeyes1234	 1764	맞았습니다!!	40900	4004	Python 3 / 수정	357	

# print(*result, sep='\n') >> print(answer) 이렇게 바꿈으로써 조금더 빨라짐 
"""