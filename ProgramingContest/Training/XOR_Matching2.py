from bisect import bisect_left
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B.sort()
X = []
for i in range(N):
    X.append(A[0]^B[i])
X.sort()
tmp = []
ans = []
for x in X:
    for a in A:
        c = x^a
        idx = bisect_left(tmp,c)
        tmp.insert(idx,c)
    if tmp==B:
        ans.append(x)
    tmp.clear()
ans_set = set(ans)
print(len(ans_set))
for a in ans_set:
    print(a)