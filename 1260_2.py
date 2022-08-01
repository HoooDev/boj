def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if visited[i] == False:
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
                queue.append(i)
                visited[i] = False


N, M, V = map(int, input().split())

visited = [False] * (N+1)
node_lst = []
graph = [[] for _ in range(N+1)]
for x in range(M):
    n1, n2 = map(int, input().split())
    node_lst.append(n1)
    node_lst.append(n2)

for i in range(0, len(node_lst), 2):
    graph[node_lst[i]].append(node_lst[i + 1])
    graph[node_lst[i+1]].append(node_lst[i])

for i in range(1, N+1):
    graph[i].sort()

print(node_lst)
dfs(V)
print()
bfs(V)