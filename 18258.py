from collections import deque
import sys

N = int(input())
input = sys.stdin.readline
q = deque()
for _ in range(N):
    a = list(input().split())

    if len(a) == 2:
        q.append(a[1])
    else:
        if a[0] == 'pop':
            if q:
                b = q.popleft()
                print(b)
            else:
                print(-1)
        elif a[0] == 'size':
            print(len(q))
        elif a[0] == 'empty':
            if q:
                print(0)
            else:
                print(1)
        elif a[0] == 'front':
            if q:
                print(q[0])
            else:
                print(-1)
        elif a[0] == 'back':
            if q:
                print(q[-1])
            else:
                print(-1)
