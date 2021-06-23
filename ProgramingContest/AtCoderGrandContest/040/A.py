S = list(input())
totalLen = len(S)+1
ans = [0]*totalLen

for i in range(len(S)):
    if S[i] =="<":
        ans[i+1] = max(ans[i+1],ans[i]+1)

for i in range(len(S)-1,-1,-1):
    if S[i] ==">":
        ans[i] = max(ans[i],ans[i+1]+1)

print(sum(ans))