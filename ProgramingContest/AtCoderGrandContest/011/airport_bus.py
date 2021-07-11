N,C,K = map(int,input().split())
T = []
for i in range(N):
    T.append(int(input()))
T.sort()

count =1
ans = 1
tmp = T[0]
for i in range(1,N):
    if T[i]-tmp<=K and count <C:
        count+=1
    else:
        count =1
        tmp = T[i]
        ans +=1
print(ans)

