arr = [list(map(int, input().split())) for _ in range(19)]

def start(lst):
    for i in range(19):
        for j in range(19):
            if lst[i][j] == 1:
                print(bfs(i, j, 1))
            elif lst[i][j] == 2:
                print(bfs(i, j, 2))

def bfs(y, x, color):
    q = []
    fst_dol = []
    q.append((y, x))
    while q:
        cy, cx = q.pop(0)
        if visited[cy][cx] == 5:
            return color, fst_dol[-4]
        for dy, dx in [(0, 1), (1, 1), (1, 0), (1, -1)]:  # 우 대각 하 대각
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < 19 and 0 <= nx < 19 and visited[ny][nx] == 0 and arr[ny][nx] == color:
                q.append((ny, nx))
                fst_dol.append((cy, cx))
                visited[ny][nx] = visited[cy][cx] + 1
    return 0

di = [0, 1, 1, 1]  # 우 대각 하 대각
dj = [1, 1, 0, -1]
visited = [[0] * 19 for _ in range(19)]
start(arr)
