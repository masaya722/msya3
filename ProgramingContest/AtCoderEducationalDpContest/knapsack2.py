n, w = map(int, input().split())
ws = [0]
vs = [0]
for _ in range(n):
    w1, v1 = map(int, input().split())
    ws.append(w1)
    vs.append(v1)
wei = []
for i in range(n + 1):
    wei.append([10 ** 10] * (sum(vs) + 1))
wei[0][0] = 0

for i in range(1, n + 1):
    for j in range(sum(vs) + 1):
        wei[i][j] = wei[i - 1][j]
        if j - vs[i] >= 0:
            wei[i][j] = min(wei[i - 1][j - vs[i]] + ws[i], wei[i][j])
for k in range(len(wei[n])):
    if wei[n][k] <= w:
        ans = k
print(ans)
