N,K = map(int,input().split())
P = list(map(int,input().split()))

cusum = [0]

total = 0
for p in P:
    p = (p+1)/2
    total +=p
    cusum.append(total)

biggest = 0
ans_list = []
for i in range(N-K+1):
    biggest = max(biggest,cusum[i+K] -cusum[i])
    if biggest == cusum[i+K]-cusum[i]:
        ans_list.append(i)

ans_list.sort(reverse=True)

ans = cusum[ans_list[0]+K]-cusum[ans_list[0]]
print(ans)
