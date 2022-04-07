def dfs(v):
    # 방문기록 리스트의 1번 인덱스를 True로 바꿔주면서 방문 체크
    visited[v] = True
    # 방문한 번호를 출력
    ans_lst.append(v)
    # 그래프를 순회하면서 방문값이 False이면 재귀를 통해 다시 실행
    for i in nod[v]:
        if visited[i] == False:
            dfs(i)

com_n = int(input())  # 컴퓨터의 수
line_n = int(input())
visited = [False] * (com_n + 1)

lst = [list(map(int, input().split())) for _ in range(line_n)]
ans_lst = []
com_lst = []
for i in lst:
    for k in i:
        com_lst.append(k)
nod = [[] for _ in range(com_n + 1)]

for i in range(0, len(com_lst), 2):
    p1 = com_lst[i]
    p2 = com_lst[i + 1]
    nod[p1].append(p2)
    nod[p2].append(p1)

dfs(1)
print(len(ans_lst) - 1)
