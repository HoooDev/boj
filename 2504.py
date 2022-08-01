arr = input()
stack = []
tmp = 1
acc = 0

for i in range(len(arr)):
    # 여는 괄호 나올때마다 * 2
    if arr[i] == '(':
        tmp *= 2
        stack.append(arr[i])
    elif arr[i] == '[':
        tmp *= 3
        stack.append(arr[i])

    elif arr[i] == ')':
        # 닫는 괄호가 나왔을 때 stack이 비어있거나 짝이 안맞으면
        if not stack or stack[-1] == '[':
            acc = 0
            break
        # 짝이 맞으면 현재까지의 값을 누적
        if arr[i - 1] == '(':
            acc += tmp
        # 짝이 하나 맞았으므로 해당 괄호에 해당하는 값만큼 나눔
        tmp //= 2
        # 계산 된 괄호 제거
        stack.pop()

    else:
        if not stack or stack[-1] == '(':
            acc = 0
            break

        if arr[i - 1] == '[':
            acc += tmp
        tmp //= 3
        stack.pop()

if stack:
    acc = 0
print(acc)