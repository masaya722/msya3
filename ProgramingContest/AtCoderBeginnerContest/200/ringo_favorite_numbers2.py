import itertools 

N = int(input())
A = list(map(int, input().split()))
B = [a%200 for a in A]
cnt = [0]*200
for i in B:
    cnt[i]+=1

ans = 0
for i in range(200):
    if cnt[i] >= 1:
        ans += cnt[i]*(cnt[i]-1)//2

print(ans)