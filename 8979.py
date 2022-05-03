N, K = map(int, input().split())

country_lst = []
for _ in range(N):
    country = list(map(int, input().split()))
    country_lst.append(country)

# 금메달 j = 1, 은메달 j = 2, 동메달 j = 3
score = [0] * (N+1)
for i in range(N):
    for j in range(1, N):
        if j == 1:
            score[country_lst[i][0]] += country_lst[i][j] * 3
        elif j == 2:
            score[country_lst[i][0]] += country_lst[i][j] * 2
        else:
            score[country_lst[i][0]] += country_lst[i][j] * 1

ans = score[K]
score2 = score[1:]

score2.sort(reverse=True)

print(score2.index(ans)+1)