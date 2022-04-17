a, b = map(int, input().split())

while a and b != 0:
    print(a+b)
    a, b = map(int, input().split())
    if a and b == 0:
        break