N = int(input())
C = list(map(int,input().split()))
Q = int(input())

sell = 0
set_sell = 0
all_sell = 0

min_set_sell = 10**10
min_all_sell = 10**10

for i in range(N):
    if i%2==0:
        min_set_sell = min(min_set_sell,C[i])
    else:
        min_all_sell = min(min_all_sell,C[i])

for _ in range(Q):
    query = list(input().split())
    if query[0]=='1':
        x = int(query[1])-1
        a = int(query[2])
        if x%2 ==0:
            if C[x]-set_sell-all_sell>=a:
                sell+=a
                C[x]-=a
                min_set_sell = min(min_set_sell,C[x])
            else:
                continue
        else:
            if C[x]-all_sell>=a:
                sell+=a
                C[x]-=a
                min_all_sell = min(min_all_sell,C[x])
            else:
                continue
    elif query[0]=='2':
        a = int(query[1])
        if min_set_sell-all_sell>=a:
            set_sell+=a
            min_set_sell-=a
    else:
        a =int(query[1])
        if min(min_set_sell-all_sell,min_all_sell)>=a:
            all_sell+=a
            min_all_sell-=a

for i in range(N):
    if i%2 ==0:
        sell+=set_sell
sell+=all_sell*N
print(sell)