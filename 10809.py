word = input()
alpha = "abcdefghijklmnopqrstuvwxyz"
lst = []
for i in alpha:
    if i in word:
        lst.append(word.index(i))
    else:
        lst.append('-1')
for ans in lst:
    print(ans, end=' ')
