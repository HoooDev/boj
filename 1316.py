T = int(input()) # 4
# 단어의 수 = T
result = T # 4

# T 만큼 for문 돌리고
for i in range(0, T):
    # T 만큼 인풋
    word = input()
    #
    for j in range(0, len(word) - 1):
        if word[j] == word[j + 1]: # aaa
            pass
        # j번째 인덱스 뒤에 모든 글자 중 word[j]가 있냐?
        # abcabc word[j + 1:]
        # 012345 < abcabc의 인덱스
        elif word[j] in word[j + 1:]:
            # 그룹 단어가 아니면 전체 단어 개수에서 -1
            result -= 1
            # break로 for문 나오기
            break
print(result)