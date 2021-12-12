N,K = map(int,input().split())
A =list(map(int,input().split()))
INF = 10**18
cnt = [INF for _ in range(N)]
cnt[0] = 0
next = 0
roop = 0
ret = 0
for i in range(N):
    next = A[next]-1
    if cnt[next] != INF:
        roop =i
        ret = cnt[next]
        break
    cnt[next] = i+1

if K<roop+1:
    for i in range(N):
        if cnt[i] == K:
            print(i+1)
            exit()
else:
    K-=roop+1
    roops = []
    for i in range(N):
        if ret <=cnt[i]<=roop:
            roops.append((cnt[i],i))

    roops.sort()
    K%=len(roops)
    i,ans = roops[K]
    print(ans+1)






