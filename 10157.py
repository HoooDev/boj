N, M = map(int, input().split())
K = int(input())

di = [1, 0, -1, 0] # 하 우 상 좌
dj = [0, 1, 0, -1]

arr = [[0]*(N) for _ in range(M)]

d = 0
i = 0
j = 0
c = 1
while c < M*N+1:
    arr[i][j] = c
    ni = i + di[d]
    nj = j + dj[d]
    if 0 > ni or ni >= M or 0 > nj or nj >= N or arr[ni][nj] != 0:
        d = (d+1) % 4
    i += di[d]
    j += dj[d]
    c += 1

for i in range(M):
    for j in range(N):
        if arr[i][j] == K:
            print(j+1, end=' ')
            print(i+1)
            break

if N*M < K:
    print(0)