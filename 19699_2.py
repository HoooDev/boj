def choice_cows(n, k, m):
    if n == k:
        cnt = 0
        for i in range(2, m+1):
            if m % i == 0:
                cnt += 1
        if cnt == 1:
            if m not in ans:
                ans.add(m)
    else:
        for j in range(M):
            if used[j] == 0:
                used[j] = 1
                choice_cows(n+1, k, cows[j]+m)
                used[j] = 0

import sys


N, M = map(int, sys.stdin.readline().split())
cows = list(map(int, sys.stdin.readline().split()))

select_cow = [0] * M
used = [0] * N

choice_cows(0, M, 0)
ans = set()

if ans:
    print(ans)
else:
    print(-1)