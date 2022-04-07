N = int(input())
cnt = 1
cnt_add = 6
room = 1
while N > cnt:
    cnt += cnt_add
    room += 1
    cnt_add += 6
print(room)