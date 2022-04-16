def bfs(y, x):
    global lst
    q = []
    q.append((y, x))
    while q:
        cy, cx = q.pop(0)
        check_lst.append(lst[cy][cx])

        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == False:
                q.append((ny, nx))
                visited[ny][nx] = True

N, M, C = map(int, input().split())
lst = [[0] * M for _ in range(N)]

cnt = 1
for i in range(N):
    for j in range(M):
        lst[i][j] = cnt
        cnt += 1
print(lst)
visited = [[False] * M for _ in range(N)]
print(visited)
check_lst = []
visited[0][0] = True
bfs(0, 0)
print(check_lst)
