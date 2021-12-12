from itertools import combinations
N = int(input())
M = []
A = []
R = []
C = []
H = []
for i in range(N):
    s = input()
    if s[0] == 'M':
        M.append(s)
    if s[0] == 'A':
        A.append(s)
    if s[0] == 'R':
        R.append(s)
    if s[0] == 'C':
        C.append(s)
    if s[0] == 'H':
        H.append(s)
S = [len(M),len(A),len(R),len(C),len(H)]
if S.count(0) >2:
    print(0)
else:
    ans = 0
    for i,j,k in combinations(S,3):
        ans+=i*j*k
    print(ans)

