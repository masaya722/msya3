A, B, K = map(int, input().split())

C = [[0]*31 for _ in range(61)]
C[0][0] = 1
for i in range(1,61):
    C[i][0] = 1
    for j in range(1,31):
        C[i][j] = C[i-1][j-1]+C[i-1][j]
ans = ""
while A+B > 0:
    x = 0
    if A >= 1:
        x = C[A+B-1][A-1]
    if K <= x:
        A -= 1
        ans += 'a'
    else:
        B -= 1
        ans += 'b'
        K -=x
print(ans)

