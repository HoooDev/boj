from sys import stdin

def facto(a):

    if a == 0:
        return 1

    return a * facto(a-1)

N, K = map(int, stdin.readline().split())

ans = facto(N) // (facto(K) * facto(N-K))
print(ans)