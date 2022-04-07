N = int(input())
for _ in range(N):
    arr = list(map(str, input().split()))

    lst = []
    for i in arr:
        lst.append(i[::-1])

    print(*lst)