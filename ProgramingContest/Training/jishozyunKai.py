N, K = map(int, input().split())
S = input()
best = sorted(S)

ans = ''
count = 0
for i in range(N):
    for c in best:
        tmp = 0
        if S[i] != c:
            tmp += 1
        t = best[:]
        t.remove(c)
        for j in range(i + 1, N):
            if S[j] in t:
                t.remove(S[j])
            else:
                tmp += 1
        if tmp + count <= K:
            if S[i] != c:
                count += 1
            best.remove(c)
            ans += c
            break

print(ans + S[len(S):])
