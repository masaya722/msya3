N = int(input())
S= []
for i in range(N-1):
    c,s,f = map(int,input().split())
    S.append((c,s,f))
dp = [[]for _ in range(N)]
for i,(c,s,f) in enumerate(S):
    if i>0:
        for j in dp[i-1]:
            if s>=j:
                dp[i].append(s+c)
            else:
                if (j-s)%f !=0:
                    dp[i].append(s+(((j-s)//f)+1)*f+c)
                else:
                    dp[i].append(s+((j-s)//f)*f+c)
    dp[i].append(s+c)
for ans in dp[N-2]:
    print(ans)
print(0)
