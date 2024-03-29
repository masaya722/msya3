R, B = map(int, input().split())
x, y = map(int, input().split())

ok = 0
ng = 10 ** 18 + 1


def check(X):
    r = R - X
    b = B - X

    if r < 0 or b < 0:
        return False
    num = r // (x - 1) + b // (y - 1)
    return num >= X


while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)
