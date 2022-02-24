D, G = map(int, input().split())
ques = []
bonus = []
for _ in range(D):
    p, c = map(int, input().split())
    ques.append(p)
    bonus.append(c)

ans = 10 ** 18


def dps(score, count, n, remain):
    global ans
    if n == D:
        if remain == []:
            if score >= G:
                if ans > count:
                    ans = count
                    return
        else:
            R = max(remain)
            for i in range(ques[R]):
                if score >= G:
                    if ans > count:
                        ans = count
                        return
                score += 100 * (R + 1)
                count += 1
        return

    s1 = score + 100 * (n + 1) * ques[n] + bonus[n]
    c1 = count + ques[n]
    dps(s1, c1, n + 1, remain)
    remain.append(n)
    dps(score, count, n + 1, remain)
    remain.pop()


dps(0, 0, 0, [])

print(ans)
