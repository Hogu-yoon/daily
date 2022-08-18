
"""
제목 : 스택
문제 주소 : https://www.acmicpc.net/problem/10828
작성일 : 2022/08/17
"""




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.count = 0

    # 집어넣는 함수(앞쪽에 배치)
    def push(self, val):
        new_head = Node(val)
        new_head.next = self.head
        self.count += 1
        self.head = new_head

    # 뽑아내는 함수
    def pop(self):
        if self.head is not None:
            pop_head = self.head
            self.head = self.head.next
            self.count -= 1
            return pop_head.data
        return -1

    # 맨위에 뭐가 있는지 확인하는 함수
    def top(self):
        if self.head is not None:
            return self.head.data
        return -1

    # 비어있는지 확인하는 함수(조건 비어있으면 1)
    def empty(self):
        if self.head is not None:
            return 0
        return 1

    def size(self):
        return self.count


#
def solution(stack: Stack, key, val=None):
    if key == 'push':
        return stack.push(val)
    elif key == 'pop':
        return stack.pop()
    elif key == 'top':
        return stack.top()
    elif key == 'empty':
        return stack.empty()
    elif key == 'size':
        return stack.size()


n = int(input())
controllers = []
stack = Stack()
result = []
for _ in range(n):
    controllers = input().split()
    if controllers[0] == 'push':
        solution(stack, controllers[0], val=controllers[1])
    else:
        result.append(solution(stack, controllers[0]))

print(*result, sep='\n')





