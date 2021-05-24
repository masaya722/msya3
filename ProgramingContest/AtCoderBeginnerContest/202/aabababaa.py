A, B, K = map(int, input().split())

ans = ""
C = []
for i in range(61):
    C.append([0]*(31))
C[0][0] = 1

for i in range(1, 61):
    C[i][0] = 1
    for j in range(1, 31):
        C[i][j] = C[i-1][j-1]+C[i-1][j]


while A+B > 0:
    x = 0
    if A >= 1:
        x = C[A+B-1][A-1]
    if K <= x:
        ans += 'a'
        A -= 1
    else:
        ans += 'b'
        B -= 1
        K -= x
print(ans)
