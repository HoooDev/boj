def bfs(s):
    global o
    q = []
    q.append(s)
    while q:
        c_s = q.pop(0)
        if c_s == time:
            return visited[n_s]
        for i in range(len(s_arr)):
            n_s = c_s + s_arr[i]
            q.append(n_s)
            visited[n_s] = visited[c_s] + 1



str_time = input()

H1, H2 = map(int, str_time[0:2])
S1 = int(str_time[3:4])
s_arr = [10, 30, 60, 600]
# print(H1, H2, S1)
o = 0
time = (H1 * 600) + (H2 * 60) + (S1 * 10)

visited = [0] * 3601

print(bfs(0))