from collections import deque
'''
총 높이 : F
현재 층 : S
건물 위치 : G
위로 U만큼 : U
아래로 D만큼 : D
'''
def bfs(s):
    global cnt, can
    queue = deque()
    queue.append(s)
    while queue:
        p_s = queue.popleft()

        if p_s == G:
            can = 1
            return cnt

        if p_s < G and U != 0 and D != 0:
            n_s = p_s + U
            if n_s <= F:
                queue.append(n_s)
                cnt += 1
            else:
                n_s = p_s - D
                queue.append(n_s)
                cnt += 1

        else:
            n_s = p_s - D
            if n_s >= F:
                queue.append(n_s)
                cnt += 1
            else:
                n_s = p_s + U
                queue.append(n_s)
                cnt += 1

F, S, G, U, D = map(int, input().split())
can = 0
cnt = 0
if can == 1:
    print(bfs(S))
else:
    print('use the stairs')