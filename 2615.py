# arr = [list(map(int, input().split())) for _ in range(19)]
#
# di = [0, 1, 1, 1]  # 우 대각 하 대각
# dj = [1, 1, 0, -1]
#
# win = []
# lst = []
# no_winner = []
# for i in range(19):
#     for j in range(19):
#         if arr[i][j] == 1:
#             for d in range(4):
#                 cnt = 1
#                 ni = i + di[d]
#                 nj = j + dj[d]
#                 while 0 <= ni < 19 and 0 <= nj < 19 and arr[ni][nj] == 1:
#                     ni += di[d]
#                     nj += dj[d]
#                     cnt += 1
#                     if cnt == 5:
#                         lst.append(i + 1)
#                         lst.append(j + 1)
#                         win.append(1)
#                     elif cnt > 5:
#                         lst.pop()
#                         lst.pop()
#                         lst.append(0)
#
#                     elif cnt < 5:
#                         no_winner.append(0)
#         elif arr[i][j] == 2:
#             for d in range(4):
#                 cnt = 1
#                 ni = i + di[d]
#                 nj = j + dj[d]
#                 while 0 <= ni < 19 and 0 <= nj < 19 and arr[ni][nj] == 2:
#                     ni += di[d]
#                     nj += dj[d]
#                     cnt += 1
#                     if cnt == 5:
#                         if
#                         lst.append(i + 1)
#                         lst.append(j + 1)
#                         win.append(2)
#                     elif cnt > 5:
#                         lst.pop()
#                         lst.pop()
#
#                     elif cnt < 5:
#                         no_winner.append(0)
#
# if lst:
#     print(*win)
#     print(*lst)
# else:
#     for i in no_winner:
#         print(i)
#         break
