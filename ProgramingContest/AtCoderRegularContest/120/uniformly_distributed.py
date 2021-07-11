H,W = map(int,input().split())
S = []
for i in range(H):
    s = input()
    S.append(s)

count = [[]for _ in range(H+W-1)]
for i in range(H):
    for j in range(W):
        count[i+j].append(S[i][j])
ans =1
for i in range(len(count)):
    if all(c=='.' for c in count[i]):
        ans*=2
    elif 'R' in count[i] and 'B' in count[i]:
        ans = 0
        break
print(ans%998244353)