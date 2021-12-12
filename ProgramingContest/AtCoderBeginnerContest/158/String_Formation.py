from collections import deque

S = list(input())
Q = int(input())
s = deque(S)
flag = False
for i in range(Q):
    query = input().split()
    if query[0] == '1':
        flag = not flag
    else:
        if query[1] == '1':
            if flag:
                s.append(query[2])
            else:
                s.appendleft(query[2])
        else:
            if flag:
                s.appendleft(query[2])
            else:
                s.append(query[2])
if flag:
    s.reverse()
print(''.join(s))
