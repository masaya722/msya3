# 4

# 実行環境
# python 3.8.8

# 気になったこと
# 例題の解答は3759ではなく、3792かと思われます。(26+4+3が含まれていないため)

s = input()
n = len(s)

def dfs(i, f):
    if i == n - 1:
        return sum(list(map(int, f.split("+"))))
    return dfs(i + 1, f + s[i + 1]) + dfs(i + 1, f + "+" + s[i + 1])

print(dfs(0, s[0]))

