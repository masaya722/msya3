def is_match(T, S):
    for i in range(0, len(S) - len(T) + 1):
        ok = True

        for j in range(0, len(T)):

            if S[i + j] != T[j] and T[j] != ".":
                ok = False

        if ok:
            return True

    return False


S = input()

C = "abcdefghijklmnopqrstuvwxyz."

M = []

# 長さ1の文字列をすべて調べ、SとマッチするものをMに入れる。
for T in C:
    if is_match(T, S):
        M.append(T)

# 長さ2の文字列をすべて調べ、SとマッチするものをMに入れる。
for c1 in C:
    for c2 in C:
        T = c1 + c2
        if is_match(T, S):
            M.append(T)

# 長さ3の文字列をすべて調べ、SとマッチするものをMに入れる。
for c1 in C:
    for c2 in C:
        for c3 in C:
            T = c1 + c2 + c3
            if is_match(T, S):
                M.append(T)

print(len(M))