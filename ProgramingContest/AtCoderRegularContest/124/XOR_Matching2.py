from bisect import bisect_left
N= int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
B.sort()
X = []
for i in range(N):
    X.append(A[0]^B[i])
X.sort()
tmp = []
ans = []
for x in X:
    for j in range(N):
        c = A[j]^x
        idx = bisect_left(tmp,c)
        tmp.insert(idx,c)
    if B ==tmp:
        ans.append(x)
    tmp.clear()
ans_dup = set(ans)
print(len(ans_dup))
for a in ans_dup:
    print(a)