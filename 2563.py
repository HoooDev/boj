N = int(input())

arr = [[0] * 100 for _ in range(100)]

for _ in range(N):
    x1, y1 = map(int, input().split())

    for i in range(x1, x1+10):
        for j in range(y1, y1+10):
            arr[i][j] = 1

cnt = 0
for r in range(100):
    for c in range(100):
        if arr[r][c] == 1:
            cnt += 1

print(cnt)