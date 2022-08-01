N, M = map(int, input().split())

n_lst = list(map(int, input().split()))

# print(n_lst)

round_q = []
for i in range(N):
    round_q.append(i+1)

# print(round_q)

rq_len = len(round_q)

cnt = 0
while True:
    rq_len = len(round_q)

    if len(n_lst) == 0:
        break

    find_idx = round_q.index(n_lst[0])
    while len(n_lst):
        if round_q[0] == n_lst[0]:
            round_q.pop(0)
            n_lst.pop(0)
            break
        if find_idx <= (rq_len//2):
            a = round_q.pop(0)
            round_q.append(a)
            cnt += 1
        elif find_idx > (rq_len//2):
            a = round_q.pop(-1)
            round_q.insert(0, a)
            cnt += 1

print(cnt)