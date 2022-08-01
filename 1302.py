N = int(input())

lst = list(input() for _ in range(N))
lst.sort()
lst2 = set(lst)

max_cnt = 0
book = ''
for i in lst2:
    cnt = 0
    for j in range(N):
        if i == lst[j]:
           cnt += 1
    if max_cnt < cnt:
        max_cnt = cnt
        book = i
print(book)