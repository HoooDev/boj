def dfs(y, x)


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
dfs(0, 0)
print(check_lst)
