from types import coroutine


N = int(input())
C = list(map(int,input().split()))
Q = int(input())
zen_sell = 0
set_sell = 0
one_sell = 0
# セット販売、全販売における最小個数
min_set = 10**18
min_zen = 10**18
for i in range(N):
    if i%2 ==0:
        min_set = min(min_set,C[i])
    else:
        min_zen = min(min_zen,C[i])

for i in range(Q):
    s = list(input().split())
    query = s[0]
    if query =='1':
        x = int(s[1])-1
        a = int(s[2])
        if x%2==0:
            if C[x]-set_sell-zen_sell<a:
                continue
            C[x]-=a
            one_sell +=a
            min_set = min(min_set,C[x])
        else:
            if C[x]-zen_sell<a:
                continue
            C[x]-=a
            one_sell +=a
            min_zen = min(min_zen,C[x])
    elif query =='2':
        a = int(s[1])
        if min_set-zen_sell>=a:
            set_sell+=a
            min_set = min(min_set,min_set-a)
    else:
        a = int(s[1])
        if min(min_zen,min_set-zen_sell) >=a:
            zen_sell+=a
            min_zen = min(min_zen,min_zen-a)

ans = one_sell
for i in range(N):
    if i%2 ==0:
        ans+=set_sell
ans+=zen_sell*N
print(ans)