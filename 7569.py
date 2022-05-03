from collections import deque


def bfs(z, y, x):
    queue = deque()
    queue.append((z, y, x))
    visited[z][y][x] = 1
    while queue:
        cz, cy, cx = queue.popleft()
        for dz, dy, dx in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            nz, ny, nx = cz + dz, cy + dy, cx + dx
            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and visited[nz][ny][nx] == 0 and arr[nz][ny][nx] == 0:
                visited[nz][ny][nx] = visited[cz][cy][cx] + 1
                queue.append((nz, ny, nx))



def start():
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if arr[h][i][j] == 1:
                    return h, i, j
    return 0, 0, 0

def is_zero(h, i, j):
    global check
    for hh in range(h):
        for ii in range(i):
            for jj in range(j):
                if arr[hh][ii][jj] == 0:
                    check = 0
                    return
    check = 1

def ans():
    global check
    max_n = 0
    for hh in range(H):
        for ii in range(N):
            for jj in range(M):
                if visited[hh][ii][jj] == 0:
                    return -1
                else:
                    if max_n < visited[hh][ii][jj]:
                        max_n = visited[hh][ii][jj]
    return max_n-1

# M = 가로, N = 세로, H = 높이
M, N, H = map(int, input().split())
check = 0
# 익은 토마토 = 1, 익지 않은 토마토 = 0, 빈 곳 = -1
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0] * M for _ in range(N)] for _ in range(H)]

is_zero(H, N, M)
if check == 0:
    h, i, j = start()
    bfs(h, i, j)
    print(visited)
    print(ans())
else:
    print(0)

