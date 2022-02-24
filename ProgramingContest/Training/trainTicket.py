s = input()
n = len(s)


def dfs(i, f, total):
    if i == n - 1 and total == 7:
        print(f + "=7")
        exit()
    else:
        if i + 1 <= n - 1:
            dfs(i + 1, f + "+" + s[i + 1], total + int(s[i + 1]))
            dfs(i + 1, f + "-" + s[i + 1], total - int(s[i + 1]))


dfs(0, s[0], int(s[0]))
