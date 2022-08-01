def bfs(y, x):
    visited[y][x] = 1
    q = [(y, x)]
    while q:
        cy, cx = q.pop(0)

        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 0 and arr[ny][nx] == 1:
                visited[ny][nx] = 1
                q.append((ny, nx))
                arr[ny][nx] = 0


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    for _ in range(K):
        b_i, b_j = map(int, input().split())

        arr[b_j][b_i] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                bfs(i, j)
                cnt += 1
    # print(visited)

    print(cnt)
