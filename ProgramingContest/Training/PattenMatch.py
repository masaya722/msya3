S = input()
C = "abcdefghijklmnopqrstuvwxyz."


def is_match(T, S):
    for i in range(0, len(S) - len(T) + 1):
        ok = True

        for j in range(len(T)):
            if S[i + j] != T[j] and T[j] != ".":
                ok = False
        if ok:
            return True

    return False


ans = 0
for c in C:
    if is_match(c, S):
        ans += 1
for c1 in C:
    for c2 in C:
        if is_match(c1 + c2, S):
            ans += 1

for c1 in C:
    for c2 in C:
        for c3 in C:
            if is_match(c1 + c2 + c3, S):
                ans += 1

print(ans)
