N, K = map(int, input().split())
arr = list(map(int, input().split()))

sum_p = sum(arr[:K])
lst = [sum_p]

for i in range(N-K):
    sum_p = sum_p - arr[i] + arr[i+K]
    lst.append(sum_p)
print(max(lst))