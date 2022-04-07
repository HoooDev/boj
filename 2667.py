def bfs(y, x):
    queue = []
    queue.append((y, x))
    arr[y][x] = 0
    n = 1
    while queue:
        y, x = queue.pop(0)
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] == 1:
                arr[ny][nx] = 0
                queue.append((ny, nx))
                n += 1
    return n

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input())))

ans = []
cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            cnt += 1
            ans.append(bfs(i, j))

ans.sort()
print(cnt)
for i in ans:
    print(i)