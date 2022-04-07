bingo = [list(map(int, input().split())) for _ in range(5)]
call_b = [list(map(int, input().split())) for _ in range(5)]
call = []
for a in range(5):
    for b in range(5):
        call.append(call_b[a][b])

for c in range(25):
    line = 0
    for i in range(5):
        for j in range(5):
            if call[c] == bingo[i][j]:
                bingo[i][j] = 0
                break

    l_cross = 0
    r_cross = 0
    for y in range(5):
        sum_garo = 0
        sum_sero = 0
        for x in range(5):
            sum_garo += bingo[y][x]
            sum_sero += bingo[x][y]
        if sum_garo == 0:
            line += 1
        if sum_sero == 0:
            line += 1

        l_cross += bingo[y][y]
        r_cross += bingo[y][4-y]
    if l_cross == 0:
        line += 1
    if r_cross == 0:
        line += 1

    if line >= 3:
        print(c+1)
        break