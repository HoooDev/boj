import sys
N, M = map(int, sys.stdin.readline().split())

Poketmon = [input() for _ in range(N)]
question = [input() for _ in range(M)]

Poketmon_dic = {}
Poketmon_dic_n = {}
for i, j in enumerate(Poketmon, start=1):
    Poketmon_dic[i] = j
    Poketmon_dic_n[j] = [i]


for i in range(M):
    if question[i].isdigit():
        print(Poketmon_dic[int(question[i])])
    else:
        print(*Poketmon_dic_n[question[i]])
