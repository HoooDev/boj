def dfs(v): # v = 1
    # v가 들어올 때 마다 visited[v]에 방문표시를 해줌
    visited[v] = True
    result.append(v)
    for i in graph[v]:
        # graph[v]의 컴퓨터 번호를 방문하지 않았다면 결과 리스트에 저장하고 재귀를 통해서 방문표시를 다시 해준다.
        if visited[i] == False:
            # 1이랑 연관이 있는 컴퓨터 번호 저장을 2, 3, 5, 6
            # i = 2
            dfs(i)
    return

N = int(input()) # 컴퓨터 대 수
link = int(input()) # 이어진 링크 개수
# 결과 저장 해 줄 리스트
result = []

node_lst = []
# 방문 표시 해 줄 리스트
visited = [False] * (N+1)
for _ in range(link):
    n, m = map(int, input().split())
    node_lst.append(n)
    node_lst.append(m)

print(node_lst) # [1, 2, 2, 3, 1, 5, 5, 2, 5, 6, 4, 7]

# 각 컴퓨터 번호마다 링크돼있는 노드를 나타내는 리스트를 만들어줌
graph = [[] for _ in range(N+1)]
# [[], [], [], [], [], [], [], []]
#|  0   1   2   3   4   5   6   7

for i in range(0, len(node_lst), 2): # i -> 0, 1
    p1 = node_lst[i] # i가 0이면, node_lst[i] = p1 = 1
    p2 = node_lst[i+1] #          node_lst[i+1] = p2 = 2
    # (1, 2) (2, 3) (1, 5) (5, 2) (5, 6) (4, 7)
    # 링크는 서로 연결 돼 있으므로 서로간의 인덱스에 값을 바꿔 넣어줌 1 - 2
    graph[p1].append(p2) # 1번 정점이랑 연결된 정점은 2번이다.
    graph[p2].append(p1) # 2번 정점이랑 연결된 정점은 1번이다.
print(graph)
# 1번 컴퓨터 부터 시작하므로 dfs(1) 부터 시작
dfs(1)
print(result)
print(len(result)-1)