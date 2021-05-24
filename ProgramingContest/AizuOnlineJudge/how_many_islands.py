import sys

sys.setrecursionlimit(10 ** 6)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        exit()
    C = []
    for i in range(h):
        c = list(map(int, input().split()))
        C.append(c)


    def dfs(i, j):
        C[i][j] = 0
        for k in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j),
                  (i + 1, j + 1)]:
            x, y = k
            if 0 <= x < h and 0<= y <w:
                if C[x][y] == 1:
                    dfs(x, y)


    count = 0
    for i in range(h):
        for j in range(w):
            if C[i][j] == 1:
                dfs(i, j)
                count += 1

    print(count)
