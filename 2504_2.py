def check(): # [ 2, 2 ]
    global lst
    lst_2 = []
    while lst:
        a = lst.pop(0)
        if not lst_2:
            lst_2.append(a)
        else:
            if len(lst_2) >= 2:
                if lst_2[-2] == '(' and type(lst_2[-1]) == int and a == ')':  # ( 2 )
                    b = lst_2.pop(-1)
                    lst_2.pop(-1)
                    lst_2.append(int(b) * 2)
                elif lst_2[-2] == '[' and type(lst_2[-1]) == int and a == ']':  # [ 2 ] 2 * 3 - > 6
                    b = lst_2.pop(-1)
                    lst_2.pop(-1)
                    lst_2.append(int(b) * 3)

                elif type(lst_2[-1]) == int and type(a) == int:
                    c = int(lst_2[-1]) + int(lst_2[-2])
                    lst_2.pop(-1)
                    lst_2.pop(-1)
                    lst_2.append(c)

                elif lst_2[-1] == '(' and a == ')':
                    lst_2.pop(-1)
                    lst_2.append(2)
                elif lst_2[-1] == '[' and a == ']':
                    lst_2.pop(-1)
                    lst_2.append(3)

                elif type(lst_2[-1]) == int and type(a) == int:
                    b = lst_2.pop(-1)
                    lst_2.append(int(a) + int(b))
                elif a == ')' or a == ']':
                    if type(lst_2[-1]) == int and type(lst_2[-2]) == int:
                        c = lst_2.pop(-1)
                        d = lst_2.pop(-1)
                        lst_2.append(c+d)
                        if lst_2[-2] == '(':
                            lst_2.pop(-2)
                            e = lst_2.pop()
                            lst_2.append(int(e) * 2)
                        elif lst_2[-2] == '[':
                            e = lst_2.pop()
                            lst_2.pop(-2)
                            lst_2.append(int(e) * 2)
                else:
                    lst_2.append(a)


            elif len(lst_2) >= 1:
                if lst_2[-1] == '(' and a == ')':
                    lst_2.pop(-1)
                    lst_2.append(2)
                elif lst_2[-1] == '[' and a == ']':
                    lst_2.pop(-1)
                    lst_2.append(3)
                else:
                    lst_2.append(a)
    return lst_2


lst = list(input())

arr = check()
ans = 0
for i in range(len(arr)):
    if type(arr[i]) == str:
        ans = 0
        break
    ans += arr[i]

print(ans)