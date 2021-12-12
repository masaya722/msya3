N = int(input())
S = [1,2,3,4,5,6]
N%=30
for i in range(N):
    S[i%5],S[i%5+1] = S[i%5+1],S[i%5]
ans = ''
for s in S:
    ans+=str(s)
print(ans)