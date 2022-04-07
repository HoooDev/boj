def dfs(x1, x2, d):
    global result
    if x1 == x2:
        result = d
        return result

    visited[x1] = True
    for i in graph[x1]:
        if visited[i] == False:
            dfs(i, x2, d+1)
    return

N = int(input())
p1, p2 = map(int, input().split())
M = int(input())

visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]
result = -1
d = 0

for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

dfs(p1, p2, d)
print(result)