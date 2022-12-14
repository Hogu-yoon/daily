"""
제목 : H-Index
문제 주소 : https://school.programmers.co.kr/learn/courses/30/lessons/42747
작성일 : 2022/08/30
"""

"""
문제 설명
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

제한사항
과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
논문별 인용 횟수는 0회 이상 10,000회 이하입니다.
입출력 예
citations	return
[3, 0, 6, 1, 5]	3
"""
"""
h가 1편이상 0 1편이하 0
h가 2편이상 0 2편이하 0
h가 3편이상 0 3편이하 0 <<< h최댓값
h가 4편이상 X 4편이하 0
"""


def solution(citations):
    citations.sort()
    i = 0
    while True:
        up_cnt = 0

        for x in citations:
            if x >= i:
                up_cnt += 1
        if up_cnt < i:
            return i - 1
        i += 1


print(solution([3, 0, 6, 1, 5]))
