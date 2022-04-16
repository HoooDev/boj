def omok():
    for y in range(19):
        for x in range(19):
            if arr[y][x] != 0:
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    cnt = 1
                    while 0 <= ny < 19 and 0 <= nx < 19 and arr[ny][nx] == arr[y][x]:
                        cnt += 1

                        if cnt == 5:
                            if 0 <= ny + dy[d] < 19 and 0 <= nx + dx[d] < 19 and arr[ny][nx] == arr[ny + dy[d]][
                                nx + dx[d]]:  # 육목 판정 1
                                break
                            if 0 <= y - dy[d] < 19 and 0 <= x - dx[d] < 19 and arr[y][x] == arr[y - dy[d]][
                                x - dx[d]]:  # 육목 판정 2
                                break
                            return arr[y][x], y + 1, x + 1
                        ny += dy[d]
                        nx += dx[d]
    return 0, -1, -1


arr = [list(map(int, input().split())) for _ in range(19)]

dx = [0, 1, 1, -1]
dy = [1, 1, 0, 1]

color, y, x = omok()
if not color:
    print(color)
else:
    print(color)
    print(y, x)
