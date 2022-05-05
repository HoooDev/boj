from collections import deque

T = int(input())
for tc in range(T):
    N = int(input())
    house_y, house_x = map(int, input().split())
    store_x_lst = []
    store_y_lst = []
    dis_lst = []
    ans = 'happy'

    if N > 0:
        for _ in range(N):
            store_y, store_x = map(int, input().split())
            store_x_lst.append(store_x)
            store_y_lst.append(store_y)

        fst_dis = abs(house_y - store_y_lst[0]) + abs(house_x - store_x_lst[0])
        dis_lst.append(fst_dis)
        rock_y, rock_x = map(int, input().split())
        for i in range(N - 1):
            dis = abs(store_y_lst[i] - store_y_lst[i + 1]) + abs(store_x_lst[i] - store_x_lst[i + 1])
            dis_lst.append(dis)

        last_dis = abs(store_y_lst[-1] - rock_y) + abs(store_x_lst[-1] - rock_x)
        dis_lst.append(last_dis)
    elif N == 0:
        rock_y, rock_x = map(int, input().split())
        fst_dis = abs(house_y - rock_y) + abs(house_x - rock_x)
        dis_lst.append(fst_dis)

    print(dis_lst)
    for i in range(len(dis_lst)):
        if dis_lst[i] > 1000:
            ans = 'sad'
            break
    print(ans)
