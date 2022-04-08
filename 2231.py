def f(n):
    for i in range(1, N + 1):
        M = i
        cnt = i
        while M > 0:
            c = M % 10
            cnt += c
            M = M // 10
        if cnt == n:
            return i
    return 0

N = int(input())
print(f(N))


        # 1, N + 1