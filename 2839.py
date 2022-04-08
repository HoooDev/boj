def f(n):
    cnt = 0

    while n >= 0:
        if n > 5:
            n -= 5
            cnt += 1
        elif n >= 3:
            n -= 3
            cnt += 1
        elif n == 0:
            return cnt
        elif n < 3:
            return -1


    return cnt


N = int(input())

print(f(N))
