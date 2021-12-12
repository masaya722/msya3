from bisect import bisect_left

N,K = map(int,input().split())
A = list(map(int,input().split()))
a_sum = [0]
s = 0
for a in A:
    s +=a
    a_sum.append(s)

idx = bisect_left(a_sum,K)
flag =False
last= False
ans = 0
if idx ==N+1:
    print(0)
    exit()
for i in range(N):
    if a_sum[idx]-a_sum[i]>=K:
        ans+=N+1-idx
    else:
        if not last:
            if idx !=N:
                while a_sum[idx]-a_sum[i]<K:
                    idx+=1
                    if idx ==N:
                        last = True
                        if a_sum[idx]-a_sum[i]>=K:
                            break
                        else:
                            flag = True
                            break
                if not flag:
                    ans+=N+1-idx
                else:
                    break
print(ans)