from collections import defaultdict
S = input()
count = defaultdict(int)
ans = 0
for i in range(len(S)-1,0,-1):
    count[S[i]] +=1
    if S[i] == S[i-1]:
        ans +=len(S)-i -count[S[i]]
        count= defaultdict(int)
        count[S[i]] = len(S)-i
print(ans)