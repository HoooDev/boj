def check():
    stack = []
    for i in lst:
        if i == ')':
            acc = 0
            while len(stack) > 0:
                p = stack.pop()
                if p == '(':
                    if acc == 0:
                        stack.append(2)
                    else:
                        stack.append(acc * 2)
                    break
                elif p == '[':

                    return stack
                else:
                    acc += p


        elif i == ']':
            acc = 0
            while len(stack) > 0:
                p = stack.pop()
                if p == '[':
                    if acc == 0:
                        stack.append(3)
                    else:
                        stack.append(acc * 3)
                    break
                elif p == '(':

                    return stack
                else:
                    acc += p
        else:
            stack.append(i)
    return stack


lst = list(input())
arr = check()

ans = 0
for i in arr:
    if i == '(' or i == '[':
        break
    else:
        ans += i

print(ans)
