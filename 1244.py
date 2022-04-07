def change(n):
    if s[n] == 1:
        s[n] = 0
    else:
        s[n] = 1

N = int(input())

s = [-1] + list(map(int, input().split()))
stu_n = int(input())

for x in range(stu_n):
    p, p_n = map(int, input().split())

    if p == 1:
        for i in range(1, N + 1):
            if i % p_n == 0:
                change(i)
    else:
        change(p_n)
        for c in range(N//2):
            if p_n - c <= 0 or p_n + c > N:
                break
            if s[p_n-c] == s[p_n+c]:
                change(p_n-c)
                change(p_n+c)
            else:
                break

for w in range(1, N+1):
    print(s[w], end=' ')
    if w % 20 == 0:
        print()