from collections import deque
S = deque(list(input()))
ans = 0
while len(S)>1:
    i =S.popleft()
    j = S.pop()
    if i !=j:
        if i =='x':
            S.append(j)
            ans+=1
        elif j =='x':
            S.appendleft(i)
            ans+=1
        else:
            print(-1)
            exit()
print(ans)
            

