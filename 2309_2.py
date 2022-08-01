def recur(N):
    global visited
    global a
    if N == 7 and sum(ans) == 100 and len(set(ans)) == 7:
        a = 1
        ans.sort()
        for i in ans:
            print(i)
        return

    for i in range(9):
        if visited[i] == 0:
            ans.append(lst[i])
            visited[i] = 1
            recur(N+1)
            if a == 1:
                break
            visited[i] = 0
            ans.pop()


lst = []

for _ in range(9):
    n = int(input())
    lst.append(n)

visited = [0] * 9
ans = []
a = 0
recur(0)