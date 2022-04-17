a = int(input())
lst_3 = []
for c in range(a):
    lst_2 = []
    lst_1 = list(input())
    cnt=0
    for i in lst_1:
        if i == 'O':
            cnt+=1
            lst_2.append(cnt)
        else :
            cnt = 0
    lst_3.append(sum(lst_2))
for ans in lst_3:
    print(ans)
