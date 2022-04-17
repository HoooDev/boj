T = int(input())
for i in range(T):
    a, b = map(str, input().split())
    for ans in b:
        print(ans*int(a),end='')
    print()