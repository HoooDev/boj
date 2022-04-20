while True:
    n_lst = input()
    if n_lst == '0':
        break
    n_lst2 = ''
    for i in n_lst:
        n_lst2 = i + n_lst2

    if n_lst == n_lst2:
        print('yes')
    else:
        print('no')