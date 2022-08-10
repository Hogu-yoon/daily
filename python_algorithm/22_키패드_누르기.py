"""
 제목 : 키패드 누르기
문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/67256,
작성일 : 2022/05/04
"""

import numpy as np


def left_right(number):
    if number == 1 or number == 4 or number == 7:
        return 'L'
    elif number == 3 or number == 6 or number == 9:
        return 'R'
    else:
        return 'M'


def keypad_coordinate(keypad, lr_last_num, num):
    num_key = np.array(keypad)
    x_1, x_2 = np.where(num_key == lr_last_num)
    num_1, num_2 = np.where(num_key == num)
    x = np.append(x_1, x_2)
    n = np.append(num_1, num_2)
    return sum(abs(x - n))


def solution(numbers, hand):
    l_list = [42]
    r_list = [35]
    keypad = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [42, 0, 35]]
    answer = ''
    a_list = []
    b_list = []
    for num in numbers:
        lr = left_right(num)
        a_list.append(lr)
        if 'L' == lr:
            l_list.append(num)
            b_list.append('L')
        elif 'R' == lr:
            r_list.append(num)
            b_list.append('R')
        #     M을 마주쳤을 때
        else:

            r = keypad_coordinate(keypad, r_list[-1], num)
            l = keypad_coordinate(keypad, l_list[-1], num)
            if r < l:
                b_list.append('R')
                r_list.append(num)
            elif r > l:
                b_list.append('L')
                l_list.append(num)
            else:

                if hand == 'right':
                    r_list.append(num)
                else:
                    l_list.append(num)
                b_list.append(hand[0].upper())
    return "".join(b_list)