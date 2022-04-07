N = int(input())

zero = [[0] * 1001 for _ in range(1001)]
for q in range(1, N+1):
    x1, y1, w, h = map(int, input().split())  # 1 4 3 2 -> 1 4 3 5

    for i in range(y1, y1 + h):
        for j in range(x1, x1 + w):
            zero[i][j] = q

# print(zero)

lst = []
for l in range(1, N + 1):
    cnt = 0
    for r in range(1001):
        for c in range(1001):
            if zero[r][c] == l:
                cnt += 1
    lst.append(cnt)
for i in lst:
    print(i)