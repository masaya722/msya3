from collections import deque

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    a = A[1:]
    b = B[1:]
    c = C[1:]
    a.insert(0, 0)
    b.insert(0, 0)
    c.insert(0, 0)
    Q = deque()
    Q.append((a, b, c, 0, -1))
    tmp = [i for i in range(0, n + 1)]

    while len(Q) > 0:
        a, b, c, count, t = Q.popleft()
        if count > m:
            print(-1)
            break
        if a == tmp or c == tmp:
            print(count)
            break
        if a[-1] > b[-1] and t != 1:
            Q.append((a[:-1], b + [a[-1]], c, count + 1, 0))
        if b[-1] > a[-1] and t != 0:
            Q.append((a + [b[-1]], b[:-1], c, count + 1, 1))
        if b[-1] > c[-1] and t != 3:
            Q.append((a, b[:-1], c + [b[-1]], count + 1, 2))
        if c[-1] > b[-1] and t != 2:
            Q.append((a, b + [c[-1]], c[:-1], count + 1, 3))
