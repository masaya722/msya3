N = int(input())
C = list(map(int, input().split()))
Q = int(input())

# 合計販売枚数の合計
sell = 0

# セット販売で売った数の合計
s = 0

# 全販売で売った数の合計
z = 0

# セット販売で売れる数の最小値
min_s_C = 10 ** 10

# 全販売で売れる数の最小値
min_z_C = 10 ** 10

for i in range(N):
    if i % 2 == 0:
        min_s_C = min(min_s_C, C[i])
    else:
        min_z_C = min(min_z_C, C[i])

for _ in range(0, Q):
    query = list(map(int, input().split()))
    # 単品販売
    if query[0] == 1:
        x = query[1] - 1
        a = query[2]
        if x % 2 == 0:
            if C[x] >= a + s + z:
                C[x] -= a
                sell += a
                min_s_C = min(C[x],min_s_C)
        else:
            if C[x] >= a + z:
                C[x] -= a
                sell += a
                min_z_C = min(C[x],min_z_C)
    # セット販売
    elif query[0] == 2:
        a = query[1]
        ok = True
        if min_s_C - z-s < a:
            ok = False
        if ok:
            s += a
    # 全販売
    elif query[0] == 3:
        a = query[1]
        ok = True
        if min(min_s_C-z-s,min_z_C-z)< a:
            ok = False
        if ok:
            z += a

for i in range(N):
    if i % 2 == 0:
        sell += s

sell += z * N

print(sell)
