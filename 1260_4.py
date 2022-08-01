def dfs(n):
    visited[n] = 1
    print(n, end=' ')

    for i in sort_graph[n]:
        if visited[i] == 0:
            dfs(i)

def bfs(n):
    visited[n] = 0
    q = [n]
    while q:
        a = q.pop(0)
        print(a, end=' ')
        for i in sort_graph[a]:
            if visited[i] == 1:
                visited[i] = 0
                q.append(i)





N, M, V = map(int, input().split())

visited = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    p1, p2 = map(int, input().split())
    graph[p1].append(p2)
    graph[p2].append(p1)

sort_graph = []
for j in range(len(graph)):
    a = sorted(graph[j])
    sort_graph.append(a)

dfs(V)
print()
bfs(V)

