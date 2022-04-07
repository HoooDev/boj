X, Y = map(int, input().split())
N = int(input())

cut_garo = [0]
cut_sero = [0]
for c in range(N):
    cut, cut_n = list(map(int, input().split()))

    if cut == 1:
        cut_sero.append(cut_n)
    elif cut == 0:
        cut_garo.append(cut_n)
cut_garo.append(Y)
cut_sero.append(X)
cut_garo.sort()
cut_sero.sort()

max_garo = 0
for i in range(1, len(cut_garo)):
    if max_garo < cut_garo[i] - cut_garo[i-1]:
        max_garo = cut_garo[i] - cut_garo[i-1]

max_sero = 0
for j in range(1, len(cut_sero)):
    if max_sero < cut_sero[j] - cut_sero[j-1]:
        max_sero = cut_sero[j] - cut_sero[j-1]

print (max_garo * max_sero)