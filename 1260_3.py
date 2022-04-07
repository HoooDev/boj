def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if visited[i] == False:
            visited[i] = True
            dfs(i)

def bfs(v):
    queue = []
    queue.append(v)
    visited[v] = False
    while queue:
        q = queue.pop(0)
        print(q, end=' ')
        for i in graph[q]:
            if visited[i] == True:
                visited[i] = False
                queue.append(i)

N, M, V = map(int, input().split())
arr = []
visited = [False] * (N+1)
for _ in range(M):
    p1, p2 = map(int, input().split())
    arr.append(p1)
    arr.append(p2)

graph = [[] for _ in range(N+1)]
for i in range(0, len(arr), 2):
    graph[arr[i]].append(arr[i+1])
    graph[arr[i+1]].append(arr[i])

for j in range(1, N+1):
    graph[j].sort()

dfs(V)
print()
bfs(V)