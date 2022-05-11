from collections import deque


#
#
# def bfs():
#     while ice_lst:
#         cy, cx = ice_lst.popleft()
#         for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#             ny, nx = cy + dy, cx + dx
#             if 0 <= ny < N and 0 <= nx < M and:

def melting():
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                # ice_lst.append((i, j))
                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
                        visited[i][j] += 1
    for i in range(N):
        for j in range(M):
            arr[i][j] = arr[i][j] - visited[i][j]
            if arr[i][j] < 0:
                arr[i][j] = 0


def check():
    for i in

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]


melting()

print(visited)
print(arr)
# si, sj = ice_lst.popleft()

# bfs()
