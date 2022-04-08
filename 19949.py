def dfs(n, k):
    global ans_lst, a, b
    if n == k:
        ans_lst.append(b)
        b = []
        n = 0
        return
    else:
        for i in a:
            b.append(i)
            dfs(n+1, k)



lst = list(map(int, input().split()))
N = len(lst)
a = [1, 2, 3, 4, 5]
b = []
ans_lst = []
dfs(0, 10)
print(ans_lst)