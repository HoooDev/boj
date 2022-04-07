def dfs(cnt, M):
    if cnt == M:
        print(*result)
        return
    for i in range(N):
        if visited[i] == False:
            visited[i] = True
            result.append(i+1)
            dfs(cnt+1)
            result.pop()
            visited[i] = False


N, M = map(int, input().split())
visited = [False] * N
result = []
dfs(0, M)