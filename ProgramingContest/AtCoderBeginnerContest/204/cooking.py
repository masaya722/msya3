_ = int(input())
S = 1
s = 0
for t in list(map(int,input().split())):
    S |= S<<t
    s +=t
ans = (s+1)//2
B =bin(S)[2:]
while B[ans] == '0':
    ans +=1
print(ans)

