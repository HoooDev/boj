def dfs(v):
    print(v, end=' ')
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(i)
    return
# 도착한 곳에 깃발을 꽂음

def bfs(v):
    # [[], [2, 3], [1, 5], [1, 4], [3, 5], [2, 4]]
    # 큐에 첫 정점 저장
    queue = [v]
    # 방문표시가 dfs에 의해 False -> True로 변경 됐으므로 (현재 모든 방문이 True) 다시 True -> False로
    visited[v] = False
    # 큐가 있는 동안
    while queue:
        # 큐 안의 정점을 뽑아서
        v = queue.pop(0)
        print(v, end=' ')
        # 노드별 정점을 순회시켜 방문표시가 안돼있으면 큐에 append(정점) 해주고 방문표시 해줌
        for i in graph[v]:
            if visited[i] == True:
                queue.append(i)
                visited[i] = False


N, M, V = map(int, input().split())
arr = []
# 방문 표시 리스트
visited = [False] * (N + 1) # 모든 공간에 깃발이 다 꽂혀있다.
for i in range(M):
    n1, n2 = map(int, input().split())
    arr.append(n1)
    arr.append(n2)
# 각 노드별 연결 정점
graph = [[] for _ in range(N + 1)]
for j in range(0, len(arr), 2):
    graph[arr[j]].append(arr[j + 1])
    graph[arr[j + 1]].append(arr[j])

# 각 노드별 정점을 오름차순 정렬시킴 (정점 중 작은 정점 먼저)
for i in range(1, N + 1):
    graph[i].sort()
print(graph)
dfs(V)
print()
bfs(V)
