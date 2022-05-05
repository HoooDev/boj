'''
총 높이 : F
건물 위치 : G
현재 층 : S
위로 U만큼 : U
아래로 D만큼 : D
'''

F, S, G, U, D = map(int, input().split())

cnt = 0
if S > G:
    while True:
        if S == G:
            break
        if S < D:
            S += U
            cnt += 1
        S -= D
        cnt += 1

elif S < G:
    while True:
        if S == G:
            break
        if S > D:
            S -= D
            cnt += 1
        S += U
        cnt += 1

print(cnt)