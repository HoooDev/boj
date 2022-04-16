def choice_cows(n, k, m):
    if n == k:
        c = sum(select_cow)
        cnt = 0
        for i in range(2, c+1):
            if c % i == 0:
                cnt += 1
        if cnt == 1:
            if c not in ans:
                ans.append(c)
    else:
        for i in range(N):
            if used[i] == 0:
                used[i] = 1
                select_cow[n] = cows[i]
                choice_cows(n+1, k, m)
                used[i] = 0

import sys


N, M = map(int, sys.stdin.readline().split())
cows = list(map(int, sys.stdin.readline().split()))

select_cow = [0] * M
used = [0] * N
ans = []
choice_cows(0, M, N)
ans.sort()

if ans:
    print(*ans)
else:
    print(-1)
