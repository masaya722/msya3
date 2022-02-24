s =input()
t = input()
slen = len(s)
tlen = len(t)
dp = [[0 for _ in range(tlen+1)]for _ in range(slen+1)]
for i in range(slen):
    for j in range(tlen):
        if s[i] ==t[j]:
            dp[i+1][j+1] =dp[i][j]+1
        else:
            dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
max_len = dp[slen][tlen]

i = slen-1
j = tlen-1

ans = []
while max_len>0:
    if s[i] ==t[j]:
        max_len -=1
        ans.append(s[i])
        i -=1
        j -=1
    elif dp[i+1][j+1] ==dp[i+1][j]:
        j -=1
    else:
        i -=1


ans.reverse()
print(''.join(ans))