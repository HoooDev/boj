N = int(input())

wh_lst = []
for _ in range(N):
    w, h = map(int, input().split())
    wh_lst.append((w, h))

# print(wh_lst)
lst_len = len(wh_lst)

cnt_lst = [1] * lst_len
for i in range(lst_len):
    for j in range(lst_len):
        if wh_lst[i][0] < wh_lst[j][0] and wh_lst[i][1] < wh_lst[j][1]:
            cnt_lst[i] += 1

print(*cnt_lst)