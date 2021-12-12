S = input()
s_nums = [1 if s =='.' else 0 for s in S]
K = int(input())
cnt = 0
n = len(S)
sum = 0
ans = 0
for i in range(n):
    while cnt <n and sum +s_nums[cnt]<=K:
        sum +=s_nums[cnt]
        cnt+=1
    sum -=s_nums[i]
    ans = max(ans,cnt-i)
print(ans)
