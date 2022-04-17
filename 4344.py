a = int(input())
lst_1 = []
for i in range(a):
    cnt=0
    b = list(map(int, input().split()))
    avg = sum(b[1::])/(len(b)-1)
    for over in b[1:]:
        if over > avg:
            cnt+=1
    lst_1.append((cnt/(len(b)-1))*100)

for ans in lst_1:
    print(f'{ans:.3f}%')