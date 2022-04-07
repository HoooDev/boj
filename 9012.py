def check():
    ans = []
    for i in lst:
        if i == '(':
            ans.append(i)
        else:
            if ans:
                ans.pop()
            else:
                return 'NO'
    if len(ans) == 0:
        return 'YES'
    else:
        return 'NO'


N = int(input())
for _ in range(N):
    lst = list(map(str, input()))

    print(check())
