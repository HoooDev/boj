N = input()

lst = []
for i in N:
    lst.append(i)
lst.sort(reverse=True)

for i in lst:
    print(i, end='')