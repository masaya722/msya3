D, G = map(int, input().split())
ques = []
bonus = []

for i in range(D):
    p, c = map(int, input().split())
    ques.append(p)
    bonus.append(c)
INF = 10 ** 100
ans = INF


def dps(count, score, i, remain):
    global ans
    # Dまで見に行っている場合
    if i == D:
        if remain == []:
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
    # Dまで見に行っていない場合、かつiを完答する場合
    c1 = count + ques[i]
    s1 = score + bonus[i] + (i + 1) * 100 * ques[i]
    dps(c1, s1, i + 1, remain)
    # Dまで見に行っていない場合、かつiを完答しない場合
    remain.append(i)
    dps(count, score, i + 1, remain)
    remain.pop()


dps(0, 0, 0, [])
print(ans)
