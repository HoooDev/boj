def bfs(y, x):
    queue = []
    queue.append((y, x))
    visited[y][x] = 1
    while queue:
        cy, cx = queue.pop(0)

        for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] != 0:
                queue.append((ny, nx))


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

max_n = 0
for r in range(N):
    for c in range(N):
        if max_n < arr[r][c]:
            max_n = arr[r][c]

n = 0  # n = 4
ans = 1
while n <= max_n:
    visited = [[0] * N for _ in range(N)]

    yy, xx = 0, 0
    cnt = 0
    for ii in range(N):
        for jj in range(N):
            if arr[ii][jj] > n and visited[ii][jj] == 0:
                yy = ii
                xx = jj
                bfs(yy, xx)
                cnt += 1

    if ans < cnt:
        ans = cnt
    n += 1
print(ans)