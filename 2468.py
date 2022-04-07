def bfs(y, x, k):
    queue = []
    queue.append((y, x))
    visited[y][x] = 1

    while queue:
        cy, cx = queue.pop(0)

        for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            ny = cy + dy
            nx = cx + dx

            if 0 <= nx < N and 0 <= ny < N and arr[ny][nx] > k and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                queue.append((ny, nx))


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

max_n = 0
for i in range(N):
    for j in range(N):
        if max_n < arr[i][j]:
            max_n = arr[i][j]

ans = 0
for k in range(max_n):
    visited = [[0] * N for _ in range(N)]
    temp = 0

    for r in range(N):
        for c in range(N):
            if arr[r][c] > k and visited[r][c] == 0:
                bfs(r, c, k)
                temp += 1

    if ans < temp:
        ans = temp

print(ans)
