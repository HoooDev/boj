import sys

N = int(sys.stdin.readline())
word_lst = []
for _ in range(N):
    word = input()
    word_lst.append(word)
set_word_lst = set(word_lst)
word_lst = list(set_word_lst)
word_lst.sort()
word_lst.sort(key=len)


for i in word_lst:
    print(i)