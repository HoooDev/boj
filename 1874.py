flag = 1
cnt = 1
stack = []
ans = []

N = int(input())
for i in range(N):
    n = int(input())

    while cnt <= n:
        stack.append(cnt)
        ans.append('+')
        cnt += 1
    if stack[-1] == n:
        stack.pop()
        ans.append('-')

    else:
        flag = 0
        break

if flag == 1:
    for j in ans:
        print(j)
else:
    print('NO')