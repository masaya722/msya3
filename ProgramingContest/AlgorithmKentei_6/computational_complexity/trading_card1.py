N = int(input())
C = list(map(int, input().split()))
Q = int(input())

# 合計販売枚数の合計
sell = 0

for _ in range(0, Q):
    query = list(map(int, input().split()))
    # 単品販売
    if query[0] == 1:
        x = query[1] - 1
        a = query[2]
        if C[x] >= a:
            C[x] -= a
            sell += a
    # セット販売
    elif query[0] == 2:
        a = query[1]
        ok = True
        for i in range(0, N):
            if i % 2 == 0:
                if C[i] < a:
                    ok = False
        if ok:
            for i in range(0, N):
                if i % 2 == 0:
                    C[i] -= a
                    sell += a
    # 全販売
    elif query[0] == 3:
        a = query[1]
        ok = True
        for i in range(0, N):
            if C[i] < a:
                ok = False
        if ok:
            for i in range(0, N):
                C[i] -= a
                sell += a

print(sell)
