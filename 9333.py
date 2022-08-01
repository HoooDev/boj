# '''
# B 달러 빌림
# R 퍼센트 이자
# 매월 말 과외비 M 달러
# '''
#
#
# T = int(input())
# for tc in range(T):
#     R, B, M = list(map(float, input().split()))
#
#     inter = 0
#     cnt = 0
#     while True:
#         cnt += 1
#         a = (B * R / 100) + 0.00000001
#         inter = round(a, 2)
#         # print(inter)
#         B = B + inter - M
#         if B <= 0:
#             print(cnt)
#             break
#         if cnt > 1200:
#             print('impossible')
#             break

a = 2.025 + 0.000000001
b = round(a, 2)
print(b)