N, K = map(int, input().split())

grade_boy = [0] * 7
grade_girl = [0] * 7
for i in range(N):
    sex, stu_grade = map(int, input().split())

    if sex == 0:
        grade_girl[stu_grade] += 1
    else:
        grade_boy[stu_grade] += 1

lst_man = []
for i in range(1, len(grade_boy)):
    if grade_boy[i] % K == 0:
        lst_man.append(grade_boy[i] // K)
    elif grade_boy[i] == 0:
        pass
    elif grade_boy[i] % K != 0 and grade_boy[i] > K:
        lst_man.append(grade_boy[i]//K + 1)
    elif grade_boy[i] < K:
        lst_man.append(1)

lst_girl = []
for i in range(1, len(grade_girl)):
    if grade_girl[i] % K == 0:
        lst_man.append(grade_girl[i] // K)
    elif grade_girl[i] == 0:
        pass
    elif grade_girl[i] % K != 0 and grade_girl[i] > K:
        lst_man.append(grade_girl[i]//K + 1)
    elif grade_girl[i] < K:
        lst_man.append(1)

print(sum(lst_girl) + sum(lst_man))