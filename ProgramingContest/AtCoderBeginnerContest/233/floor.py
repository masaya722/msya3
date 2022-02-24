X = input()
s = 0
for x in X:
    s+=int(x)
tmp = 0
res = []
for i in range(len(X)-1,-2,-1):
    tmp+=s
    res.append(tmp%10)
    tmp//=10
    if s != -1:
        s -=int(X[i])
    if tmp ==0 and s ==0:
        break
res.reverse()
ans = ''
for r in res:
    ans+=str(r)
print(ans)
