def dfs(cnt, new_i):
    if cnt == M:
        print(*result)
        return
    for i in range(new_i, N):
        result.append(i+1)
        dfs(cnt + 1, i)
        result.pop()


N, M = map(int, input().split())
visited = [False] * N
result = []
dfs(0, 0)
