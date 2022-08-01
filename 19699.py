def choice_cow(n, k, m):
    if n == M:
        cnt = 0
        for i in range(2, m+1):
            if m % i == 0:
                cnt += 1
        if cnt == 1 and (m not in ans):
            ans.append(m)

    for i in range(n, N):
        if visited[i] == 0:
            visited[i] = 1
            choice_cow(n+1, k, cow_w[i] + m)
            visited[i] = 0


import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())

cow_w = list(map(int, input().strip().split()))

# print(cow_w)

select_cow = [0] * M
visited = [0] * N
ans = []
choice_cow(0, 0, 0)
if ans:
    ans.sort()
    print(*ans)
else:
    print(-1)