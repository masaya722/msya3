S = input()
T = input()
sLen = len(S)
tLen = len(T)

ans = "UNRESTORABLE"
for i in range(sLen - tLen + 1):
    t_kari = S[i:i + tLen]
    for j in range(tLen):
        if t_kari[j] == '?':
            continue
        elif t_kari[j] != T[j]:
            break
    else:
        ans = (S[:i] + T + S[i + tLen:]).replace("?", "a")
print(ans)
