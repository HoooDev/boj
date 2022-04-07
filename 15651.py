def dfs(cnt):
    if cnt == M:
        print(*result)
        return

    for i in range(N):
        result.append(i+1)
        dfs(cnt + 1)
        result.pop()

N, M = map(int, input().split())
result = []
dfs(0)