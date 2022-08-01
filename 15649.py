def recur(lev):
    if lev == M:
        print(*path)
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            path.append(i+1)
            recur(lev+1)
            path.pop()
            visited[i] = 0

N, M = map(int, input().split())
path = []
visited = [0] * N
recur(0)