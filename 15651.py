def recur(lev):
    if lev == M:
        print(*path)
        return
    for i in range(N):
        path.append(i+1)
        recur(lev+1)
        path.pop()

N, M = map(int, input().split())
path = []
recur(0)