N, M = map(int,input().split())

C = max(N, M)
P_C = 1
while C > 0:
    if N % C == 0 and M % C == 0:
        N = N // C
        M = M // C
        P_C = P_C * C
    C -= 1

print(P_C)
print(N*M*P_C)