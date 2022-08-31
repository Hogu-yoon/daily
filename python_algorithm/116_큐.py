"""
제목 : 큐
문제 주소 : https://www.acmicpc.net/problem/10845
작성일 : 2022/08/24
"""

"""
문제
정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여섯 가지이다.

push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
입력
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

출력
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

예제 입력 1 
15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front
예제 출력 1 
1
2
2
0
1
2
-1
0
1
-1
0
3
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.last = -1
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        self.last = new_node.data
        self.size += 1
        if self.empty():
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def pop(self):
        if self.empty():
            return -1
        delete_head = self.head
        self.head = self.head.next
        if self.size > 0:
            self.size -= 1

        # 바로 뽑아 쓰기 용이하게
        return delete_head.data

    def front(self):
        if self.empty():
            return -1
        return self.head.data

    def back(self):
        if self.empty():
            return -1
        return self.last

    def empty(self):
        return self.head is None


def solution(queue: Queue, key, val=None):
    if key == 'push':
        return queue.push(val)
    elif key == 'pop':
        return queue.pop()
    elif key == 'empty':
        if queue.empty():
            return 1
        return 0
    elif key == 'size':
        return queue.size
    elif key == 'back':
        return queue.back()
    elif key == 'front':
        return queue.front()


n = int(input())
controllers = []
queue = Queue()
result = []
for _ in range(n):
    controllers = input().split()
    if controllers[0] == 'push':
        solution(queue, controllers[0], val=controllers[1])
    else:
        result.append(solution(queue, controllers[0]))

for x in result:
    print(x)

"""
20
push 1
push 2
front
back
push 3
push 4
front
back
size
pop
size
pop
pop
size
pop
size
pop
size
pop
size
"""
