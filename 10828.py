def push(n):
    lst.append(n)

def pop():
    if lst:
        return lst.pop()
    else:
        return -1
def size():
    return len(lst)

def empty():
    if len(lst) == 0:
        return 1
    else:
        return 0

def top():
    if lst:
        return lst[-1]
    else:
        return -1
import sys

lst = []
N = int(sys.stdin.readline())
for _ in range(N):
    a = sys.stdin.readline().split()
    if len(a) == 2:
        push(int(a[-1]))
    elif a[0] == 'top':
        print(top())
    elif a[0] == 'size':
        print(size())
    elif a[0] == 'empty':
        print(empty())
    elif a[0] == 'pop':
        print(pop())
