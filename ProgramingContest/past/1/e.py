N,Q = map(int,input().split())
friends = [[False]*N for _ in range(N)]
for i in range(Q):
    S = list(map(int,input().split()))
    a = S[1]-1
    if S[0] == 1:
        friends[a][S[2]-1] = True
    elif S[0] == 2:
        for j in range(N):
            if friends[j][a] and j !=a:
                friends[a][j] = True
    else:
        to_follow = []
        for j in range(N):
            if friends[a][j]:
                for k in range(N):
                    if friends[j][k] and k!=a:
                        to_follow.append(k)
        for t in to_follow:
            friends[a][t] = True
for i in range(N):
    temp = ''
    for j in range(N):
        if friends[i][j]:
            temp+='Y'
        else:
            temp+='N'
    print(temp)

