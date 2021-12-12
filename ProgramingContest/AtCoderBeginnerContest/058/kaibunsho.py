import string
n = int(input())
tmp = 'abcdefghijklmnopqrstuvwxyz'
INF = 10**18
S = [INF for _ in range(26)]
for i in range(n):
    s = input()
    for a in tmp:
        S[ord(a)-97] = min(S[ord(a)-97],s.count(a))
ans = []
for i in range(26):
    ans.append(chr(i+97)*S[i])
print(''.join(ans))




