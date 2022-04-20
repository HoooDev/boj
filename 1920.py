import sys

def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start+end) // 2

        if data[mid] == target:
            return 1
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0



N = sys.stdin.readline()
check = list(map(int, sys.stdin.readline().split()))
M = sys.stdin.readline()
num = list(map(int, sys.stdin.readline().split()))
check.sort()
for i in num:
    print(binary_search(i, check))