n, m = map(int, input().split())
ps = [[]for i in range(n+1)]


def popcount(x):
    '''xの立っているビット数をカウントする関数
    (xは64bit整数)'''

    # 2bitごとの組に分け、立っているビット数を2bitで表現する
    x = x - ((x >> 1) & 0x5555555555555555)

    # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f  # 8bitごと
    x = x + (x >> 8)  # 16bitごと
    x = x + (x >> 16)  # 32bitごと
    x = x + (x >> 32)  # 64bitごと = 全部の合計
    return x & 0x0000007f


for i in range(m):
    x, y, z = map(int, input().split())
    ps[x].append((y, z))

n2 = 1 << n
dp = [0 for _ in range(n2)]
dp[0] = 1
mask = [0 for _ in range(n+1)]
for i in range(n):
    mask[i+1] = mask[i] << 1 | 1
for s in range(n2):
    x = popcount(s)
    for p in ps[x]:
        y, z = p
        if popcount(s & mask[y]) > z:
            dp[s] = 0
    for j in range(n):
        if ~s >> j & 1:
            dp[s | 1 << j] += dp[s]

print(dp.pop())
