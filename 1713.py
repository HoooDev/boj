'''
학생들이 추천을 시작하기 전에 모든 사진틀은 비어있다.

어떤 학생이 특정 학생을 추천하면, 추천받은 학생의 사진이 반드시 사진틀에 게시되어야 한다.

비어있는 사진틀이 없는 경우에는 현재까지 추천 받은 횟수가 가장 적은 학생의 사진을 삭제하고,
그 자리에 새롭게 추천받은 학생의 사진을 게시한다.
이때, 현재까지 추천 받은 횟수가 가장 적은 학생이 두 명 이상일 경우에는
그러한 학생들 중 게시된 지 가장 오래된 사진을 삭제한다.

현재 사진이 게시된 학생이 다른 학생의 추천을 받은 경우에는 추천받은 횟수만 증가시킨다.

사진틀에 게시된 사진이 삭제되는 경우에는 해당 학생이 추천받은 횟수는 0으로 바뀐다.
'''

# N = 사진틀의 갯수
N = int(input())
rec = int(input())
rec_n = list(map(int, input().split()))

N_lst = []
rec_count = [0] * (max(rec_n)+1)

for i in rec_n:
    rec_count[i] += 1
    if len(N_lst) < 3:
        N_lst.append(i)
    else:
        # 현재 액자 안에 있는 사람들 중 카운팅이 제일 낮은 사람
        min_n = 1000000000
        min_person = 0
        for k in N_lst:
            if min_n > rec_count[k]:
                min_n = rec_count[k]
                min_person = k
        for c in N_lst:
            rec_count[min_person] = 0
            a = N_lst.index(min_person)
            N_lst[a] = i
            break

print(N_lst)