def bfs(y, x):
    queue = []
    queue.append((y, x))
    visited[y][x] = 1
    while queue:
        y, x = queue.pop(0)
        if y == N-1 and x == M-1:
            print(visited[y][x])
        else:
            for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] == 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append((ny, nx))


N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

visited = [[0] * M for _ in range(N)]

bfs(0, 0)
