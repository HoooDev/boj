bingo = [list(map(int, input().split())) for _ in range(5)]
call_lst = [list(map(int, input().split())) for _ in range(5)]

call = []
for i in call_lst:
    for j in i:
        call.append(j)

for k in range(25):
    for r in range(5):
        for c in range(5):
            if call[k] == bingo[r][c]:
                bingo[r][c] = 0
                break

    cnt = 0
    sum_rcross = 0
    sum_lcross = 0
    for i in range(5):
        sum_garo = 0
        sum_sero = 0
        for j in range(5):
            sum_garo += bingo[i][j]
            sum_sero += bingo[j][i]
        if sum_garo == 0:
            cnt += 1
        if sum_sero == 0:
            cnt += 1
        sum_lcross += bingo[i][i]
        sum_rcross += bingo[i][4-i]

    if sum_lcross == 0:
        cnt += 1
    if sum_rcross == 0:
        cnt += 1

    if cnt >= 3:
        print(k+1)
        break