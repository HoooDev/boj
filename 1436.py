N = int(input())

cnt = 0
a = 0
while True:
    b = str(a)
    if "666" in b:
        cnt += 1
    if cnt == N:
        print(b)
        break
    a += 1
