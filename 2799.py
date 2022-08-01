from collections import deque

def bfs(y, x):
    global cnt
    q = deque()
    q.append((y, x))
    visited[y][x] = 1
    while q:
        cy, cx = q.popleft()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny = cy + dy
            nx = cx + dx
            if 0<= ny <(5*M+1) and 0<= nx < (5*N+1) and visited[ny][nx] == 0 and arr[ny][nx] == '.':
                cnt += 1
                visited[ny][nx] = 1
                q.append((ny, nx))
    return cnt
M, N = map(int, input().split())

arr = []
for _ in range(5*M+1):
    a = list(input())
    arr.append(a)

check = [0] * 5
cnt = 0
visited = [[0]*(5*N+1) for _ in range(5*M+1) ]
for i in range(5*M+1):
    for j in range(5*N+1):
        if arr[i][j] == '.' and visited[i][j] == 0:
            count = bfs(i, j)
            if count + 1 == 16:
                check[0] += 1
            elif count + 1 == 12:
                check[1] += 1
            elif count + 1 == 8:
                check[2] += 1
            elif count + 1 == 4:
                check[3] += 1
            cnt = 0

a = M*N - sum(check)
if a != 0:
    check[4] = a
print(*check)