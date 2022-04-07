a1, a2, a3 = map(int, input().split())

ans = 0
if a1 == a2 == a3:
    ans = 10000+a1*1000
elif a1==a2 or a1 == a3:
    ans = 1000+a1*100
elif a2 == a3:
    ans = 1000 + a2 * 100
elif a1 != a2 != a3:
    ans = max(a1, a2, a3) * 100
print(ans)