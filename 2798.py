def dfs(n, k, m):
    global black
    global ssum

    if n == k:
        if sum(black) == M or sum(black) > ssum and sum(black) <= M:
            ssum = sum(black)
            return ssum
    else:
        for i in range(m):
            if used[i] == 0:
                used[i] = 1
                black[n] = arr[i]
                dfs(n+1, k, m)
                used[i] = 0

N, M = map(int, input().split())
arr = list(map(int, input().split()))

ssum = 0
black = [0] * 3
used = [0] * N
dfs(0, 3, N)
print(ssum)

# ans = 0
# for i in range(1 << N):
#     sum_lst = []
#     for j in range(3):
#         if i & (1 << j):
#             sum_lst.append(arr[j])
#     if sum(sum_lst) == M or sum(sum_lst) > ans and sum(sum_lst) < M:
#         ans = sum(sum_lst)
# print(ans)