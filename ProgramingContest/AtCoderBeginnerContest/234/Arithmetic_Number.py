from bisect import bisect_left
X = int(input())
eq_diffs = [i for i in range(1,100)]
for i in range(2,18):
    for j in range(1,10):
        max_diff = (9-j)//i

        for k in range(max_diff+1):
            patn = ''
            tmp = j
            for l in range(i+1):
                patn+=str(tmp)
                tmp+=k
            eq_diffs.append(int(patn))

    for j in range(0,10):
        max_diff = (9-j)//i
        for k in range(max_diff+1):
            patn = ''
            tmp = j
            for l in range(i+1):
                patn+=str(tmp)
                tmp+=k
            s = list(patn)
            s.reverse()
            
            eq_diffs.append(int(''.join(s)))

eq_diffs.sort()

idx = bisect_left(eq_diffs,X)
print(eq_diffs[idx])