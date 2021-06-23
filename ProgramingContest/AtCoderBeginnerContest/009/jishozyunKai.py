n, k = map(int, input().split())
s = input()
best = sorted(s)

ans = ''
count = 0

for i in range(n):
    for c in best:
        tmp = 0
        if c != s[i]:
            tmp += 1

        t = best[:]
        t.remove(c)
        for j in range(i + 1, n):
            if s[j] in t:
                t.remove(s[j])
            else:
                tmp += 1

        if count + tmp <= k:
            ans += c
            best.remove(c)
            if c != s[i]:
                count += 1
            break

print(ans)
