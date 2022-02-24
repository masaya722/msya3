A, B, X = list(map(int, input().split()))

ok = 0
ng = 10 ** 9 + 1

while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    price = A * mid + B * (len(str(mid)))
    if X >= price:
        ok = mid
    else:
        ng = mid

print(ok)
