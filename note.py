T = int(input())

for i in range(T):
    CASE = list(map(int,input().split()))
    SUM = 0
    for k in CASE:
        SUM += k
    print("#{} {}"  .format((i+1), round(SUM/len(CASE))))
