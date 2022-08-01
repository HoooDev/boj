N = int(input())
for _ in range(N):
    m, n = map(int, input().split())
    words = list(input().split())
    blank_lst = [0 for _ in range(m)]
    for _ in range(n):
        c1, c2 = map(int, input().split())
        blank_lst[c2-1] = words[c1-1]
    for i in range(m):
        for j in range(m):
            if blank_lst[i] == 0 and words[j] not in blank_lst:
                blank_lst[i] = words[j]
    print(*blank_lst)

# t = int(input())
# for _ in range(t):
#     m, n = map(int, input().split())
#     s = list(input().split())
#     arr = [[] for i in range(m)]
#     for _ in range(n):
#         a, b = map(int, input().split())
#         arr[b-1] = s[a-1]
#     for j in range(m):
#         for ss in s:
#             if len(arr[j]) == 0 and ss not in arr:
#                 arr[j] = ss
#                 print(arr)
#
#                 break
#     print(*arr)