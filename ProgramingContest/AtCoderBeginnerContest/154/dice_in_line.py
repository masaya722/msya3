N,K = map(int,input().split())
P = list(map(int,input().split()))

total =0
cusum= [0]
for p in P:
    total +=p
    cusum.append(total)

tmp = 0
ans_list = []
for i in range(N-K+1):
    tmp = max(cusum[i+K] - cusum[i],tmp)
    if tmp == cusum[i+K] - cusum[i]:
        ans_list.append(i+1)

ans_list.sort(reverse=True)
ans =0
for i in range(ans_list[0],ans_list[0]+K):
    ans +=(P[i-1]+1)/2

print(ans)