'''
N*M 크기의 직사각형
r : 지도의 북쪽에서부터 r 번째
c : 지도의 서쪽에서부터 c 번째
0 북, 1 동, 2 남, 3 서
빈칸 0, 벽 1

1. 현재 위치를 청소한다.

2. 현재 위치에서 다음을 반복하면서 인접한 칸을 탐색한다.

   a.현재 위치의 바로 왼쪽에 아직 청소하지 않은 빈 공간이 존재한다면,
    왼쪽 방향으로 회전한 다음 한 칸을 전진하고 1번으로 돌아간다. 그렇지 않을 경우,
    왼쪽 방향으로 회전한다. 이때, 왼쪽은 현재 바라보는 방향을 기준으로 한다.

   b. 1번으로 돌아가거나 후진하지 않고 2a번 단계가 연속으로 네 번 실행되었을 경우,
     바로 뒤쪽이 벽이라면 작동을 멈춘다. 그렇지 않다면 한 칸 후진한다.
'''
N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

direction = [0, 1, 2, 3]
opp = [3, 0, 1, 2]
back = [2, 3, 0, 1]

arr[r][c] = -1
cnt = 0
while True:
    if cnt == 4 and arr[]:
        break

    if d == 0:
        if arr[r][c-1] == 0:
            d = opp[d]
            arr[r][c-1] = -1
            c -= 1
        else:
            d = opp[d]

    elif d == 1:
        if arr[r-1][c] == 0:
            d = opp[d]
            arr[r-1][c] = -1
            r -= 1
        else:
            d = opp[d]

    elif d == 2:
        if arr[r][c+1] == 0:
            d = opp[d]
            arr[r][c+1] = -1
            c += 1
        else:
            d = opp[d]

    else:
        if arr[r+1][c] == 0:
            d = opp[d]
            arr[r+1][c] = -1
            r += 1
        else:
            d = opp[d]

ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == -1:
            ans += 1

print(ans)