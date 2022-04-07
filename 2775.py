T = int(input())
for tc in range(T):
    k = int(input()) # k층 0 ~ / 1 <= k   1
    n = int(input()) # n호 1 ~ / N <= 14  3

    arr = [[0] * n for _ in range(k+1)]
    for i in range(k+1):
        for j in range(n):
            if i == 0:
                arr[i][j] = j+1 # arr[0][0] = 1, 2, 3 ...
            else:
                # 각층의 0호는 모두 1명 // 0호 ~~층 , 0층에 ~~호
                arr[i][0] = 1
    # print(arr)
    for z in range(1, k+1):
        # 각 0번째 호수는 1로 고정이 돼있으므로 제외
        for x in range(1, n):
            # 해당 층의 명 수 = 옆집 명 수 + 아랫집 명 수
            arr[z][x] = arr[z-1][x] + arr[z][x-1]
            #   1  1         0   1        1  0
    # print(arr)
    # print(arr[k][n-1])