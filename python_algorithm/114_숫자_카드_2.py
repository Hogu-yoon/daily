"""
제목 : 숫자 카드 2
문제 주소 : https://www.acmicpc.net/problem/10816
작성일 : 2022/08/22
"""

"""
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10
"""
from sys import stdin

n = stdin.readline().rstrip()
sang_cards = list(map(int, stdin.readline().split()))
m = stdin.readline().rstrip()
target_cards = list(map(int, stdin.readline().split()))
sang_cards.sort()


def binary_search(target, cards):
    start = 0
    end = len(cards) - 1
    while start <= end:
        mid = (start + end) // 2
        if target == cards[mid]:
            cnt = 1
            i = 1
            esc_states = [False, False]
            while True:
                if mid + i < len(cards) and cards[mid + i] == target:
                    cnt += 1
                else:
                    esc_states[0] = True
                if mid - i >= 0 and cards[mid - i] == target:
                    cnt += 1
                else:
                    esc_states[1] = True
                i += 1
                if all(esc_states):
                    break
            return cnt
        elif target > cards[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return 0


def binary_search_idx(target, cards):
    start = 0
    end = len(cards) - 1
    while start <= end:
        mid = (start + end) // 2
        if target == cards[mid]:
            return mid
        elif target > cards[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return 0


# print(binary_search(target_cards[0], sang_cards))


from bisect import bisect_left as left, bisect_right as right

result = []
for x in target_cards:
    # print(binary_search(x, sang_cards), end=" ")
    left_index = left(sang_cards, x)
    right_index = right(sang_cards, x)
    print(right_index - left_index, end=" ")


print()

print("ddd",left([1,2,3,4],5),right([1,2,3,4],5))