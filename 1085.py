while True:
    lst = list(map(int,input().split()))
    d = max(lst)
    if sum(lst) == 0:
        break
    lst.remove(d)
    if d ** 2 == lst[0] ** 2 + lst[1] ** 2:
        print('right')
    else:
        print('wrong')