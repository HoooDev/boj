num = set()
all_num = set(range(1,10001))
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    num.add(i)
self_num = sorted(all_num - num)
for ans in self_num:
    print(ans)

