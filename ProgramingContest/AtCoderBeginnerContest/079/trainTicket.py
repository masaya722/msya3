s = input()


def dfs(i, f, total):
    if i == 3:
        if total == 7:
            exit(print(f + "=7"))
    else:
        dfs(i + 1, f + "+" + s[i + 1], total + int(s[i + 1]))
        dfs(i + 1, f + "-" + s[i + 1], total - int(s[i + 1]))


dfs(0, s[0], int(s[0]))
