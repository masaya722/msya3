from collections import deque
s = input()
t = input()
slen = len(s)
tlen = len(t)
dp = [[0]*(tlen+1)for _ in range(slen+1)]

for i in range(slen):
    for j in range(tlen):
        if s[i] == t[j]:
            dp[i+1][j+1] = dp[i][j]+1
        else:
            dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])
max_len = dp[slen][tlen]

ans = deque()
i = slen-1
j = tlen -1
while max_len>0:
    if s[i] == t[j]:
        ans.appendleft(s[i])
        i -=1
        j -=1
        max_len-=1
    elif dp[i+1][j+1] ==dp[i][j+1]:
        i -=1
    else:
        j -=1
print(''.join(ans))

