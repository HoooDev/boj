bingo = [list(map(int, input().split())) for _ in range(5)]
call = []
for _ in range(5):
    a = list(map(int, input().split()))
    call.extend(a)
line = 0
ans_lst = [0] * 12 # 행 5개 열 5개 대각 2개 [5 0 3 2 0 4 0 1 0 5 0 5] 총 나올 수 있는 빙고 줄 = 12
for i in range(25):
    for r in range(5):
        for c in range(5):
            if call[i] == bingo[r][c]:
                bingo[r][c] = 0
                ans_lst[r] += 1 # 행 바뀌면 +=1 idx => 0~4 까지 카운팅 부르면 += 1
                ans_lst[c+5] += 1 # 열 바뀌면 += 1 -> 5 9 까지
                if r == c:
                    ans_lst[10] += 1
                if r + c == 4:
                    ans_lst[11] += 1
                    # 카운팅 솔트
                for d in range(12):
                    if ans_lst[d] == 5:
                        ans_lst[d] = 0
                        line += 1
                        if line == 3:
                            print(i+1)
