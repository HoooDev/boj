import sys
N = int(sys.stdin.readline())
lst = [0] * (10000+1)
for _ in range(N):
    i = int(sys.stdin.readline())
    lst[i] += 1

for i in range(1, 10000+1):
    for j in range(lst[i]):
        print(i)