# def search(lst, k):
#     for i in range(lst):
#         for j in range(lst):
#             if lst[i][0] == k:
#                 return i
#
# def grade(i):
#
#
# N, K = map(int, input().split())
#
# country_lst = []
# for _ in range(N):
#     country = list(map(int, input().split()))
#     country_lst.append(country)
#
# country_lst.sort(key=lambda x : (-x[1], -x[2], -x[3]))
#
# target = search(country_lst, K)
# grade(target)