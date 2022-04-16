N = int(input())
n_lst = list(map(int, input().split()))

ans = []
for i in n_lst:
    cnt = 0
    if i == 1:
        continue
    for j in range(2, i + 1):
        if i % j == 0:
            cnt += 1
    if cnt == 1:
        ans.append(i)
print(len(ans))