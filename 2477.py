K = int(input())

lst_1 = []
lst_2 = []
for i in range(6):
    d, n = map(int, input().split())
    lst_1.append(n)

    max_len = 0
    for i in lst_1:
        if max_len < i:
            max_len = i